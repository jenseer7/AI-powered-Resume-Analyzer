from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from typing import Optional

from backend.models.schemas import ResumeAnalysis, ErrorResponse
from backend.services.parser import PDFParser
from backend.services.analyzer import AnalyzerService

load_dotenv()

app = FastAPI(title="Professional Resume AI Analyzer")

# Configure CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend origin
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze", response_model=ResumeAnalysis)
async def analyze_resume_endpoint(
    file: UploadFile = File(...),
    job_description: Optional[str] = Form(None),
    api_key: Optional[str] = Form(None)
):
    # Prefer provided API key, then env variable
    active_key = api_key or os.getenv("GEMINI_API_KEY")
    
    if not active_key:
        raise HTTPException(status_code=400, detail="Gemini API Key is required. Provide it in settings or .env file.")

    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    try:
        # 1. Read and parse PDF
        content = await file.read()
        text = await PDFParser.extract_text(content)
        
        # 2. Analyze with AI
        analyzer = AnalyzerService(api_key=active_key)
        result = await analyzer.analyze(text, job_description)
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

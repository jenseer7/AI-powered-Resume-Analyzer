# AI Resume Analyzer

A high-performance, single-file web application to analyze resumes and get structured feedback using the Gemini 1.5 Flash API.

## 🚀 How to Run
Since this is a zero-install application, you don't need Node.js or Python.

1.  Locate the `index.html` file in the project folder.
2.  Right-click the file and select **Open with** > **Google Chrome** (or any modern browser).
3.  Alternatively, you can open this link directly in your browser:
    [Open Resume Analyzer](file:///C:/Users/user/.gemini/antigravity/scratch/resume-analyzer/index.html)

## 🏗️ Architecture & Flow
1.  **Frontend**: Built with HTML5, CSS3 (Vanilla), and JavaScript.
2.  **PDF Parsing**: Uses the `pdf.js` library (via CDN) to extract text content from PDF files directly in the browser.
3.  **AI Analysis**:
    *   The extracted text is sent to the **Gemini 1.5 Flash API**.
    *   A structured prompt ensures the response is returned as a JSON object.
    *   **Demo Mode**: If no API key is provided, the application switches to a simulated analysis for demonstration purposes.
4.  **UI/UX**: Implements a glassmorphism design system with responsive layouts and CSS animations.

## 🤖 AI Tools & Prompts
*   **AI Model**: Gemini 1.5 Flash (via API).
*   **Prompt Used**:
    ```text
    Analyze the following resume text and provide structured feedback. 
    Return the result ONLY as a JSON object with these keys: 
    "score" (number 1-100), 
    "summary" (string), 
    "strengths" (array of strings), 
    "weaknesses" (array of strings), 
    "missing" (array of strings), 
    "suggestions" (array of strings).

    Resume Text: [EXTRACTED_TEXT]
    ```

## 📝 What Worked Well & Manual Corrections
*   **Worked Well**: The `pdf.js` extraction is very fast and handles basic layouts perfectly. The glassmorphism CSS provides a premium feel without heavy frameworks.
*   **Manual Corrections**:
    *   The AI sometimes wraps JSON in markdown code blocks (` ```json `), so I added a regex cleanup step in JavaScript to handle that.
    *   Initial score animations were jerky; I switched to standard CSS transitions for better performance on various browsers.

## ⚠️ Assumptions
1.  **PDF Only**: The current version assumes the resume is a text-based PDF (not a scanned image).
2.  **API Key**: User has or can generate a Gemini API key for real-time analysis.
3.  **Internet**: Required to load the PDF.js script and call the Gemini API.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ResumeAI | Intelligent Analyzer</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.4.120/pdf.min.js"></script>
    <style>
        :root {
            --bg: #050b18;
            --card-bg: rgba(15, 23, 42, 0.7);
            --primary: #6366f1;
            --secondary: #a855f7;
            --accent: #ec4899;
            --text: #f8fafc;
            --text-dim: #94a3b8;
            --border: rgba(255, 255, 255, 0.1);
            --glass: rgba(255, 255, 255, 0.03);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Outfit', sans-serif;
        }

        body {
            background-color: var(--bg);
            color: var(--text);
            min-height: 100vh;
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 20% 20%, rgba(99, 102, 241, 0.15) 0%, transparent 40%),
                radial-gradient(circle at 80% 80%, rgba(168, 85, 247, 0.15) 0%, transparent 40%);
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 2rem;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 4rem;
            animation: fadeInDown 0.8s ease-out;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 800;
            background: linear-gradient(to right, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -1px;
        }

        .hero {
            text-align: center;
            margin-bottom: 4rem;
            animation: fadeInUp 0.8s ease-out;
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 1rem;
            line-height: 1.1;
        }

        .hero p {
            font-size: 1.25rem;
            color: var(--text-dim);
            max-width: 600px;
            margin: 0 auto;
        }

        /* Upload Area */
        .upload-card {
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 3rem;
            text-align: center;
            transition: all 0.3s ease;
            cursor: pointer;
            margin-bottom: 2rem;
            box-shadow: 0 20px 50px rgba(0,0,0,0.3);
        }

        .upload-card:hover {
            border-color: var(--primary);
            transform: translateY(-5px);
            box-shadow: 0 20px 50px rgba(99, 102, 241, 0.2);
        }

        .upload-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
            display: block;
        }

        .upload-card h3 {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }

        .upload-card p {
            color: var(--text-dim);
        }

        #fileInput { display: none; }

        /* Settings Accordion */
        .settings-container {
            margin-bottom: 2rem;
        }

        .settings-header {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--text-dim);
            font-size: 0.9rem;
            cursor: pointer;
            justify-content: center;
            padding: 1rem;
        }

        .settings-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease;
            background: var(--glass);
            border-radius: 12px;
            margin-top: 0.5rem;
        }

        .settings-content.active {
            max-height: 200px;
            padding: 1.5rem;
            border: 1px solid var(--border);
        }

        input[type="password"] {
            width: 100%;
            background: rgba(0,0,0,0.3);
            border: 1px solid var(--border);
            padding: 0.75rem 1rem;
            border-radius: 8px;
            color: white;
            outline: none;
            transition: border-color 0.3s;
        }

        input[type="password"]:focus {
            border-color: var(--primary);
        }

        /* Status & Results */
        .status-container {
            display: none;
            text-align: center;
            padding: 2rem;
        }

        .jd-section {
            margin-top: 1rem;
            text-align: left;
            background: var(--glass);
            padding: 1rem;
            border-radius: 12px;
            border: 1px solid var(--border);
        }

        textarea {
            width: 100%;
            height: 100px;
            background: rgba(0,0,0,0.3);
            border: 1px solid var(--border);
            padding: 0.75rem;
            border-radius: 8px;
            color: white;
            font-size: 0.9rem;
            margin-top: 0.5rem;
            resize: none;
        }

        textarea:focus { border-color: var(--primary); outline: none; }

        .loader {
            width: 48px;
            height: 48px;
            border: 5px solid var(--glass);
            border-bottom-color: var(--primary);
            border-radius: 50%;
            display: inline-block;
            animation: rotation 1s linear infinite;
            margin-bottom: 1rem;
        }

        .results-container {
            display: none;
            animation: fadeIn 0.5s ease-in;
        }

        .score-card {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 2rem;
            display: flex;
            align-items: center;
            gap: 2rem;
        }

        .score-circle {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: rgba(0,0,0,0.2);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.5rem;
            font-weight: 800;
            border: 4px solid rgba(255,255,255,0.2);
        }

        .profile-summary {
            flex: 1;
        }

        .profile-summary h2 { margin-bottom: 0.5rem; }

        .grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1.5rem;
            margin-bottom: 2rem;
        }

        .card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 1.5rem;
        }

        .card h3 {
            font-size: 1.1rem;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--secondary);
        }

        .list-item {
            display: flex;
            gap: 0.75rem;
            margin-bottom: 0.75rem;
            font-size: 0.95rem;
            line-height: 1.4;
        }

        .bullet-point {
            color: var(--primary);
            font-weight: bold;
        }

        .full-width { grid-column: span 2; }

        /* Buttons */
        .btn-reset {
            background: var(--glass);
            border: 1px solid var(--border);
            color: var(--text);
            padding: 0.75rem 1.5rem;
            border-radius: 12px;
            cursor: pointer;
            margin-top: 2rem;
            transition: background 0.3s;
        }

        .btn-reset:hover { background: rgba(255,255,255,0.1); }

        /* Animations */
        @keyframes rotation { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        @keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes fadeInDown { from { opacity: 0; transform: translateY(-20px); } to { opacity: 1; transform: translateY(0); } }

        @media (max-width: 768px) {
            .grid { grid-template-columns: 1fr; }
            .full-width { grid-column: span 1; }
            .score-card { flex-direction: column; text-align: center; }
            .hero h1 { font-size: 2.5rem; }
        }
    </style>
</head>
<body>
    <div class="container" id="mainContainer">
        <header>
            <div class="logo">RESUME AI</div>
            <div class="badge">BETA v1.0</div>
        </header>

        <section class="hero" id="heroSection">
            <h1>Elevate Your Career with <br>AI Insights</h1>
            <p>Upload your resume and get an instant, intelligent analysis of your strengths, gaps, and professional profile score.</p>
        </section>

        <section id="uploadSection">
            <div class="upload-card" onclick="document.getElementById('fileInput').click()">
                <span class="upload-icon">📄</span>
                <h3>Drop your resume here</h3>
                <p>Supports PDF only for now. Max 5MB.</p>
                <input type="file" id="fileInput" accept=".pdf">
            </div>

            <div class="settings-container">
                <div class="settings-header" onclick="toggleSettings()">
                    <span>⚙️</span>
                    <span>AI Settings & Job Matching</span>
                </div>
                <div class="settings-content" id="settingsContent">
                    <div style="margin-bottom: 1rem;">
                        <p style="font-size: 0.8rem; margin-bottom: 0.5rem; color: var(--text-dim);">Enter your Gemini API Key for real analysis.</p>
                        <input type="password" id="apiKey" placeholder="Paste your API Key here...">
                    </div>
                    <div class="jd-section">
                        <p style="font-size: 0.8rem; font-weight: 600; color: var(--primary);">Target Job Description (Optional)</p>
                        <textarea id="jobDesc" placeholder="Paste the job requirements here to get a match score..."></textarea>
                    </div>
                </div>
            </div>
        </section>

        <section class="status-container" id="statusSection">
            <div class="loader"></div>
            <h3 id="statusText">Analyzing Documents...</h3>
            <p id="statusSubtext">This usually takes about 5-10 seconds.</p>
        </section>

        <section class="results-container" id="resultsSection">
            <div class="score-card">
                <div class="score-circle" id="overallScore">85</div>
                <div class="profile-summary">
                    <h2>Candidate Profile Summary</h2>
                    <p id="summaryText">A highly motivated software engineer with strong expertise in full-stack development and cloud architecture.</p>
                </div>
            </div>

            <div class="grid">
                <div class="card">
                    <h3><span>✅</span> Key Strengths</h3>
                    <div id="strengthsList"></div>
                </div>
                <div class="card">
                    <h3><span>⚠️</span> Areas for Improvement</h3>
                    <div id="weaknessesList"></div>
                </div>
                <div class="card">
                    <h3><span>🎯</span> Missing Skills / Sections</h3>
                    <div id="missingList"></div>
                </div>
                <div class="card">
                    <h3><span>🚀</span> Actionable Suggestions</h3>
                    <div id="suggestionsList"></div>
                </div>
            </div>

            <div style="text-align: center;">
                <button class="btn-reset" onclick="resetApp()">Analyze Another Resume</button>
            </div>
        </section>
    </div>

    <script>
        // PDF.js worker setup
        pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.4.120/pdf.worker.min.js';

        const fileInput = document.getElementById('fileInput');
        const uploadSection = document.getElementById('uploadSection');
        const statusSection = document.getElementById('statusSection');
        const resultsSection = document.getElementById('resultsSection');
        const heroSection = document.getElementById('heroSection');
        const statusText = document.getElementById('statusText');

        fileInput.addEventListener('change', handleFileUpload);

        function toggleSettings() {
            document.getElementById('settingsContent').classList.toggle('active');
        }

        async function handleFileUpload(e) {
            const file = e.target.files[0];
            if (!file) return;

            // Transition to loading
            heroSection.style.display = 'none';
            uploadSection.style.display = 'none';
            statusSection.style.display = 'block';

            try {
                updateStatus("Extracting text...", "Reading the PDF structure locally.");
                const text = await extractTextFromPDF(file);
                
                updateStatus("Analyzing with AI...", "Interpreting your career history.");
                const analysis = await analyzeResume(text);
                
                displayResults(analysis);
            } catch (error) {
                console.error(error);
                alert("Error processing resume: " + error.message);
                resetApp();
            }
        }

        function updateStatus(main, sub) {
            statusText.innerText = main;
            document.getElementById('statusSubtext').innerText = sub;
        }

        async function extractTextFromPDF(file) {
            const arrayBuffer = await file.arrayBuffer();
            const pdf = await pdfjsLib.getDocument({ data: arrayBuffer }).promise;
            let fullText = "";

            for (let i = 1; i <= pdf.numPages; i++) {
                const page = await pdf.getPage(i);
                const textContent = await page.getTextContent();
                fullText += textContent.items.map(item => item.str).join(" ") + "\n";
            }
            return fullText;
        }

        async function analyzeResume(text) {
            const apiKey = document.getElementById('apiKey').value;
            const jd = document.getElementById('jobDesc').value;

            if (!apiKey) {
                // Simulate delay and return demo data
                await new Promise(r => setTimeout(r, 2000));
                return getDemoAnalysis(jd ? true : false);
            }

            const prompt = `Analyze the following resume text${jd ? ' against the provided job description' : ''} and provide structured feedback. 
            Return the result ONLY as a JSON object with these keys: 
            "score" (number 1-100), 
            "matchScore" (number 1-100, only if job description provided, else null),
            "summary" (string), 
            "strengths" (array of strings), 
            "weaknesses" (array of strings), 
            "missing" (array of strings), 
            "suggestions" (array of strings).

            Resume Text:
            ${text}

            ${jd ? `Job Description:\n${jd}` : ''}`;

            const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    contents: [{ parts: [{ text: prompt }] }]
                })
            });

            const data = await response.json();
            if (data.error) throw new Error(data.error.message);
            
            try {
                const aiText = data.candidates[0].content.parts[0].text;
                // Clean markdown if AI returns it
                const jsonStr = aiText.replace(/```json|```/g, '').trim();
                return JSON.parse(jsonStr);
            } catch (e) {
                console.error("Failed to parse AI response", e);
                return getDemoAnalysis(); // Fallback
            }
        }

        function displayResults(data) {
            statusSection.style.display = 'none';
            resultsSection.style.display = 'block';

            document.getElementById('overallScore').innerText = data.score;
            
            let summaryHtml = data.summary;
            if (data.matchScore) {
                summaryHtml = `<div style="display: inline-block; background: rgba(16, 185, 129, 0.2); color: #10b981; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; margin-bottom: 10px; font-weight: 600;">Match Score: ${data.matchScore}%</div><br>` + summaryHtml;
            }
            document.getElementById('summaryText').innerHTML = summaryHtml;
            
            fillList('strengthsList', data.strengths);
            fillList('weaknessesList', data.weaknesses);
            fillList('missingList', data.missing);
            fillList('suggestionsList', data.suggestions);
        }

        function fillList(elementId, items) {
            const container = document.getElementById(elementId);
            container.innerHTML = '';
            items.forEach(item => {
                const div = document.createElement('div');
                div.className = 'list-item';
                div.innerHTML = `<span class="bullet-point">/</span> <span>${item}</span>`;
                container.appendChild(div);
            });
        }

        function resetApp() {
            resultsSection.style.display = 'none';
            statusSection.style.display = 'none';
            heroSection.style.display = 'block';
            uploadSection.style.display = 'block';
            fileInput.value = '';
        }

        function getDemoAnalysis(hasJD) {
            return {
                score: 82,
                matchScore: hasJD ? 74 : null,
                summary: "You are viewing the DEMO MODE because no API key was provided. This candidate demonstrates strong technical proficiency but could improve their quantification of accomplishments.",
                strengths: [
                    "Strong technical foundation in modern frameworks",
                    "Clear and professional layout",
                    "Consistent career progression"
                ],
                weaknesses: [
                    "Lack of specific metric-driven achievements",
                    "A bit text-heavy in the middle sections",
                    "Summary could be more impactful"
                ],
                missing: [
                    "GitHub profile link or Portfolio",
                    "Certifications section",
                    "Keywords related to 'Cloud Infrastructure'"
                ],
                suggestions: [
                    "Use the STAR method for bullet points",
                    "Add 3-5 key metrics (e.g., 'Reduced latency by 20%')",
                    "Include a dedicated 'Core Values' or 'Soft Skills' section"
                ]
            };
        }
    </script>
</body>
</html>

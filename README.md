# 📄 AI Resume Analyzer

An AI-powered resume analysis tool built with **Streamlit** and **Google Gemini 3.6 Flash**. Upload your resume in PDF or TXT format, select your target job role, and get actionable feedback on your resume, including ATS optimization, skills relevance, project quality, and improvement suggestions.

---

## 🚀 Features

* 📄 **PDF & TXT Resume Upload**
* 🤖 **AI-powered Resume Analysis**
* 🎯 **Job Role-specific Feedback**
* 📊 **ATS Optimization Analysis**
* 💪 **Resume Strength Identification**
* ⚠️ **Areas for Improvement**
* 🛠️ **Skills & Experience Analysis**
* 💡 **Actionable Recommendations**
* ✍️ **AI-powered Bullet Point Improvements**
* 🔒 **Environment-based API Key Management**
* ⚡ Fast and simple Streamlit interface
* 🛡️ Robust error handling for API and file-processing issues

---

## 🖥️ Demo

### Upload Resume

Upload your resume in either:

* PDF format
* TXT format

Then enter the job role you're targeting.

Example:

```text
Job Role:
Software Engineer
```

Click:

```text
Analyze Resume
```

The application sends the extracted resume content to Gemini and generates a structured analysis.

---


## 🧠 AI Analysis

The application analyzes your resume across multiple dimensions.

### 1. Overall Assessment

Provides a high-level evaluation of the resume.

### 2. Strengths

Identifies the strongest sections and accomplishments.

### 3. Areas for Improvement

Highlights weaknesses and provides practical suggestions.

### 4. Skills Analysis

Evaluates technical and soft skills against the target role.

### 5. Experience & Projects

Analyzes:

* Technical depth
* Problem-solving ability
* Technologies
* Impact
* Measurable results
* Job relevance

### 6. ATS Optimization

Checks for:

* Relevant keywords
* Missing keywords
* Formatting concerns
* Weak bullet points
* Missing sections
* Irrelevant information

### 7. Job-Specific Recommendations

Provides recommendations based on the target position.

### 8. Bullet Point Improvements

Suggests stronger versions of weak resume bullet points while avoiding fabricated experience or achievements.

### 9. Final Verdict

Provides an overall assessment along with the **top three improvements** the candidate should prioritize.

---

## 🏗️ Project Architecture

```text
AI-Resume-Analyzer/
│
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── screenshots/
│   ├── home.png
│   └── analysis.png
│
└── .env
```

> `.env` should never be committed to GitHub.

---

## 🛠️ Tech Stack

| Technology                 | Purpose                         |
| -------------------------- | ------------------------------- |
| 🐍 Python                  | Core programming language       |
| 🎨 Streamlit               | Web application interface       |
| 🤖 Google Gemini 3.6 Flash | AI resume analysis              |
| 📑 PyPDF2                  | PDF text extraction             |
| 🔐 python-dotenv           | Environment variable management |
| 📦 google-genai            | Gemini API integration          |

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git
```

Navigate into the project:

```bash
cd AI-Resume-Analyzer
```

---

### 2. Create a virtual environment

Using Python:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Or using `uv`:

```powershell
uv venv
.venv\Scripts\activate
```

---

### 3. Install dependencies

Using `pip`:

```bash
pip install -r requirements.txt
```

Or using `uv`:

```powershell
uv pip install -r requirements.txt
```

---

## 🔑 API Key Configuration

This project uses the **Google Gemini API**.

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

The application loads the API key using:

```python
from dotenv import load_dotenv

load_dotenv()
```

and initializes the Gemini client:

```python
from google import genai

client = genai.Client(
    api_key=GEMINI_API_KEY
)
```

### ⚠️ Security

Never commit your `.env` file.

Your `.gitignore` should contain:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

## ▶️ Running the Application

Start Streamlit:

```bash
streamlit run main.py
```

The application will open in your browser.

---

## 🔄 How It Works

```text
             ┌─────────────────────┐
             │   Upload Resume     │
             │    PDF / TXT        │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │  Extract Resume     │
             │       Text          │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Select Target       │
             │     Job Role        │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Construct AI Prompt │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Gemini 3.6 Flash    │
             │   Analysis          │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Structured Resume   │
             │     Feedback        │
             └─────────────────────┘
```

---

## 📂 Supported Files

| File Type | Supported |
| --------- | --------- |
| PDF       | ✅         |
| TXT       | ✅         |
| DOCX      | ❌         |
| DOC       | ❌         |

Currently, the application focuses on PDF and TXT resumes.

---

## 🧪 Example Use Case

### Input

```text
Resume:
Software engineering student
Python
C++
React
SQL
Multiple academic projects

Target Role:
Software Engineer
```

### Output

The AI evaluates:

```text
Overall Assessment
        ↓
Strengths
        ↓
Areas for Improvement
        ↓
Skills Analysis
        ↓
Projects & Experience
        ↓
ATS Optimization
        ↓
Job-Specific Recommendations
        ↓
Bullet Point Improvements
        ↓
Final Verdict
```

---

## 🛡️ Error Handling

The application handles common issues including:

* Missing API key
* Invalid API credentials
* API quota/rate-limit errors
* Unsupported file types
* Empty resumes
* Invalid PDF files
* Empty AI responses
* Unavailable Gemini models
* Large resume content

Instead of exposing raw errors to users, the application provides meaningful error messages wherever possible.

---

## 📈 Future Improvements

Potential improvements include:
📊 ATS score out of 100
🔍 Job Description upload
🧩 Resume vs Job Description keyword matching
📑 DOCX support
📋 Download analysis as PDF
📈 Resume scoring dashboard
🎯 Missing skills identification
🔄 Resume improvement suggestions
🌐 Deployment on Streamlit Cloud
💾 Resume analysis history
👤 User authentication
📊 Resume comparison between versions

---

## 🤝 Contributing

Contributions are welcome!

### Fork the repository

```bash
git fork
```

Create a new branch:

```bash
git checkout -b feature/your-feature
```

Make your changes and commit:

```bash
git add .
git commit -m "Add new feature"
```

Push the branch:

```bash
git push origin feature/your-feature
```

Then open a Pull Request.

---

## ⚠️ Disclaimer

This tool provides **AI-generated resume feedback** and should be used as a supporting tool rather than a replacement for professional career advice.

AI-generated suggestions may occasionally be inaccurate. Always review recommendations before applying them to your resume.

---

## 👨‍💻 Author

**Deepanshu Mandhyan**


## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📜 License

This project is available under the **MIT License**.

---

<p align="center">

**Built with ❤️ using Python, Streamlit & Gemini**

</p>
```

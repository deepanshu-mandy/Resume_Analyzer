
import streamlit as st
import PyPDF2
import io
import os

from google import genai
from dotenv import load_dotenv


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# STREAMLIT PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📃",
    layout="centered"
)


# ============================================================
# TITLE
# ============================================================

st.title("AI Resume Analyzer")

st.markdown(
    "Upload your resume in PDF or TXT format and let our AI "
    "analyze it for you!"
)


# ============================================================
# GEMINI API KEY
# ============================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:

    st.error(
        "GEMINI_API_KEY is not configured. "
        "Please add it to your .env file."
    )

    st.stop()


# ============================================================
# GEMINI CLIENT
# ============================================================

try:

    client = genai.Client(
        api_key=GEMINI_API_KEY
    )

except Exception as e:

    st.error(
        f"Could not initialize Gemini API: {str(e)}"
    )

    st.stop()


# ============================================================
# USER INPUT
# ============================================================

uploaded_file = st.file_uploader(
    "Choose a resume file (PDF or TXT)",
    type=["pdf", "txt"]
)

job_role = st.text_input(
    "Enter the job role you are applying for (optional):"
)

analyze = st.button("Analyze Resume")


# ============================================================
# PDF TEXT EXTRACTION
# ============================================================

def extract_text_from_pdf(file_object):
    """
    Extract text from a PDF file.
    """

    try:

        pdf_reader = PyPDF2.PdfReader(
            file_object
        )

        if len(pdf_reader.pages) == 0:
            return ""

        text = ""

        for page in pdf_reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text.strip()

    except Exception as e:

        raise Exception(
            f"Unable to read the PDF file: {str(e)}"
        )


# ============================================================
# FILE TEXT EXTRACTION
# ============================================================

def extract_text_from_file(uploaded_file):
    """
    Extract text from PDF or TXT file.
    """

    try:

        if uploaded_file.type == "application/pdf":

            pdf_data = io.BytesIO(
                uploaded_file.read()
            )

            return extract_text_from_pdf(
                pdf_data
            )

        elif uploaded_file.type == "text/plain":

            return uploaded_file.read().decode(
                "utf-8",
                errors="ignore"
            ).strip()

        else:

            raise Exception(
                "Unsupported file type. "
                "Please upload a PDF or TXT file."
            )

    except Exception as e:

        raise Exception(
            f"Could not extract text from the file: {str(e)}"
        )


# ============================================================
# ANALYZE RESUME
# ============================================================

if analyze:

    # --------------------------------------------------------
    # CHECK FILE
    # --------------------------------------------------------

    if not uploaded_file:

        st.warning(
            "Please upload a resume before clicking Analyze Resume."
        )

        st.stop()


    try:

        # ----------------------------------------------------
        # EXTRACT RESUME TEXT
        # ----------------------------------------------------

        with st.spinner("Reading your resume..."):

            file_content = extract_text_from_file(
                uploaded_file
            )


        # ----------------------------------------------------
        # CHECK CONTENT
        # ----------------------------------------------------

        if not file_content.strip():

            st.error(
                "The uploaded file is empty or could not be read. "
                "Please upload a valid PDF or TXT resume."
            )

            st.stop()


        # ----------------------------------------------------
        # LIMIT RESUME SIZE
        # ----------------------------------------------------

        MAX_RESUME_CHARACTERS = 20000

        if len(file_content) > MAX_RESUME_CHARACTERS:

            st.warning(
                "Your resume is very large. "
                "Only the first 20,000 characters will be analyzed."
            )

            file_content = file_content[
                :MAX_RESUME_CHARACTERS
            ]


        # ----------------------------------------------------
        # JOB ROLE
        # ----------------------------------------------------

        selected_job_role = (
            job_role.strip()
            if job_role.strip()
            else "General job application"
        )


        # ====================================================
        # PROMPT
        # ====================================================

        prompt = f"""
Analyze the following resume as an expert technical recruiter,
ATS specialist, and resume reviewer.

TARGET JOB ROLE:
{selected_job_role}


RESUME:
--------------------------------------------------
{file_content}
--------------------------------------------------


Provide a professional, honest, and practical analysis.

Use exactly the following sections:


## 1. Overall Assessment

Give a concise summary of the resume and its overall quality.


## 2. Strengths

Identify the strongest parts of the resume.

Mention specific strengths from the actual resume.


## 3. Areas for Improvement

Identify weaknesses in the resume.

Explain how each weakness can be improved.


## 4. Skills Analysis

Analyze the technical and soft skills.

Explain how relevant they are to the target job role.


## 5. Experience and Projects

Evaluate the candidate's experience and projects.

Consider:

- Technical skills
- Problem-solving ability
- Impact
- Measurable results
- Technologies used
- Relevance to the target role


## 6. ATS Optimization

Analyze the resume from an Applicant Tracking System perspective.

Identify:

- Missing keywords
- Weak keywords
- Formatting concerns
- Missing sections
- Weak bullet points
- Irrelevant information


## 7. Job-Specific Recommendations

Give specific recommendations for the target job role.

Suggest relevant improvements to:

- Skills
- Keywords
- Projects
- Experience descriptions
- Resume structure


## 8. Suggested Bullet Point Improvements

Identify weak bullet points from the resume.

Rewrite them to be stronger using:

- Action verbs
- Technical detail
- Measurable impact
- Clear outcomes

Only rewrite information that is supported by the
original resume.

DO NOT invent:

- Experience
- Skills
- Companies
- Qualifications
- Achievements
- Technologies
- Metrics


## 9. Final Verdict

Give a concise final assessment.

Include:

- Resume quality
- ATS readiness
- Job-role relevance
- Top 3 improvements the candidate should make first
"""


        # ====================================================
        # GEMINI INTERACTIONS API
        # ====================================================

        with st.spinner(
            "Gemini 3.6 Flash is analyzing your resume..."
        ):

            interaction = client.interactions.create(

                model="gemini-3.6-flash",

                input=prompt,

                system_instruction=(
                    "You are an expert technical recruiter, "
                    "ATS specialist, and professional resume reviewer. "
                    "Be accurate, constructive, and practical. "
                    "Never invent information that is not present "
                    "in the resume."
                )
            )


        # ====================================================
        # GET GEMINI RESPONSE
        # ====================================================

        feedback = interaction.output_text


        # ====================================================
        # DISPLAY RESULTS
        # ====================================================

        st.markdown(
            "### AI Feedback on Your Resume:"
        )

        if feedback:

            st.markdown(feedback)

        else:

            st.warning(
                "Gemini returned an empty response. "
                "Please try again."
            )


    # ========================================================
    # ERROR HANDLING
    # ========================================================

    except Exception as e:

        error_message = str(e)

        # ----------------------------------------------------
        # API KEY ERROR
        # ----------------------------------------------------

        if (
            "api key" in error_message.lower()
            or "authentication" in error_message.lower()
            or "unauthorized" in error_message.lower()
            or "permission denied" in error_message.lower()
        ):

            st.error(
                "Gemini API authentication failed."
            )

            st.info(
                "Please check your GEMINI_API_KEY "
                "in the .env file."
            )


        # ----------------------------------------------------
        # QUOTA / RATE LIMIT
        # ----------------------------------------------------

        elif (
            "429" in error_message
            or "quota" in error_message.lower()
            or "resource exhausted" in error_message.lower()
            or "rate limit" in error_message.lower()
        ):

            st.error(
                "Gemini API quota or rate limit reached."
            )

            st.info(
                "Please wait and try again later, "
                "or check your Gemini API usage."
            )


        # ----------------------------------------------------
        # MODEL NOT FOUND
        # ----------------------------------------------------

        elif (
            "404" in error_message
            or "not found" in error_message.lower()
            or "no longer available" in error_message.lower()
        ):

            st.error(
                "The Gemini model is unavailable for this API key."
            )

            st.info(
                "Make sure you are using the latest "
                "google-genai package and the model "
                "gemini-3.6-flash."
            )


        # ----------------------------------------------------
        # GENERIC ERROR
        # ----------------------------------------------------

        else:

            st.error(
                "An error occurred while analyzing the resume:"
            )

            st.code(
                error_message
            )


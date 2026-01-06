from flask import Flask, render_template, request
from utils.resume_parser import extract_text_from_pdf, extract_skills
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    match_score = None
    extracted_skills = []
    missing_skills = []
    jd_skills = []

    if request.method == "POST":
        resume_file = request.files.get("resume")
        jd = request.form.get("jd", "")

        # SAVE FILE
        resume_path = os.path.join(UPLOAD_FOLDER, resume_file.filename)
        resume_file.save(resume_path)

        # EXTRACT TEXT
        resume_text = extract_text_from_pdf(resume_path)

        # SKILL EXTRACTION
        extracted_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd)

        matched = set(extracted_skills) & set(jd_skills)

        if len(jd_skills) > 0:
            match_score = (len(matched) / len(jd_skills)) * 100
        else:
            match_score = 0

        missing_skills = list(set(jd_skills) - set(extracted_skills))

    return render_template(
        "index.html",
        match_score=match_score,
        extracted_skills=extracted_skills,
        jd_skills=jd_skills,
        missing_skills=missing_skills
    )

if __name__ == "__main__":
    app.run(debug=True)

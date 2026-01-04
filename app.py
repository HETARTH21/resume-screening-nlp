from flask import Flask, render_template, request
from utils.resume_parser import extract_text_from_pdf, extract_skills
from utils.matcher import calculate_match_score

app = Flask(__name__)

# Skill database
skills = [
    "python", "java", "c++", "sql", "machine learning",
    "data analysis", "nlp", "flask", "git", "linux"
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # Get job description text
        jd = request.form["jd"]

        # Get uploaded resume
        resume_file = request.files["resume"]
        resume_text = extract_text_from_pdf(resume_file)

        # Extract skills
        extracted_skills = extract_skills(resume_text, skills)
        jd_skills = extract_skills(jd, skills)

        # Text similarity score
        match_score = calculate_match_score(resume_text, jd)

        # Skill match score
        if len(jd_skills) > 0:
            skill_match_score = round(
                (len(set(extracted_skills) & set(jd_skills)) / len(jd_skills)) * 100, 2
            )
        else:
            skill_match_score = 0

        # Missing skills
        missing_skills = list(set(jd_skills) - set(extracted_skills))

        return render_template(
            "index.html",
            score=match_score,
            skill_score=skill_match_score,
            skills=extracted_skills,
            jd_skills=jd_skills,
            missing=missing_skills
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
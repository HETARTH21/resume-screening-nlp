import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text.lower()

def extract_skills(text):
    skills = [
        "python", "java", "c++", "sql",
        "machine learning", "data analysis",
        "nlp", "flask", "git", "linux"
    ]

    text = text.lower()
    found = []

    for skill in skills:
        if skill in text:
            found.append(skill)

    return found

def extract_skills(text):
    skills_list = [
        "python", "java", "c++", "sql", "machine learning",
        "data analysis", "nlp", "flask", "git", "linux"
    ]

    text = text.lower()
    extracted = []

    for skill in skills_list:
        if skill in text:
            extracted.append(skill)

    return extracted

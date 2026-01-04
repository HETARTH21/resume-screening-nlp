import re

def extract_skills(text, skill_list):
    text = text.lower()
    extracted_skills = []

    for skill in skill_list:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, text):
            extracted_skills.append(skill)

    return extracted_skills

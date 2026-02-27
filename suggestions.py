def missing_skills(resume_skills, job_skills):
    return list(set(job_skills) - set(resume_skills))

def suggestions(missing):
    if not missing:
        return "Your resume matches the job well."

    text = "To improve your resume, add these skills:\n"
    for skill in missing:
        text += f"- {skill}\n"

    return text
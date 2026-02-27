from read_resume import read_resume
from skill_extractor import extract_skills
from matcher import match_score
from suggestions import missing_skills, suggestions
import nltk

# read resume
resume_text = read_resume("resume.pdf")

# read job description
with open("job_description.txt","r",encoding="utf-8") as f:
    job_text = f.read()

# extract skills
resume_sk = extract_skills(resume_text)
job_sk = extract_skills(job_text)

print("Resume Skills:", resume_sk)
print("Job Skills:", job_sk)

# match score
score = match_score(resume_sk, job_sk)
print("\nMatch Score:", score,"%")

# missing skills
missing = missing_skills(resume_sk, job_sk)
print("\nMissing Skills:", missing)

print("\nSuggestions:")
print(suggestions(missing))
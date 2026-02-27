from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def match_score(resume_skills, job_skills):
    resume_vec = model.encode([" ".join(resume_skills)])
    job_vec = model.encode([" ".join(job_skills)])

    score = cosine_similarity(resume_vec, job_vec)[0][0]
    return round(score * 100,2)
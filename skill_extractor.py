import re

SKILLS_DB = [
    "machine learning",
    "statistics",
    "predictive modeling",
    "model evaluation",
    "hypothesis testing",
    "data modeling",
    "data analysis",
    "exploratory data analysis",
    "data exploration",
    "data interpretation",
    "analytical thinking",
    "problem solving",
    "insight generation",
    "python",
    "programming",
    "data structures",
    "algorithms",
    "data processing",
    "product analytics",
    "business analytics",
    "customer analytics",
    "model validation",
    "performance monitoring",
    "model improvement",
    "nlp",
    "power bi",
    "tableau",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "aws",
    "communication"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if re.search(r'\b' + skill + r'\b', text):
            found_skills.append(skill)

    return list(set(found_skills))
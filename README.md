# AI-Resume-Analyzer-ATS-Skill-Matcher
An intelligent AI-powered Resume Screening System that analyzes a candidate’s resume against a job description and calculates how well the resume matches the role — similar to how real Applicant Tracking Systems (ATS) used by companies work.

The system extracts skills automatically from both the resume and the job description, identifies missing skills, and gives improvement suggestions.

1. Problem Statement: Recruiters receive hundreds of resumes for a single job posting. Companies therefore use ATS (Applicant Tracking Systems) to automatically filter resumes before a human even reads them.

Many good candidates get rejected simply because: keywords are missing, resume is not optimized, skills don’t align with job description

This project simulates a real ATS and helps candidates improve their resume before applying.
2. Technologies Used: Python, NLP, Sentence Transformers, Scikit-learn, PyTorch, PDF Parsing
3. AI / NLP Techniques Used: Natural Language Processing (NLP)
                             Sentence Embeddings
                             Semantic Similarity Matching
                             Keyword Extraction
                             Resume Parsing
                             Cosine Similarity
This model understands meaning, not just keywords. So even if wording is different, it still recognizes similar skills.
4. Project Architecture
main.py
│
├── read_resume.py        → Extracts text from PDF resume
├── skill_extractor.py    → Extracts skills using skill database
├── matcher.py            → Calculates semantic similarity
├── suggestions.py        → Suggests missing skills
└── SKILLS_DB             → Predefined technical skill list
5. Workflow: User uploads resume (PDF) -> User provides job description -> Resume text is extracted -> Skills are extracted from both texts -> AI model calculates similarity score -> System outputs(Match percentage, Missing skills, Suggestions to improve resume)
6. Required Libraries: numpy==1.26.4, torch==2.2.2, sentence-transformers, transformers, scikit-learn, pypdf, safetensors

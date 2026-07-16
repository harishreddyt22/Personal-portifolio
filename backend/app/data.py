"""
Single source of truth for all portfolio content.

Edit the values below to update your links, experience, projects,
skills, education, and certificates. The FastAPI routers in
`app/routers/` read directly from this file, and the frontend fetches
it over the API — so you only ever edit content in ONE place.
"""

# ---- SOCIAL / PROFILE LINKS ------------------------------------------------
# TODO: replace with your real profile URLs.
SOCIALS = [
    {"label": "GitHub", "icon": "github", "url": "https://github.com/harishreddyt22"},
    {"label": "Kaggle", "icon": "kaggle", "url": "https://www.kaggle.com/tharishreddy22"},
    {"label": "Google Developer Profile", "icon": "google", "url": "https://g.dev/YOUR_USERNAME"},
    {"label": "LinkedIn", "icon": "linkedin", "url": "https://www.linkedin.com/in/harish-reddy-aaa0b2260/"},
]

# ---- HERO TYPED ROLES -------------------------------------------------------
TYPED_ROLES = [
    "Software Engineer at Andor Tech",
    "AI & ML Tech focused",
    "GenAI & ML Researcher",
    "Agentic AI Systems Builder",
]

# ---- EXPERIENCE (newest first) ---------------------------------------------
EXPERIENCE = [
    {

        "role": "Software Engineer (Full-time)",
        "company": "Andor Tech",
        "location": "Bengaluru, India",
        "date": "Jun 2026 — Present",
        "current": True,
        "bullets": [
            "Promoted to a full-time engineering role after two internship cycles, now owning end-to-end delivery of AI-driven product features rather than individual workstreams.",
            "Designing and scaling LLM-agent and RAG pipelines from prototype to production, with a focus on reliability, latency, and evaluation of model outputs.",
            "Driving the team's shift toward applied AI/ML research — reading recent papers, running small-scale experiments, and feeding findings back into production systems.",
            "Mentoring incoming interns on the same OCR/RAG/embeddings stack the team relies on.",
        ],
        "skills": ["Python", "LLM Agents", "RAG", "System Design", "Evaluation"],
    },
    {
    
        "role": "Trainee Data Engineer (Intern)",
        "company": "Andor Tech",
        "location": "Bengaluru, India",
        "date": "Dec 2025 — May 2026",
        "current": False,
        "bullets": [
            "Developed AI-driven systems using LLMs with agent-based architectures to automate complex workflows and decision-making tasks.",
            "Implemented Retrieval-Augmented Generation (RAG) pipelines for semantic search and context-aware Q&A over structured and unstructured datasets.",
            "Built document processing pipelines using OCR (Tesseract) to extract and structure data from PDFs and scanned documents.",
            "Worked with Vision-Language Models (VLMs) for combined text and image understanding.",
            "Designed embedding pipelines and vector similarity search for efficient information retrieval.",
        ],
        "skills": ["LLMs", "RAG", "AI Agents", "VLMs", "OCR", "Vector DBs"],
    },
    {
    
        "role": "Trainee Data Engineer",
        "company": "Andor Tech",
        "location": "Bengaluru, India",
        "date": "May 2025 — Oct 2025",
        "current": False,
        "bullets": [
            "Built and optimized data workflows with Python, Pandas, and PySpark across large-scale, distributed datasets.",
            "Designed ETL pipelines for smooth ingestion, transformation, and loading across multiple systems.",
            "Prepared datasets for ML models using Spark MLlib; contributed to early predictive-analytics work.",
            "Delivered analysis and visualization with Pandas and Matplotlib for business and technical stakeholders.",
            "Supported MySQL and PostgreSQL database operations.",
        ],
        "skills": ["PySpark", "Pandas", "ETL", "Spark MLlib", "MySQL/Postgres"],
    },
    {

        "role": "Student Research Intern",
        "company": "MURTI Research Center",
        "location": "Bengaluru, India",
        "date": "Jan 2025 — Mar 2025",
        "current": False,
        "bullets": [
            "Researched the Urban Heat Island (UHI) effect via Google Scholar and OpenAthens to identify key environmental drivers.",
            "Processed satellite imagery and geospatial data using Google Earth Engine and ArcMap.",
            "Built a Random Forest Regression model to predict and map UHI hotspots for climate adaptation planning.",
        ],
        "skills": ["Random Forest", "Google Earth Engine", "ArcMap", "Geospatial"],
    },
]

# ---- PROJECTS ---------------------------------------------------------------
PROJECTS = [
    {
        "title": "Lung CT: Normal vs. Cancer Classification",
        "blurb": "CNN-based classification of lung CT scans, benchmarking VGG16, ResNet50 and DenseNet architectures for cancer detection.",
        "metrics": [
            {"value": "98.75%", "label": "accuracy (DenseNet)"},
            {"value": "100%", "label": "recall / sensitivity"},
            {"value": "98.7%", "label": "F1-score"},
        ],
        "tags": ["Python", "CNN", "VGG16", "ResNet50", "DenseNet"],
    },
    {
        "title": "AI Supply Chain Control Tower",
        "blurb": "End-to-end system predicting logistics disruptions 24–48h in advance and dynamically re-routing shipments in real time.",
        "metrics": [
            {"value": "10M+", "label": "records ingested"},
            {"value": "24–48h", "label": "risk-prediction lead time"},
            {"value": "RL", "label": "policy-based routing"},
        ],
        "tags": ["Random Forest", "Gradient Boosting", "Reinforcement Learning", "Flask", "WebSockets", "Docker", "Kubernetes"],
    },
    {
        "title": "Urban Heat Island Analysis — Bengaluru",
        "blurb": "Random Forest regression over satellite and geospatial data to map and predict Bengaluru's urban heat hotspots.",
        "metrics": [
            {"value": "95%", "label": "model accuracy"},
            {"value": "0.94", "label": "R² score"},
            {"value": "1.8", "label": "RMSE"},
        ],
        "tags": ["Random Forest", "Google Earth Engine", "ArcMap"],
    },
]

# ---- SKILLS -----------------------------------------------------------------
SKILLS = [
    {"group": "Languages", "items": ["Python"]},
    {"group": "GenAI / LLM", "items": ["LLM Agents", "RAG", "VLMs", "Embeddings", "Vector Databases", "Prompt Engineering"]},
    {"group": "ML / Deep Learning", "items": ["CNNs (VGG16, ResNet50, DenseNet)", "Random Forest", "Gradient Boosting", "Spark MLlib", "Reinforcement Learning (basics)"]},
    {"group": "Data Engineering", "items": ["PySpark", "Pandas", "ETL Pipelines", "OCR (Tesseract)"]},
    {"group": "Systems", "items": ["Flask", "WebSockets", "Docker", "Kubernetes"]},
    {"group": "Databases", "items": ["MySQL", "PostgreSQL"]},
    {"group": "Visualization & Tools", "items": ["Matplotlib", "PyCharm", "pgAdmin"]},
]

# ---- EDUCATION ---------------------------------------------------------------
EDUCATION = [
    {
        "school": "Gandhi Institute Of Technology And Management",
        "degree": "B.Tech, CSE (AI & ML)",
        "date": "Aug 2022 — April 2026",
        "location": "Bengaluru",
    },
    {
        "school": "Mother Teresa Junior College",
        "degree": "Board of Intermediate Education",
        "date": "Jun 2020 — May 2022",
        "location": "Palamaner",
    },
    {
        "school": "Vijaya Vani (EM) High School",
        "degree": "Board of Secondary Education",
        "date": "Jun 2019 — Mar 2020",
        "location": "Chowdepalli",
    },
]

# ---- CERTIFICATIONS ----------------------------------------------------------
# `filename` must match a file you place inside `static/certificates/`.
# If the file isn't there yet, the API reports it as unavailable and the
# frontend falls back to the `link` field instead.
CERTIFICATES = [
    {
        "id": "python-for-everybody",
        "title": "Programming for Everybody (Getting Started with Python)",
        "issuer": "University of Michigan · Coursera",
        "filename": "python-for-everybody.pdf",
        "link": "",  # TODO: paste your certificate verification link here
    },
    {
        "id": "python-data-science-ai",
        "title": "Python for Data Science, AI and Development",
        "issuer": "IBM · Coursera",
        "filename": "python-data-science-ai.pdf",
        "link": "",  # TODO: paste your certificate verification link here
    },
]

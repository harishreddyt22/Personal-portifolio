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
    {"label": "LinkedIn", "icon": "linkedin", "url": "https://www.linkedin.com/in/harish-reddy-aaa0b2260/"},
    {"label": "Kaggle", "icon": "kaggle", "url": "https://www.kaggle.com/tharishreddy22"},
    {"label": "GitHub", "icon": "github", "url": "https://github.com/harishreddyt22"},
    {"label": "Credly", "icon": "credly", "url": "https://www.credly.com/users/t-harish-reddy"},
]

# ---- EMAILJS CONTACT CONFIG -------------------------------------------------
# Add your EmailJS service/template/public key values here.
EMAILJS_CONFIG = {
    "service_id": "service_wkjmrxg",
    "template_id": "template_un10llt",
    "public_key": "EOLKS6dxRrhSAIEGr",
}

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
     " Promoted to a full-time engineering role after two internship cycles, taking ownership of end-to-end development of AI-driven engineering solutions and production-ready features.",
" Built agentic AI workflows using LLMs, RAG, and embeddings for engineering use cases, improving automation, document understanding, and intelligent decision-making.",
" Worked extensively with ANSYS Mechanical using PyMechanical, PyMAPDL, PyAnsys Core, and PyVista to extract simulation data, process raw engineering outputs, and generate interactive 3D visualizations for deeper analysis.",
" Applied machine learning algorithms to ANSYS simulation datasets to identify patterns, cluster engineering results, and transform raw simulation data into actionable insights for engineering workflows.",
" Contributed to applied AI/ML research by evaluating recent techniques, running experiments, and integrating validated approaches into production systems to improve performance and reliability.",
   ],
        "skills": ["Python", "LLM Agents", "RAG", "PyMAPDL", "Pyvista", "Machine Learning", "Applied Research"],
    },
    {
    
        "role": "Trainee Data Engineer (Intern)",
        "company": "Andor Tech",
        "location": "Bengaluru, India",
        "date": "Dec 2025 — June 2026",
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
    
        "role": "Trainee Data Engineer (Intern)",
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

        "role": "Student Research (Intern)",
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
        "title": "Horizon Bank Validator & AI Agent (ARIA)",
        "blurb": "AI-powered banking platform for automated document validation and intelligent document Q&A using RAG, LangGraph, and LLMs. Features parallel document validation, compliance reporting, semantic retrieval, and an interactive AI assistant.",
        "metrics": [
            {"value": "4+", "label": "bank form types supported"},
            {"value": "RAG", "label": "context-aware document retrieval"},
            {"value": "AI", "label": "automated validation & compliance"},
        ],
        "tags": [
            "Python",
            "Flask",
            "LangGraph",
            "RAG",
            "ChromaDB",
            "SentenceTransformers",
            "Qwen2.5",
            "LlamaIndex",
            "Docling",
            "Ocr",
        ],
    },

    {
        "title": "AI Supply Chain Control Tower",
        "blurb": "End-to-end system predicting logistics disruptions 24–48h in advance and dynamically re-routing shipments in real time. Integrated machine learning models with real-time analytics dashboards to optimize delivery efficiency, reduce delays, and improve supply chain resilience.",
        "metrics": [
            {"value": "10M+", "label": "records ingested"},
            {"value": "24–48h", "label": "risk-prediction lead time"},
            {"value": "RL", "label": "policy-based routing"},
        ],
        "tags": ["Python","Random Forest", "Gradient Boosting","Logistic Regression", "Reinforcement Learning", "Flask", "PostgreSQL", "Matplotlib"],
    },
{
    "title": "Urban Heat Island Analysis — Bengaluru",
    "blurb": "Developed a geospatial AI pipeline to analyze and predict Urban Heat Island (UHI) intensity across Bengaluru using satellite imagery and environmental datasets. Processed multi-temporal remote sensing data in Google Earth Engine, performed spatial analysis in ArcMap, and applied Random Forest Regression to model land surface temperature (LST) and identify urban heat hotspots.",
    "metrics": [
        {"value": "95%", "label": "model accuracy"},
        {"value": "0.94", "label": "R² score"},
        {"value": "1.8", "label": "RMSE"},
    ],
    "tags": [
        "Python",
        "Random Forest",
        "Google Earth Engine",
        "ArcMap",
        "Remote Sensing",
        "Landsat",
        "Geospatial AI"
    ],
},
]

# ---- SKILLS -----------------------------------------------------------------
SKILLS = [
    {"group": "Languages", "items": ["Python"]},
    {"group": "GenAI / LLM", "items": ["LLM Agents", "RAG", "VLMs", "Embeddings", "Vector Databases", "LangChain", "LlamaIndex"]},
    {"group": "ML / Deep Learning", "items": ["CNNs (VGG16, ResNet50, DenseNet)","PyTorch", "Time series and forecasting", "Random Forest", "Gradient Boosting", "Spark MLlib"]},
    {"group": "Data Engineering", "items": ["PySpark", "Pandas", "ETL Pipelines"]},
   # {"group": "Systems", "items": ["Flask", "WebSockets", "Docker", "Kubernetes"]},
    {"group": "Databases", "items": ["MySQL", "PostgreSQL", "MongoDB (Basics)", "Redis (Basics)"]},
    {"group": "Visualization & Tools", "items": ["Matplotlib", "PyCharm", "pgAdmin", "VS Code", "Jupyter Notebook", "Spyder", "Google Earth Engine", "ArcMap"]},
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
        "link": "https://www.coursera.org/account/accomplishments/verify/EZB8ZU7PGZZZ",  # TODO: paste your certificate verification link here
    },
    {
        "id": "python-data-science-ai",
        "title": "Python for Data Science, AI and Development",
        "issuer": "IBM · Coursera",
        "filename": "python-data-science-ai.pdf",
        "link": "https://www.coursera.org/account/accomplishments/verify/64QDFCTWFFB6?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=pdf_header_button&utm_product=course",  # TODO: paste your certificate verification link here
    },
        {
        "id": "Introduction to Data Engineering on Google Cloud",
        "title": "Introduction to Data Engineering on Google Cloud",
        "issuer": "Google Cloud",
        "filename": "Introduction to Data Engineering on Google Cloud.pdf",
        "link": "https://www.skills.google/public_profiles/88fd161b-65fb-4f85-9d71-06e379dc0916/badges/19211514?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share",  # TODO: paste your certificate verification link here
    },
        
        
        {
        "id": "Data Engineering Course Online - With Hadoop and Spark",
        "title": "Data Engineering Course Online - With Hadoop and Spark",
        "issuer": "GeeksforGeeks",
        "filename": "Data Engineering Course Online - With Hadoop and Spark.pdf",
        "link": "https://media.geeksforgeeks.org/courses/certificates/c45779be13451908b23e6327ab1d7932.pdf",  # TODO: paste your certificate verification link here
    },
             
             
        {
        "id": "Introduction to Artificial Intelligence (AI)",
        "title": "Introduction to Artificial Intelligence (AI)",
        "issuer": "IBM · Coursera",
        "filename": "Introduction to Artificial Intelligence (AI).pdf",
        "link": "https://www.coursera.org/account/accomplishments/verify/LWRUGGF2X7YD"
                  
        },          
                  
        {
        "id": "PyTorch Bootcamp",
        "title": "PyTorch Bootcamp",
        "issuer": "OpenCv University",
        "filename": "PyTorch Bootcamp.pdf",
        "link": "https://courses.opencv.org/certificates/eaf27c7a8b8c4772a1d6fc65d56a4806"
    },
        
            {
        "id": "Vision Language Models (VLM) Bootcamp",
        "title": "Vision Language Models (VLM) Bootcamp",
        "issuer": "OpenCv University",
        "filename": "Vision Language Models (VLM) Bootcamp.pdf",
        "link": "https://courses.opencv.org/certificates/21a904e88ea84115a8f8b5934d63b141"
    },
            
            
                {
        "id": "Develop GenAI Apps with Gemini and Streamlit",
        "title": "Develop GenAI Apps with Gemini and Streamlit",
        "issuer": "GOOGLE CLOUD",
        "filename": "Develop GenAI Apps with Gemini and Streamlit.pdf",
        "link": "https://www.credly.com/badges/8369e18d-48db-4cf1-b9b4-b939bca65426/linked_in_profile"
    },
                
                    {
        "id": "Inspect Rich Documents with Gemini Multimodality and Multimodal RAG",
        "title": "Inspect Rich Documents with Gemini Multimodality and Multimodal RAG",
        "issuer": "GOOGLE CLOUD",
        "filename": "Inspect Rich Documents with Gemini Multimodality and Multimodal RAG.pdf",
        "link": "https://www.credly.com/badges/cc3907ee-01e8-4ab2-9b8c-1686c87c76c9/linked_in_profile"
                    },
                    
]






# Harish Reddy — Portfolio (FastAPI + HTML/CSS/JS)

A personal portfolio site: FastAPI backend serving your résumé, certificates,
and profile content over a small JSON API, with a vanilla HTML/CSS/JS
frontend consuming it. Dark, code-editor-inspired design with an animated
neural-net backdrop, a typed hero terminal, a git-log style experience
timeline, and an in-page certificate viewer.

```
portfolio-app/
├── backend/
│   ├── app/
│   │   ├── main.py            FastAPI app + static mounts
│   │   ├── data.py            ← EDIT THIS to update all content
│   │   └── routers/
│   │       ├── profile.py     GET /api/profile
│   │       ├── certificates.py GET /api/certificates, GET /api/certificates/{id}/file
│   │       └── resume.py      GET /api/resume
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js              fetches everything from /api/*
├── static/
│   ├── resume/
│   │   └── Harish_Reddy_Resume.pdf
│   └── certificates/
│       └── README.md          how to add certificate files
└── README.md                  you are here
```

## Run it

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# launch the site from the project root:
python main.py
```

Open **http://127.0.0.1:8000** in a browser. The frontend is served at `/`,
and the API lives under `/api` (interactive docs at `/docs`).

## Editing content

Everything — experience, projects, skills, education, socials, and
certificate metadata — lives in **`backend/app/data.py`**. Edit that one
file and refresh the browser; there's no separate copy to keep in sync on
the frontend.

Three things you should personalize before sharing this:

1. **Social links** — `SOCIALS` near the top of `data.py`: swap in your real
   GitHub, Kaggle, Google Developer Profile, and LinkedIn URLs.
2. **Software Engineer role bullets** — `EXPERIENCE[0]["bullets"]`: written
   as a reasonable placeholder continuing your LLM/RAG/agent work; edit to
   match what you're actually doing.
3. **Certificates** — drop PDFs/images into `static/certificates/` (see the
   README there) matching the `filename` fields in `CERTIFICATES`, and add
   new entries for anything new (e.g. an Andor Tech certificate).

## API reference

| Method | Path | Description |
|---|---|---|
| GET | `/api/profile` | socials, typed roles, experience, projects, skills, education |
| GET | `/api/certificates` | certificate metadata + `available` flag per cert |
| GET | `/api/certificates/{id}/file` | streams the certificate file (404 if not uploaded) |
| GET | `/api/resume` | downloads the résumé PDF |

## Deploying

Any host that runs a Python ASGI app works (Render, Railway, Fly.io, a VPS
with `uvicorn`/`gunicorn`). Point the start command at
`uvicorn app.main:app --host 0.0.0.0 --port $PORT` from inside `backend/`,
and make sure the `static/` and `frontend/` folders are deployed alongside
`backend/` (the app resolves paths relative to the project root).

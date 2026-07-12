"""
FastAPI backend for Harish Reddy's portfolio site.

Run from the project root with:
    uvicorn backend.app.main:app --reload

Then open http://127.0.0.1:8000 in a browser.
"""
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .routers import certificates, profile, resume

# backend/app/main.py -> project_root
PROJECT_ROOT = Path(__file__).resolve().parents[2]
FRONTEND_DIR = PROJECT_ROOT / "frontend"
STATIC_DIR = PROJECT_ROOT / "static"

app = FastAPI(
    title="Harish Reddy — Portfolio API",
    description="Serves portfolio content, résumé, and certificates.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- API routes (must be registered before the catch-all frontend mount) ---
app.include_router(profile.router, prefix="/api")
app.include_router(certificates.router, prefix="/api")
app.include_router(resume.router, prefix="/api")

# ---- static asset mounts -----------------------------------------------------
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# ---- frontend (index.html, style.css, script.js) — mounted last as a catch-all
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")

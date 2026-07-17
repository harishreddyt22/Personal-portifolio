from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(tags=["resume"])

# backend/app/routers/resume.py -> project_root/static/resume
RESUME_DIR = Path(__file__).resolve().parents[3] / "static" / "resume"
RESUME_FILENAME = "Harish_Reddy_Resume.pdf"


@router.get("/resume")
def view_resume():
    """Serve the résumé PDF inline so it can be previewed in the browser/iframe."""
    file_path = RESUME_DIR / RESUME_FILENAME
    if not file_path.is_file():
        raise HTTPException(status_code=404, detail="Resume file not found on server")
    return FileResponse(
        file_path,
        media_type="application/pdf",
        filename=RESUME_FILENAME,
        content_disposition_type="inline",
    )


@router.get("/resume/download")
def download_resume():
    """Serve the résumé PDF as a forced download."""
    file_path = RESUME_DIR / RESUME_FILENAME
    if not file_path.is_file():
        raise HTTPException(status_code=404, detail="Resume file not found on server")
    return FileResponse(
        file_path,
        media_type="application/pdf",
        filename=RESUME_FILENAME,
        content_disposition_type="attachment",
    )
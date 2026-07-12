from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from ..data import CERTIFICATES

router = APIRouter(tags=["certificates"])

# backend/app/routers/certificates.py -> project_root/static/certificates
CERT_DIR = Path(__file__).resolve().parents[3] / "static" / "certificates"


@router.get("/certificates")
def list_certificates():
    """List all certificates with a flag for whether the file has been uploaded yet."""
    results = []
    for cert in CERTIFICATES:
        file_path = CERT_DIR / cert["filename"]
        available = file_path.is_file()
        results.append(
            {
                **cert,
                "available": available,
                "file_url": f"/api/certificates/{cert['id']}/file" if available else None,
            }
        )
    return results


@router.get("/certificates/{cert_id}/file")
def get_certificate_file(cert_id: str):
    """Stream the certificate file (PDF or image) for the in-page viewer."""
    cert = next((c for c in CERTIFICATES if c["id"] == cert_id), None)
    if cert is None:
        raise HTTPException(status_code=404, detail="Unknown certificate id")

    file_path = CERT_DIR / cert["filename"]
    if not file_path.is_file():
        raise HTTPException(
            status_code=404,
            detail=f"'{cert['filename']}' hasn't been uploaded to static/certificates/ yet",
        )
    return FileResponse(file_path)

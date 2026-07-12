from fastapi import APIRouter

from ..data import EDUCATION, EXPERIENCE, PROJECTS, SKILLS, SOCIALS, TYPED_ROLES

router = APIRouter(tags=["profile"])


@router.get("/profile")
def get_profile():
    """Return every content block the frontend needs in one call."""
    return {
        "socials": SOCIALS,
        "typed_roles": TYPED_ROLES,
        "experience": EXPERIENCE,
        "projects": PROJECTS,
        "skills": SKILLS,
        "education": EDUCATION,
    }

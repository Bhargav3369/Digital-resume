"""
Schemas package initialization.
"""
from api.schemas.profile import ProfileSchema, ProfileCreate, ProfileUpdate
from api.schemas.research import ResearchSchema, ResearchCreate, ResearchUpdate
from api.schemas.education import EducationSchema, EducationCreate, EducationUpdate
from api.schemas.skill import SkillSchema, SkillCreate, SkillUpdate
from api.schemas.project import ProjectSchema, ProjectCreate, ProjectUpdate
from api.schemas.contact import ContactSchema, ContactCreate
from api.schemas.analytics import PageViewSchema, PageViewCreate, AnalyticsStats

__all__ = [
    "ProfileSchema", "ProfileCreate", "ProfileUpdate",
    "ResearchSchema", "ResearchCreate", "ResearchUpdate",
    "EducationSchema", "EducationCreate", "EducationUpdate",
    "SkillSchema", "SkillCreate", "SkillUpdate",
    "ProjectSchema", "ProjectCreate", "ProjectUpdate",
    "ContactSchema", "ContactCreate",
    "PageViewSchema", "PageViewCreate", "AnalyticsStats",
]

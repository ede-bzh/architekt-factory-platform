"""Architekt doctrine skills are indexed in the skill library."""

from platform.skills.library import get_skill_library

_EXPECTED = {
    "architekt-ai-governance",
    "architekt-archi",
    "architekt-commercial",
    "architekt-compliance",
    "architekt-data",
    "architekt-delivery",
    "architekt-finops",
    "architekt-i18n",
    "architekt-product",
    "architekt-qa",
    "architekt-security",
    "architekt-sre",
    "architekt-tech",
    "architekt-ux",
}


def test_all_architekt_skills_indexed():
    lib = get_skill_library()
    lib.scan_all()
    found = {sid for sid in lib._cache if sid.startswith("architekt-")}
    assert found == _EXPECTED

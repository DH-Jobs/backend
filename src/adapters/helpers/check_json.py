from typing import Dict, List


def check_json_structure(json_data: Dict[str, object]) -> bool:
    expected_keys = {"id", "name", "birthdate", "userQualifications"}
    expected_user_qual_keys = {"resume", "role", "range_salary", "skills"}
    expected_skills_keys = {"tech", "years"}

    # Check if all expected keys are present in the JSON
    if not expected_keys.issubset(json_data.keys()):
        return False

    # Check if all userQualifications keys are present and have the expected structure
    user_qual = json_data.get("userQualifications", {})
    if not expected_user_qual_keys.issubset(user_qual.keys()):
        return False
    if not isinstance(user_qual.get("resume"), str):
        return False
    if not isinstance(user_qual.get("role"), str):
        return False
    if not isinstance(user_qual.get("range_salary"), str):
        return False
    if not isinstance(user_qual.get("skills"), list):
        return False
    for skill in user_qual.get("skills", []):
        if not expected_skills_keys.issubset(skill.keys()):
            return False
        if not isinstance(skill.get("tech"), str):
            return False
        if not isinstance(skill.get("years"), str):
            return False

    return True

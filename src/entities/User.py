from typing import Dict, List


class UserQualifications(Dict[str, object]):
    resume: str
    role: str
    range_salary: str
    skills: List[Dict[str, str]]
    # array of techs and years have been experience


class User(Dict[str, object]):
    id: str
    name: str
    lastname: str
    birthdate: str
    userQualifications: UserQualifications


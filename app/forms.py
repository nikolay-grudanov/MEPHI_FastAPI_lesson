from pydantic import BaseModel


class UserNameParts(BaseModel):
    lastName: str
    firstName: str
    middleName: str

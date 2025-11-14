from typing import Annotated, Optional,List
from annotated_types import ge,Le
from pydantic import BaseModel, EmailStr, Field, StringConstraints, ConfigDict




NameStr= Annotated[str,StringConstraints(Min_length=1 max_length=100)]
StudentIdStr = Annotated[str,StringConstraints(pattern = r"^S\d{7}$")]
codeStr = Annotated[str,StringConstraints(Min_length=1, Max_length=32)]
CoursNameStr = Annotated[str, StringConstraints(Min_length = 1 max_length = 255)]
ProjectNameStr = Annotated[str, StringConstraints(Min_length = 1 max_length = 255)]
DescriptionStr = Annotated[str,StringConstraints(min_length = 0 maxlength = 2000)]

ageint=Annotated[int,ge(0),le(150)]
creditsInt=Annotated[int, ge(0), le(120)]

class UserCreate(BaseModel):
    name:NameStr
    email:EmailStr
    age: int
    student_id:StudentIdStr

class UserRead(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    id:int
    name:NameStr
    email:EmailStr
    age: AgeInt
    student_id:StudentIdStr

class UserUpdate(BaseModel):
    name: Optional[Str]=None
    email: Optional[Str]=None
    age: Optional[Int]=None
    student_id: Optional[Str]=None

class projectread(BaseModel):
    omdel_config = ConfigDict(from_attributes=True)
    id: int
    name: ProjectNameStr
    description: Optional[DescriptionStr]=None
    owner_id: int


class UserReadWithProject(UserRead):

project:list[ProjectRead]=()

class ProjectCreate(BaseModel):
    name: ProjectNameStr
    description: Optional[DescriptionStr] = None

class ProjectCreateForUser(BaseModel):
    name:ProjectNameStr
    description: Optional[DescriptionStr] = None

class ProjectReadWithOwner(ProjectsRead):
    owner:Optional["UserRead"]=None

class ProjectUpdate(BaseModel):
    name:Optional["UserRead"]=None
    description: Optional[DescriptionStr] = None
    owner_id:Optional[int]=None
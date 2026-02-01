from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email : EmailStr
    fullname : str
    
    
class UserCreate(UserBase):
    password:str
    
    
class UserUpdate(BaseModel):
    fullname: Optional[str]=None
    email:Optional[EmailStr]=None
    password: Optional[str]=None
    
    
class UserOut(UserBase):
    id :int
    is_admin:bool
    is_active:bool
    created_at:datetime
    
    model_config =ConfigDict(from_attributes=True)
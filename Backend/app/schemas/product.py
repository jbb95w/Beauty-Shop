from pydantic import BaseModel, ConfigDict
from typing import Optional
from app.schemas.category import CategoryOut


class ProductBase(BaseModel):
    name :str
    description :Optional[str]=None
    price : float
    stock_qty :int
    category_id : int
    
    
class ProductCreate(ProductBase):
    image_url : Optional[str]= None
    
    
class ProductOut(BaseModel):
    id :int
    image_url: Optional[str] = None
    category: Optional[CategoryOut] = None 
    
    model_config = ConfigDict(from_attributes=True)
    
    
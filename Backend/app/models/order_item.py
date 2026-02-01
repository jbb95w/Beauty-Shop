from sqlalchemy import Column,String,Integer,Boolean,DateTime,ForeignKey,Numeric
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy.sql import func

class Order_item(Base):
    __tablename__= "order_items"
    
    id = Column(Integer, primary_key=True,index=True)
    #linking it with orders and products
    order_id =Column(Integer,ForeignKey("orders.id"))
    product_id =Column(Integer,ForeignKey("products.id"))
    quantity = Column(Integer)
    price_at_purchase= Column(Numeric(10,2))
    
    #relationships
    order = relationship("Order", back_populates="items")
    product = relationship("Product")
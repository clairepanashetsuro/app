# from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
# from sqlalchemy.sql import func
# from database import Base 

# class Sale(Base):
#     __tablename__ = "sales"

#     sale_id = Column(Integer, primary_key=True, index=True)
#     transaction_number = Column(String, nullable=False, unique=True, index=True)
#     sale_datetime = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
#     user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
#     customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=True)
#     terminal_id = Column(String, nullable=False)
#     subtotal = Column(Numeric(10, 2), nullable=False)
#     discount_amount = Column(Numeric(10, 2), nullable=False, default=0.00)
#     tax_amount = Column(Numeric(10, 2), nullable=False)
#     total_amount = Column(Numeric(10, 2), nullable=False)
#     payment_method = Column(String, nullable=False)  
#     status = Column(String, nullable=False, default="Completed")  

from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Sale(Base):
    __tablename__ = "sales"

    sale_id = Column(Integer, primary_key=True, index=True)
    transaction_number = Column(String, nullable=False, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    terminal_id = Column(String, nullable=False)
    subtotal = Column(Numeric(10, 2), nullable=False)
    discount_amount = Column(Numeric(10, 2), nullable=False, default=0.0)
    tax_amount = Column(Numeric(10, 2), nullable=False, default=0.0)
    total_amount = Column(Numeric(10, 2), nullable=False)
    payment_method = Column(String, nullable=False)
    status = Column(String, nullable=False, default="Completed")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

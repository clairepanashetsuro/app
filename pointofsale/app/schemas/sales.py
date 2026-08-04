# from datetime import datetime
# from decimal import Decimal
# from pydantic import BaseModel, ConfigDict

# class SaleBase(BaseModel):
#     transaction_number: str
#     user_id: int
#     customer_id: int = None  
#     terminal_id: str
#     subtotal: Decimal
#     discount_amount: Decimal = Decimal("0.00")
#     tax_amount: Decimal
#     total_amount: Decimal
#     payment_method: str
#     status: str = "Completed"

# class SaleCreate(SaleBase):
#     pass

# class SaleUpdate(BaseModel):
#     transaction_number: str = None
#     user_id: int = None
#     customer_id: int = None  
#     terminal_id: str = None
#     subtotal: Decimal = None
#     discount_amount: Decimal = None
#     tax_amount: Decimal = None
#     total_amount: Decimal = None
#     payment_method: str = None
#     status: str = None

# class SaleRead(SaleBase):
#     model_config = ConfigDict(from_attributes=True)

#     sale_id: int
#     sale_datetime: datetime

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class SaleBase(BaseModel):
    transaction_number: str
    user_id: int
    customer_id: int
    terminal_id: str
    subtotal: float
    discount_amount: float = 0.0
    tax_amount: float = 0.0
    total_amount: float
    payment_method: str
    status: str = "Completed"

class SaleCreate(SaleBase):
    pass

class SaleUpdate(BaseModel):
    transaction_number: Optional[str] = None
    user_id: Optional[int] = None
    customer_id: Optional[int] = None
    terminal_id: Optional[str] = None
    subtotal: Optional[float] = None
    discount_amount: Optional[float] = None
    tax_amount: Optional[float] = None
    total_amount: Optional[float] = None
    payment_method: Optional[str] = None
    status: Optional[str] = None

class SaleRead(SaleBase):
    model_config = ConfigDict(from_attributes=True)

    sale_id: int
    created_at: datetime

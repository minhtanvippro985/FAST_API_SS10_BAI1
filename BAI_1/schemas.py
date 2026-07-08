from pydantic import BaseModel

# Schema định nghĩa cấu trúc dữ liệu gửi lên từ Client
class ProductCreate(BaseModel):
    sku: str
    name: str
    price: float 




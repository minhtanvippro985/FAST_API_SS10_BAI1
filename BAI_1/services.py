from sqlalchemy.orm import Session
from model import *
from schemas import *

# Logic xử lý nghiệp vụ: nhận dữ liệu, lưu vào database và trả về kết quả
def handle_create_product_service(db: Session, product: ProductCreate):
    new_product = ProductModel(
        sku=product.sku,
        name=product.name,
        price=product.price
    )
    db.add(new_product)      # Thêm vào hàng đợi theo dõi của session
    db.commit()              # Xác thực ghi dữ liệu xuống MySQL
    db.refresh(new_product)  # Làm mới để lấy ID tự động tăng
    
    return new_product

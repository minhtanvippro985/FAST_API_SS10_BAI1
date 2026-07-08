from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

# Import tường minh để tránh xung đột đè dữ liệu
from database import engine, Base, get_db
from schemas import *
from services import *
from model import *

# Đồng bộ cấu trúc bảng vào Database trước khi ứng dụng khởi chạy

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.post("/products")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    # Gọi hàm xử lý từ services với đúng thứ tự tham số (db trước, dữ liệu sau)
    result = handle_create_product_service(db=db, product=product)
    return {"data": result}



# add  chỉ là để thêm vào rồi theo dõi chứ chưa lưu vào csdl 
# db.commit() để xác thức lưu dư liệu

# Không giải phóng session thì dẫn đến tràn bôn nhớ , giảm hiệu suất
# dùng db.close() 
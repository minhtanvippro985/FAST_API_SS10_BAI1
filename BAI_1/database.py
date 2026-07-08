from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker 

# Kết nối tới cơ sở dữ liệu MySQL
DATABASE_URL = "mysql+pymysql://san:12345@127.0.0.1/ecommerce_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Sử dụng Base viết hoa chữ cái đầu theo đúng chuẩn SQLAlchemy
Base = declarative_base()

# Hàm yield session và tự động đóng kết nối sau khi xử lý xong API
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 

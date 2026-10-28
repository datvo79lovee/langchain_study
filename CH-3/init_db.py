import sqlite3
import os 
import sys

# Tự động tính đường dẫn tuyệt đối dựa trên vị trí của file này
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "SalesDB", "sales.db")

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

# Xóa dữ liệu cũ trước khi insert
cursor.execute("DELETE FROM orders")
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
id INTEGER PRIMARY KEY AUTOINCREMENT,
customer_name TEXT NOT NULL,
product_name TEXT NOT NULL,
quantity INTEGER NOT NULL,
price REAL NOT NULL,
total REAL NOT NULL
)
""")


cursor.execute("""
INSERT INTO orders (customer_name, product_name, quantity, price, total) VALUES
("John Doe", "Laptop", 1, 1000.00, 1000.00),
("Jane Smith", "Smartphone", 2, 500.00, 1000.00),
("Bob Johnson", "Tablet", 3, 200.00, 600.00)
""")

conn.commit()
conn.close()

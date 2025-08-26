# init_db.py
import sqlite3

conn = sqlite3.connect("data/sample.db")
cursor = conn.cursor()

# Create tables
cursor.execute("DROP TABLE IF EXISTS products;")
cursor.execute("DROP TABLE IF EXISTS sales;")

cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT
);
""")

cursor.execute("""
CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    product_id INTEGER,
    quantity INTEGER,
    price REAL,
    FOREIGN KEY(product_id) REFERENCES products(id)
);
""")

# Insert sample data
cursor.executemany("INSERT INTO products (name, category) VALUES (?, ?);", [
    ("Laptop", "Electronics"),
    ("Phone", "Electronics"),
    ("Desk Chair", "Furniture"),
    ("Pen", "Stationery"),
    ("Notebook", "Stationery"),
])

cursor.executemany("INSERT INTO sales (product_id, quantity, price) VALUES (?, ?, ?);", [
    (1, 10, 999.99),
    (2, 25, 599.99),
    (3, 5, 199.99),
    (4, 100, 1.99),
    (5, 50, 4.99),
])

conn.commit()
conn.close()

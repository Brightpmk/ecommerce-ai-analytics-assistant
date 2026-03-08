from app.validator import validate_sql

test_cases = [
    "SELECT * FROM orders LIMIT 10",
    "WITH x AS (SELECT * FROM orders) SELECT * FROM x LIMIT 5",
    "DELETE FROM orders",
    "DROP TABLE orders",
    "SELECT * FROM orders; DROP TABLE orders;",
    "UPDATE orders SET order_status='x'",
]

for sql in test_cases:
    is_valid, message = validate_sql(sql)
    print("=" * 50)
    print("SQL:", sql)
    print("VALID:", is_valid)
    print("MESSAGE:", message)
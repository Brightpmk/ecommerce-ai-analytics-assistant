from app.db import run_select_query

sql = "SELECT COUNT(*) AS total_orders FROM orders;"
df = run_select_query(sql)
print(df)
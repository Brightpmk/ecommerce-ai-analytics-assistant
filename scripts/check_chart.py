from app.db import run_select_query
from app.charts import build_chart

sql = """
SELECT
    DATE_TRUNC('month', o.order_purchase_timestamp) AS month,
    SUM(oi.price) AS revenue
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY 1
ORDER BY 1;
"""

df = run_select_query(sql)
chart = build_chart(df)

print(df.head())
print("Chart created:", chart is not None)
from app.db import run_select_query
from app.insights import generate_insight

question = "Which payment types are most common?"

sql = """
SELECT
    payment_type,
    COUNT(*) AS cnt
FROM order_payments
GROUP BY 1
ORDER BY cnt DESC;
"""

df = run_select_query(sql)
insight = generate_insight(question, df)

print(df.head())
print("\nINSIGHT:\n")
print(insight)
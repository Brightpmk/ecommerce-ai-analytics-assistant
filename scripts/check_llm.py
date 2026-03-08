from app.llm import generate_sql

questions = [
    "What is the monthly revenue trend?",
    "Which product categories generate the highest revenue?",
    "Which states have the most customers?",
]

for q in questions:
    print("=" * 80)
    print("QUESTION:", q)
    sql = generate_sql(q)
    print(sql)
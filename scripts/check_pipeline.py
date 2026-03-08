from app.llm import generate_sql
from app.validator import validate_sql
from app.db import run_select_query

question = "Which product categories generate the highest revenue?"

sql = generate_sql(question)
print("Generated SQL:\n", sql)

is_valid, message = validate_sql(sql)
print("Validation:", is_valid, message)

if is_valid:
    df = run_select_query(sql)
    print(df.head())
else:
    print("SQL was rejected.")
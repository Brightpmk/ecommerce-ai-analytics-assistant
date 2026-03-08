from app.db import run_select_query

queries = {
    "orders_count": "SELECT COUNT(*) AS total_orders FROM orders;",
    "customers_count": "SELECT COUNT(*) AS total_customers FROM customers;",
    "top_categories": """
        SELECT
            pct.product_category_name_english AS category,
            SUM(oi.price) AS revenue
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        LEFT JOIN product_category_translation pct
            ON p.product_category_name = pct.product_category_name
        GROUP BY 1
        ORDER BY revenue DESC
        LIMIT 10;
    """
}

def main():
    for name, sql in queries.items():
        print(f"\n--- {name} ---")
        df = run_select_query(sql)
        print(df.head())

if __name__ == "__main__":
    main()
SCHEMA_DESCRIPTION = """
You are generating PostgreSQL SQL for an e-commerce analytics application.

Available tables and columns:

1) customers
- customer_id
- customer_unique_id
- customer_zip_code_prefix
- customer_city
- customer_state

2) orders
- order_id
- customer_id
- order_status
- order_purchase_timestamp
- order_approved_at
- order_delivered_carrier_date
- order_delivered_customer_date
- order_estimated_delivery_date

3) order_items
- order_id
- order_item_id
- product_id
- seller_id
- shipping_limit_date
- price
- freight_value

4) order_payments
- order_id
- payment_sequential
- payment_type
- payment_installments
- payment_value

5) products
- product_id
- product_category_name
- product_name_lenght
- product_description_lenght
- product_photos_qty
- product_weight_g
- product_length_cm
- product_height_cm
- product_width_cm

6) product_category_translation
- product_category_name
- product_category_name_english

Relationships:
- orders.customer_id = customers.customer_id
- order_items.order_id = orders.order_id
- order_payments.order_id = orders.order_id
- order_items.product_id = products.product_id
- products.product_category_name = product_category_translation.product_category_name

Business guidance:
- Revenue should usually be calculated from order_items.price unless the question is explicitly about payments.
- Freight cost should come from order_items.freight_value.
- Monthly trends should usually use orders.order_purchase_timestamp.
- Category names should prefer product_category_name_english when available.
- Order counts should usually count DISTINCT orders.order_id when joins may duplicate rows.
- For customer distribution, use customers.customer_state or customers.customer_city.
- For payment analysis, use order_payments.payment_type, payment_installments, and payment_value.

SQL generation rules:
- Generate exactly one SQL query.
- Use PostgreSQL syntax.
- Only generate SELECT queries.
- Do not generate INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE, CREATE, GRANT, or REVOKE.
- Do not generate multiple statements.
- Use readable aliases.
- Add ORDER BY when useful.
- Add LIMIT 100 for non-aggregated detailed row outputs.
- Return only raw SQL. No markdown. No explanation. No code fences.
"""


def build_sql_generation_prompt(user_question: str) -> str:
    return f"""
{SCHEMA_DESCRIPTION}

User business question:
{user_question}

Return only the SQL query.
""".strip()
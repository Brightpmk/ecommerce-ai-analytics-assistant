from app.validator import validate_sql

def test_select_passes():
    ok, _ = validate_sql("SELECT * FROM orders LIMIT 5")
    assert ok is True

def test_with_select_passes():
    ok, _ = validate_sql("WITH x AS (SELECT * FROM orders) SELECT * FROM x")
    assert ok is True

def test_delete_rejected():
    ok, _ = validate_sql("DELETE FROM orders")
    assert ok is False

def test_drop_rejected():
    ok, _ = validate_sql("DROP TABLE orders")
    assert ok is False

def test_multiple_statements_rejected():
    ok, _ = validate_sql("SELECT * FROM orders; DROP TABLE orders;")
    assert ok is False

def test_empty_sql_rejected():
    ok, _ = validate_sql("")
    assert ok is False
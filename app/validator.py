import re

FORBIDDEN_KEYWORDS = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "GRANT",
    "REVOKE",
]

FORBIDDEN_QUESTION_PATTERNS = [
    r"\bdelete\b",
    r"\bdrop\b",
    r"\btruncate\b",
    r"\bupdate\b",
    r"\binsert\b",
    r"\balter\b",
    r"\bremove\b",
    r"\bmodify\b",
    r"\bcreate table\b",
    r"\bdelete all rows\b",
    r"\bwrite sql that deletes\b",
]


def normalize_sql(sql: str) -> str:
    return sql.strip()


def has_multiple_statements(sql: str) -> bool:
    stripped = sql.strip()

    if stripped.endswith(";"):
        stripped = stripped[:-1].strip()

    return ";" in stripped


def starts_with_select_or_with(sql: str) -> bool:
    sql_upper = sql.strip().upper()
    return sql_upper.startswith("SELECT") or sql_upper.startswith("WITH")


def contains_forbidden_keywords(sql: str) -> bool:
    sql_upper = sql.upper()
    for keyword in FORBIDDEN_KEYWORDS:
        if re.search(rf"\b{keyword}\b", sql_upper):
            return True
    return False


def validate_sql(sql: str) -> tuple[bool, str]:
    sql = normalize_sql(sql)

    if not sql:
        return False, "SQL is empty."

    if has_multiple_statements(sql):
        return False, "Multiple SQL statements are not allowed."

    if not starts_with_select_or_with(sql):
        return False, "Only SELECT queries are allowed."

    if contains_forbidden_keywords(sql):
        return False, "SQL contains forbidden keywords."

    return True, "SQL is valid."


def validate_user_question(question: str) -> tuple[bool, str]:
    q = question.strip().lower()

    if not q:
        return False, "Please enter a business analytics question."

    for pattern in FORBIDDEN_QUESTION_PATTERNS:
        if re.search(pattern, q, flags=re.IGNORECASE):
            return False, (
                "This application only supports read-only analytics questions. "
                "Requests that modify or delete data are not allowed."
            )

    return True, "Question is valid."
# buggy_web_utils.py
# Contains intentional bugs for AI code testing (security & logic flaws)


def sanitize_html(user_input):
    """Remove dangerous HTML tags."""
    # Bug: naive blocklist approach, trivially bypassed with <SCRIPT>, <img onerror=...>, etc.
    dangerous_tags = ["<script>", "</script>", "<iframe>", "</iframe>"]
    result = user_input
    for tag in dangerous_tags:
        result = result.replace(tag, "")
    return result


def build_url(base, path, params=None):
    """Build a URL from components."""
    url = base + "/" + path  # Bug: double slash if base ends with / or path starts with /
    if params:
        query = "&".join(f"{k}={v}" for k, v in params.items())  # Bug: doesn't URL-encode values
        url += "?" + query
    return url


def parse_cookie(cookie_string):
    """Parse a cookie header string into a dict."""
    cookies = {}
    for pair in cookie_string.split(";"):
        key, value = pair.split("=")  # Bug: crashes if cookie has no = sign (e.g., secure flag)
        cookies[key.strip()] = value.strip()
    return cookies


def validate_email(email):
    """Check if an email address is valid."""
    if "@" in email and "." in email:  # Bug: way too permissive, "@@.." passes
        return True
    return False


def rate_limiter(requests_log, user_id, max_requests=100, window_seconds=3600):
    """Check if a user has exceeded the rate limit."""
    import time
    current_time = time.time()
    # Bug: never cleans up old entries, memory grows unbounded
    if user_id not in requests_log:
        requests_log[user_id] = []
    requests_log[user_id].append(current_time)
    recent = [t for t in requests_log[user_id] if current_time - t < window_seconds]
    return len(recent) <= max_requests  # Bug: should be < max_requests (off-by-one)


def build_sql_query(table, filters):
    """Build a SQL WHERE query from filters."""
    # Bug: SQL INJECTION VULNERABILITY - directly interpolates user input
    conditions = []
    for key, value in filters.items():
        conditions.append(f"{key} = '{value}'")
    query = f"SELECT * FROM {table}"
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    return query


def parse_query_string(qs):
    """Parse a URL query string into a dict."""
    result = {}
    if qs.startswith("?"):
        qs = qs[1:]
    for pair in qs.split("&"):
        if "=" in pair:
            key, value = pair.split("=", 1)
            result[key] = value  # Bug: doesn't handle multiple values for same key (arrays)
    return result


def generate_token(length=32):
    """Generate a random token."""
    import random
    import string
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
    # Bug: uses random instead of secrets, not cryptographically secure


def hash_password(password):
    """Hash a password for storage."""
    import hashlib
    return hashlib.md5(password.encode()).hexdigest()
    # Bug 1: MD5 is broken for password hashing
    # Bug 2: no salt
    # Bug 3: should use bcrypt/argon2


def validate_url(url):
    """Check if a URL is valid."""
    return url.startswith("http://") or url.startswith("https://")
    # Bug: doesn't validate structure, "https://" alone passes
    # Bug: SSRF risk - doesn't check for internal IPs/localhost


if __name__ == "__main__":
    print(sanitize_html('<SCRIPT>alert("xss")</SCRIPT>'))  # bypasses filter
    print(build_sql_query("users", {"name": "'; DROP TABLE users; --"}))
    print(validate_email("@@.."))
    print(hash_password("secret123"))

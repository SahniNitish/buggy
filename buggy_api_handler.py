# buggy_api_handler.py
# Contains intentional bugs for AI code testing (API/validation patterns)

from datetime import datetime, timedelta


def validate_age(age):
    """Validate user age."""
    if age > 0 and age < 150:  # Bug: doesn't handle non-integer input
        return True
    return False


def paginate(items, page, per_page=10):
    """Return a page of items."""
    start = page * per_page  # Bug: should be (page - 1) * per_page if pages are 1-indexed
    end = start + per_page
    return {
        "data": items[start:end],
        "page": page,
        "total": len(items),
        "total_pages": len(items) // per_page,  # Bug: should use ceil division
    }


def merge_dicts(base, override):
    """Deep merge two dicts."""
    result = base  # Bug: modifies original base dict — should be base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result


def parse_date(date_string):
    """Parse a date string in multiple formats."""
    formats = ["%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    return None  # Bug: "01-02-2023" is ambiguous (DD-MM or MM-DD?), silently picks first match


def calculate_discount(price, discount_percent):
    """Apply a percentage discount."""
    if discount_percent > 1:  # Bug: assumes >1 means percentage, but 0.5 could mean 50%
        discount_percent = discount_percent / 100
    return price * (1 - discount_percent)


def retry(func, max_retries=3, delay=1):
    """Retry a function on failure."""
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            import time
            time.sleep(delay)
            # Bug: no exponential backoff, fixed delay hammers the service
            # Bug: catches ALL exceptions including KeyboardInterrupt


def flatten_dict(d, parent_key='', sep='.'):
    """Flatten a nested dict with dot notation keys."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            items.append((new_key, v))  # Bug: doesn't flatten lists
        else:
            items.append((new_key, v))
    return dict(items)


def check_password_strength(password):
    """Check if a password meets strength requirements."""
    if len(password) < 8:
        return "weak"
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    if has_upper and has_lower and has_digit:
        return "strong"
    return "medium"
    # Bug: doesn't check for special characters
    # Bug: "Aa1aaaaa" is "strong" which is actually weak
    # Bug: doesn't check against common passwords


def generate_date_range(start_date, end_date):
    """Generate all dates between start and end (inclusive)."""
    dates = []
    current = start_date
    while current < end_date:  # Bug: should be <= for inclusive end
        dates.append(current)
        current += timedelta(days=1)
    return dates


def safe_divide(a, b, default=0):
    """Safely divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        return default
    # Bug: silently returns 0 on division by zero — caller can't distinguish 0/5 from 5/0
    # Bug: doesn't handle TypeError for non-numeric inputs


def chunk_list(lst, chunk_size):
    """Split a list into chunks of given size."""
    if chunk_size <= 0:
        return lst  # Bug: should raise error, returns original list instead
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


if __name__ == "__main__":
    print(paginate(list(range(25)), 1))  # page 1 should be first 10 items
    print(calculate_discount(100, 20))  # 20% off
    print(calculate_discount(100, 0.2))  # also 20% off — but gives different result!
    print(check_password_strength("Aa1aaaaa"))  # "strong" but it's really not

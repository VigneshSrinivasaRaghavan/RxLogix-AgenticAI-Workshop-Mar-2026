import time
import functools
from contextlib import contextmanager


# ─────────────────────────────────────────────
# PART 1: The problem — repeated code in every function
# ─────────────────────────────────────────────

print("=== PART 1: Without decorator (repeated code) ===")

def test_login():
    start = time.time()
    print("Running: test_login")
    time.sleep(0.5)
    print(f"Finished in {time.time() - start:.2f}s")

def test_logout():
    start = time.time()
    print("Running: test_logout")
    time.sleep(0.3)
    print(f"Finished in {time.time() - start:.2f}s")

test_login()
test_logout()
print()


# ─────────────────────────────────────────────
# PART 2: Basic decorator — move the timing logic out
# ─────────────────────────────────────────────

print("=== PART 2: With decorator (timing in one place) ===")

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Finished in {time.time() - start:.2f}s")
        return result
    return wrapper

@timer
def test_login():
    print("Running: test_login")
    time.sleep(0.5)

@timer
def test_logout():
    print("Running: test_logout")
    time.sleep(0.3)

test_login()
test_logout()
print()


# ─────────────────────────────────────────────
# PART 3: functools.wraps — preserve the function name
# ─────────────────────────────────────────────

print("=== PART 3: functools.wraps ===")

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Finished in {time.time() - start:.2f}s")
        return result
    return wrapper

@timer
def test_dashboard():
    print("Running: test_dashboard")
    time.sleep(0.2)

print(f"Function name: {test_dashboard.__name__}")
test_dashboard()
print()


# ─────────────────────────────────────────────
# PART 4: Context Manager class
# ─────────────────────────────────────────────

print("=== PART 4: Context Manager class ===")

class TestSession:
    def __enter__(self):
        print("Opening browser session...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing browser session...")

with TestSession():
    print("Running tests inside session...")
    time.sleep(0.2)

print()


# ─────────────────────────────────────────────
# PART 5: Context Manager using @contextmanager (shortcut)
# ─────────────────────────────────────────────

print("=== PART 5: @contextmanager shortcut ===")

@contextmanager
def test_session():
    print("Opening browser session...")
    yield
    print("Closing browser session...")

with test_session():
    print("Running tests inside session...")
    time.sleep(0.2)

print()
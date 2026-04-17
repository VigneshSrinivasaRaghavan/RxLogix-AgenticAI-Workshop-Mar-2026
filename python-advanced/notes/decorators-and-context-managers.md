# Decorators & Context Managers

---

## The Problem Both Solve

Imagine you want to log the start and end time of every test function you run.

Without decorators, you'd write this in every function:
```python
def test_login():
    print("Starting test...")
    start = time.time()
    # actual test code
    print(f"Done in {time.time() - start:.2f}s")

def test_logout():
    print("Starting test...")
    start = time.time()
    # actual test code
    print(f"Done in {time.time() - start:.2f}s")
```

That's repeated code in every function. If you have 50 test functions, you write that 50 times. And if you want to change the log format, you change it 50 times.

**Decorators and Context Managers both solve this: add behaviour around your code without repeating yourself.**

---

## What is a Decorator?

A decorator is a function that wraps another function to add behaviour before and/or after it runs — without modifying the original function.

You apply it with `@` symbol above the function definition.

**Real-world analogy:**
A security guard at a building entrance. Every person who enters goes through the same check (show ID, sign in) and the same exit process (sign out). The guard is the decorator — the people entering are your functions. The guard's process runs around every person without each person having to manage it themselves.

---

## What is a Context Manager?

A context manager automatically handles setup and cleanup around a block of code using the `with` statement.

You already use one every time you open a file:
```python
with open("file.csv") as f:
    data = f.read()
# file is automatically closed here, even if an error occurred
```

Without `with`, you'd have to remember to close the file manually. With `with`, Python guarantees cleanup happens no matter what.

**Real-world analogy:**
A hotel room. When you check in, the room is prepared (setup). When you check out, the room is cleaned (cleanup). You don't manage that — the hotel handles it automatically around your stay.

---

## Decorator vs Context Manager

| | Decorator | Context Manager |
|---|---|---|
| Wraps | A function | A block of code |
| Applied with | `@` symbol | `with` statement |
| Best for | Logging, timing, retrying, auth checks | File handling, DB connections, resource cleanup |

---

## Key Terms in Code

| Term | What it means |
|---|---|
| `@decorator_name` | Apply this decorator to the function below |
| `functools.wraps` | Preserve the original function's name and docstring |
| `wrapper` | The inner function that runs before/after the original |
| `with` | Start a context manager block |
| `__enter__` | Runs when `with` block starts (setup) |
| `__exit__` | Runs when `with` block ends (cleanup) |
| `@contextmanager` | Shortcut to build a context manager using `yield` |

---

## Why Does This Matter for QA / Agentic AI?

**QA use case:**
- Decorator: add timing, logging, or screenshot-on-failure to every test function with one line
- Context Manager: manage browser sessions, DB connections, or temp files — guaranteed cleanup even if the test crashes

**Agentic AI use case:**
- Decorator: add retry logic to every LLM API call — if it fails, wait and try again automatically
- Context Manager: manage agent sessions, API client lifecycles, or tracing spans around tool calls
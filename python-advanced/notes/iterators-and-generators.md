# Iterators & Generators

---

## What is an Iterator?

An iterator is any object that gives you one item at a time when you loop over it.

**Real-world analogy:**
A token counter at a government office. You don't get all tokens at once. You press the button, get token 1, press again, get token 2. One at a time, on demand.

When you write a `for` loop in Python, Python is secretly using an iterator behind the scenes.

```python
for item in [1, 2, 3]:
    print(item)
```

Python internally calls two things on the list:
- `__iter__()` — give me an iterator object
- `__next__()` — give me the next item

When there are no more items, it raises `StopIteration` and the loop stops.

---

## What is a Generator?

A generator is a simpler way to create an iterator using the `yield` keyword.

Instead of building a full class with `__iter__` and `__next__`, you just write a function with `yield`. Python handles the rest.

**Real-world analogy:**
Same token counter — but now instead of a machine you built from scratch (iterator class), you use a readymade dispenser (generator). Same result, much less effort.

---

## yield vs return

| | `return` | `yield` |
|---|---|---|
| What it does | Exits the function, sends one value back | Pauses the function, sends one value back |
| Next call | Starts the function from the beginning | Resumes from where it paused |
| Memory | All values computed at once | One value at a time, on demand |

---

## for loop vs yield — The Key Difference

This is the most important thing to understand. The output looks the same. The difference is invisible — it is about **memory**.

### for loop
- Python collects ALL items into memory first
- Then loops through them one by one
- You have no control — it runs to the end automatically

### yield (generator)
- Python gives you ONE item, then pauses
- Waits for you to ask for the next one
- The rest of the items are NOT in memory yet

---

### See it with a real example

Imagine your CSV file has 1 million test cases.

**Using a normal list (bad for large data):**
```python
# ALL 1 million rows are read and stored in RAM first
test_cases = open("file.csv").readlines()

for test in test_cases:
    run_test(test)
```

**Using a generator (memory-safe):**
```python
# Only 1 row is in memory at a time
def read_tests(filepath):
    with open(filepath) as f:
        for line in f:
            yield line

for test in read_tests("file.csv"):
    run_test(test)
```

The `for` loop on the outside looks identical. But inside, the generator is loading one row, processing it, throwing it away, then loading the next. RAM usage stays flat.

---

### Simple mental model

| | for loop over a list | generator with yield |
|---|---|---|
| Memory | Loads everything upfront | Loads one item at a time |
| Control | Runs automatically to the end | Pauses after each item |
| Best for | Small, known data | Large files, streaming, unknown size |

---

## Why Does This Matter for QA / Agentic AI?

**QA use case:**
You have a CSV with 10,000 test cases. A normal list loads all 10,000 into RAM at once. A generator reads one row, runs the test, moves to the next — memory stays low no matter the file size.

**Agentic AI use case:**
LLM streaming responses use generators. When ChatGPT types word by word, that is a generator on the backend — each token is `yield`-ed one at a time instead of waiting for the full response to be ready.

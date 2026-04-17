# ─────────────────────────────────────────────
# PART 1: Normal for loop (you already know this)
# ─────────────────────────────────────────────

print("=== PART 1: Normal for loop ===")

test_cases = ["Login Test", "Logout Test", "Dashboard Test"]

for test in test_cases:
    print(f"Running: {test}")

print()


# ─────────────────────────────────────────────
# PART 2: Iterator class — gives items one at a time using next()
# ─────────────────────────────────────────────

print("=== PART 2: Iterator Class — one item at a time ===")

class TestCaseIterator:
    def __init__(self, tests):
        self.tests = tests
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.tests):
            raise StopIteration
        test = self.tests[self.index]
        self.index += 1
        return test


iterator = TestCaseIterator(["Login Test", "Logout Test", "Dashboard Test"])

print(next(iterator))   # manually get item 1
print(next(iterator))   # manually get item 2
print(next(iterator))   # manually get item 3

print()


# ─────────────────────────────────────────────
# PART 3: Generator — same result, far less code
# ─────────────────────────────────────────────

print("=== PART 3: Generator with yield ===")

def test_case_generator(tests):
    for test in tests:
        yield test


gen = test_case_generator(["Login Test", "Logout Test", "Dashboard Test"])

print(next(gen))   # manually get item 1
print(next(gen))   # manually get item 2
print(next(gen))   # manually get item 3

print()


# ─────────────────────────────────────────────
# PART 4: QA Practical — read 20 test cases from CSV one at a time
# ─────────────────────────────────────────────

print("=== PART 4: QA Practical — reading test data lazily ===")

def read_test_data(filepath):
    with open(filepath) as f:
        next(f)  # skip header
        for line in f:
            username, password, expected = line.strip().split(",")
            yield {"username": username, "password": password, "expected": expected}


for test in read_test_data("test_data/login_test_cases.csv"):
    print(f"  {test['username']:<15} | expected: {test['expected']}")

print()


# ─────────────────────────────────────────────
# PART 5: Memory proof — list vs generator on 100,000 rows
# ─────────────────────────────────────────────

print("=== PART 5: Memory comparison — list vs generator ===")

import tracemalloc


def generate_large_data_list(n):
    return [{"id": i, "username": f"user_{i}", "expected": "success"} for i in range(n)]


def generate_large_data_generator(n):
    for i in range(n):
        yield {"id": i, "username": f"user_{i}", "expected": "success"}


N = 100_000

tracemalloc.start()
data = generate_large_data_list(N)
for _ in data:
    pass
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"List      — Peak memory used: {peak / 1024 / 1024:.2f} MB")

tracemalloc.start()
for _ in generate_large_data_generator(N):
    pass
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Generator — Peak memory used: {peak / 1024 / 1024:.2f} MB")
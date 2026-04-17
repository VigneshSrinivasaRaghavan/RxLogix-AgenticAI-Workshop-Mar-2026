# Tips for Using AI in Programming

> You already know prompt engineering, prompt types, and CoT from earlier sessions.
> This session is different — it's about using AI specifically inside your coding workflow.

---

## 1. Using AI in the IDE (Cursor / VS Code)

Both Cursor and VS Code have AI assistants built in. Unlike ChatGPT where you copy-paste code back and forth, these tools know your open files and project context.

- **Cursor** — has AI built in natively
- **VS Code** — use GitHub Copilot Chat (install from Extensions if not already installed)

The features and workflow are nearly identical in both.

### Keyboard Shortcuts

| Action | Cursor (Mac) | Cursor (Windows) | VS Code with Copilot (Mac) | VS Code with Copilot (Windows) |
|---|---|---|---|---|
| Generate code inline | `Cmd+K` | `Ctrl+K` | `Cmd+I` | `Ctrl+I` |
| Open AI chat | `Cmd+L` | `Ctrl+L` | `Cmd+Shift+I` | `Ctrl+Shift+I` |

### What you can do

**Generate code inline**
Place your cursor in the file, use the inline shortcut, describe what you want:
```
Write a Python function that reads a CSV and returns rows where expected = "failure"
```
AI writes the code directly in your file.

**Chat with your codebase**
Open the AI chat panel. Ask questions about your own code:
```
What does the read_test_data function in 02_iterators_generators.py do?
```
AI reads your file and explains it.

**Explain selected code**
Select any block of code → open chat → ask:
```
Explain this code in simple terms
```

**Refactor selected code**
Select code → inline shortcut → ask:
```
Rewrite this to use a generator instead of a list
```

---

## 2. AI for Debugging — Paste the Error, Get the Fix

When your Python code throws an error, don't guess. Paste both the error and the code into AI.

### The right way to ask

**Bad prompt:**
```
My code has an error, fix it
```

**Good prompt:**
```
I am running this Python code:

[paste your code]

I am getting this error:

[paste the full error message]

What is causing this error and how do I fix it?
```

### Example

Error you got:
```
AttributeError: module 'tracemalloc' has no attribute 'traced_memory'
```

Good prompt to AI:
```
I am using Python 3.13. I called tracemalloc.traced_memory() and got:
AttributeError: module 'tracemalloc' has no attribute 'traced_memory'

What is the correct method name and why?
```

AI will tell you: the correct method is `get_traced_memory()`.

**Rule: Always paste the full error, not just the last line.**

---

## 3. Converting Manual Test Cases to Scripts

This is the most powerful use case for QAs. You already write test cases in plain English — AI can turn them into Test Scripts.

### How to do it

Take a manual test case like this:

```
Test Case: Login with valid credentials
Steps:
1. Open browser and go to https://example.com/login
2. Enter username: admin
3. Enter password: admin123
4. Click Login button
5. Verify dashboard page is displayed
Expected: User is redirected to dashboard
```

Prompt to AI:
```
Convert this manual test case into a Playwright test script using TypeScript.
Use the Page Object Model pattern.
The test should use the Playwright test runner.
Python Scripts
[paste the manual test case]
```

AI gives you a working TypeScript Playwright test. You review it, run it, adjust as needed.

---

## 4. AI for Code Review — Find What You Missed

After writing a test script, paste it into AI and ask:

```
Review this Python test script and tell me:
1. What test scenarios am I missing?
2. Are there any bugs or logical errors?
3. What edge cases should I add?

[paste your script]
```

This is AI acting as a senior QA reviewing your work — available 24/7.

### Other useful review prompts

```
Is there a simpler way to write this code?
```

```
What happens if the CSV file is empty? Does this code handle it?
```

```
Rewrite this using a generator to reduce memory usage
```

---

## 5. When AI Gets Code Wrong — and How to Catch It

AI can write code that looks correct but has a logical bug. This is called a hallucination in a code context.

### Common ways AI gets it wrong

| Situation | What AI does |
|---|---|
| Outdated library version | Uses an old method that no longer exists |
| Wrong assumption | Assumes CSV has a header when yours doesn't |
| Missing edge case | Code works for happy path but crashes on empty input |
| Confident but wrong logic | Loop off by one, wrong comparison operator |

### How to protect yourself

**Rule 1: Always run the code — never just read it.**
Code that looks right can still fail. Run it with real data.

**Rule 2: Test with edge cases immediately.**
Empty file, wrong password, missing column — try these before calling it done.

**Rule 3: If something looks strange, ask AI to explain it.**
```
Explain line by line what this function does
```
If AI's explanation doesn't match what you expected, the code is wrong.

**Rule 4: Use specific versions in your prompt.**
```
I am using Python 3.13 and Playwright 1.40. Write a test that...
```
This reduces outdated code being generated.

---

## 6. Iterative Prompting for Code — First Answer Is Rarely Final

Unlike test step generation, code prompts often need refinement. Expect 2-3 rounds.

### Typical flow

**Round 1:** Ask for the code
```
Write a Python function that reads login_test_cases.csv and prints only failed test cases
```

**Round 2:** Refine based on output
```
Good, but change the output format to show the row number alongside each failed case
```

**Round 3:** Ask for improvement
```
Now add error handling for when the file doesn't exist
```

Each round builds on the previous. Don't try to put everything in the first prompt — it makes the output messy and harder to verify.

---

## Quick Reference — Prompts to Keep Handy

| What you want | Prompt pattern |
|---|---|
| Write new code | "Write a Python function that [describe exactly what it does, input, output]" |
| Fix an error | "I got this error: [error]. My code is: [code]. What is wrong and how to fix?" |
| Understand code | "Explain this Python code in simple terms: [paste code]" |
| Convert manual test | "Convert this manual test case to a Python Playwright script using pytest: [paste test case]" |
| Review your code | "Review this script. What scenarios am I missing? Are there bugs? [paste code]" |
| Refactor | "Rewrite this using [generators / async / decorators]: [paste code]" |
| Edge cases | "What happens if [empty input / wrong type / file missing] with this code? [paste code]" |

# RxLogix Agentic AI Workshop

## Prerequisites

### 1. Install Python

Download and install **Python 3.11 or higher** from the official site:
https://www.python.org/downloads/

> **Windows users:** During installation, make sure to check **"Add Python to PATH"** before clicking Install.

Verify the installation:

```cmd
python --version
```

### 2. Install Git & Create a GitHub Account

Download and install Git from: https://git-scm.com/downloads

You also need a **GitHub account** to clone this repository:
https://github.com/join

Verify Git is installed:

```cmd
git --version
```

---

## Training Day Tags

> **Important:** Code is pushed with a tag for each day of the training. You can switch to any day's codebase using the tag.

List all available tags:

```powershell
git tag
```

Switch to a specific day's code (example: Day 1 and Day 2):

```powershell
git checkout day-01
```

```powershell
git checkout day-02
```

To come back to the latest code:

```powershell
git checkout main
```

---

## Getting Started

### Step 1: Clone the Repository

```cmd
git clone https://github.com/VigneshSrinivasaRaghavan/RxLogix-AgenticAI-Workshop-Mar-2026.git
cd RxLogix-AgenticAI-Workshop-Mar-2026
```

### Step 2: Navigate to the Working Directory

All agent code lives inside the `agentic-ai` folder:

```cmd
cd agentic-ai
```

### Step 3: Create a Virtual Environment

```powershell
py -m venv .venv
```

This creates a `.venv` folder inside `agentic-ai`.

### Step 4: Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

You should see `(.venv)` appear at the beginning of your terminal prompt. This means the virtual environment is active.

> To deactivate later, just run: `deactivate`

### Step 5: Install Dependencies

```cmd
pip install -r requirements.txt
```

### Step 6: Set Up Environment Variables

Copy the example environment file and fill in your API keys:

```cmd
copy .env.example .env
```

Open `.env` in any text editor (Notepad, VS Code, etc.) and fill in your API key for the provider you want to use:

```
PROVIDER=openai
MODEL=gpt-4o-mini

OPENAI_API_KEY=your-openai-key-here
GOOGLE_API_KEY=your-google-key-here
ANTHROPIC_API_KEY=your-anthropic-key-here
```

Only the key for the provider you set in `PROVIDER` needs to be filled.

---

## Running an Agent

Make sure you are inside the `agentic-ai` folder and your virtual environment is active `(venv)`.

Run any agent from the `src/agents/` folder. For example:

```cmd
python src/agents/testcase_agent.py
```

---

## Troubleshooting

**`python` is not recognized**
- Reinstall Python and make sure **"Add Python to PATH"** is checked during setup.
- Or try `py` instead of `python`.

**`.\.venv\Scripts\Activate.ps1` gives an error about execution policy**
- Run this once in PowerShell, then try again:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

**`pip install` fails with version conflicts**
- Make sure your virtual environment is active (`(.venv)` in prompt) before running pip.

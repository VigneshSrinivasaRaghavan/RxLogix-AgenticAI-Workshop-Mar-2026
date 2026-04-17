# SKILL.md vs GitHub Copilot Instructions — Same Content, Different Mechanism

> The **content** of your instruction file is identical in both IDEs.  
> Only the **location** and **how the agent picks it up** differs.

---

## Side-by-Side Comparison

| | Cursor (SKILL.md) | VS Code + GitHub Copilot |
|--|-------------------|--------------------------|
| File location | `.cursor/skills/<skill-name>/SKILL.md` | `.github/copilot-instructions.md` OR any `.md` file referenced manually |
| How agent reads it | Auto-discovered — Cursor injects it into the agent's context automatically | Persistent: `copilot-instructions.md` is always active. Manual: `#file:` reference per chat |
| Invocation | Describe the task — agent recognizes the skill and applies it | Open Copilot Chat → `#file:path/to/skill.md` + your instruction |
| Scope | Per-skill (targeted, purpose-specific) | `copilot-instructions.md` applies to ALL Copilot chats in the repo |
| Agent autonomy | High — Cursor agent executes multi-step tasks autonomously | Moderate — Copilot Chat follows instructions but is more conversational |
| Content format | Markdown with YAML frontmatter | Plain markdown (no frontmatter needed) |

---

## The Same Content, Used in Both

The markdown body of your skill is **completely portable**. Example:

```
Your SKILL.md content (the instructions, phases, guardrails)
         │
         ├──► Cursor:  paste into .cursor/skills/playwright-self-healing/SKILL.md
         │             → agent auto-discovers and executes
         │
         └──► VS Code: paste into .github/copilot-instructions.md
                       → OR save as any .md and reference with #file: in chat
```

---

## Demo Steps — Cursor

1. Create `.cursor/skills/playwright-self-healing/SKILL.md` with your content
2. Open Cursor agent (Cmd+I or Chat panel)
3. Type: `"Fix the failing Playwright tests"` — agent discovers the skill and follows it
4. Watch the agent: detect failure → analyze locators → propose fix → validate → patch file → re-run

---

## Demo Steps — VS Code + GitHub Copilot

### Method 1: Persistent (copilot-instructions.md)
1. Create `.github/copilot-instructions.md` in the repo root
2. Paste the same SKILL.md content (without the YAML frontmatter)
3. Open Copilot Chat
4. Type: `"Fix the failing Playwright tests"` — Copilot uses the instructions automatically

### Method 2: On-demand (file reference)
1. Keep the SKILL.md file anywhere in the repo (e.g., `agentic-ai/notes/playwright-self-healing/SKILL.md`)
2. Open Copilot Chat
3. Type: `#file:agentic-ai/notes/playwright-self-healing/SKILL.md Fix the failing Playwright tests`
4. Copilot reads the file inline and follows the instructions for that session only

---

## Key Difference

> **Cursor** is proactive — it finds the skill and uses it.  
> **Copilot** is reactive — you point it to the instructions.  
> The instructions themselves are identical.

Use `copilot-instructions.md` when you want the instructions always active for the whole repo.  
Use `#file:` when you want to apply a specific skill only for one task.

# Socratic — A Misconception-Diagnosing Algebra Tutor

> Most AI tutors just hand over the answer. **Socratic** figures out *why* a student got a problem wrong — the specific misconception behind the mistake — and guides them out of it with questions, never answers.

Built for the **Microsoft Agents League Hackathon** · Reasoning Agents track · grounded with **Foundry IQ**.

---

## The problem

Most AI homework helpers give the final answer, which short-circuits learning. The genuinely valuable thing is diagnosing the *misconception* behind a wrong answer and teaching the student past it. That is what Socratic does.

## What it does

When a student submits incorrect work, the agent:

1. **Parses the student's steps** — not just the final answer — to find where it first goes wrong.
2. **Diagnoses the misconception** by retrieving the best-matching entry from a knowledge base via **Foundry IQ**.
3. **Asks a Socratic probe question** that helps the student notice the issue themselves.
4. **Scaffolds** with a smaller sub-question so the student discovers the correct rule.
5. **Confirms** by having the student restate the corrected step.

It **never reveals the final answer**, admits uncertainty when an error doesn't match any known misconception, and offers an **accessibility mode** (plain language + text-to-speech-friendly output).

## Architecture

![Architecture](architecture.svg)

| Layer | Technology |
|---|---|
| Agent | Microsoft Foundry prompt agent (`gpt-4.1-mini`) |
| Knowledge / grounding | **Foundry IQ** knowledge base (`algebra-misconceptions`, Extractive mode) |
| Retrieval engine | Azure AI Search (Basic tier), vector + semantic |
| Embeddings | `text-embedding-3-small` |
| Knowledge source | `knowledge-base.md` — 8 classic algebra misconceptions |

The required Microsoft IQ integration is **Foundry IQ**: a reusable knowledge base that grounds the agent's diagnoses in real pedagogy and returns cited results.

## How the knowledge base works

`knowledge-base.md` contains 8 common middle/high-school algebra misconceptions. Each entry has the tell-tale error pattern, the root cause, a Socratic probe question, and a scaffold step. Foundry IQ indexes this content and, at query time, returns the single best-matching entry for the agent to teach from.

## Repository contents

```
.
├── README.md              # this file
├── architecture.svg       # architecture diagram
├── agent-instructions.md  # the agent's system prompt (paste into Foundry)
├── knowledge-base.md      # the 8-misconception knowledge base (Foundry IQ source)
├── agent.yaml             # exported agent definition from the Foundry portal
├── call_agent.py          # minimal script to call the deployed agent from code
└── requirements.txt       # Python dependencies
```

## Running it

**Option A — Foundry portal (no setup):** open the agent in the Microsoft Foundry playground and chat with it.

**Option B — from code:**

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Sign in to Azure (keyless auth):
   ```bash
   az login
   ```
3. Set environment variables (find these in the Foundry portal → your project → Overview):
   ```bash
   export PROJECT_ENDPOINT="https://socratic-tutor-resource.services.ai.azure.com/api/projects/socratic-tutor"
   export AGENT_NAME="Socratic"
   ```
4. Run:
   ```bash
   python call_agent.py
   ```

> The exact SDK call for your agent is also generated for you in the Foundry portal under your agent's **"Call agent"** tab — `call_agent.py` mirrors that pattern.

## Safety & reliability

- Hard rule: the agent never states the final answer or the fully corrected line.
- It admits uncertainty ("walk me through your steps") rather than guessing when an error matches no known misconception.
- It stays scoped to algebra tutoring and declines to complete graded tests for the student.

## Accessibility

An accessibility mode adjusts to plain language, defines terms, and writes so replies read naturally aloud (e.g. "x squared" instead of "x²") for screen-reader and lower-literacy users.

## Limitations & future work

- Scope is intentionally narrow (8 algebra misconceptions) for reliability; the knowledge base is designed to expand to more topics by adding entries.
- A custom web front-end could replace the playground for a richer student experience.

---

*Submitted to the Microsoft Agents League Hackathon, 2026.*

# Algebra Misconception Knowledge Base
### Grounding content for the "Socratic" tutor agent (served via Microsoft Foundry IQ)

**Purpose of this document:** This is the knowledge base the tutor agent retrieves from. When a student submits work with an error, the agent searches this content, identifies the matching misconception, and uses the *probe* and *scaffold* fields to teach — never revealing the final answer. Each entry is self-contained so Foundry IQ can retrieve the right one and cite it.

**How to read each entry:**
- **Misconception** — the false belief the student is acting on.
- **Tell-tale error** — what the wrong work looks like, so the agent can recognize it.
- **Why it happens** — the root misunderstanding to address.
- **Correct principle** — the rule, stated plainly.
- **Socratic probe** — a question the agent asks to surface the error (NOT the answer).
- **Scaffold** — a smaller sub-step that lets the student discover the fix themselves.
- **Worked example** — the correct reasoning, for the agent's internal grounding only.

---

### Misconception 1: Moving a term without changing its operation

**Misconception:** "To move a number to the other side of the equals sign, I just write it over there as-is."

**Tell-tale error:** From `x + 5 = 12`, the student writes `x = 12 + 5` (gets 17).

**Why it happens:** The student pictures "moving" a term physically, instead of doing the same inverse operation to both sides.

**Correct principle:** To isolate a variable, apply the *inverse* operation to *both* sides. The inverse of "+5" is "−5".

**Socratic probe:** "You have `+5` stuck to the x. What operation undoes adding 5 — and if you do it on the left, what do you have to do on the right?"

**Scaffold:** "Forget the x for a second. If I have `5 = 12` and I subtract 5 from the left, what do I do to the right to keep it balanced?"

**Worked example (internal):** `x + 5 = 12` → subtract 5 from both sides → `x = 12 − 5` → `x = 7`.

---

### Misconception 2: Distributing to only the first term

**Misconception:** "When I multiply into parentheses, I only multiply the first thing inside."

**Tell-tale error:** `2(x − 3)` becomes `2x − 3` instead of `2x − 6`.

**Why it happens:** The student stops after the first multiplication and forgets the factor applies to every term inside.

**Correct principle:** The distributive law: `a(b + c) = ab + ac`. The outside factor multiplies *every* term inside.

**Socratic probe:** "Does the 2 out front multiply everything inside the parentheses, or only the x? What is `2 × (−3)`?"

**Scaffold:** "Let's split it: `2(x − 3)` is `2·x` and then `2·(−3)`. What's the second piece?"

**Worked example (internal):** `2(x − 3) = 2x − 6`.

---

### Misconception 3: Dividing only one term by the denominator

**Misconception:** "When a sum is over a number, I divide just the first term."

**Tell-tale error:** `(2x + 4) / 2` becomes `x + 4` instead of `x + 2`.

**Why it happens:** The student applies the division to the leading term only.

**Correct principle:** A denominator divides *every* term in the numerator: `(a + b)/c = a/c + b/c`.

**Socratic probe:** "If we break `(2x + 4)/2` into two separate fractions, what is `4/2`?"

**Scaffold:** "Write it as `2x/2 + 4/2`. Now simplify each piece on its own."

**Worked example (internal):** `(2x + 4)/2 = 2x/2 + 4/2 = x + 2`.

---

### Misconception 4: Cancelling terms that are added, not multiplied

**Misconception:** "Matching numbers on top and bottom always cancel."

**Tell-tale error:** `(x + 2) / 2` is simplified to `x` by "cancelling" the 2s.

**Why it happens:** The student remembers that factors cancel but doesn't notice the 2 on top is *added* to x, not multiplied.

**Correct principle:** You can only cancel a *factor* shared by the entire numerator and denominator — not a term that's part of a sum.

**Socratic probe:** "Is the 2 on top multiplied by something, or added to the x? Can we cancel something that's only being added?"

**Scaffold:** "Try a number: let x = 4. What's `(4 + 2)/2`? Is that the same as just 4?"

**Worked example (internal):** `(x + 2)/2 = x/2 + 1`. It does *not* simplify to x. (Check: x=4 gives 3, not 4.)

---

### Misconception 5: Squaring a sum term-by-term

**Misconception:** "`(a + b)²` is just `a² + b²`."

**Tell-tale error:** `(x + 3)²` written as `x² + 9`.

**Why it happens:** The student treats the exponent as if it distributes over addition.

**Correct principle:** `(a + b)²` means `(a + b)(a + b) = a² + 2ab + b²`. The middle term `2ab` is what gets missed.

**Socratic probe:** "What does the little 2 actually tell us to do — how many copies of `(x + 3)` are multiplied together? What happens when you multiply them out?"

**Scaffold:** "Write `(x + 3)(x + 3)` and multiply each term in the first bracket by each term in the second. How many products do you get?"

**Worked example (internal):** `(x + 3)² = x² + 6x + 9`.

---

### Misconception 6: Dropping the negative on the second term

**Misconception:** "A minus sign in front of parentheses only affects the first thing inside."

**Tell-tale error:** `−(x − 3)` becomes `−x − 3` instead of `−x + 3`.

**Why it happens:** The student applies the negative to x but not to the −3.

**Correct principle:** A leading minus is multiplying by −1, and −1 multiplies *every* term: `−(x − 3) = −x + 3`.

**Socratic probe:** "The minus out front multiplies everything inside. What is `−1 × (−3)`?"

**Scaffold:** "Rewrite `−(x − 3)` as `−1 · x` plus `−1 · (−3)`. What does the second piece become?"

**Worked example (internal):** `−(x − 3) = −x + 3`.

---

### Misconception 7: Cross-multiplying the wrong pairs

**Misconception:** "In a proportion, I multiply the two tops and the two bottoms."

**Tell-tale error:** From `a/b = c/d`, the student writes `ac = bd` instead of `ad = bc`.

**Why it happens:** The student multiplies straight across instead of diagonally.

**Correct principle:** Cross-multiplication pairs each numerator with the *opposite* denominator: `a/b = c/d` ⟹ `a·d = b·c`.

**Socratic probe:** "Which number is diagonally across from the top-left one? That's the pair you multiply."

**Scaffold:** "Draw the two diagonals of the equation like an X. Which two numbers does each diagonal connect?"

**Worked example (internal):** `2/3 = x/9` → `2·9 = 3·x` → `18 = 3x` → `x = 6`.

---

### Misconception 8: Adding before multiplying (order of operations)

**Misconception:** "I just work left to right."

**Tell-tale error:** `2 + 3 × 4` evaluated as `(2 + 3) × 4 = 20` instead of `14`.

**Why it happens:** The student reads left-to-right and ignores operation priority.

**Correct principle:** Multiplication and division happen before addition and subtraction (PEMDAS/BODMAS), regardless of left-to-right order.

**Socratic probe:** "Looking at `2 + 3 × 4`, which operation has to happen first — the adding or the multiplying? Why?"

**Scaffold:** "Box the multiplication part first: what is `3 × 4`? Now what's left to add?"

**Worked example (internal):** `2 + 3 × 4 = 2 + 12 = 14`.

---

## Agent grounding rules (read by the agent alongside this content)

- Match the student's error to exactly **one** misconception above before responding.
- Use that entry's **probe** first. Wait for the student's reply before moving on.
- If the reply shows partial understanding, use the **scaffold**. Otherwise, ask a simpler version.
- **Never** state the final answer or the corrected line. The worked examples are for *your* grounding only — do not reveal them.
- If the error matches **no** entry here, say honestly: "I'm not sure what tripped you up — can you walk me through your steps?" Do not guess.
- Always cite which misconception you're drawing on (Foundry IQ provides the citation).

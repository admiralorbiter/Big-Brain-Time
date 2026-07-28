# Synthesis Note — Module 00: Introduction to Calculus & Method of Exhaustion
**Book:** *Apostol, Calculus Volume 1 (Introduction, Part 1)*  
**Date:** 2026-07-27  

---

## 💡 Core Conceptual Takeaways

1. **The Core Duality of Calculus:**
   Calculus revolves around two fundamental geometric problems:
   - **Integral Calculus:** Assigning a precise number to measure the **area under a curve**.
   - **Differential Calculus:** Assigning a precise number to measure the **steepness of a tangent line**.

2. **Historical Genesis (Method of Exhaustion):**
   - The Greeks (Archimedes, ~287–212 B.C.) originated calculus via the *method of exhaustion*—inscribing and circumscribing polygons to approximate curvilinear areas.
   - Without modern algebraic notation (which developed in the 16th century), extending Archimedes' method took nearly 1,800 years.

3. **The Squeeze Argument for $f(x) = x^2$:**
   - Slicing the base $[0, b]$ into $n$ equal strips of width $b/n$:
     - **Inner Rectangles ($s_n$):** Underestimate area using left-hand height.
     - **Outer Rectangles ($S_n$):** Overestimate area using right-hand height.
   - Squeeze inequality:
     $$s_n < \frac{b^3}{3} < S_n \quad \text{for all } n \ge 1$$
   - By proof by contradiction (the "Sherlock Holmes" method of exhausting all alternatives), $A = \frac{b^3}{3}$ is the **only** number that satisfies $s_n < A < S_n$ for all $n$.

4. **The Gap Invariant Identity:**
   $$S_n - s_n = \frac{b^3}{n^3} \cdot n^2 = \frac{b^3}{n}$$
   - Demonstrates geometrically and algebraically *why* the trap becomes arbitrarily narrow.
   - Proves that $b^3/3$ is the unique number lying between $s_n$ and $S_n$ for every $n$.

---

## 🛠️ The Squeeze Forge (Complete 5-Mission Suite)

- **Interactive Proof Laboratory:** [`experiments/00-parabola-exhaustion/index.html`](file:///c:/Users/admir/Github/Big-Brain-Time/pilot/math-reconstruction/experiments/00-parabola-exhaustion/index.html)
  - **Mission 1: Compile a Rectangle (`BIND`)** — Two-step concrete to general flow:
    - *Step 1 (Concrete):* Bind Rectangle #3 width ($b/n$) and height ($(3b/n)^2$) to compile $\text{Area}_3 = \frac{3^2 b^3}{n^3}$.
    - *Step 2 (Generalization):* Replace $3 \to k$ to compile general $\text{Area}_k = \frac{b^3 k^2}{n^3}$.
  - **Mission 2: Build the Sums (`CONSTRUCT`)** — Construct $S_n$ ($1 \dots n$) vs $s_n$ ($1 \dots n-1$) index ranges with real-time canvas highlighting.
  - **Mission 3: Discover Gap Invariant (`ALIGN & REWRITE`)** — Align terms, cancel shared pairs, simplify $(b^3/n^3)\cdot n^2 \implies b^3/n$, paper reconstruction prompt.
  - **Mission 4: Play Proof Adversary (`CHALLENGE & CERTIFY`)** — Construct algebraic witness $n > b^3/\delta$ to defeat false claim $A = b^3/3 + \delta$.
  - **Mission 5: Perturb & Transfer (`TRANSFER`)** — Update squeeze model for $f(x) = a \cdot x^2 + c$ to derive $\text{Area} = a(b^3/3) + cb$.

---

## ⏩ Next Step
- **Part 2 of Introduction:** Set Theory & Notation (collections of elements, operations, intervals).

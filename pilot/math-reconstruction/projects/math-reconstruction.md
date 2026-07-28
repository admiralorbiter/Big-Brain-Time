# Mathematics Reconstruction Lab

**Purpose:** Rebuild a rigorous calculus-to-analysis foundation through textbook study, computational experiments, and selective Lean 4 formalization, while producing a public portfolio of notes, computational notebooks, and verified proofs.

---

## 📚 Core Textbooks & Calibration

- **Spine (Primary Textbook):** *Apostol, Calculus, Volume 1* (Integration before differentiation; technical rigor integrated with linear algebra).
- **Boss Problems & Taste:** *Spivak, Calculus* (Challenging theoretical problems).
- **Free Exercise Companion:** *Active Calculus, 2nd Edition* (Conceptual activity workbook).
- **External Calibration:** *MIT 18.01SC Single Variable Calculus* (Problem sets & exams for transfer testing).
- **Formalization Companion:** *Mathematics in Lean (Lean 4)* (Interactive theorem proving).

---

## 🔄 The 5-Language Learning Loop

For each core concept/theorem, produce five outputs:

1. **Intuitive Model:** Geometric, dynamic, or computational explanation.
2. **Hand Solution / Proof:** Pen-and-paper derivation without code.
3. **Computational Experiment:** Python script/notebook testing behavior, numerical approximations, or edge cases.
4. **Lean Artifact:** Formalized theorem or algebraic/logic property in Lean 4.
5. **Synthesis Note:** One-page summary addressing central ideas, indispensable assumptions, failure modes, and cross-domain connections.

```text
Intuition ➔ Handwritten Proof ➔ Python Computation ➔ Lean Formalization ➔ Synthesis Note
```

---

## 📅 Initial 8-Module Cycle

| Module | Mathematical Focus | Computational Work | Lean Work |
|---|---|---|---|
| **0. Diagnostic & Setup** | Mathematical language & notation | Python numerical plotting environment | Setup VS Code Lean 4 interactive environment |
| **1. Foundations & Sums** | Functions, inequalities, induction, finite sums | Floating-point representations & cancellation | Prove algebraic identities & simple inequalities |
| **2. Limits & Continuity** | Sequences, limit definitions, discontinuities | Numerical limit investigation & discontinuity plots | Quantifiers, sequences, and function bounds |
| **3. Integration** | Accumulation, Riemann sums, Darboux sums | Implement Riemann, Trapezoidal, Simpson rules | Formalize finite-sum identities & integral facts |
| **4. FTC** | Fundamental Theorem of Calculus | Compare accumulated sums with numerical derivatives | Use Mathlib differentiation/integration lemmas |
| **5. Derivatives** | Local linearization, rate of change | Forward, central, and symbolic differentiation | Formalize polynomial derivative examples |
| **6. Taylor Series** | Polynomial approximation & error bounds | Build Taylor polynomials & error heatmaps | Prove finite polynomial bounds |
| **7. Sequences & Series** | Convergence tests & power series | Convergence-testing laboratory | Work through sequences & convergence |
| **8. Synthesis Project** | Calculus Laboratory Python package | Full `analyze_function()` numerical suite | Formalize 1 primary project result |

---

## 📁 Portfolio Directory Structure

```text
math-reconstruction/
├── projects/
│   └── math-reconstruction.md       # Canonical narrative & master plan
├── notes/
│   ├── synthesis/                   # 1-page synthesis notes
│   ├── proofs/                      # Proof reconstructions
│   └── counterexamples/             # Hypothesis counterexample ledger
├── experiments/                     # Python computational notebooks & calculus lab
├── lean/                            # Lean 4 formalization files (.lean)
└── .bbt/
    └── records/project-transitions/ # Versioned YAML closeout records
```

---

## 🔁 Weekly 5-Session Rhythm

1. **Explore:** Read section, predict definitions and results before reading proofs.
2. **Solve:** Work selected exercises by hand (4 technique, 3 conceptual, 2 proofs, 1 boss problem, 1 code problem).
3. **Reconstruct:** Close book, reproduce one proof from memory, compare.
4. **Compute:** Turn 1 concept into a Python computational notebook.
5. **Formalize & Synthesize:** Complete 1 Lean theorem & 1-page synthesis note.

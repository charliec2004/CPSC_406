---
title: Determinization of NFAs

---

# NFAs vs DFAs and Determinization

How do NFAs and DFAs compare? At first glance, the behavior of NFAs seems more complex: as we have seen, the same word can be processed in multiple ways, even resulting in states that differ in whether they are accepting or not.

We will see that despite this fact, NFAs do not give rise to more computational power: they detect exactly the same languages that DFA do.

## DFAs as NFAs

To start off, we should convince ourselves that any DFA can be canonically regarded as an NFA.

:::warning 
**Exercise 1.**
Let $\mathcal A = (Q, \Sigma, \delta \colon Q \times \Sigma \to Q, q_0, F)$ be an DFA. Explain in what way you can view $\mathcal A$ as an *NFA* by doing the following:
1. Let $\mathcal A$ denote the following DFA:
![Image 03.03.2025 at 17.49](https://hackmd.io/_uploads/S1FNn0QiJg.jpg)
Explain how you can understand $\mathcal A$ also as an an *NFA*.
2. Now, more generally, let $\mathcal A = (Q, \Sigma, \delta \colon Q \times \Sigma \to Q, q_0, F)$ be a DFA. Define an NFA $\mathcal A' = (Q', \Sigma, \delta' \colon Q' \times \Sigma \to \mathcal P(Q'), q'_0, F')$ such that $L(\mathcal A) = L(\mathcal A')$.
2. Justify why your construction satisfies the desired condition.
:::

## The power set construction

Any DFA can be seen as an NFA, but actually there is also a way to go the other way around: for any NFA $\mathcal A = (Q, \Sigma, \delta \colon Q \times \Sigma \to \mathcal P(Q), q_0, F)$ there is a *DFA* $\mathcal A^{\mathrm{D}} = (Q^{\mathrm{D}}, \Sigma, \delta^{\mathrm{D}} \colon Q^{\mathrm{D}} \times \Sigma \to Q^{\mathrm{D}}, q_0^{\mathrm{D}}, F^{\mathrm{D}})$ such that $L(\mathcal A) = L(\mathcal A^{\mathrm{D}})$. This is achieved through the following construction:

:::info
**Construction (power set automaton).**
Let $\mathcal A = (Q, \Sigma, \delta \colon Q \times \Sigma \to \mathcal P(Q), q_0, F)$ be an NFA. Then its **power set automaton** or **determinization** is defined as $\mathcal A^{\mathrm{D}}$ as follows:
* $Q^{\mathrm{D}} := \mathcal P(Q^{\mathrm{D}})$
* $\delta^{\mathrm{D}}(S,a) := \bigcup_{q \in S} \delta(q,a)$, for $S \subseteq Q$ and $a \in \Sigma$
* $q_0^{\mathrm{D}} := \{q_0\}$
* $F^{\mathrm{D}} := \{ S \subseteq Q \; | \; S \cap F \neq \emptyset \}$
:::

The idea is that the states in $Q^{\mathrm{D}}$ are labeled by *multiple* states from the original NFA $\mathcal A$. The transitions $\delta^{\mathrm{D}}(S,a)$ are defined as the set of all states that are reachable with $a$ from any state $q \in S$. The starting state $q_0^{\mathrm{D}}$ is the singleton set containing $q_0$. Then, $S \in F^{\mathrm{D}}$ should be accepting if it contains *at least* one accepting state $q \in F$, i.e. $q \in S$.

One can show that the construction of the power set automaton preserves the accepted language, i.e., $L(\mathcal A) = L(\mathcal A^{\mathrm{D}})$.

:::success
**Example 1.** Consider the following NFA $\mathcal A = (Q,\Sigma,q_0,\delta,F)$:
![Image 03.03.2025 at 17.45](https://hackmd.io/_uploads/By4rjyNo1x.jpg)
Its specification is as follows:
* The set of states is $Q = \{1,2,3\}$.
* The alphabet is $\Sigma = \{a,b\}$.
* The initial state is $q_0 = 1$.
* The NFA transition function is given by $\delta : Q \times \Sigma \to \mathcal P(\Sigma)$
defined as:
$\delta(1,a) = \{1,2\}$
$\delta(1,b) = \{1\}$
$\delta(2,a) = \emptyset$
$\delta(2,b) = \{3\}$
$\delta(3,a) = \delta(3,b) = \emptyset$
* The set of accepting states is $F=\{3\}$.

We want to construct the power set automaton $\mathcal A^{\mathrm{D}}$. Starting from the initial state $\{q_0\}$ we can successively describe the transition function giving rise to the following transition table completely describing $\mathcal A^{\mathrm{D}}$:
|              | $a$           | $b$ |
| --------     | --------      | -------- |
| $\to \{1\}$  | $\{1,2\}$     | $\{1\}$  |
| $\{1,2\}$    | $\{1,2\}$     | $\{1,3\}$|
| $*\{1,3\}$    | $\{1,2\}$     | $\{1\}$|

As a transition diagram, we can draw $\mathcal A^{\mathrm{D}}$ as follows:
![Image 03.03.2025 at 17.48](https://hackmd.io/_uploads/rJaBC1Njkl.jpg)
:::
Note how in the example, we built up the diagram step by step starting from the initial state $\{1\}$. In this example, the number of states did not change, though in general we have that $|Q^{\mathrm{D}}| = |\mathcal P(Q)| = 2^{|Q|}$. But often not all of these states are reachable, hence they do not contribute to the language accepted by the automaton, and we leave them out when drawing the transition diagram.

:::success
**Example 2.**
Consider the following NFA $\mathcal A$:
![Image 03.03.2025 at 19.36](https://hackmd.io/_uploads/rk9UBgNikg.jpg)
We successively find the following entries for the transition table for $\mathcal A^{\mathrm{D}}$:
|              | $a$           | $b$ |
| --------     | --------      | -------- |
| $\to \{1\}$  | $\{1,2\}$     | $\emptyset$  |
| $*\{1,2\}$    | $\{1,2\}$     | $\{1\}$|
| $\emptyset$    | $\emptyset$     | $\emptyset$|

This gives rise to the following DFA:
![Image 03.03.2025 at 19.44](https://hackmd.io/_uploads/SJ18vgNsJg.jpg)

Note the *trap state* $\emptyset$ which models that there is no $b$-transition from $1$. 
:::


:::danger
**Homework 1.**
For the alphabet $\Sigma = \{a,b,c\}$ consider the following NFA $\mathcal A$:
![Image 24.02.2026 at 12.42](https://hackmd.io/_uploads/Hk4UTYsuZl.jpg)
1. Describe the language accepted by $\mathcal A$ using a regular expression.
2. Specify the NFA $\mathcal A$ in the form $(Q,\Sigma,\delta,q_0,F)$.
3. Find *all* paths in $\mathcal A$ for the word $v = abab$. Represent them in a diagram as we did [here](https://hackmd.io/_uploads/rJ3QfUh5kx.jpg). (You do not need to represent the paths that get stuck before parsing the whole word.)
4. Construct the determinization $\mathcal A^{\mathrm{D}}$ of $\mathcal A$ using the power set construction. Create both a transition table and a graphical depiction of $\mathcal A^{\mathrm{D}}$.
:::

:::danger
**Homework 2.**
For the alphabet $\Sigma = \{0,1\}$ consider the following NFA $\mathcal A$:
![Image 24.02.2026 at 12.56](https://hackmd.io/_uploads/SkBag9j_Wl.jpg)
1. Construct the determinization $\mathcal A^{\mathrm{D}}$ of $\mathcal A$ using the power set construction. Create both a transition table and a graphical depiction of $\mathcal A^{\mathrm{D}}$.
2. Is there a smaller DFA accepting the same language
as AP?
:::
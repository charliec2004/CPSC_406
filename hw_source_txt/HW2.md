---
title: Operations on automata

---

# Operations on automata

## Product automata

**Example.**
Consider the following automata $\mathcal A^{(1)} = (Q^{(1)}, \Sigma, \delta^{(1)}, q_0^{(1)}, F^{(1)})$ and $\mathcal A^{(2)} = (Q^{(2)}, \Sigma, \delta^{(2)}, q_0^{(2)}, F^{(2)})$:

$\mathcal A^{(1)}$:
![aut_prime](https://hackmd.io/_uploads/ByjYbHjFJl.jpg)

$\mathcal A^{(2)}$:
![aut_new](https://hackmd.io/_uploads/rkKCWUoY1e.jpg)

**Question:** How can we construct an automaton $\mathcal A$ that recognizes exactly those words that are both in $L(\mathcal A^{(1)})$ and $L(\mathcal A^{(2)})$?

We have to keep track of both automata simultaneously, observing at every transition if the letter that we are reading is accepted in **both** automata.

The general recipe is as follows:

:::info
**Definition (Product automaton).** For DFAs $\mathcal A^{(1)} = (Q^{(1)}, \Sigma, \delta^{(1)}, q_0^{(1)}, F^{(1)})$ and $\mathcal A^{(2)} = (Q^{(2)}, \Sigma, \delta^{(2)}, q_0^{(2)}, F^{(2)})$ we define an automaton $\mathcal A=(Q, \Sigma, \delta, q_0, F)$ as follows:
* $Q := Q^{(1)} \times Q^{(2)}$, i.e., a state $q \in Q$ is a pair $q = (q^{(1)}, q^{(2)})$ with $q^{(1)} \in Q^{(1)}$ and $q^{(2)} \in Q^{(2)}$
* $\delta(q,a) := (\delta^{(1)}(q,a), \delta^{(2)}(q,a))$
* $q_0 := (q_0^{(1)}, q_0^{(2)})$
Since its set of states $Q$ is given as the cartesian product $Q^{(1)} \times Q^{(2)}$ we call $\mathcal A$ a **product automaton**.
:::

We have not yet specified what $F$ should be. This depends on what kind of operation on the languages we want to model.

In the case of the intersection, of two languages, a word in the product automaton should be accepted if and only if it is accepted in both the original automata. This motivates the following definition:

:::info
**Definition (Intersection automaton).** Let $\mathcal A=(Q, \Sigma, \delta, q_0, F)$ be a product automaton of two DFAs $\mathcal A^{(1)} = (Q^{(1)}, \Sigma, \delta^{(1)}, q_0^{(1)}, F^{(1)})$ and $\mathcal A^{(2)} = (Q^{(2)}, \Sigma, \delta^{(2)}, q_0^{(2)}, F^{(2)})$. We set $F := F^{(1)} \times F^{(2)}$. Then, $\mathcal A$ is called the **intersection automaton** of $\mathcal A^{(1)}$ and $\mathcal A^{(2)}$.
:::

:::warning
**Exercise 1 (Product automata).**
Consider the following automata:

$\mathcal A^{(1)}$:
![aut_prime](https://hackmd.io/_uploads/ByjYbHjFJl.jpg)

$\mathcal A^{(2)}$:
![aut_new](https://hackmd.io/_uploads/rkKCWUoY1e.jpg)

1. Describe $L(\mathcal A^{(1)})$ and $L(\mathcal A^{(2)})$.
2. Construct the intersection automaton $\mathcal A$ for $\mathcal A^{(1)}$ and $\mathcal A^{(2)}$ as given above by drawing its transition diagram (if there are unreachable states you do not have to draw them).
3. Argue that indeed $L(\mathcal A) = L(\mathcal A^{(1)}) \cap L(\mathcal A^{(2)})$.
4. How can you change $\mathcal A$ to define a new automaton $\mathcal A'$ such that $L(\mathcal A') = L(\mathcal A^{(1)}) \cup L(\mathcal A^{(2)})$?
:::

:::warning
**Exercise 2 (More automata).**
Consider the following automata:

$\mathcal B^{(1)}$:
![Image 17.02.2026 at 10.52](https://hackmd.io/_uploads/rJAmtEz_Zg.jpg)


$\mathcal B^{(2)}$:
![Image 17.02.2026 at 10.52 (1)](https://hackmd.io/_uploads/Hkjrt4GdZe.jpg)


1. Describe $L(\mathcal B^{(1)})$ and $L(\mathcal B^{(2)})$.
2. Construct the intersection automaton $\mathcal B$ for $\mathcal B^{(1)}$ and $\mathcal B^{(2)}$ as given above by drawing its transition diagram (if there are unreachable states you do not have to draw them).
3. Argue that indeed $L(\mathcal B) = L(\mathcal B^{(1)}) \cap L(\mathcal B^{(2)})$.
4. How can you change $\mathcal B$ to define a new automaton $\mathcal B'$ such that $L(\mathcal B') = L(\mathcal B^{(1)}) \cup \overline{L(\mathcal B^{(2)})}$? (If $L \subseteq \Sigma^*$ is a language, then $\overline{L} := \Sigma^* \subseteq L$ is its [complement](https://en.wikipedia.org/wiki/Complement_(set_theory)))
:::




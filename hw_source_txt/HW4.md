# Kleene's algorithm

## Converting a DFA to a regular expression

We will present [*Kleene's algorithm*](https://en.wikipedia.org/wiki/Kleene%27s_algorithm), converting a DFA to a regular expression describing the same language.

:::info
**Kleene's algorithm**
**In:** a DFA $\mathcal A$
**Out:** a regular expression $R_\mathcal A$ such that $L(\mathcal A) = L(R_\mathcal A)$

**Procedure**:
Given a DFA $\mathcal A$, first rename the states to $Q = \{1,2,\ldots n\}$.
For $0\leq k \leq n$ and $1 \leq i,j \leq n$ we will construct regular expressions $R^{(k)}_{ij}$ describing all possible paths from state $i$ to state $j$ such that all intermediate states $q_m$ with $q_m \leq k$:
$i \to \underbrace{q_1 \to q_2 \to \ldots \to q_m}_{\leq k} \to j$
We let $L^{(k)}_{ij} := L(R^{(k)}_{ij})$.
1. **Induction base $k=0$**: If $k=0$, then there can be *no* states between $i$ and $j$ which are below $k$. Thus, $R^{(0)}_{ij}$ describes the possible ways to go from $i$ to $j$. If $i=j$, we can transition from $i$ to $j$ via $\varepsilon$. We have:
$$L^{(0)}_{ij} = \begin{cases}
    \{ a \in \Sigma \; | \; \delta(i,a) = j\} & \text{if $i\neq j$} \\
    \{\varepsilon\} \cup \{ a \in \Sigma \; | \; \delta(i,a) = j\} & \text{if $i = j$} \\
\end{cases}$$
We can readily read off the corresponding regular expressions in both of these cases. This goes as follows:
If $i \neq j$ we have three possible cases:
    * If there is no transition from $i$ to $j$, then $R^{(0)}_{ij} = \emptyset$.
    * If there is exactly one transition from $i$ to $j$, say via $a$, then $R^{(0)}_{ij} = \mathbf{a}$.
    * If there are several transitions from $i$ to $j$, say via $a_1, \ldots, a_n$, then $R^{(0)}_{ij} = \mathbf{a}_1 + \ldots + \mathbf{a}_n$.

If $i = j$ the same cases occur, but we have to add the empty word $\varepsilon$ in each case, yielding either $\varepsilon$, $\varepsilon + \mathbf{a}$, or, $\varepsilon + \mathbf{a}_1 + \ldots + \mathbf{a}_n$.

2. **Induction step $(k-1) \mapsto k$ (where $k \leq n$):** We assume that $R^{(k-1)}_{ij}$ has been defined.

We then obtain $R^{(k)}_{ij}$ as follows:
$$ R^{(k)}_{ij} = \underbrace{R^{(k-1)}_{ij}}_{(1)} +  \underbrace{R^{(k-1)}_{ik}}_{(2)}  \underbrace{\big( R^{(k-1)}_{kk} \big)^*}_{(3)} \underbrace{R^{(k-1)}_{kj}}_{(4)} $$
The formula is explained as follows: The two parts of the sum distinguish the two cases that going from $i$ to $j$ we do not pass through $k$ or we do.
Part (1) describes paths that do not contain $k-1$ as an intermediate state.

If we do pass through $k$, we break down the path into three further parts:
Part (2) describes paths from $i$ to the first occurence of $k$.
Part (3) describes looping from $k$ to itself.
Part (4) describes paths from $k$ to $j$.

**Result:** After having computed all regular expressions $R_{ij}^{(k)}$, for $0 \leq k \leq n$, we then compute the final desired expression as
$$ R_\mathcal A := \sum_{q \in F} R^{(n)}_{q_0q} = R^{(n)}_{q_0q_1} + R^{(n)}_{q_0q_2} + \ldots + R^{(n)}_{q_0q_\ell}$$
where $q_0$ is the initial state, and $F = \{q_1, q_2, \ldots, q_\ell\}$ is the set of final states of $\mathcal A$. 
Thus, the corresponding language can be expressed as a union:
$$L(R_\mathcal A) = \bigcup_{q \in F} L^{(n)}_{q_0q}$$
:::

For a detailed example run of this algorithm, see [ITALC, Section 3.2, Example 3.5].

:::success
**Remark.** One can show that this algorithm actually works for an ($\varepsilon$-)NFA, too. It is, however, quite expensve: given $n$ states, the number of expressions we have to compute is in the order of $n^3$. Each expression can have up to the order of $4^n$-many symbols, i.e., the length grows exponentially!

A more economical variation on this algorithm is known as the *state elimination method*, see [ITALC, Section 3.2.2].
:::

:::warning
**Exercise (Kleene's algorithm).**
Consider the following DFA:
![Image 05.03.2026 at 14.27](https://hackmd.io/_uploads/rJfXItvF-x.jpg)

For $p = 1$ and $q = 2$ compute via Kleene's algorithm all regular expressions $R^{(k)}_{ij}$ and from this a resulting regular expression $R$ describing $L(\mathcal A)$, i.e., such that $L(R) = L(\mathcal A)$.
:::
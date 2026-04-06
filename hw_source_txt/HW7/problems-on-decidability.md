---
title:

---

# Problems on decidability

:::warning
**Exercise 1.** 
Which of the following statements is true? If yes, give an argument; if no, give a counterexample.
1. If $L_1$ and $L_2$ are decidable, then so is $L_1 \cup L_2$.
2. If $L$ is decidable, then so is the complement $\overline{L} := \Sigma^* \backslash L = \{w \in \Sigma^* \; | \; w \notin L\}$.
3. If $L$ is decidable, then so is $L^*$.
4. If $L_1$ and $L_2$ are r.e., then $L_1 \cup L_2$ is r.e.
5. If $L$ is r.e., then so is $\overline{L}$.
6. If $L$ is r.e., then so is $L^*$.
:::

:::warning
**Exercise 2.** 
Argue for each of the languages $L_1$, $L_2$, $L_3$ if they are
* decidable,
* recursively enumerable (r.e.),
* or have recursively enumerable complement (co-r.e.).

1. $$L_1 := \{M \; | \; \text{$M$ halts on itself} \}$$
2. $$L_2 := \{(M,w) \; | \; \text{$M$ halts on the word $w$} \}$$
3. $$L_3 := \{(M,w,k) \; | \; \text{$M$ halts on $w$ in at most $k$ steps} \}$$
:::




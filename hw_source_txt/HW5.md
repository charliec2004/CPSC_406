---
title: The Pumping Lemma

---

# The pumping lemma

## Motivating example

:::success
**Example.** Consider the language 
$L:=\{a^n b^n \in \{a,b\}^* \; | \; n \geq 0\}$. Is $L$ regular?
:::

**Solution:**
:::spoiler
The language is *not* regular. One way to see this is roughly the following: Assume $L$ were regular, thus accepted by a DFA $\mathcal A$. Consider the prefixes $\{a^n \; | \; n \geq 0\}$. Since this set is finite but the set of states of $\mathcal A$ is infinite, there exist $k,\ell \in \mathbb N$ with $k \neq \ell$ and $\widehat{\delta}(q_0,a^k) = \widehat{\delta}(q_0,a^\ell) =: q$. Having read $a^k$, we would get $\widehat{\delta}(q,b^k) =: q' \in F$ since $a^kb^k \in L$.  But we could equally have read $a^\ell$ at $q$ in which case we should have $\widehat{\delta}(q,b^k) = q' \notin F$. Contradiction!
:::

How can we spot more generally if a given language is **not** regular?

## Statement of the pumping lemma

:::info
**Theorem (Pumping lemma).** Let $L$ be a regular language. Then there exists a constant $n > 0$ (depending on $L$) such that for every word $w \in L$ with $|w| \geq n$, $w$ decomposes into $w = xyz$ such that:
1. $y \neq \varepsilon$
2. $|xy| \leq n$
3. For all $k \geq 0$ the string $w' := xy^kz$ is in $L$, too.
:::

**Proof.** Assume $L$ is regular. Then $L = L(\mathcal A)$ for some DFA. We assume $\mathcal A$ has $n$ states. Let $w = a_1 a_2 \cdots a_m \in L$ be an accepted string of length $m \geq n$. For $0 \leq i \leq n$, we define:
$$p_i := \begin{cases}
q_0 & \text{if $i=0$} \\
\widehat{\delta}(q_0,a_1 a_2 \cdots a_i) & \text{if $1 \leq i \leq n$}
\end{cases}$$
This defines $n+1$ states $p_0, \ldots, p_n$, but $\mathcal A$ has only $n$ states, so there must exist $0 \leq i < j \leq n$ with $p_i = p_j$. We now decompose $w$ as $w=xyz$ where:
* $x := a_1 \cdots a_i$
* $y := a_{i+1} \cdots a_j$
* $z := a_{j+1} \cdots a_m$

In the automaton, this corresponds to the following paths:
![Image 18.03.2025 at 12.14](https://hackmd.io/_uploads/Sk6EIBwnJx.jpg)


This indeed satisfies the condition from the beginning:
1. $y$ is nonempty since $j \ngeq i$, although it could happen that $x = \varepsilon$ (if $i=0$) or $z = \varepsilon$ (if $j=n=m$)
2. By construction $|xy| \leq n$ (count the indices).
3. We have to check that for all $k \geq 0$, $xy^k z \in L$. If $k = 0$, then $p_i = p_j$, and $w' = xz$ since the path ends in a final state, see above. If $k \geq 1$, then $w' = xy^k z$, meaning we take the path as above, looping through the sub-path reading $y$ exactly $k$ times. This also ultimately ends in an accepting state.

:::success
**Example.** We want to show the application of the pumping lemma to the example from above, $L= \{a^n b^n \; | \; n \geq 0\}$. Here is a proof using the pumping lemma, step by step:
* *Assumption:* Assume, $L$ *were* regular. Then $L$ would satisfy the property from the pumping lemma.
* Let $n$ be a pumping number of $L$. Consider the word $w:=a^n b^n$. We have $|w| = 2n \geq n$.
* By 2., we have that $|xy| \leq n$, so the substring $xy$ has to be completely contained in $a^n$, meaning that $xy$ only consists of $a$'s.
* By 1., $y \neq \varepsilon$, so $y$ contains at least one occurrence of $a$.
* By 3., we can "pump" $w$: let $k := 2$, so $w' = xy^2z$.
* Now, $xy$ contains only $a$'s and no $b$'s. This means $|w'|_a > |w|_a = n = |w|_b$. On the other hand, $|w'|_b = |w|_b = |w|_a$ since $b$'s only occur within $z$ and we have left this part unaltered.
* But this means $|w'|_a > |w'|_b = n$ which is a a contradiction, since it entails that $w' \notin L$.
:::

## Problems on the pumping lemma

:::warning
**Exercise.**
Show that the following languages are not regular using the pumping lemma:
$L_1 = \{ a^n b^m \in \{a,b\}^* \; | \; n,m \in \mathbb N, ~ n > m \ge 0 \}$
$L_2 = \{ a^{n^2} \in \{a\}^* \; | \; n \in \mathbb N, ~ n \ge 1 \}$
$L_3 = \{ a^p \in \{a\}^\ast \; | \; p \in \mathbb N, ~ p\,\,\mathrm{prime} \}$
$L_4 = \{ a^k b^m a^{k+m} \; | \; k,m \geq 0\}$
:::

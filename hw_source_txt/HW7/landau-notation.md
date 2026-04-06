# Landau Notation ("Big O"), or Mathematics as a metaphor

## Introduction

The definition of Big O is quite technical and it is not immediately clear from the technical definition why it is so important.

In these notes we argue that the definition of Big O is less important for its mathematical content but rather because the precise mathematical definition creates a powerful *metaphor*. This metaphor, together with its countless variations and ramifications, underpins all of practical software engineering. But we never use the definition of Big O to crunch some numbers or establish benchmarks.

We first state the definition of Big O and then explain its importance as a metaphor for software engineering. In fact, we can see the previous two lectures on Turing machines and P vs NP in that new light as well.

## Warmup: Growth of functions

:::warning
**Exercise 1 (Warmup).**
Let $\mathrm{log}$ denote the natural logarithm, i.e., the logarithm w.r.t. the base $\mathrm{e}$. Order the following functions by their order of growth (from slow to fast):
a. $2^{2^n}$
b. $\mathrm{e}^{\log n}$
c. $\log(n)$
d. $\mathrm{e}^n$
e.  $\mathrm{e}^{2\log(n)}$
f. $\log(\log(n))$
g. $2^n$
h. $n!$
:::

## Big O: Definition

We now change direction, instead of working from the problem (classification of algorithms) to the solution (Big O), we now start from the definition of Big O and then discuss whether it meets our requirements.

Given non-negative functions $f,g \colon \mathbb N \to \mathbb R_{\geq 0}$ one writes
$$f \in \mathcal O(g)$$
(or $f(n) \in \mathcal O(g(n))$ or $f(n) = \mathcal O(g(n))$)
if there are $N$ and $M$ such that
$$f(n) \leq M \cdot g(n)$$
for all $n \geq N$.

## Big O: Properties

We now list some desirable properties of the Big O notation. It is instructive to prove these yourself.

:::warning
**Exercise 2.**
For functions $f,g,h \colon \mathbb N \to \mathbb R_{\geq 0}$ prove the following:
1. $f \in \mathcal O(f)$
2. If $c > 0$ is a constant then $\mathcal O(c \cdot f)
 = \mathcal O(f)$.
3. If $f \leq g$ for large enough inputs, then $\mathcal O(f) \subseteq \mathcal O(g)$.
4. If $\mathcal O(f) \subseteq \mathcal O(g)$, then $\mathcal O(f+h) \subseteq \mathcal O(g+h)$.
5. If $h(n) > 0$ for all $n \in \mathbb N$, and $\mathcal O(f) \subseteq \mathcal O(g)$, then $\mathcal O(f\cdot h) \subseteq \mathcal O(g \cdot h)$.
 :::
 
We can use these basic properties to derive further useful properties:

:::warning
**Exercise 3.**
Let $i,j,k,n \in \mathbb N$. Prove that the following hold:
1. If $j \leq k$, then $\mathcal O(n^j) \subseteq \mathcal O(n^k)$.
2. If $j \leq k$, then $\mathcal O(n^j + n^k) \subseteq \mathcal O(n^k)$.
3. $\mathcal O(\sum_{i=0}^k a_i n^i) = \mathcal O(n^k)$
4. $\mathcal O(\log n) \subseteq \mathcal O(n)$
5. $\mathcal O(n \log n) \subseteq \mathcal O(n^2)$
:::

We can use our insights to compare the growth of functions:

:::warning
**Exercise 4.**
Which relationships do we have between the following? Prove your claim.
1. $\mathcal O(n)$ and $\mathcal O(\sqrt{n})$
2. $\mathcal O(n^2)$ and $\mathcal O(2^n)$
3. $\mathcal O(\log n)$ and $\mathcal O(\log n \cdot \log n)$
4. $\mathcal O(2^n)$ and $\mathcal O(3^n)$
5. $\mathcal O(\log_2n)$ and $\mathcal O(\log_3 n)$
:::

## Classifying algorithms

The aim is to classify algorithms into broad clusters according to the amount of resources they consume. Most often, the resources we are interested in are time (runtime) or space (memory usage).

Given a problem we want to distinguish algorithms that use less resources from those that use more resources.
We also want to distinguish problems that can be solved using less resources from problems that can only be solving using more resources.

Ok, so what can we do to work towards a classification of algorithms and a classification of problems?

Choose your favourite algorithm $A$.

Let $f$ be the function that measures how long the algorithm runs depending on the size of its input.

Now let us say we have two algorithms, $A$ and $B$ and two functions $f$ and $g$. The function $f$ measures the runtime of $A$, and $B$ measures the runtime of $g$?

:::warning
**Exercise 5.**

Classic examples of the above come from sorting. Discuss the comparisons of the runtimes of the following algorithms:

| $A$ | $B$ |
| -------- | -------- | 
| bubble sort     | insertion sort     |
| insertion sort     | merge sort     |
| merge sort | quick sort |

:::



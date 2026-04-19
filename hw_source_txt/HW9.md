---
title: Exercises on resolution

---

# Homework: Resolution and Horn Resolution

In the following exercises, show your resolution steps via trees e.g. as follows:

:::info
**Example (Resolution).**
Consider the following formula:
$$\xi := (p \lor q) \land (\lnot p \lor r) \land (\lnot q \lor s) \land (\lnot r \lor s) \land \lnot s$$

1. Conversion of $\varphi$ into a set of clauses:
$$\{\{p,q\}, \{\lnot p,r\}, \{\lnot q,s\}, \{\lnot r,s\}, \{\lnot s\} \}$$
2. Applying resolution repeatedly to derive the empty clause $\Box$, concluding that $\xi$ is unsatisfiable:
![Image 16.04.2026 at 00.18](https://hackmd.io/_uploads/HJ6wRbChWx.jpg)

:::

For typesetting you can use e.g. [quiver](https://q.uiver.app).

:::warning
**Exercise 1 (General vs. Horn resolution).**

**1a)** Use resolution to show that the following formula is unsatisfiable, following the recipe supplied below (and see the example above):

$$
\varphi :=(a \lor b)\land(\neg a \lor c)\land(\neg b \lor c)\land(\neg c \lor d)\land \neg d
$$

Instructions:

1. Convert the formula into a set of clauses.
2. Apply resolution repeatedly to derive the empty clause $\Box$, concluding that $\varphi$ is unsatisfiable.

**1b)** Use **unit resolution** to show that the following Horn formula is unsatisfiable, following the recipe supplied below:

$$
\psi= p \land q \land (\neg p \lor \neg q \lor r)\land(\neg r \lor s)\land \neg s
$$

Instructions:

1. Convert the formula into a set of clauses. Why is this a Horn formula?
2. Perform **unit resolution** repeatedly, i.e., for every resolution step one of the clauses must consist of only **one** literal.
3. Conclude that $\psi$ is unsatisfiable.
:::

:::warning
**Exercise 2 (Drone control system).**
A drone control system uses a safety interlock for enabling motor power.

The following controller policy is in place:

1. If GPS lock and battery health are both good, enabling motor power is allowed.
2. A manual override key also allows enabling motor power.
3. If battery health is bad, enabling motor power must be blocked.

Incident log reports:

```
* GPS lock valid
* battery unhealthy
* manual override present
* motor power enabled
```
Tasks:

1. Formalize the policy and incident log as propositional formulas. Clearly define the intended use of your propositional variables.
3. Convert your formalization into a set of clauses.
4. Use resolution to determine whether the log is consistent with the policy.
5. If unsatisfiable, identify how the policy and the log conflict.
:::
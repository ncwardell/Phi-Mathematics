---
title: "Fibonacci Numbers as Spiral Accumulations"
type: theorem
status: proven
depends_on:
  - golden-spiral.md
tags:
  - theorem-31
  - fibonacci
  - lucas
  - spiral-geometry
  - convergents
---

# Fibonacci Numbers as Spiral Accumulations

> **Theorem 31 (Fibonacci Numbers from Spiral Geometry):** *The Fibonacci numbers F(n) are the accumulated lengths at each step of the golden spiral. They are the integers the self-referential spiral produces as it unwinds.*

## Statement

The Fibonacci numbers F(n) are the accumulated lengths at each step of the golden spiral. They are the integers the self-referential spiral produces as it unwinds.

## Proof

The golden rectangle subdivision at step n produces a square of side length equal to F(n). This follows directly from the Fibonacci recurrence: the rectangle at step n has dimensions F(n+1) x F(n), and removing the F(n) x F(n) square leaves a rectangle of dimensions F(n) x F(n-1), which is the next golden rectangle.

The convergents of the continued fraction [1; 1, 1, 1, ...] are ratios of successive Fibonacci numbers:

1/1, 2/1, 3/2, 5/3, 8/5, 13/8, 21/13, 34/21, 55/34, 89/55, ...

These ratios converge to phi from alternating sides (above and below).

The integers appearing in the Fibonacci sequence -- {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...} -- are the specific integers the system "has access to" at each depth of unfolding. The Lucas sequence L(n) = {2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, ...} provides the complementary set.

Together, Fibonacci and Lucas generate the integers that the phi-spiral makes available to the system. QED

## Corollaries

(None stated separately; the key consequence is that the Fibonacci and Lucas integers become available for generating metallic means -- see Theorem 32.)

## Dependencies

- [The Golden Spiral as Recursive Bifurcation](golden-spiral.md) -- Theorem 30
- Theorem 11: Fibonacci (dynamic self-reference)

## Dependents

- [Metallic Means as Harmonic Overtones](metallic-means.md) -- Theorem 32 (Fibonacci integers birth metallic families)
- [Enumeration of Meeting Points](enumeration.md) -- Theorem 34 (Fibonacci and Lucas sequences are among those enumerated)

## Tags

`theorem-31` `fibonacci` `lucas` `spiral-geometry` `convergents` `golden-rectangle` `continued-fraction`

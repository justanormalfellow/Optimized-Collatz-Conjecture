# Optimized-Collatz-Conjecture
This program calculates Collatz sequence lengths while using memoization to avoid recalculating paths that have already been explored.
Base approach:
- For every number, independently calculate its entire Collatz sequence.
- Time complexity: O(n * k), where:
    n = amount of starting numbers tested
    k = average Collatz sequence length.

Optimized approach:
- Store previously calculated sequence lengths in a cache.
- Intermediate numbers are also stored, so future calculations can reuse them.
- The search through a range remains O(n), but the repeated Collatz calculations
  are reduced significantly because many paths are retrieved in O(1) from the cache.

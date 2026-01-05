# AGENT GOVERNANCE RULES
## When to Add, When to Stop (v1.0)

Purpose:
Prevent agent sprawl, over-engineering,
and system fragility.

This document is append-only.

—

## 1. DEFAULT POSITION

The system assumes:
- Fewer agents = more stability
- New agents introduce risk

Adding an agent is an exception, not a norm.

—

## 2. CONDITIONS REQUIRED TO ADD A NEW AGENT

A new agent may be added only if:

1. A real failure occurred
2. The failure repeated at least twice
3. The failure cannot be fixed by parameter tuning
4. The failure caused real cost or risk

If all four are not true:
    DO NOT ADD AGENT

—

## 3. FORBIDDEN REASONS TO ADD AGENTS

Never add an agent because:
- “It might be useful”
- “It sounds smart”
- “Other systems do this”
- “AI can handle it”

—

## 4. EARLY PHASE (FIRST 90 DAYS)

Rules:
- No new agent types
- Only threshold tuning
- Only rule clarification
- No new decision layers

Learning happens via observation, not expansion.

—

## 5. DEPRECATION RULE

If an agent:
- Has not influenced decisions for 60 days
- Produces only INFO-level events
- Adds cognitive load

Then:
    MARK_FOR_DEPRECATION

—

## END OF AGENT GOVERNANCE RULES
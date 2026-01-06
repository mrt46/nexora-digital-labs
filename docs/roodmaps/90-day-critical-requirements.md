# NEXORA 90-DAY CRITICAL REQUIREMENTS ANALYSIS
## Mandatory Foundations, Deferred Risks & Build Order (v1.0)

Role Context:
Chief Systems Architect
Chief AI Platform Engineer
Senior Software Architect
Risk & Scalability Analyst

Purpose:
Define, for the first 90 days, which components are:
- Mandatory to avoid system collapse
- Safe to defer without long-term damage
- Dangerous to ignore (will break the system later)

This document establishes:
- Non-negotiable minimums
- Deferred-but-required items
- Exact build order

This document is append-only.

—

## PART 1 — CORE ASSUMPTION (90-DAY SCOPE)

Constraints:
- Maximum 3 active sites
- Low traffic volatility
- Founder-driven oversight
- No full automation of scaling decisions
- Google ban risk must be near zero
- AI cost explosion must be impossible

—

## PART 2 — ABSOLUTELY MANDATORY (IF MISSING → SYSTEM BREAKS)

These MUST exist in the first 90 days.
If skipped now, they will cause architectural failure later.

—

### 1. CENTRAL AI ROUTER (SINGLE ENTRY POINT)

Responsible Roles:
- Chief AI Platform Engineer
- Senior Software Architect

Why Mandatory:
- Without it, model usage fragments
- API keys leak into agents
- Model switching becomes impossible
- Cost control is unmanageable

Collapse Scenario if Missing:
- 10+ agents hardcode different models
- Vendor change requires full rewrite
- Debugging becomes impossible

Status:
MANDATORY — BUILD FIRST

—

### 2. AGENT → CAPABILITY MAPPING (CENTRALIZED)

Responsible Roles:
- Chief Systems Architect
- AI Platform Engineer

Why Mandatory:
- Prevents agents from choosing expensive models
- Enforces intelligence hierarchy
- Enables predictable cost behavior

Collapse Scenario if Missing:
- Content agents use reasoning models
- Guard agents burn tokens unnecessarily
- Monthly cost becomes unpredictable

Status:
MANDATORY — BUILD WITH ROUTER

—

### 3. GLOBAL HARD BUDGET LIMIT (KILL SWITCH)

Responsible Roles:
- AI Platform Engineer
- Risk Analyst

Why Mandatory:
- AI systems fail silently
- One loop can burn the entire budget
- Human reaction is too slow

Collapse Scenario if Missing:
- Overnight cost spike
- No automatic stop
- Financial damage before detection

Status:
MANDATORY — BUILD DAY 1

—

## PART 3 — STRONGLY REQUIRED (SAFE TO DEFER, BUT MUST EXIST)

These do not break the system immediately,
but skipping them guarantees future pain.

—

### 4. USAGE LOGGING (MINIMAL)

Responsible Roles:
- Backend Engineer
- AI Platform Engineer

Why Required:
- Without logs, optimization is impossible
- Cost attribution per agent is blind
- Debugging relies on guesswork

Deferred Risk:
- Scaling becomes guess-based
- Inefficient agents remain hidden

90-Day Rule:
Log everything, analyze later.

Status:
REQUIRED — BUILD EARLY, ANALYZE LATER

—

### 5. SEARCH API ABSTRACTION (NOT HARD-CODED)

Responsible Roles:
- Software Architect
- Backend Engineer

Why Required:
- SERP providers change pricing
- Rate limits vary
- Failover is necessary

Deferred Risk:
- Search failures break trend intelligence
- Manual fixes required under pressure

90-Day Rule:
Abstraction now, optimization later.

Status:
REQUIRED — BUILD AFTER CORE ROUTER

—

## PART 4 — SAFE TO DEFER (DO NOT BUILD YET)

These are valuable but unnecessary in the first 90 days.

—

### 6. AUTOMATIC DEGRADE / THROTTLING LOGIC

Responsible Roles:
- Systems Architect
- AI Platform Engineer

Why Deferrable:
- Low traffic
- Human oversight exists
- Manual intervention is acceptable

Future Risk:
- Required at scale
- Required without human monitoring

Status:
DEFER — DO NOT BUILD IN FIRST 90 DAYS

—

### 7. FULL COST DASHBOARD UI

Responsible Roles:
- Backend Engineer
- Product Engineer

Why Deferrable:
- SQL queries sufficient initially
- Dashboard adds no control power early

Future Risk:
- Monitoring friction increases
- Optimization slows

Status:
DEFER — LOG ONLY

—

## PART 5 — BUILD ORDER (NON-NEGOTIABLE SEQUENCE)

This order minimizes rework and risk.

1. Central AI Router
2. Agent → Capability Mapping
3. Global Budget Kill Switch
4. Usage Logging
5. Search API Abstraction
6. (STOP — 90 DAY HOLD)
7. Automatic Degrade Logic (Later)
8. Cost Dashboard UI (Later)

Any deviation increases complexity.

—

## PART 6 — ROLE RESPONSIBILITY MATRIX (90 DAYS)

Chief Systems Architect:
- Enforce boundaries
- Prevent over-engineering
- Approve architecture changes

AI Platform Engineer:
- Own router
- Own cost control
- Own provider abstraction

Senior Software Architect:
- Ensure clean interfaces
- Prevent agent-level coupling

Risk & Scalability Analyst:
- Identify silent failure paths
- Monitor deferred risks

—

## FINAL 90-DAY PRINCIPLE

Do not build for scale.
Build so scale does not break you later.

The goal is not speed.
The goal is survivability.

—

END OF DOCUMENT
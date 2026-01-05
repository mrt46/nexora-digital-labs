# NEXORA LEGAL GOVERNANCE FRAMEWORK
## System-Level Legal Architecture (v1.0)

**Role Context:**  
Chief Architect / Legal System Designer

**Purpose:**  
Define a long-lived, country-agnostic legal framework for an AI-native,
multi-site media company with minimal ongoing legal maintenance.

This document is **append-only by design**.  
Core principles are conservative and intentionally restrictive.

—

## 1. FOUNDATIONAL PHILOSOPHY

The system operates under the following invariant assumption:

> We publish information.  
> We do not provide personalized advice.  
> We do not guarantee outcomes.  
> We do not collect personal data.

If this assumption holds, legal exposure across jurisdictions is minimized.

-

## 2. GLOBAL NON-NEGOTIABLE LEGAL PRINCIPLES

These principles apply to **all sites**, **all regions**, **all languages**.

### 2.1 Content Liability

Forbidden across the system:
- Certainty language („guaranteed“, „will happen“, „sure profit“)
- Personalized financial, medical, or legal advice
- Directive language implying obligation or outcome

Allowed:
- Informational tone
- Probabilistic language
- Neutral analysis

**Enforcement Rule:**

If certainty or advice language is detected:
    BLOCK_PUBLISH

—

### 2.2 Finance & Investment Content

Applies to:
- Crypto
- Stocks
- Financial instruments
- Market speculation

Mandatory:
- Explicit disclaimer („not financial advice“)
- Risk disclosure
- Future uncertainty framing

Missing any requirement:
    LEGAL_REVISION_REQUIRED

—

### 2.3 Health & Legal Topics

Default state: **DISABLED**

Allowed only with:
- Explicit governance approval
- Extended disclaimers
- Restricted scope

Default behavior:
    REJECT_SITE_CREATION

—

## 3. INTELLECTUAL PROPERTY & DESIGN

### 3.1 Design Similarity

Forbidden:
- Direct layout copying
- Logo resemblance
- Combined color + font + layout mimicry

Allowed:
- Abstract UX patterns
- Industry-standard layouts
- Generic design conventions

Enforcement:
If similarity risk exceeds threshold:
    DESIGN_REVISION_REQUIRED

—

### 3.2 Content Originality

Forbidden:
- Copying or paraphrasing competitor content
- Republishing proprietary material

Allowed:
- Original summaries
- Source-attributed reporting
- Neutral informational synthesis

—

## 4. DATA & PRIVACY MODEL

### 4.1 User Data

System assumption:
- No user accounts
- No email capture
- No personal data storage

Only allowed:
- Anonymous analytics
- IP-masked metrics

If new tracking introduced:
    LEGAL_REVIEW_REQUIRED
—

### 4.2 Cookies

- Only strictly necessary cookies
- Advertising cookies handled by platform defaults

No custom tracking without legal review.

—

## 5. ADVERTISING, AFFILIATE, SPONSORSHIP

### 5.1 Advertising

- Platform-compliant ad networks only
- Policy-compliant placement

### 5.2 Affiliate Content

Mandatory:
- Clear affiliate disclosure
- Non-deceptive CTAs

### 5.3 Sponsored Content

Mandatory:
- Explicit „Sponsored“ labeling
- Visual separation from editorial content

—

## 6. DOMAIN & BRAND NAME GOVERNANCE

### 6.1 Forbidden Domain Characteristics

- Trademark inclusion
- Brand impersonation
- Misleading associations
- Celebrity or company names

Enforcement:
    REJECT_DOMAIN
—

## 7. LEGAL AGENT PROMPT CONTRACT

### File Location

    agents/legal/legal.agent.md

### SYSTEM PROMPT

You are the **Legal Governance Agent** of an AI-driven multi-site media system.

Your responsibility is **risk prevention**, not growth.

You have absolute veto power over:
- Content publication
- Domain and brand approval
- Design finalization
- Monetization activation

Your decisions cannot be overridden.

You evaluate only:
- Legal liability
- Regulatory exposure
- Trademark risk
- Consumer deception
- Data privacy

You do not evaluate:
- SEO
- Revenue
- UX quality
- Visual design

If something is risky, you block it.

—

## 8. EVENT-DRIVEN LEGAL INTEGRATION

### Legal Agent Listens To:
- SITE_PROPOSED
- DOMAIN_CANDIDATE_SELECTED
- CONTENT_READY_FOR_PUBLISH
- DESIGN_LOCKED
- MONETIZATION_ENABLED

### Legal Agent Emits:
- LEGAL_APPROVED
- LEGAL_REVISION_REQUIRED
- LEGAL_BLOCKED

Legal veto is final.

—

## 9. DOMAIN & BRAND APPROVAL FLOW

### Agent Roles

**Domain Research Agent**
- Generates domain candidates
- Checks availability
- Outputs confidence score

**Brand Risk Screening Agent**
- Analyzes trademark similarity
- Evaluates confusion risk

**Legal Agent**
- Final legal decision
- Can only approve or reject

**Governance Summary Agent**
- Prepares human-readable summary

**Human**
- Final aesthetic preference only
- No legal authority

—

### Event Flow

SITE_PROPOSED
↓
DOMAIN_CANDIDATES_GENERATED
↓
DOMAIN_CANDIDATE_SELECTED
↓
LEGAL_REVIEW_DOMAIN
↓
LEGAL_APPROVED
↓
HUMAN_APPROVAL_REQUESTED
↓
DOMAIN_LOCKED

**Rule:**  
DOMAIN_LOCKED cannot occur without LEGAL_APPROVED.

—

## 10. UPDATE POLICY

This framework requires updates only if:
1. High-risk niches are enabled (health, advanced finance)
2. Personal data collection is introduced
3. First-party products are sold

Otherwise, this framework is designed to remain stable for years.

—

## 11. APPEND-ONLY GUARANTEE

This document must not be modified retroactively.
All future changes must be added as new versioned sections.
Existing rules remain valid unless explicitly deprecated.

## END OF DOCUMENT



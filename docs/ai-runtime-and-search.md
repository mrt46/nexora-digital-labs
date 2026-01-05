# NEXORA AI RUNTIME & SEARCH INTEGRATION
## Environment Variables, API Routing & External AI Tools (v1.1)

Role Context:
Chief AI Infrastructure & Cost Optimization Architect

Purpose:
Define a unified runtime configuration for AI models and external search tools,
ensuring minimal cost, maximum flexibility, and zero agent-level coupling.

This document is append-only.

—

## 1. CORE ARCHITECTURE PRINCIPLE

Agents never:
- Choose models
- Hold API keys
- Call external tools directly

Agents only request capabilities.

A centralized router:
- Selects the provider
- Selects the model
- Selects the external tool
- Applies budget and safety rules

—

## 2. ENVIRONMENT VARIABLE LAYER

All configuration is injected at runtime via environment variables.

—

### 2.1 AI PROVIDER API KEYS

OPENAI_API_KEY=xxxx  
GEMINI_API_KEY=xxxx  
ANTHROPIC_API_KEY=xxxx  

Notes:
- Gemini free tier may be used for development and testing
- Production usage assumes paid tiers when limits are exceeded

—

### 2.2 AI CAPABILITY TO MODEL MAPPING

Models are abstracted behind capability levels.

MODEL_REASONING=openai:gpt-4.1  
MODEL_STANDARD=google:gemini-1.5-pro  
MODEL_FAST=openai:gpt-3.5-turbo  
MODEL_ULTRA_FAST=anthropic:claude-haiku  

Changing a model here updates the entire system globally.

—

### 2.3 GLOBAL AI COST LIMITS

MAX_TOKENS_PER_CALL=4000  
MAX_CALLS_PER_AGENT_PER_DAY=200  
MONTHLY_AI_BUDGET_USD=100  

If limits are exceeded:
- Calls are throttled or downgraded
- Orchestrator is notified

—

## 3. EXTERNAL SEARCH & WEB DATA APIS

AI models do not browse the web.
All live data must come from search APIs.

—

### 3.1 SEARCH API KEYS

SERPER_API_KEY=xxxx  
BRAVE_SEARCH_API_KEY=xxxx  

At least one search provider must be active.

—

### 3.2 SEARCH TOOL SELECTION LOGIC

Default routing strategy:
- Breaking news and SERP analysis → Serper (Google SERP)
- General research and fallback → Brave Search
- Automatic failover if one provider is unavailable

Agents never know which provider is used.

—

## 4. AGENT TO CAPABILITY AND TOOL ROUTING

### 4.1 AI CAPABILITY LEVELS

REASONING:
High-stakes decisions, governance, legal, orchestration

STANDARD:
Content planning, design generation, trend analysis

FAST:
Classification, scoring, QA checks

ULTRA_FAST:
Guards, similarity checks, lightweight validation

—

### 4.2 SEARCH TOOL USAGE BY AGENT

Trend Intelligence Agent:
- SERPER
- BRAVE (fallback)

Domain Research Agent:
- SERPER

Brand Risk Screening Agent:
- SERPER

Site Experience Critic Agent:
- BRAVE

Content Generation Agents:
- No direct search access
- Consume prepared and cached data

—

## 5. CENTRAL ROUTER LOGIC

All AI and search calls go through a single router.

Execution flow:

Agent requests capability (and optional search)
→ Router checks budget and limits
→ Router resolves model from environment variables
→ Router resolves search provider if required
→ External API call is executed
→ Result is cached
→ Response returned to agent

Agents never see:
- Provider names
- Model names
- API keys

—

## 6. COST OPTIMIZATION POLICY

1. Gemini models are preferred for STANDARD workloads
2. Reasoning models are reserved for governance-only events
3. Search results are aggressively cached
4. Identical queries are never executed twice in a short window
5. Guard agents always use the cheapest viable models

—

## 7. WHY THIS ARCHITECTURE WORKS

- Vendor lock-in is avoided
- Free tiers can be leveraged safely
- Production costs are predictable
- Agents remain simple and disposable
- Scaling does not multiply mistakes

—

FINAL PRINCIPLE

Agents do not know tools.
They know intent.

The router knows everything else.

—

END OF DOCUMENT
# NEXORA AI API CONTROL PLANE
## Database-Driven AI & Tool Routing Architecture (v1.0)

Role Context:
Chief Software Architect & AI Platform Engineer

Purpose:
Define a fully centralized, database-driven AI API and external tool
management system that removes all manual per-agent configuration
and guarantees cost control, scalability, and operational safety.

This document is append-only.

—

## CORE ANSWER (ABSOLUTE)

You do NOT manage AI APIs per agent manually.

You manage:
- Capabilities
- Policies
- Budgets

The system manages:
- Providers
- Models
- Routing
- Failover
- Cost enforcement

—

## HIGH-LEVEL AI API MAP (SYSTEM SCHEMA)


                ┌─────────────────────────┐
                │   ENVIRONMENT VARIABLES │
                │   (API KEYS ONLY)       │
                └───────────┬─────────────┘
                            │
                ┌───────────▼─────────────┐
                │     AI ROUTER CORE       │
                │   (SINGLE ENTRY POINT)  │
                └───────────┬─────────────┘
                            │
    ┌───────────────────────▼────────────────────────┐
    │              POLICY & ROUTING DATABASE          │
    │                                                  │
    │  agent_capabilities                              │
    │  model_mapping                                   │
    │  search_providers                                │
    │  cost_limits                                     │
    │  cache_rules                                     │
    └───────────┬───────────────────┬────────────────┘
                │                   │
    ┌───────────▼──────────┐   ┌────▼────────────────┐
    │     AI PROVIDERS      │   │   SEARCH PROVIDERS   │
    │                       │   │                     │
    │ OpenAI                │   │ Serper (Google SERP) │
    │ Google Gemini         │   │ Brave Search         │
    │ Anthropic             │   │ Fallback / Backup   │
    └───────────────────────┘   └─────────────────────┘
    
    —

## DATABASE-DRIVEN CONTROL (NO MANUAL WORK)

Agents never know:
- Model names
- Provider names
- API keys
- Pricing
- Failover logic

Agents only send:
- agent_name
- requested_capability
- optional: needs_search

Everything else is resolved centrally.

—

## CORE DATABASE TABLES

### AGENT_CAPABILITIES

Defines what level of intelligence each agent is allowed to request.

| agent_name              | capability_level |
|————————|——————|
| orchestrator            | REASONING        |
| legal_agent             | REASONING        |
| design_orchestrator     | REASONING        |
| experience_meta_learner | REASONING        |
| web_designer            | STANDARD         |
| content_writer          | STANDARD         |
| seo_architect           | STANDARD         |
| trend_intelligence      | STANDARD         |
| site_experience_critic  | STANDARD         |
| design_qa               | FAST             |
| site_tester             | FAST             |
| originality_guard       | ULTRA_FAST       |

—

### MODEL_MAPPING

Maps capability levels to actual providers and models.

| capability  | provider    | model_name        |
|————|-————|-——————|
| REASONING  | openai      | gpt-4.1           |
| STANDARD   | google      | gemini-1.5-pro    |
| FAST       | openai      | gpt-3.5-turbo     |
| ULTRA_FAST | anthropic  | claude-haiku      |

Changing one row reroutes the entire system instantly.

—

### SEARCH_PROVIDERS

Controls live web data access and failover.

| provider | priority | enabled |
|———|-———|———|
| serper  | 1        | true    |
| brave   | 2        | true    |

Failover is automatic based on priority.

—

### COST_LIMITS

Hard safety rails for spending.

| scope  | limit_type              | value |
|-——|-————————|-——|
| global| monthly_budget_usd      | 100   |
| agent | max_calls_per_day       | 200   |
| call  | max_tokens_per_request  | 4000  |

Exceeding limits triggers throttling or downgrade.

—

### CACHE_RULES

Prevents redundant API usage.

| resource_type | ttl_minutes |
|—————|-————|
| search_query  | 1440        |
| trend_report  | 720         |
| design_asset  | 10080       |

—

## RUNTIME EXECUTION FLOW

Agent
    → sends (agent_name, capability_request, needs_search?)
    → Router
    → lookup agent_capabilities
    → lookup model_mapping
    →enforce cost_limits
    → check cache_rules
    → select AI or Search provider
    → execute external call
    → log usage
    → cache result
    → return response
    
No human intervention.
No per-agent configuration.
No manual routing.

—

## WHY THIS ELIMINATES MANUAL WORK

You never:
- Edit agent code to change models
- Touch API keys per agent
- Manually switch providers
- Reconfigure costs in code

You only:
- Update database rows
- Adjust environment variables once

—

## SCALING GUARANTEE

Adding a new agent requires:
1. One database row in agent_capabilities
2. Zero code changes
3. Zero API configuration changes

This architecture scales from:
5 agents → 50 agents → 500 agents

—

FINAL PRINCIPLE

AI infrastructure is a control-plane problem,
not a prompt problem.

Centralize control.
Decentralize execution.

—

END OF DOCUMENT 
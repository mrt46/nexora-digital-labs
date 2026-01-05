# AI CONTROL PLANE DATABASE SCHEMA
## SQLite / Postgres Compatible (v1.0)

CREATE TABLE agent_capabilities (
    agent_name TEXT PRIMARY KEY,
    capability_level TEXT NOT NULL
);

CREATE TABLE model_mapping (
    capability TEXT PRIMARY KEY,
    provider TEXT NOT NULL,
    model_name TEXT NOT NULL
);

CREATE TABLE search_providers (
    provider TEXT PRIMARY KEY,
    priority INTEGER NOT NULL,
    enabled BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE cost_limits (
    scope TEXT NOT NULL,
    limit_type TEXT NOT NULL,
    value INTEGER NOT NULL,
    PRIMARY KEY (scope, limit_type)
);

CREATE TABLE usage_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_name TEXT,
    provider TEXT,
    model_name TEXT,
    tokens_used INTEGER,
    cost_usd REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cache_rules (
    resource_type TEXT PRIMARY KEY,
    ttl_minutes INTEGER NOT NULL
);
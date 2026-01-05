# AI COST DASHBOARD LOGIC
## Query & Threshold Definitions (v1.0)

SELECT SUM(cost_usd)
FROM usage_logs
WHERE strftime(‘%Y-%m’, created_at) = strftime(‘%Y-%m’, ‘now’);

SELECT agent_name, SUM(cost_usd)
FROM usage_logs
GROUP BY agent_name;

SELECT model_name, SUM(cost_usd)
FROM usage_logs
GROUP BY model_name
ORDER BY SUM(cost_usd) DESC;

BUDGET_WARNING_THRESHOLD = 0.70
BUDGET_THROTTLE_THRESHOLD = 0.90
BUDGET_FREEZE_THRESHOLD = 1.00
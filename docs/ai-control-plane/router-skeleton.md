# AI ROUTER CORE
## Minimal Python Skeleton (v1.0)

class AIRouter:
    def __init__(self, db, providers):
        self.db = db
        self.providers = providers

    def handle_request(self, agent_name, capability, prompt):
        self._check_budget()
        model = self._resolve_model(capability)
        provider = self.providers[model[“provider”]]

        response = provider.call(
            model=model[“model_name”],
            prompt=prompt
        )

        self._log_usage(
            agent_name,
            model[“provider”],
            model[“model_name”],
            response.tokens,
            response.cost
        )

        return response.output

    def _resolve_model(self, capability):
        return self.db.query_one(
            “SELECT provider, model_name FROM model_mapping WHERE capability = ?”,
            (capability,)
        )

    def _check_budget(self):
        spent = self.db.query_value(
            “SELECT SUM(cost_usd) FROM usage_logs WHERE strftime(‘%Y-%m’, created_at) = strftime(‘%Y-%m’, ‘now’)”
        )
        limit = self.db.query_value(
            “SELECT value FROM cost_limits WHERE scope=‘global’ AND limit_type=‘monthly_budget_usd’”
        )
        if spent >= limit:
            raise Exception(“AI_BUDGET_EXCEEDED”)

    def _log_usage(self, agent, provider, model, tokens, cost):
        self.db.execute(
            “INSERT INTO usage_logs (agent_name, provider, model_name, tokens_used, cost_usd) VALUES (?, ?, ?, ?, ?)”,
            (agent, provider, model, tokens, cost)
        )
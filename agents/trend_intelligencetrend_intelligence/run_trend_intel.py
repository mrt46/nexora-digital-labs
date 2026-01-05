# run_trend_intel.py

import json
from agents.regional_trend_scanner import RegionalTrendScanner
from agents.performance_decomposer import PerformanceDecomposer
from agents.yield_analysis import YieldAnalysisAgent
from agents.adaptation_feasibility import AdaptationFeasibilityAgent
from agents.strategy_inquiry import StrategyInquiryAgent
from data.db import init_db, get_conn


def main():
    # --- DB init ---
    init_db()

    # --- Context ---
    context = {"region": "TR"}

    # --- Agents ---
    scanner = RegionalTrendScanner(
        "scanner", "prompts/regional-trend-scanner.agent.md"
    )
    perf = PerformanceDecomposer(
        "decomposer", "prompts/performance-decomposer.agent.md"
    )
    yield_agent = YieldAnalysisAgent(
        "yield", "prompts/yield-analysis.agent.md"
    )
    adapt = AdaptationFeasibilityAgent(
        "adapt", "prompts/adaptation-feasibility.agent.md"
    )
    inquiry = StrategyInquiryAgent(
        "inquiry", "prompts/strategy-inquiry.agent.md"
    )

    # --- Run pipeline ---
    report = {}
    report["trend"] = scanner.run(context)
    report["performance"] = perf.run(report)
    report["yield"] = yield_agent.run(report)
    report["adaptation"] = adapt.run(report)
    report["strategy_questions"] = inquiry.run(report)

    # --- Save JSON report ---
    with open("output/reports.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    # --- Save to DB ---
    conn = get_conn()
    c = conn.cursor()

    c.execute("""
    INSERT INTO trend_reports
    (region, site, topic, traffic_level, velocity, adaptability, risk_level)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        report["trend"]["region"],
        report["trend"]["site"],
        report["trend"]["primary_topic"],
        report["trend"]["traffic_level"],
        report["trend"]["velocity"],
        report["adaptation"]["adaptable"],
        report["adaptation"]["risk_level"]
    ))

    conn.commit()
    conn.close()

    print("Trend Intelligence report generated and stored.")


if __name__ == "__main__":
    main()

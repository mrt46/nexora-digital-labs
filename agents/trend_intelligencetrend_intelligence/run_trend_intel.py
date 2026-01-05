# run_trend_intel.py

import json

from agents.regional_trend_scanner import RegionalTrendScanner
from agents.performance_decomposer import PerformanceDecomposer
from agents.yield_analysis import YieldAnalysisAgent
from agents.adaptation_feasibility import AdaptationFeasibilityAgent
from agents.strategy_inquiry import StrategyInquiryAgent

from data.db import init_db, get_conn
from events import emit_event
from scoring import score_report
from content_brief import generate_content_brief


def main():
    # --- DB init ---
    init_db()

    REGIONS = ["TR", "US", "EU"]

    # --- Agents (tek kez oluşturulur) ---
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

    # --- Loop regions ---
    for region in REGIONS:
        context = {"region": region}

        report = {}
        report["trend"] = scanner.run(context)
        report["performance"] = perf.run(report)
        report["yield"] = yield_agent.run(report)
        report["adaptation"] = adapt.run(report)
        report["strategy_questions"] = inquiry.run(report)

        # --- Save JSON report per region ---
        with open(f"output/reports_{region}.json", "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        # --- Save to DB ---
        conn = get_conn()
        c = conn.cursor()
        c.execute("""
            INSERT INTO trend_reports
            (region, site, topic, traffic_level, velocity, adaptability, risk_level)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            region,
            report["trend"]["site"],
            report["trend"]["primary_topic"],
            report["trend"]["traffic_level"],
            report["trend"]["velocity"],
            report["adaptation"]["adaptable"],
            report["adaptation"]["risk_level"]
        ))
        conn.commit()
        conn.close()

        # --- Event: Trend ready ---
        emit_event(
            "TREND_INTELLIGENCE_REPORT_READY",
            {
                "region": region,
                "topic": report["trend"]["primary_topic"],
                "traffic": report["trend"]["traffic_level"],
                "velocity": report["trend"]["velocity"],
                "risk": report["adaptation"]["risk_level"]
            }
        )

        # --- Scoring & Governance ---
        governance_summary = score_report(report)

        emit_event(
            "GOVERNANCE_SUMMARY_READY",
            {
                "region": region,
                **governance_summary
            }
        )

        # --- Content brief (if approved) ---
        brief = generate_content_brief(report, governance_summary)
        if brief:
            emit_event(
                "CONTENT_BRIEF_READY",
                {
                    "region": region,
                    **brief
                }
            )

    print("Trend Intelligence pipeline completed for all regions.")


if __name__ == "__main__":
    main()        "inquiry", "prompts/strategy-inquiry.agent.md"
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

    # --- EVENT: Trend report ready ---
    emit_event(
        "TREND_INTELLIGENCE_REPORT_READY",
        {
            "region": report["trend"]["region"],
            "topic": report["trend"]["primary_topic"],
            "adaptability": report["adaptation"]["adaptable"],
            "risk": report["adaptation"]["risk_level"]
        }
    )

    # --- SCORING & GOVERNANCE SUMMARY ---
    governance_summary = score_report(report)

    emit_event(
        "GOVERNANCE_SUMMARY_READY",
        governance_summary
    )

    print("Trend Intelligence pipeline completed.")


if __name__ == "__main__":
    main()    report = {}
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

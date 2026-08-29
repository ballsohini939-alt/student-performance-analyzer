import {
  TrendingUp,
  Award,
  Target,
} from "lucide-react";

import PerformanceChart from "../components/PerformanceChart";
import SectionHeader from "../components/SectionHeader";

function Performance() {
  return (
    <section className="dashboard-content">
      <SectionHeader
        eyebrow="PERFORMANCE ANALYTICS"
        title="Student performance"
        action="View trends"
      />

      <div className="page-intro">
        <p>
          Analyze academic performance, identify progress patterns,
          and understand where students need additional support.
        </p>
      </div>

      <div className="stats-grid">
        <article className="stat-card">
          <div className="stat-card-top">
            <div className="stat-card-icon">
              <TrendingUp size={21} />
            </div>
          </div>

          <div className="stat-card-content">
            <p>Average Performance</p>
            <h3>78.4%</h3>
            <span>Overall class average</span>
          </div>
        </article>

        <article className="stat-card">
          <div className="stat-card-top">
            <div className="stat-card-icon">
              <Award size={21} />
            </div>
          </div>

          <div className="stat-card-content">
            <p>Highest Performance</p>
            <h3>92.6%</h3>
            <span>Top student score</span>
          </div>
        </article>

        <article className="stat-card">
          <div className="stat-card-top">
            <div className="stat-card-icon">
              <Target size={21} />
            </div>
          </div>

          <div className="stat-card-content">
            <p>Pass Rate</p>
            <h3>90%</h3>
            <span>Students meeting criteria</span>
          </div>
        </article>
      </div>

      <div className="analytics-panel large-panel">
        <SectionHeader
          eyebrow="PERFORMANCE TREND"
          title="Academic progress"
        />

        <PerformanceChart />
      </div>
    </section>
  );
}

export default Performance;

import {
  TrendingUp,
  TrendingDown,
  Activity,
  Target,
} from "lucide-react";

import SectionHeader from "../components/SectionHeader";
import PerformanceChart from "../components/PerformanceChart";

function PerformanceTrends() {
  return (
    <section className="dashboard-content">
      <SectionHeader
        eyebrow="PERFORMANCE TRENDS"
        title="Academic progress"
        action="View performance"
      />

      <div className="page-intro">
        <p>
          Track academic progress over time, identify improvement
          patterns, and detect students who may need additional
          support.
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
            <p>Improving Students</p>
            <h3>6</h3>
            <span>Showing positive progress</span>
          </div>
        </article>

        <article className="stat-card">
          <div className="stat-card-top">
            <div className="stat-card-icon">
              <TrendingDown size={21} />
            </div>
          </div>

          <div className="stat-card-content">
            <p>Declining Students</p>
            <h3>2</h3>
            <span>Require additional attention</span>
          </div>
        </article>

        <article className="stat-card">
          <div className="stat-card-top">
            <div className="stat-card-icon">
              <Activity size={21} />
            </div>
          </div>

          <div className="stat-card-content">
            <p>Stable Students</p>
            <h3>2</h3>
            <span>Maintaining similar results</span>
          </div>
        </article>

        <article className="stat-card">
          <div className="stat-card-top">
            <div className="stat-card-icon">
              <Target size={21} />
            </div>
          </div>

          <div className="stat-card-content">
            <p>Class Growth</p>
            <h3>4.2%</h3>
            <span>Change from previous assessment</span>
          </div>
        </article>
      </div>

      <div className="analytics-panel">
        <SectionHeader
          eyebrow="ACADEMIC PROGRESS"
          title="Performance over time"
        />

        <PerformanceChart />
      </div>

      <div className="analytics-panel">
        <SectionHeader
          eyebrow="TREND INTERPRETATION"
          title="Performance monitoring"
        />

        <div className="page-intro">
          <p>
            Performance history can be used to identify improving,
            declining, and stable students. These insights can help
            guide targeted academic support and learning strategies.
          </p>
        </div>
      </div>
    </section>
  );
}

export default PerformanceTrends;
import { Trophy, Medal, TrendingUp } from "lucide-react";

import RankingTable from "../components/RankingTable";
import SectionHeader from "../components/SectionHeader";

function Rankings() {
  return (
    <section className="dashboard-content">
      <SectionHeader
        eyebrow="STUDENT RANKINGS"
        title="Top performers"
        action="View performance"
      />

      <div className="page-intro">
        <p>
          Compare students based on academic performance and
          identify the strongest performers in the dataset.
        </p>
      </div>

      <div className="stats-grid">
        <article className="stat-card">
          <div className="stat-card-top">
            <div className="stat-card-icon">
              <Trophy size={21} />
            </div>
          </div>

          <div className="stat-card-content">
            <p>Top Performer</p>
            <h3>92.6%</h3>
            <span>Highest percentage</span>
          </div>
        </article>

        <article className="stat-card">
          <div className="stat-card-top">
            <div className="stat-card-icon">
              <Medal size={21} />
            </div>
          </div>

          <div className="stat-card-content">
            <p>Top 3 Average</p>
            <h3>89.6%</h3>
            <span>Average of top performers</span>
          </div>
        </article>

        <article className="stat-card">
          <div className="stat-card-top">
            <div className="stat-card-icon">
              <TrendingUp size={21} />
            </div>
          </div>

          <div className="stat-card-content">
            <p>High Performers</p>
            <h3>5</h3>
            <span>Students above 80%</span>
          </div>
        </article>
      </div>

      <div className="analytics-panel">
        <SectionHeader
          eyebrow="CLASS RANKING"
          title="Student leaderboard"
        />

        <RankingTable />
      </div>
    </section>
  );
}

export default Rankings;

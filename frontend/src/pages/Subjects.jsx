import { BookOpen, TrendingUp, Award } from "lucide-react";

import SectionHeader from "../components/SectionHeader";
import SubjectPerformance from "../components/SubjectPerformance";

function Subjects() {
  return (
    <section className="dashboard-content">
      <SectionHeader
        eyebrow="SUBJECT ANALYTICS"
        title="Subject performance"
        action="View details"
      />

      <div className="page-intro">
        <p>
          Analyze subject-wise performance and identify academic
          strengths and areas that need improvement.
        </p>
      </div>

      <div className="stats-grid">
        <article className="stat-card">
          <div className="stat-card-top">
            <div className="stat-card-icon">
              <BookOpen size={21} />
            </div>
          </div>

          <div className="stat-card-content">
            <p>Subjects Analyzed</p>
            <h3>5</h3>
            <span>Academic subjects</span>
          </div>
        </article>

        <article className="stat-card">
          <div className="stat-card-top">
            <div className="stat-card-icon">
              <Award size={21} />
            </div>
          </div>

          <div className="stat-card-content">
            <p>Strongest Subject</p>
            <h3>88%</h3>
            <span>Computer Science</span>
          </div>
        </article>

        <article className="stat-card">
          <div className="stat-card-top">
            <div className="stat-card-icon">
              <TrendingUp size={21} />
            </div>
          </div>

          <div className="stat-card-content">
            <p>Subject Average</p>
            <h3>81.2%</h3>
            <span>Across analyzed subjects</span>
          </div>
        </article>
      </div>

      <div className="analytics-panel">
        <SectionHeader
          eyebrow="SUBJECT BREAKDOWN"
          title="Performance by subject"
        />

        <SubjectPerformance />
      </div>
    </section>
  );
}

export default Subjects;
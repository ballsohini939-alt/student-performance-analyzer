import {
  Clock3,
  TrendingUp,
  BookOpen,
  Target,
} from "lucide-react";

import SectionHeader from "../components/SectionHeader";

function StudyHours() {
  return (
    <section className="dashboard-content">
      <SectionHeader
        eyebrow="STUDY HABITS"
        title="Study hours analysis"
        action="View analytics"
      />

      <div className="page-intro">
        <p>
          Understand study-hour patterns and explore how learning
          habits relate to academic performance.
        </p>
      </div>

      <div className="stats-grid">
        <article className="stat-card">
          <div className="stat-card-top">
            <div className="stat-card-icon">
              <Clock3 size={21} />
            </div>
          </div>

          <div className="stat-card-content">
            <p>Average Study Hours</p>
            <h3>5.8h</h3>
            <span>Per student</span>
          </div>
        </article>

        <article className="stat-card">
          <div className="stat-card-top">
            <div className="stat-card-icon">
              <TrendingUp size={21} />
            </div>
          </div>

          <div className="stat-card-content">
            <p>Highest Study Time</p>
            <h3>8.2h</h3>
            <span>Daily average</span>
          </div>
        </article>

        <article className="stat-card">
          <div className="stat-card-top">
            <div className="stat-card-icon">
              <BookOpen size={21} />
            </div>
          </div>

          <div className="stat-card-content">
            <p>Study Consistency</p>
            <h3>82%</h3>
            <span>Learning consistency score</span>
          </div>
        </article>

        <article className="stat-card">
          <div className="stat-card-top">
            <div className="stat-card-icon">
              <Target size={21} />
            </div>
          </div>

          <div className="stat-card-content">
            <p>Recommended Target</p>
            <h3>6h</h3>
            <span>Suggested daily study time</span>
          </div>
        </article>
      </div>

      <div className="analytics-panel">
        <SectionHeader
          eyebrow="STUDY VS PERFORMANCE"
          title="Learning habit analysis"
        />

        <div className="placeholder-panel">
          <h2>Study hours vs academic performance</h2>

          <p>
            This workspace will display the relationship between
            study hours and student performance using the existing
            study-hours dataset.
          </p>
        </div>
      </div>
    </section>
  );
}

export default StudyHours;
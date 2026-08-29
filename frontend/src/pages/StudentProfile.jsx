import {
  User,
  Award,
  Target,
  BookOpen,
} from "lucide-react";

import SectionHeader from "../components/SectionHeader";

function StudentProfile() {
  return (
    <section className="dashboard-content">
      <SectionHeader
        eyebrow="STUDENT PROFILE"
        title="Academic profile"
        action="View students"
      />

      <div className="page-intro">
        <p>
          Review individual student performance, strengths,
          weaknesses, and learning patterns.
        </p>
      </div>

      <div className="profile-layout">
        <article className="analytics-panel profile-card">
          <div className="profile-avatar">
            SB
          </div>

          <div className="profile-details">
            <p className="section-eyebrow">
              STUDENT
            </p>

            <h2>Sohini Ball</h2>

            <p>
              Student Performance Analyzer dataset
            </p>
          </div>
        </article>

        <div className="stats-grid profile-stats">
          <article className="stat-card">
            <div className="stat-card-top">
              <div className="stat-card-icon">
                <Award size={21} />
              </div>
            </div>

            <div className="stat-card-content">
              <p>Percentage</p>
              <h3>92.6%</h3>
              <span>Overall performance</span>
            </div>
          </article>

          <article className="stat-card">
            <div className="stat-card-top">
              <div className="stat-card-icon">
                <Target size={21} />
              </div>
            </div>

            <div className="stat-card-content">
              <p>Grade</p>
              <h3>A</h3>
              <span>Current academic grade</span>
            </div>
          </article>

          <article className="stat-card">
            <div className="stat-card-top">
              <div className="stat-card-icon">
                <BookOpen size={21} />
              </div>
            </div>

            <div className="stat-card-content">
              <p>Strongest Subject</p>
              <h3>Computer Science</h3>
              <span>Highest subject score</span>
            </div>
          </article>

          <article className="stat-card">
            <div className="stat-card-top">
              <div className="stat-card-icon">
                <User size={21} />
              </div>
            </div>

            <div className="stat-card-content">
              <p>Performance</p>
              <h3>Excellent</h3>
              <span>Overall performance category</span>
            </div>
          </article>
        </div>
      </div>

      <div className="analytics-panel">
        <SectionHeader
          eyebrow="LEARNING ANALYSIS"
          title="Personalized learning insight"
        />

        <div className="profile-insight">
          <h3>Keep building on your strengths</h3>

          <p>
            Your current performance indicates strong academic
            progress. Continue focusing on weaker subjects while
            maintaining consistent study habits.
          </p>
        </div>
      </div>
    </section>
  );
}

export default StudentProfile;
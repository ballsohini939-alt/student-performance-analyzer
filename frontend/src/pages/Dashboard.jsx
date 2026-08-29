import {
  Users,
  Trophy,
  Target,
  GraduationCap,
  TrendingUp,
  ArrowUpRight,
} from "lucide-react";

import StatCard from "../components/StatCard";
import PerformanceChart from "../components/PerformanceChart";
import GradeDistribution from "../components/GradeDistribution";
import SubjectPerformance from "../components/SubjectPerformance";
import RankingTable from "../components/RankingTable";
import InsightCard from "../components/InsightCard";
import SectionHeader from "../components/SectionHeader";

function Dashboard() {
  return (
    <section className="dashboard-content">

      {/* Welcome */}
      <div className="welcome-section">
        <div>
          <p className="section-eyebrow">
            STUDENT PERFORMANCE ANALYZER
          </p>

          <h1>
            Academic performance,
            <br />
            <span>made measurable.</span>
          </h1>

          <p className="welcome-description">
            Analyze student performance, understand learning patterns,
            and turn academic data into actionable insights.
          </p>
        </div>

        <div className="welcome-badge">
          <GraduationCap size={20} />
          <span>Academic Intelligence</span>
        </div>
      </div>

      {/* Statistics */}
      <div className="stats-grid">
        <StatCard
          title="Total Students"
          value="10"
          description="Students in dataset"
          icon={Users}
          trend="+2"
          trendLabel="new this term"
        />

        <StatCard
          title="Class Average"
          value="78.4%"
          description="Overall academic average"
          icon={Target}
          trend="+4.2%"
          trendLabel="from previous term"
        />

        <StatCard
          title="Top Performer"
          value="92.6%"
          description="Highest student percentage"
          icon={Trophy}
          trend="+3.1%"
          trendLabel="performance growth"
        />

        <StatCard
          title="Pass Rate"
          value="90%"
          description="Students meeting pass criteria"
          icon={GraduationCap}
          trend="+5%"
          trendLabel="from previous assessment"
        />
      </div>

      {/* Main Analytics */}
      <div className="analytics-grid">

        <div className="analytics-panel large-panel">
          <SectionHeader
            eyebrow="PERFORMANCE OVERVIEW"
            title="Class performance"
            action="View analytics"
          />

          <PerformanceChart />
        </div>

        <div className="analytics-panel">
          <SectionHeader
            eyebrow="GRADE DISTRIBUTION"
            title="Academic grades"
          />

          <GradeDistribution />
        </div>

      </div>

      {/* Subject + Ranking */}
      <div className="analytics-grid">

        <div className="analytics-panel">
          <SectionHeader
            eyebrow="SUBJECT ANALYSIS"
            title="Subject performance"
          />

          <SubjectPerformance />
        </div>

        <div className="analytics-panel">
          <SectionHeader
            eyebrow="TOP PERFORMERS"
            title="Student rankings"
            action="View all"
          />

          <RankingTable />
        </div>

      </div>

      {/* Insights */}
      <div className="section-heading-row">
        <div>
          <p className="section-eyebrow">LEARNING INTELLIGENCE</p>
          <h2>Actionable insights</h2>
        </div>

        <button className="text-action">
          Explore insights
          <ArrowUpRight size={16} />
        </button>
      </div>

      <div className="insights-grid">

        <InsightCard
          icon={TrendingUp}
          title="Performance improving"
          description="Most students are showing positive academic progress compared with their previous assessment."
          type="positive"
        />

        <InsightCard
          icon={Target}
          title="Focus needed"
          description="Students with lower subject scores may benefit from additional practice and targeted study plans."
          type="attention"
        />

        <InsightCard
          icon={GraduationCap}
          title="Learning opportunity"
          description="Study-hour patterns can help identify students who may benefit from improved study strategies."
          type="info"
        />

      </div>

    </section>
  );
}

export default Dashboard;
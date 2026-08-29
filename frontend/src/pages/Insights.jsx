import {
  TrendingUp,
  Target,
  GraduationCap,
  Lightbulb,
} from "lucide-react";

import InsightCard from "../components/InsightCard";
import SectionHeader from "../components/SectionHeader";

function Insights() {
  return (
    <section className="dashboard-content">
      <SectionHeader
        eyebrow="LEARNING INTELLIGENCE"
        title="Learning insights"
        action="Refresh insights"
      />

      <div className="page-intro">
        <p>
          Understand academic patterns and identify opportunities
          for targeted improvement.
        </p>
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

        <InsightCard
          icon={Lightbulb}
          title="Personalized recommendation"
          description="Combining subject performance and study habits can help create more focused learning recommendations."
          type="positive"
        />
      </div>
    </section>
  );
}

export default Insights;
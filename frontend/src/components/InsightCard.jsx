import { ArrowUpRight } from "lucide-react";

function InsightCard({
  icon: Icon,
  title,
  description,
  type = "info",
}) {
  return (
    <article className={`insight-card insight-${type}`}>
      <div className="insight-card-top">
        <div className="insight-icon">
          {Icon && <Icon size={20} strokeWidth={2} />}
        </div>

        <ArrowUpRight size={18} />
      </div>

      <div className="insight-card-content">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </article>
  );
}

export default InsightCard;
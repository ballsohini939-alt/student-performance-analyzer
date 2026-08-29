import { ArrowUpRight, ArrowDownRight } from "lucide-react";

function StatCard({
  title,
  value,
  description,
  icon: Icon,
  trend,
  trendLabel,
  positive = true,
}) {
  return (
    <article className="stat-card">
      <div className="stat-card-top">
        <div className="stat-card-icon">
          <Icon size={21} strokeWidth={2} />
        </div>

        {trend && (
          <div
            className={`stat-trend ${
              positive ? "stat-trend-positive" : "stat-trend-negative"
            }`}
          >
            {positive ? (
              <ArrowUpRight size={15} />
            ) : (
              <ArrowDownRight size={15} />
            )}
            {trend}
          </div>
        )}
      </div>

      <div className="stat-card-content">
        <p>{title}</p>
        <h3>{value}</h3>
        <span>{trendLabel || description}</span>
      </div>
    </article>
  );
}

export default StatCard;
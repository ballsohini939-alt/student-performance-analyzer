import {
  LayoutDashboard,
  UserRound,
  Trophy,
  ChartColumn,
  BookOpen,
  Clock3,
  TrendingUp,
  Lightbulb,
} from "lucide-react";

const navigationItems = [
  {
    label: "Overview",
    icon: LayoutDashboard,
  },
  {
    label: "Student Profile",
    icon: UserRound,
  },
  {
    label: "Rankings",
    icon: Trophy,
  },
  {
    label: "Performance",
    icon: ChartColumn,
  },
  {
    label: "Subjects",
    icon: BookOpen,
  },
  {
    label: "Study Hours",
    icon: Clock3,
  },
  {
    label: "Performance Trend",
    icon: TrendingUp,
  },
  {
    label: "Learning Insights",
    icon: Lightbulb,
  },
];

function Sidebar({ activePage, onPageChange }) {
  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <div className="brand-icon">
          <ChartColumn size={22} strokeWidth={2.4} />
        </div>

        <div>
          <h1>Student Analytics</h1>
          <span>Performance Intelligence</span>
        </div>
      </div>

      <nav className="sidebar-navigation">
        <p className="navigation-title">ANALYTICS</p>

        {navigationItems.map((item) => {
          const Icon = item.icon;
          const isActive = activePage === item.label;

          return (
            <button
              key={item.label}
              className={`navigation-item ${
                isActive ? "navigation-item-active" : ""
              }`}
              onClick={() => onPageChange(item.label)}
            >
              <Icon size={19} strokeWidth={2} />
              <span>{item.label}</span>
            </button>
          );
        })}
      </nav>

      <div className="sidebar-footer">
        <div className="footer-status">
          <span className="status-dot" />
          <span>Analytics system ready</span>
        </div>

        <p>Student Performance Analyzer</p>
      </div>
    </aside>
  );
}

export default Sidebar;
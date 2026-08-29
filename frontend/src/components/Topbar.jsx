import {
  Search,
  Bell,
  ChevronDown,
  CalendarDays,
} from "lucide-react";

function Topbar({ activePage }) {
  return (
    <header className="topbar">
      <div className="topbar-left">
        <div>
          <p className="topbar-eyebrow">ACADEMIC ANALYTICS</p>
          <h2>{activePage}</h2>
        </div>
      </div>

      <div className="topbar-actions">
        <div className="topbar-search">
          <Search size={18} />
          <input
            type="text"
            placeholder="Search students..."
            aria-label="Search students"
          />
        </div>

        <button className="topbar-icon-button" aria-label="Academic calendar">
          <CalendarDays size={19} />
        </button>

        <button
          className="topbar-icon-button notification-button"
          aria-label="Notifications"
        >
          <Bell size={19} />
          <span className="notification-dot" />
        </button>

        <div className="profile-menu">
          <div className="profile-avatar">SB</div>

          <div className="profile-info">
            <strong>Sohini Ball</strong>
            <span>Administrator</span>
          </div>

          <ChevronDown size={16} />
        </div>
      </div>
    </header>
  );
}

export default Topbar;
import { useState } from "react";

import Sidebar from "./components/Sidebar";
import Topbar from "./components/Topbar";

import Dashboard from "./pages/Dashboard";
import StudentProfile from "./pages/StudentProfile";
import Rankings from "./pages/Rankings";
import Performance from "./pages/Performance";
import Subjects from "./pages/Subjects";
import StudyHours from "./pages/StudyHours";
import PerformanceTrends from "./pages/PerformanceTrends";
import Insights from "./pages/Insights";

function App() {
  const [activePage, setActivePage] = useState("Overview");

  const renderPage = () => {
    switch (activePage) {
      case "Overview":
        return <Dashboard />;

      case "Student Profile":
        return <StudentProfile />;

      case "Rankings":
        return <Rankings />;

      case "Performance":
        return <Performance />;

      case "Subjects":
        return <Subjects />;

      case "Study Hours":
        return <StudyHours />;

      case "Performance Trend":
        return <PerformanceTrends />;

      case "Learning Insights":
        return <Insights />;

      default:
        return <Dashboard />;
    }
  };

  return (
    <div className="app-shell">
      <Sidebar
        activePage={activePage}
        onPageChange={setActivePage}
      />

      <main className="main-content">
        <Topbar activePage={activePage} />

        {renderPage()}
      </main>
    </div>
  );
}

export default App;
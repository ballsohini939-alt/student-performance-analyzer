const students = [
  {
    rank: 1,
    name: "Aarav Sharma",
    percentage: "92.6%",
    grade: "A",
  },
  {
    rank: 2,
    name: "Priya Das",
    percentage: "89.4%",
    grade: "A",
  },
  {
    rank: 3,
    name: "Rahul Singh",
    percentage: "86.8%",
    grade: "B",
  },
  {
    rank: 4,
    name: "Ananya Roy",
    percentage: "84.2%",
    grade: "B",
  },
  {
    rank: 5,
    name: "Soham Ghosh",
    percentage: "81.7%",
    grade: "B",
  },
];

function RankingTable() {
  return (
    <div className="ranking-table">
      <div className="ranking-header">
        <span>Student</span>
        <span>Score</span>
        <span>Grade</span>
      </div>

      {students.map((student) => (
        <div className="ranking-row" key={student.rank}>
          <div className="ranking-student">
            <span className="ranking-number">
              {student.rank}
            </span>

            <span>{student.name}</span>
          </div>

          <strong>{student.percentage}</strong>

          <span className="ranking-grade">
            {student.grade}
          </span>
        </div>
      ))}
    </div>
  );
}

export default RankingTable;

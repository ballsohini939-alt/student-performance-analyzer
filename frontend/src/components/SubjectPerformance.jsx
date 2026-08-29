const subjects = [
  { name: "Mathematics", score: 84 },
  { name: "Computer Science", score: 88 },
  { name: "Data Science", score: 79 },
  { name: "Operating Systems", score: 74 },
  { name: "Database Systems", score: 81 },
];

function SubjectPerformance() {
  return (
    <div className="subject-performance">
      {subjects.map((subject) => (
        <div className="subject-row" key={subject.name}>
          <div className="subject-info">
            <span>{subject.name}</span>
            <strong>{subject.score}%</strong>
          </div>

          <div className="subject-progress">
            <div
              className="subject-progress-fill"
              style={{ width: `${subject.score}%` }}
            />
          </div>
        </div>
      ))}
    </div>
  );
}

export default SubjectPerformance;

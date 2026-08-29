import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip } from "recharts";

const data = [
  { name: "A", value: 3 },
  { name: "B", value: 3 },
  { name: "C", value: 2 },
  { name: "D", value: 1 },
  { name: "F", value: 1 },
];

function GradeDistribution() {
  return (
    <div className="grade-distribution">
      <div className="grade-chart">
        <ResponsiveContainer width="100%" height={230}>
          <PieChart>
            <Pie
              data={data}
              dataKey="value"
              nameKey="name"
              cx="50%"
              cy="50%"
              innerRadius={58}
              outerRadius={82}
              paddingAngle={3}
            >
              {data.map((entry, index) => (
                <Cell key={`cell-${index}`} />
              ))}
            </Pie>

            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      </div>

      <div className="grade-legend">
        {data.map((item) => (
          <div className="grade-legend-item" key={item.name}>
            <span className="grade-label">
              Grade {item.name}
            </span>

            <strong>{item.value}</strong>
          </div>
        ))}
      </div>
    </div>
  );
}

export default GradeDistribution;
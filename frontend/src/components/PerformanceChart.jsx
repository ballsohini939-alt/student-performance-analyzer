import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const data = [
  { month: "Jan", performance: 72 },
  { month: "Feb", performance: 75 },
  { month: "Mar", performance: 73 },
  { month: "Apr", performance: 78 },
  { month: "May", performance: 81 },
  { month: "Jun", performance: 84 },
];

function PerformanceChart() {
  return (
    <div className="performance-chart">
      <ResponsiveContainer width="100%" height={300}>
        <LineChart
          data={data}
          margin={{
            top: 10,
            right: 10,
            left: 0,
            bottom: 0,
          }}
        >
          <CartesianGrid
            strokeDasharray="3 3"
            vertical={false}
          />

          <XAxis
            dataKey="month"
            axisLine={false}
            tickLine={false}
          />

          <YAxis
            domain={[0, 100]}
            axisLine={false}
            tickLine={false}
          />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="performance"
            strokeWidth={3}
            dot={{ r: 4 }}
            activeDot={{ r: 6 }}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default PerformanceChart;
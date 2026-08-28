# Student Performance Analyzer

A Python-based academic analytics application that analyzes student performance, subject-wise marks, study habits, learning patterns, and academic progress.

The project started as a Python learning project and has evolved into a feature-rich data analysis application using CSV, Pandas, Matplotlib, and ReportLab.

---

## Features

### Student Management

* Add student records
* Update existing student records
* Store subject-wise marks
* Calculate total marks and percentage
* Automatically calculate grades
* View all students
* Search for individual students

### Student Profile

* Detailed academic profile
* Performance category
* Strongest subject
* Weakest subject
* Study-hour analysis
* Personalized learning recommendations
* Learning insights

### Student Comparison

* Compare two students
* Compare total marks and percentage
* Compare grades and performance categories
* Subject-wise comparison
* Identify subject winners
* Analyze performance gaps
* Compare learning habits when data is available

### Class Performance Dashboard

* Total students
* Class average
* Highest and lowest percentage
* Top performers
* Student needing most attention
* Pass rate
* Grade distribution
* Performance categories
* Subject performance
* Learning-habit statistics
* Class-level insights
* Academic recommendations

### Performance Trend Analysis

* Compare current and previous performance
* Track percentage changes
* Track grade changes
* View performance history
* Identify improving, declining, or stable performance

### Advanced Analytics

* Dataset summary
* Class average
* Top-performing student
* Lowest-performing student
* Grade statistics
* Performance categories
* Subject averages
* Study-hour statistics
* Study hours vs performance
* Personalized learning recommendations

### Pandas Data Analysis

* Statistical summary
* Mean and median performance
* Student ranking
* Grade distribution
* Performance categories
* Subject statistics
* Study-hour statistics
* Study hours vs performance analysis
* Correlation analysis

### Data Visualizations

The project generates five analytical charts:

1. Student Performance
2. Subject Performance
3. Grade Distribution
4. Performance Categories
5. Study Hours vs Performance

Charts are automatically saved as PNG files inside the `charts/` directory.

### Report Generation

* Generate individual student text reports
* Generate professional PDF student reports
* Store generated reports inside the `reports/` directory

---

## Technologies Used

* Python
* CSV for data storage
* Pandas for data analysis
* Matplotlib for data visualization
* ReportLab for PDF report generation
* Git for version control
* GitHub for project hosting



## Project Structure


student-performance-analyzer/
|
|-- main.py
|-- student.py
|-- analyzer.py
|-- analytics.py
|-- data_analysis.py
|-- visualizations.py
|-- student_profile.py
|-- performance_comparison.py
|-- performance_trend.py
|-- class_dashboard.py
|-- report_generator.py
|-- pdf_report_generator.py
|-- utils.py
|
|-- data/
|   |-- students.csv
|   |-- subject_marks.csv
|   |-- study_hours.csv
|   `-- performance_history.csv
|
|-- charts/
|   `-- Generated visualization charts
|
|-- reports/
|   `-- Generated student reports
|
|-- requirements.txt
|-- .gitignore
`-- README.md


---

## How to Run

### 1. Clone the repository


git clone https://github.com/ballsohini939-alt/student-performance-analyzer.git


### 2. Open the project directory


cd student-performance-analyzer


### 3. Install dependencies


pip install -r requirements.txt


### 4. Run the application


python main.py


---

## Example Capabilities

The application provides:

* Individual student profiles
* Academic performance comparisons
* Class-level performance dashboards
* Performance trend analysis
* Statistical analysis using Pandas
* Correlation analysis between study hours and performance
* Automated visualization generation
* Personalized learning recommendations
* Text-based student reports
* Professional PDF student reports

---

## Project Status

**Completed Core Analytics Version**

The project currently includes:

* Student management
* Academic analytics
* Data visualization
* Performance tracking
* Student comparison
* Class dashboard
* Pandas analysis
* Automated text reports
* Professional PDF reports

### Future Improvements

* SQLite database integration
* Interactive Streamlit dashboard
* Automated testing
* More advanced predictive analytics
* Machine-learning-based performance prediction

---

## Author

**Sohini Ball**

B.Tech CSE Student | Aspiring Software Engineer

This project is part of my journey of learning Python, data analysis, and practical software development.

---

## License

This project is created for educational and portfolio purposes.

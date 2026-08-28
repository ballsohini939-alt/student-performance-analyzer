import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from report_generator import get_student_data


REPORTS_FOLDER = "reports"


def generate_student_pdf_report(name):
    """Generate a professional PDF report for a student."""

    data = get_student_data(name)

    if data is None:
        return None

    os.makedirs(REPORTS_FOLDER, exist_ok=True)

    safe_name = "".join(
        character
        if character.isalnum() or character in "_-"
        else "_"
        for character in data["name"]
    )

    pdf_path = os.path.join(
        REPORTS_FOLDER,
        f"{safe_name}_report.pdf"
    )

    document = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=20,
        spaceAfter=8
    )

    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontSize=10,
        spaceAfter=15
    )

    heading_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontSize=13,
        spaceBefore=10,
        spaceAfter=7
    )

    normal_style = ParagraphStyle(
        "ReportNormal",
        parent=styles["Normal"],
        fontSize=10,
        leading=14
    )

    story = []

    # ---------------------------------------------------------
    # TITLE
    # ---------------------------------------------------------

    story.append(
        Paragraph(
            "STUDENT PERFORMANCE REPORT",
            title_style
        )
    )

    story.append(
        Paragraph(
            "Student Performance Analyzer",
            subtitle_style
        )
    )

    # ---------------------------------------------------------
    # STUDENT INFORMATION
    # ---------------------------------------------------------

    story.append(
        Paragraph(
            "Student Information",
            heading_style
        )
    )

    student_data = [
        ["Name", data["name"]],
        ["Total Marks", f"{data['total']:.2f}"],
        ["Percentage", f"{data['percentage']:.2f}%"],
        ["Grade", data["grade"]]
    ]

    student_table = Table(
        student_data,
        colWidths=[55 * mm, 110 * mm]
    )

    student_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
                ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
                ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7)
            ]
        )
    )

    story.append(student_table)
    story.append(Spacer(1, 10))

    # ---------------------------------------------------------
    # SUBJECT PERFORMANCE
    # ---------------------------------------------------------

    story.append(
        Paragraph(
            "Subject Performance",
            heading_style
        )
    )

    if data["subjects"]:

        subject_table_data = [
            ["Subject", "Marks"]
        ]

        for subject in data["subjects"]:
            subject_table_data.append(
                [
                    subject["subject"],
                    f"{subject['marks']:.2f}"
                ]
            )

        marks = [
            subject["marks"]
            for subject in data["subjects"]
        ]

        strongest_index = marks.index(max(marks))
        weakest_index = marks.index(min(marks))

        subject_table = Table(
            subject_table_data,
            colWidths=[110 * mm, 55 * mm]
        )

        subject_table.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, -1), 10),
                    ("ALIGN", (1, 1), (1, -1), "CENTER"),
                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6)
                ]
            )
        )

        story.append(subject_table)
        story.append(Spacer(1, 7))

        strongest_subject = data["subjects"][strongest_index]
        weakest_subject = data["subjects"][weakest_index]

        story.append(
            Paragraph(
                f"<b>Strongest Subject:</b> "
                f"{strongest_subject['subject']} "
                f"({strongest_subject['marks']:.2f}%)",
                normal_style
            )
        )

        story.append(
            Paragraph(
                f"<b>Weakest Subject:</b> "
                f"{weakest_subject['subject']} "
                f"({weakest_subject['marks']:.2f}%)",
                normal_style
            )
        )

    else:

        story.append(
            Paragraph(
                "No subject-wise data available.",
                normal_style
            )
        )

    # ---------------------------------------------------------
    # LEARNING HABITS
    # ---------------------------------------------------------

    story.append(
        Paragraph(
            "Learning Habits",
            heading_style
        )
    )

    if data["study_hours"] is not None:

        study_hours = data["study_hours"]

        if study_hours >= 8:
            study_assessment = (
                "Excellent study commitment."
            )
        elif study_hours >= 5:
            study_assessment = (
                "Good study routine. Maintain consistency."
            )
        elif study_hours >= 3:
            study_assessment = (
                "Moderate study time. Consider increasing "
                "regular study practice."
            )
        else:
            study_assessment = (
                "Low study time. A more consistent study "
                "schedule is recommended."
            )

        story.append(
            Paragraph(
                f"<b>Average Study Hours:</b> "
                f"{study_hours:.2f} hours/day",
                normal_style
            )
        )

        story.append(
            Paragraph(
                f"<b>Assessment:</b> "
                f"{study_assessment}",
                normal_style
            )
        )

    else:

        story.append(
            Paragraph(
                "Study hours data not available.",
                normal_style
            )
        )

    # ---------------------------------------------------------
    # PERFORMANCE CATEGORY
    # ---------------------------------------------------------

    story.append(
        Paragraph(
            "Performance Assessment",
            heading_style
        )
    )

    percentage = data["percentage"]

    if percentage >= 90:
        category = "Excellent"
    elif percentage >= 70:
        category = "Good"
    elif percentage >= 50:
        category = "Average"
    else:
        category = "Needs Attention"

    story.append(
        Paragraph(
            f"<b>Performance Category:</b> {category}",
            normal_style
        )
    )

    # ---------------------------------------------------------
    # PERSONALIZED RECOMMENDATION
    # ---------------------------------------------------------

    story.append(
        Paragraph(
            "Personalized Recommendation",
            heading_style
        )
    )

    story.append(
        Paragraph(
            data["recommendation"],
            normal_style
        )
    )

    # ---------------------------------------------------------
    # FOOTER
    # ---------------------------------------------------------

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Generated by Student Performance Analyzer",
            subtitle_style
        )
    )

    document.build(story)

    return pdf_path
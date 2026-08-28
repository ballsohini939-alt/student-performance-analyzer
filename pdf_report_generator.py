
import os
from datetime import datetime

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
    TableStyle,
    PageBreak
)

from report_generator import get_student_data


REPORTS_FOLDER = "reports"


def generate_student_pdf_report(name):
    """
    Generate a professional PDF report for a student.
    """

    data = get_student_data(name)

    if data is None:
        return None

    os.makedirs(REPORTS_FOLDER, exist_ok=True)

    # ---------------------------------------------------------
    # SAFE FILE NAME
    # ---------------------------------------------------------

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

    # ---------------------------------------------------------
    # PDF DOCUMENT
    # ---------------------------------------------------------

    document = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm
    )

    # ---------------------------------------------------------
    # STYLES
    # ---------------------------------------------------------

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=20,
        leading=24,
        spaceAfter=6,
        textColor=colors.HexColor("#1F2937")
    )

    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontSize=10,
        leading=13,
        spaceAfter=12,
        textColor=colors.HexColor("#6B7280")
    )

    heading_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontSize=13,
        leading=16,
        spaceBefore=10,
        spaceAfter=7,
        textColor=colors.HexColor("#111827")
    )

    normal_style = ParagraphStyle(
        "ReportNormal",
        parent=styles["Normal"],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#374151")
    )

    small_style = ParagraphStyle(
        "SmallText",
        parent=styles["Normal"],
        fontSize=8,
        leading=10,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#6B7280")
    )

    # ---------------------------------------------------------
    # STORY
    # ---------------------------------------------------------

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

    story.append(
        Paragraph(
            f"Report Generated: "
            f"{datetime.now().strftime('%d %B %Y, %I:%M %p')}",
            small_style
        )
    )

    story.append(Spacer(1, 10))

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
        ["Student Name", data["name"]],
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
                (
                    "BACKGROUND",
                    (0, 0),
                    (0, -1),
                    colors.HexColor("#E5E7EB")
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (0, -1),
                    "Helvetica-Bold"
                ),
                ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8)
            ]
        )
    )

    story.append(student_table)

    story.append(Spacer(1, 12))

    # ---------------------------------------------------------
    # PERFORMANCE SUMMARY
    # ---------------------------------------------------------

    story.append(
        Paragraph(
            "Performance Summary",
            heading_style
        )
    )

    percentage = data["percentage"]

    if percentage >= 90:
        category = "Excellent"
        assessment = (
            "Outstanding academic performance. "
            "Continue maintaining this level."
        )

    elif percentage >= 70:
        category = "Good"
        assessment = (
            "Good academic performance. "
            "Continue regular practice to improve further."
        )

    elif percentage >= 50:
        category = "Average"
        assessment = (
            "Average performance. "
            "Focus on weaker areas and increase practice."
        )

    else:
        category = "Needs Attention"
        assessment = (
            "Performance needs improvement. "
            "A structured study plan is recommended."
        )

    summary_data = [
        ["Performance Category", category],
        ["Overall Assessment", assessment]
    ]

    summary_table = Table(
        summary_data,
        colWidths=[55 * mm, 110 * mm]
    )

    summary_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                (
                    "BACKGROUND",
                    (0, 0),
                    (0, -1),
                    colors.HexColor("#E5E7EB")
                ),
                ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
                ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8)
            ]
        )
    )

    story.append(summary_table)

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
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor("#E5E7EB")
                    ),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, -1), 10),
                    ("ALIGN", (1, 1), (1, -1), "CENTER"),
                    ("TOPPADDING", (0, 0), (-1, -1), 7),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 7)
                ]
            )
        )

        story.append(subject_table)

        story.append(Spacer(1, 8))

        strongest_subject = data["subjects"][strongest_index]
        weakest_subject = data["subjects"][weakest_index]

        insight_data = [
            [
                "Strongest Subject",
                f"{strongest_subject['subject']} "
                f"({strongest_subject['marks']:.2f}%)"
            ],
            [
                "Weakest Subject",
                f"{weakest_subject['subject']} "
                f"({weakest_subject['marks']:.2f}%)"
            ]
        ]

        insight_table = Table(
            insight_data,
            colWidths=[55 * mm, 110 * mm]
        )

        insight_table.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    (
                        "BACKGROUND",
                        (0, 0),
                        (0, -1),
                        colors.HexColor("#F3F4F6")
                    ),
                    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, -1), 10),
                    ("LEFTPADDING", (0, 0), (-1, -1), 8),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 7),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 7)
                ]
            )
        )

        story.append(insight_table)

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
                "Good study routine. "
                "Maintain consistency."
            )

        elif study_hours >= 3:

            study_assessment = (
                "Moderate study time. "
                "Consider increasing regular study practice."
            )

        else:

            study_assessment = (
                "Low study time. "
                "A more consistent study schedule is recommended."
            )

        learning_data = [
            [
                "Average Study Hours",
                f"{study_hours:.2f} hours/day"
            ],
            [
                "Assessment",
                study_assessment
            ]
        ]

        learning_table = Table(
            learning_data,
            colWidths=[55 * mm, 110 * mm]
        )

        learning_table.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    (
                        "BACKGROUND",
                        (0, 0),
                        (0, -1),
                        colors.HexColor("#F3F4F6")
                    ),
                    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, -1), 10),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 8),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 7),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 7)
                ]
            )
        )

        story.append(learning_table)

    else:

        story.append(
            Paragraph(
                "Study hours data not available.",
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

    recommendation_table = Table(
        [
            [
                Paragraph(
                    data["recommendation"],
                    normal_style
                )
            ]
        ],
        colWidths=[165 * mm]
    )

    recommendation_table.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.7, colors.grey),
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    colors.HexColor("#F9FAFB")
                ),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10)
            ]
        )
    )

    story.append(recommendation_table)

    # ---------------------------------------------------------
    # FOOTER
    # ---------------------------------------------------------

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Generated by Student Performance Analyzer",
            small_style
        )
    )

    story.append(
        Paragraph(
            "Academic Performance & Learning Analytics System",
            small_style
        )
    )

    # ---------------------------------------------------------
    # BUILD PDF
    # ---------------------------------------------------------

    document.build(story)

    return pdf_path


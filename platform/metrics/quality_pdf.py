"""Quality report PDF generation — POC using reportlab."""

from __future__ import annotations

import io
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


def _score_color(score: float) -> colors.Color:
    if score >= 80:
        return colors.HexColor("#16a34a")
    if score >= 60:
        return colors.HexColor("#3b82f6")
    if score >= 40:
        return colors.HexColor("#ea580c")
    return colors.HexColor("#dc2626")


def render_quality_pdf(snapshot: dict) -> bytes:
    """Render a quality snapshot dict as a PDF byte stream."""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Heading1"],
        fontSize=18,
        spaceAfter=6,
        textColor=colors.HexColor("#4c1d95"),
    )
    subtitle_style = ParagraphStyle(
        "ReportSubtitle",
        parent=styles["Normal"],
        fontSize=10,
        textColor=colors.grey,
        spaceAfter=12,
    )

    global_score = float(snapshot.get("global_score") or 0)
    breakdown = snapshot.get("breakdown") or {}
    dimensions = breakdown.get("dimensions") or {}
    timestamp = snapshot.get("timestamp") or datetime.utcnow().isoformat()

    story = [
        Paragraph("Quality Report", title_style),
        Paragraph(f"Generated: {timestamp}", subtitle_style),
        Paragraph(
            f'<font size="14"><b>Global Score: {global_score:.1f}/100</b></font>',
            styles["Normal"],
        ),
        Spacer(1, 12),
        Paragraph("Dimension Breakdown", styles["Heading2"]),
        Spacer(1, 6),
    ]

    table_data = [["Dimension", "Score", "Tool"]]
    for dim_name, dim_val in sorted(dimensions.items()):
        if isinstance(dim_val, dict):
            score = float(dim_val.get("score") or 0)
            tool = dim_val.get("tool") or "-"
        else:
            score = float(dim_val or 0)
            tool = "-"
        label = dim_name.replace("_", " ").title()
        table_data.append([label, f"{score:.1f}", tool])

    if len(table_data) == 1:
        table_data.append(["No dimensions scanned", "-", "-"])

    table = Table(table_data, colWidths=[90 * mm, 30 * mm, 50 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#4c1d95")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.lightgrey),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f5f3ff")]),
                ("ALIGN", (1, 1), (1, -1), "CENTER"),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 12))
    story.append(
        Paragraph(
            f'<font color="#{_score_color(global_score).hexval()[2:]}">'
            f"Status: {'Pass' if global_score >= 60 else 'Needs attention'}</font>",
            styles["Normal"],
        )
    )

    doc.build(story)
    return buffer.getvalue()

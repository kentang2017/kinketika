"""
wheel_chart.py
==============
Generate Plotly-based wheel (polar-bar) diagrams for Ketika Lima
and Bintang Tujuh period visualisation.
"""

from typing import List
import plotly.graph_objects as go
from ketika_data import KetikaPeriod, _time_to_minutes, FORTUNE_LABELS


def _period_span_degrees(p: KetikaPeriod) -> tuple:
    """Return (start_deg, span_deg) mapping 24 h onto 360°."""
    start_min = _time_to_minutes(p.time_start)
    end_min   = _time_to_minutes(p.time_end)
    if end_min <= start_min:          # wraps midnight
        span_min = (1440 - start_min) + end_min
    else:
        span_min = end_min - start_min
    start_deg = (start_min / 1440) * 360
    span_deg  = (span_min / 1440)  * 360
    return start_deg, span_deg


def make_wheel(
    periods: List[KetikaPeriod],
    lang: str = "en",
    current_index: int | None = None,
    title: str = "",
) -> go.Figure:
    """
    Create a polar-bar wheel chart.

    Parameters
    ----------
    periods : list of KetikaPeriod
    lang : 'en' | 'zh'
    current_index : highlight this period index (1-based)
    title : chart title
    """
    fig = go.Figure()

    for p in periods:
        start_deg, span_deg = _period_span_degrees(p)
        # centre angle for the bar
        theta_centre = start_deg + span_deg / 2

        name_display = p.name_zh if lang == "zh" else p.name_en
        fortune_lbl  = FORTUNE_LABELS[p.fortune][lang]

        opacity = 1.0 if (current_index is None or p.index == current_index) else 0.45

        fig.add_trace(go.Barpolar(
            r=[1],
            theta=[theta_centre],
            width=[span_deg],
            marker_color=p.colour,
            marker_line_color="#FFFFFF",
            marker_line_width=2,
            opacity=opacity,
            name=name_display,
            text=f"{p.emoji} {name_display}<br>{fortune_lbl}<br>{p.time_start}–{p.time_end}",
            hoverinfo="text",
        ))

    fig.update_layout(
        title=dict(text=title, font=dict(size=18, color="#3E2723")),
        polar=dict(
            angularaxis=dict(
                direction="clockwise",
                rotation=90,
                tickmode="array",
                tickvals=[0, 90, 180, 270],
                ticktext=["00:00", "06:00", "12:00", "18:00"],
                linecolor="#BFA97A",
                gridcolor="#E8DCC8",
            ),
            radialaxis=dict(visible=False),
            bgcolor="rgba(255,248,230,0.6)",
        ),
        showlegend=True,
        legend=dict(
            font=dict(size=11),
            bgcolor="rgba(255,248,230,0.85)",
            bordercolor="#BFA97A",
            borderwidth=1,
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=60, b=20, l=20, r=20),
        height=520,
    )
    return fig

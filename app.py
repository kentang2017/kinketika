"""
app.py — Kinketika（堅克提卡）: Malay Time Divination
=====================================================
A culturally respectful, bilingual (English / 繁體中文) Streamlit
application that implements two classical Malay Archipelago
time-divination systems:

  1. Ketika Lima  (Five-period)
  2. Bintang Tujuh  (Seven-star / seven-period)

Run:  streamlit run app.py
"""

import datetime
import streamlit as st

from ketika_data import (
    KETIKA_LIMA,
    BINTANG_TUJUH,
    FORTUNE_LABELS,
    ACTIVITY_CATALOGUE,
    KetikaPeriod,
    get_current_period,
    get_periods_for_activity,
    daily_summary,
)
from wheel_chart import make_wheel

# ------------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------------
st.set_page_config(
    page_title="Kinketika — Malay Time Divination",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------------
# Custom CSS for traditional Malay manuscript aesthetics
# ------------------------------------------------------------------
st.markdown("""
<style>
/* Import a serif / manuscript-style font */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Noto+Serif+TC:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Playfair Display', 'Noto Serif TC', serif;
}

/* Header banner */
.main-banner {
    background: linear-gradient(135deg, #3E2723 0%, #5D4037 50%, #3E2723 100%);
    color: #D4AF37;
    padding: 1.5rem 2rem;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 1.2rem;
    border: 2px solid #D4AF37;
    box-shadow: 0 4px 20px rgba(0,0,0,0.25);
}
.main-banner h1 { margin: 0; font-size: 2rem; letter-spacing: 2px; }
.main-banner p  { margin: 0.3rem 0 0; font-size: 0.95rem; color: #EFEBE9; }

/* Period card */
.period-card {
    border: 2px solid #D4AF37;
    border-radius: 12px;
    padding: 1.4rem;
    margin: 0.6rem 0;
    box-shadow: 0 2px 12px rgba(0,0,0,0.10);
}
.period-card h3 { margin-top: 0; }

/* Cultural disclaimer */
.cultural-note {
    background-color: #FFF3E0;
    border-left: 4px solid #D4AF37;
    padding: 0.8rem 1rem;
    border-radius: 0 8px 8px 0;
    font-size: 0.85rem;
    color: #5D4037;
    margin-bottom: 1.2rem;
}

/* Fortune badges */
.badge-baik      { background:#E8F5E9; color:#2E7D32; padding:4px 12px; border-radius:20px; font-weight:700; }
.badge-nahas     { background:#FFEBEE; color:#C62828; padding:4px 12px; border-radius:20px; font-weight:700; }
.badge-sederhana { background:#FFF8E1; color:#F57F17; padding:4px 12px; border-radius:20px; font-weight:700; }

/* Table-like period overview */
.period-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
}
.period-table th {
    background: #5D4037; color: #D4AF37;
    padding: 8px 10px; text-align: left;
}
.period-table td {
    padding: 8px 10px; border-bottom: 1px solid #E8DCC8;
}
.period-table tr:nth-child(even) { background: #FFF8E6; }
.period-table tr:nth-child(odd)  { background: #FFF3E0; }

/* Ornamental dividers */
.ornament {
    text-align: center;
    color: #D4AF37;
    font-size: 1.4rem;
    letter-spacing: 8px;
    margin: 0.6rem 0;
}
</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------------------
# Sidebar — mode, language, time input, activity selection
# ------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🌙 Settings / 設定")

    lang = st.selectbox(
        "Language / 語言",
        ["English", "繁體中文"],
        index=0,
    )
    lang_key = "zh" if lang == "繁體中文" else "en"

    system_label = (
        "占卜系統" if lang_key == "zh" else "Divination System"
    )
    system = st.radio(
        system_label,
        ["Ketika Lima（五時刻）", "Bintang Tujuh（七星時刻）"],
        index=0,
    )

    st.markdown("---")

    time_mode_label = "時間模式" if lang_key == "zh" else "Time Mode"
    time_mode = st.radio(
        time_mode_label,
        [
            "Auto (now)" if lang_key == "en" else "自動（現在）",
            "Custom" if lang_key == "en" else "自訂",
        ],
    )

    if time_mode in ("Custom", "自訂"):
        custom_date = st.date_input(
            "Date / 日期",
            value=datetime.date.today(),
        )
        custom_time = st.time_input(
            "Time / 時間",
            value=datetime.datetime.now().time().replace(second=0, microsecond=0),
        )
        query_dt = datetime.datetime.combine(custom_date, custom_time)
    else:
        query_dt = datetime.datetime.now()

    st.markdown("---")

    activity_label = "活動擇時" if lang_key == "zh" else "Activity Planner"
    st.markdown(f"### 📋 {activity_label}")
    activity_options = {
        k: v[lang_key] for k, v in ACTIVITY_CATALOGUE.items()
    }
    selected_activity = st.selectbox(
        "Choose activity / 選擇活動",
        options=list(activity_options.keys()),
        format_func=lambda k: activity_options[k],
    )

# ------------------------------------------------------------------
# Resolve chosen dataset
# ------------------------------------------------------------------
periods = KETIKA_LIMA if "Lima" in system else BINTANG_TUJUH
system_name_en = "Ketika Lima" if "Lima" in system else "Bintang Tujuh"
system_name_zh = "五時刻占卜" if "Lima" in system else "七星時刻占卜"
current = get_current_period(periods, query_dt.hour, query_dt.minute)

# ------------------------------------------------------------------
# Banner
# ------------------------------------------------------------------
banner_title = (
    "Kinketika（堅克提卡）— 馬來群島傳統時間占卜"
    if lang_key == "zh"
    else "Kinketika — Malay Time Divination"
)
banner_sub = (
    "融合馬來半島、蘇門答臘、爪哇及南蘇拉威西傳統智慧"
    if lang_key == "zh"
    else "Drawing from the traditional wisdom of the Malay Peninsula, Sumatra, Java &amp; South Sulawesi"
)
st.markdown(
    f'<div class="main-banner"><h1>{banner_title}</h1>'
    f'<p>{banner_sub}</p></div>',
    unsafe_allow_html=True,
)

# Cultural disclaimer
if lang_key == "zh":
    disclaimer = (
        "📜 **文化聲明：** 此應用為文化學習與參考工具。傳統占卜需尊重當地 "
        "Bomoh（馬來療癒師）/ Panrita（武吉士智者）的指導。"
        "重要決定請結合理性判斷。"
    )
else:
    disclaimer = (
        '📜 **Cultural Note:** This app is a cultural-learning and reference tool. '
        'Traditional divination should respect the guidance of local '
        'Bomoh / Panrita practitioners. Important decisions should be '
        'combined with rational judgement.'
    )
st.markdown(f'<div class="cultural-note">{disclaimer}</div>', unsafe_allow_html=True)

# ------------------------------------------------------------------
# Ornamental divider
# ------------------------------------------------------------------
st.markdown('<div class="ornament">✦ ✦ ✦ ✦ ✦</div>', unsafe_allow_html=True)

# ------------------------------------------------------------------
# Current Period — hero card
# ------------------------------------------------------------------
hero_title = (
    f"🕰️ 當前時刻 — {system_name_zh}"
    if lang_key == "zh"
    else f"🕰️ Current Period — {system_name_en}"
)
st.subheader(hero_title)

display_time = query_dt.strftime("%Y-%m-%d  %H:%M")
st.caption(
    f"{'查詢時間' if lang_key == 'zh' else 'Query time'}: **{display_time}**"
)

fortune_badge_class = f"badge-{current.fortune}"
fortune_label = FORTUNE_LABELS[current.fortune][lang_key]

col_info, col_wheel = st.columns([1, 1], gap="large")

with col_info:
    name_display = current.name_zh if lang_key == "zh" else current.name_en
    note_display = current.note_zh if lang_key == "zh" else current.note_en

    card_bg = "#FFF8E6" if current.fortune != "nahas" else "#FFF0F0"
    st.markdown(
        f"""
        <div class="period-card" style="background:{card_bg};">
            <h3>{current.emoji} {name_display}</h3>
            <p><strong>{'時段' if lang_key == 'zh' else 'Time'}:</strong> {current.time_start} – {current.time_end}</p>
            <p><strong>{'天體' if lang_key == 'zh' else 'Celestial body'}:</strong> {current.planet_or_star}</p>
            <p><span class="{fortune_badge_class}">{fortune_label}</span></p>
            <hr style="border-color:#E8DCC8;">
            <p style="font-size:0.92rem;">{note_display}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Good / bad activities for current period
    good_label = "✅ 適合活動" if lang_key == "zh" else "✅ Recommended"
    bad_label  = "❌ 不宜活動" if lang_key == "zh" else "❌ Discouraged"
    good_acts = ", ".join(ACTIVITY_CATALOGUE[a][lang_key] for a in current.good_activities)
    bad_acts  = ", ".join(ACTIVITY_CATALOGUE[a][lang_key] for a in current.bad_activities)
    st.markdown(f"**{good_label}:** {good_acts}")
    st.markdown(f"**{bad_label}:** {bad_acts}")

with col_wheel:
    wheel_title = (
        f"{system_name_zh} 時刻輪盤" if lang_key == "zh"
        else f"{system_name_en} Wheel"
    )
    fig = make_wheel(
        periods,
        lang=lang_key,
        current_index=current.index,
        title=wheel_title,
    )
    st.plotly_chart(fig, use_container_width=True)

# ------------------------------------------------------------------
# Ornamental divider
# ------------------------------------------------------------------
st.markdown('<div class="ornament">✦ ✦ ✦ ✦ ✦</div>', unsafe_allow_html=True)

# ------------------------------------------------------------------
# Daily Summary
# ------------------------------------------------------------------
summary_title = "📊 今日整體吉凶" if lang_key == "zh" else "📊 Daily Fortune Summary"
st.subheader(summary_title)
st.markdown(daily_summary(periods, lang_key))

# Metrics row
bcol1, bcol2, bcol3 = st.columns(3)
baik_cnt   = sum(1 for p in periods if p.fortune == "baik")
nahas_cnt  = sum(1 for p in periods if p.fortune == "nahas")
neutral_cnt = sum(1 for p in periods if p.fortune == "sederhana")

bcol1.metric(
    "吉 Auspicious" if lang_key == "zh" else "Auspicious",
    f"{baik_cnt} {'段' if lang_key == 'zh' else 'periods'}",
)
bcol2.metric(
    "凶 Inauspicious" if lang_key == "zh" else "Inauspicious",
    f"{nahas_cnt} {'段' if lang_key == 'zh' else 'periods'}",
)
bcol3.metric(
    "中平 Neutral" if lang_key == "zh" else "Neutral",
    f"{neutral_cnt} {'段' if lang_key == 'zh' else 'periods'}",
)

# ------------------------------------------------------------------
# Full Period Overview Table
# ------------------------------------------------------------------
st.markdown('<div class="ornament">✦ ✦ ✦ ✦ ✦</div>', unsafe_allow_html=True)

table_title = (
    f"📋 {system_name_zh} 完整時段一覽"
    if lang_key == "zh"
    else f"📋 {system_name_en} — All Periods"
)
st.subheader(table_title)

# Build HTML table
th_time  = "時段" if lang_key == "zh" else "Time"
th_name  = "名稱" if lang_key == "zh" else "Name"
th_body  = "天體" if lang_key == "zh" else "Body"
th_fort  = "吉凶" if lang_key == "zh" else "Fortune"
th_good  = "適合" if lang_key == "zh" else "Good for"
th_bad   = "不宜" if lang_key == "zh" else "Avoid"

rows_html = ""
for p in periods:
    pname = p.name_zh if lang_key == "zh" else p.name_en
    fort  = FORTUNE_LABELS[p.fortune][lang_key]
    g_act = ", ".join(ACTIVITY_CATALOGUE[a][lang_key] for a in p.good_activities)
    b_act = ", ".join(ACTIVITY_CATALOGUE[a][lang_key] for a in p.bad_activities)
    highlight = 'style="outline:3px solid #D4AF37; outline-offset:-3px;"' if p.index == current.index else ""
    rows_html += (
        f'<tr {highlight}>'
        f'<td>{p.time_start}–{p.time_end}</td>'
        f'<td>{p.emoji} {pname}</td>'
        f'<td>{p.planet_or_star}</td>'
        f'<td><span class="badge-{p.fortune}">{fort}</span></td>'
        f'<td>{g_act}</td>'
        f'<td>{b_act}</td>'
        f'</tr>'
    )

st.markdown(
    f"""
    <table class="period-table">
        <tr>
            <th>{th_time}</th><th>{th_name}</th><th>{th_body}</th>
            <th>{th_fort}</th><th>{th_good}</th><th>{th_bad}</th>
        </tr>
        {rows_html}
    </table>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------
# Activity Planner
# ------------------------------------------------------------------
st.markdown('<div class="ornament">✦ ✦ ✦ ✦ ✦</div>', unsafe_allow_html=True)

planner_title = (
    f"🗓️ 活動擇時 — {ACTIVITY_CATALOGUE[selected_activity][lang_key]}"
    if lang_key == "zh"
    else f"🗓️ Activity Planner — {ACTIVITY_CATALOGUE[selected_activity][lang_key]}"
)
st.subheader(planner_title)

result = get_periods_for_activity(periods, selected_activity)

if result["good"]:
    rec_label = "推薦時段" if lang_key == "zh" else "Recommended periods"
    st.markdown(f"**✅ {rec_label}:**")
    for p in result["good"]:
        pname = p.name_zh if lang_key == "zh" else p.name_en
        fl    = FORTUNE_LABELS[p.fortune][lang_key]
        st.success(f"{p.emoji} **{pname}** ({p.time_start}–{p.time_end}) — {fl}")
else:
    no_good = "此系統中無特別推薦的時段" if lang_key == "zh" else "No particularly recommended period in this system"
    st.info(no_good)

if result["bad"]:
    avoid_label = "不宜時段" if lang_key == "zh" else "Periods to avoid"
    st.markdown(f"**❌ {avoid_label}:**")
    for p in result["bad"]:
        pname = p.name_zh if lang_key == "zh" else p.name_en
        fl    = FORTUNE_LABELS[p.fortune][lang_key]
        st.error(f"{p.emoji} **{pname}** ({p.time_start}–{p.time_end}) — {fl}")

# ------------------------------------------------------------------
# Expanded detail per period (collapsible)
# ------------------------------------------------------------------
st.markdown('<div class="ornament">✦ ✦ ✦ ✦ ✦</div>', unsafe_allow_html=True)

detail_title = (
    f"📖 各時段詳細說明 — {system_name_zh}"
    if lang_key == "zh"
    else f"📖 Period Details — {system_name_en}"
)
st.subheader(detail_title)

for p in periods:
    pname = p.name_zh if lang_key == "zh" else p.name_en
    fl    = FORTUNE_LABELS[p.fortune][lang_key]
    with st.expander(f"{p.emoji} {pname}  ({p.time_start}–{p.time_end})  —  {fl}"):
        st.markdown(f"**{'天體' if lang_key == 'zh' else 'Celestial body'}:** {p.planet_or_star}")
        st.markdown(f"**{'顏色' if lang_key == 'zh' else 'Colour'}:** <span style='display:inline-block;width:16px;height:16px;background:{p.colour};border-radius:50%;vertical-align:middle;border:1px solid #999;'></span> `{p.colour}`", unsafe_allow_html=True)
        st.markdown("---")
        note = p.note_zh if lang_key == "zh" else p.note_en
        st.markdown(note)
        st.markdown("---")
        g_act = ", ".join(ACTIVITY_CATALOGUE[a][lang_key] for a in p.good_activities)
        b_act = ", ".join(ACTIVITY_CATALOGUE[a][lang_key] for a in p.bad_activities)
        st.markdown(f"✅ **{'適合' if lang_key == 'zh' else 'Good for'}:** {g_act}")
        st.markdown(f"❌ **{'不宜' if lang_key == 'zh' else 'Avoid'}:** {b_act}")

# ------------------------------------------------------------------
# Footer
# ------------------------------------------------------------------
st.markdown('<div class="ornament">✦ ✦ ✦ ✦ ✦</div>', unsafe_allow_html=True)

if lang_key == "zh":
    footer_text = (
        "📜 **文化聲明：** 此應用為文化學習與參考工具，呈現馬來群島（Nusantara）"
        "傳統的 Ketika 時間占卜智慧。傳統占卜需尊重當地 Bomoh（馬來療癒師）"
        "/ Panrita（武吉士智者）的指導。重要決定請結合理性判斷。\n\n"
        "*資料參考自馬來半島、蘇門答臘、爪哇及南蘇拉威西傳統手稿。*"
    )
else:
    footer_text = (
        '📜 **Cultural Disclaimer:** This application is a cultural-learning '
        'and reference tool presenting the traditional Ketika time-divination '
        'wisdom of the Malay Archipelago (Nusantara). Traditional divination '
        'should respect the guidance of local Bomoh / Panrita practitioners. '
        'Important life decisions should always be combined with rational '
        'judgement.\n\n'
        '*Data referenced from traditional manuscripts of the Malay Peninsula, '
        'Sumatra, Java, and South Sulawesi.*'
    )

st.markdown(f'<div class="cultural-note">{footer_text}</div>', unsafe_allow_html=True)
st.caption("© Kinketika（堅克提卡）— Malay Time Divination Tool")

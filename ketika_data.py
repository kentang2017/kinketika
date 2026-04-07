"""
ketika_data.py
==============
Data structures for the Malay Archipelago traditional time-divination systems:
  • Ketika Lima  (五時刻占卜 — Five-period system)
  • Bintang Tujuh / Ketika Tujuh  (七星時刻占卜 — Seven-period system)

Each entry is bilingual (English / 繁體中文) and includes:
  - time range, traditional name, fortune quality, colour,
    recommended / discouraged activities, and a cultural note.

References draw on common Malay manuscript (kitab) traditions from
the Malay Peninsula, Sumatra, Java, and South Sulawesi (Bugis-Makassar).
"""

from dataclasses import dataclass, field
from typing import List, Dict

# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

FORTUNE_LABELS: Dict[str, Dict[str, str]] = {
    "baik":      {"en": "Auspicious ✨",       "zh": "吉 ✨"},
    "nahas":     {"en": "Inauspicious ⚠️",     "zh": "凶 ⚠️"},
    "sederhana": {"en": "Moderate / Neutral 🔸", "zh": "中平 🔸"},
}

ACTIVITY_CATALOGUE: Dict[str, Dict[str, str]] = {
    "sailing":     {"en": "Sailing / Travel",         "zh": "航海／出行"},
    "marriage":    {"en": "Marriage / Engagement",     "zh": "結婚／訂婚"},
    "building":    {"en": "Building / Groundbreaking", "zh": "建屋／動土"},
    "healing":     {"en": "Healing / Medicine",        "zh": "療癒／醫藥"},
    "business":    {"en": "Business / Trade",          "zh": "生意／貿易"},
    "study":       {"en": "Study / Learning",          "zh": "學習／進修"},
    "prayer":      {"en": "Prayer / Spiritual",        "zh": "祈禱／靈修"},
    "agriculture": {"en": "Agriculture / Planting",    "zh": "農耕／種植"},
    "meeting":     {"en": "Meeting / Negotiation",     "zh": "會面／談判"},
    "ceremony":    {"en": "Ceremony / Celebration",    "zh": "慶典／儀式"},
    "war":         {"en": "Warfare / Competition",     "zh": "戰事／競爭"},
    "rest":        {"en": "Rest / Retreat",             "zh": "休息／靜養"},
}


# ---------------------------------------------------------------------------
# Data class
# ---------------------------------------------------------------------------

@dataclass
class KetikaPeriod:
    """One time-division period."""
    index: int
    name_malay: str           # Traditional Malay / Arabic-derived name
    name_en: str
    name_zh: str
    time_start: str           # HH:MM (24 h)
    time_end: str
    fortune: str              # key into FORTUNE_LABELS
    colour: str               # CSS-compatible colour string
    emoji: str
    planet_or_star: str       # Associated celestial body (if any)
    good_activities: List[str] = field(default_factory=list)   # keys
    bad_activities: List[str]  = field(default_factory=list)
    note_en: str = ""
    note_zh: str = ""


# ===================================================================
# KETIKA LIMA  —  五時刻占卜
# ===================================================================
# Traditionally tied to the five Islamic prayer times (Subuh, Zohor,
# Asar, Maghrib, Isyak) and their associated spiritual energies.

KETIKA_LIMA: List[KetikaPeriod] = [
    KetikaPeriod(
        index=1,
        name_malay="Maswara (Subuh)",
        name_en="Dawn — Maswara",
        name_zh="黎明 — 瑪斯瓦拉（晨禮）",
        time_start="05:00",
        time_end="08:00",
        fortune="baik",
        colour="#D4AF37",       # gold
        emoji="🌅",
        planet_or_star="Zuhrah (Venus)",
        good_activities=["prayer", "healing", "study", "agriculture"],
        bad_activities=["war", "business"],
        note_en=(
            "The dawn period is ruled by Maswara, a gentle and sacred energy. "
            "Traditional Malay healers (bomoh) consider this the best time for "
            "spiritual cleansing, reciting doa, and beginning new learning."
        ),
        note_zh=(
            "黎明時段由瑪斯瓦拉主宰，能量溫和而神聖。"
            "傳統馬來療癒師（Bomoh）認為此時最適合靈性淨化、"
            "誦念祈禱詞（Doa）及展開新的學習。"
        ),
    ),
    KetikaPeriod(
        index=2,
        name_malay="Kala (Zohor)",
        name_en="Midday — Kala",
        name_zh="正午 — 卡拉（午禮）",
        time_start="08:00",
        time_end="12:00",
        fortune="nahas",
        colour="#8B0000",       # dark red
        emoji="☀️",
        planet_or_star="Marikh (Mars)",
        good_activities=["war", "meeting"],
        bad_activities=["marriage", "sailing", "building", "healing"],
        note_en=(
            "Kala is associated with fierce and aggressive energy (Mars). "
            "Manuscripts warn against starting marriages, voyages, or "
            "construction during this period. Only martial or competitive "
            "endeavours are considered fitting."
        ),
        note_zh=(
            "卡拉與火星的猛烈攻擊性能量相關。"
            "手稿警告此時段不宜展開婚事、航行或建造工程，"
            "唯有戰事或競爭性活動較為合適。"
        ),
    ),
    KetikaPeriod(
        index=3,
        name_malay="Sri (Asar)",
        name_en="Afternoon — Sri",
        name_zh="下午 — 斯里（晡禮）",
        time_start="12:00",
        time_end="16:00",
        fortune="baik",
        colour="#228B22",       # forest green
        emoji="🌿",
        planet_or_star="Musytari (Jupiter)",
        good_activities=["business", "marriage", "ceremony", "meeting", "building"],
        bad_activities=["rest"],
        note_en=(
            "Sri carries the benevolent influence of Jupiter — prosperity, "
            "nobility, and success. This is the most favoured period for "
            "trade, weddings, house-building, and important negotiations."
        ),
        note_zh=(
            "斯里承載木星的慈愛影響——繁榮、尊貴與成功。"
            "此時段最受傳統推崇，適合貿易、婚禮、建屋及重要談判。"
        ),
    ),
    KetikaPeriod(
        index=4,
        name_malay="Laba (Maghrib)",
        name_en="Dusk — Laba",
        name_zh="黃昏 — 拉巴（昏禮）",
        time_start="16:00",
        time_end="20:00",
        fortune="sederhana",
        colour="#DAA520",       # goldenrod
        emoji="🌇",
        planet_or_star="Utarid (Mercury)",
        good_activities=["prayer", "healing", "rest", "study"],
        bad_activities=["sailing", "building", "war"],
        note_en=(
            "Laba is a transitional time governed by Mercury — quick-witted "
            "but unpredictable. Suitable for intellectual and spiritual "
            "pursuits; physical or risky ventures should be postponed."
        ),
        note_zh=(
            "拉巴是由水星主宰的過渡時段——敏銳但難以預測。"
            "適合知識性與靈修活動；體力勞動或冒險行為宜延後。"
        ),
    ),
    KetikaPeriod(
        index=5,
        name_malay="Dana (Isyak)",
        name_en="Night — Dana",
        name_zh="夜晚 — 達那（宵禮）",
        time_start="20:00",
        time_end="05:00",
        fortune="sederhana",
        colour="#191970",       # midnight blue
        emoji="🌙",
        planet_or_star="Zuhal (Saturn)",
        good_activities=["prayer", "rest", "study", "healing"],
        bad_activities=["sailing", "business", "building", "agriculture"],
        note_en=(
            "Dana falls under Saturn's deep, contemplative energy. "
            "The night is reserved for rest, devotion, and inner work. "
            "Malay tradition cautions against starting outward ventures "
            "after dark."
        ),
        note_zh=(
            "達那處於土星深沉、沉思的能量之下。"
            "夜晚宜用於休息、祈禱和內省。"
            "馬來傳統忌諱在天黑後展開外向活動。"
        ),
    ),
]


# ===================================================================
# BINTANG TUJUH / KETIKA TUJUH  —  七星時刻占卜
# ===================================================================
# Seven periods mapped to the seven classical celestial bodies
# (Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn).
# The 24-hour day is divided into ~3.4 h blocks.

BINTANG_TUJUH: List[KetikaPeriod] = [
    KetikaPeriod(
        index=1,
        name_malay="Bintang Syams (Matahari)",
        name_en="Star of the Sun",
        name_zh="太陽星",
        time_start="05:00",
        time_end="08:25",
        fortune="baik",
        colour="#FFD700",       # gold
        emoji="☀️",
        planet_or_star="Syams (Sun / 太陽)",
        good_activities=["prayer", "ceremony", "business", "meeting"],
        bad_activities=["rest"],
        note_en=(
            "Ruled by the Sun — energy of authority, clarity, and new "
            "beginnings. Ideal for opening ceremonies, audiences with "
            "leaders, and launching enterprises."
        ),
        note_zh=(
            "由太陽主宰——代表權威、明晰與新的開端。"
            "最適合開幕儀式、拜見長輩或展開事業。"
        ),
    ),
    KetikaPeriod(
        index=2,
        name_malay="Bintang Qamar (Bulan)",
        name_en="Star of the Moon",
        name_zh="月亮星",
        time_start="08:25",
        time_end="11:50",
        fortune="baik",
        colour="#C0C0C0",       # silver
        emoji="🌙",
        planet_or_star="Qamar (Moon / 月亮)",
        good_activities=["healing", "agriculture", "marriage", "study"],
        bad_activities=["war", "sailing"],
        note_en=(
            "The Moon bestows gentle, nurturing energy. A time favoured "
            "for healing, planting, and romantic unions."
        ),
        note_zh=(
            "月亮賦予溫和滋養的能量。此時段適合療癒、種植及婚戀。"
        ),
    ),
    KetikaPeriod(
        index=3,
        name_malay="Bintang Marikh (Merah)",
        name_en="Star of Mars",
        name_zh="火星",
        time_start="11:50",
        time_end="15:15",
        fortune="nahas",
        colour="#DC143C",       # crimson
        emoji="🔴",
        planet_or_star="Marikh (Mars / 火星)",
        good_activities=["war"],
        bad_activities=["marriage", "building", "sailing", "business", "healing"],
        note_en=(
            "Mars brings aggressive, disruptive energy. Malay manuscripts "
            "list this as a period of nahas (misfortune) for most "
            "activities except warfare or defence."
        ),
        note_zh=(
            "火星帶來攻擊性、破壞性的能量。"
            "馬來手稿將此列為大部分活動的凶時，唯有戰事或防禦例外。"
        ),
    ),
    KetikaPeriod(
        index=4,
        name_malay="Bintang Utarid (Kelabu)",
        name_en="Star of Mercury",
        name_zh="水星",
        time_start="15:15",
        time_end="18:40",
        fortune="sederhana",
        colour="#708090",       # slate grey
        emoji="⚡",
        planet_or_star="Utarid (Mercury / 水星)",
        good_activities=["study", "meeting", "business"],
        bad_activities=["building", "agriculture"],
        note_en=(
            "Mercury governs communication and intellect. Moderate fortune — "
            "good for study and negotiations, but unreliable for physical "
            "construction or planting."
        ),
        note_zh=(
            "水星掌管溝通與智識。運勢中平——"
            "適合學習與談判，但不宜建造或種植。"
        ),
    ),
    KetikaPeriod(
        index=5,
        name_malay="Bintang Musytari (Hijau)",
        name_en="Star of Jupiter",
        name_zh="木星",
        time_start="18:40",
        time_end="22:05",
        fortune="baik",
        colour="#006400",       # dark green
        emoji="🍀",
        planet_or_star="Musytari (Jupiter / 木星)",
        good_activities=["marriage", "business", "ceremony", "building", "meeting"],
        bad_activities=["war"],
        note_en=(
            "Jupiter radiates abundance, justice, and honour. One of the "
            "most auspicious periods — excellent for weddings, deals, and "
            "community gatherings."
        ),
        note_zh=(
            "木星散發豐饒、正義與榮譽之光。"
            "最吉利的時段之一——婚禮、交易、社區聚會皆宜。"
        ),
    ),
    KetikaPeriod(
        index=6,
        name_malay="Bintang Zuhrah (Putih)",
        name_en="Star of Venus",
        name_zh="金星",
        time_start="22:05",
        time_end="01:30",
        fortune="baik",
        colour="#FF69B4",       # hot pink
        emoji="💖",
        planet_or_star="Zuhrah (Venus / 金星)",
        good_activities=["marriage", "healing", "prayer", "rest", "ceremony"],
        bad_activities=["war", "agriculture"],
        note_en=(
            "Venus brings love, beauty, and harmony. A blessed period for "
            "romantic matters, artistic endeavours, spiritual devotion, "
            "and healing rituals."
        ),
        note_zh=(
            "金星帶來愛、美與和諧。此時段受祝福——"
            "適合浪漫事宜、藝術創作、靈修及療癒儀式。"
        ),
    ),
    KetikaPeriod(
        index=7,
        name_malay="Bintang Zuhal (Hitam)",
        name_en="Star of Saturn",
        name_zh="土星",
        time_start="01:30",
        time_end="05:00",
        fortune="nahas",
        colour="#2F2F2F",       # near-black
        emoji="🪐",
        planet_or_star="Zuhal (Saturn / 土星)",
        good_activities=["rest", "prayer"],
        bad_activities=["sailing", "marriage", "building", "business", "agriculture", "meeting"],
        note_en=(
            "Saturn's cold, heavy energy dominates the deepest hours of "
            "night. Manuscripts classify this as highly inauspicious for "
            "almost all worldly activities; only rest and devotion are "
            "advised."
        ),
        note_zh=(
            "土星冷冽沉重的能量主宰深夜時分。"
            "手稿將此列為大部分世俗活動的大凶時段，"
            "僅建議休息與祈禱。"
        ),
    ),
]


# ===================================================================
# Helper functions
# ===================================================================

def _time_to_minutes(t: str) -> int:
    """Convert 'HH:MM' to minutes since midnight."""
    h, m = map(int, t.split(":"))
    return h * 60 + m


def get_current_period(
    periods: List[KetikaPeriod],
    hour: int,
    minute: int,
) -> KetikaPeriod:
    """Return the KetikaPeriod that contains the given time (24-h clock)."""
    now_min = hour * 60 + minute
    for p in periods:
        start = _time_to_minutes(p.time_start)
        end   = _time_to_minutes(p.time_end)
        if start < end:
            if start <= now_min < end:
                return p
        else:  # wraps midnight (e.g. 22:05 → 01:30)
            if now_min >= start or now_min < end:
                return p
    # Fallback — should never happen if data covers 24 h
    return periods[0]


def get_periods_for_activity(
    periods: List[KetikaPeriod],
    activity_key: str,
) -> Dict[str, List[KetikaPeriod]]:
    """Return dict with 'good' and 'bad' lists for the requested activity."""
    good = [p for p in periods if activity_key in p.good_activities]
    bad  = [p for p in periods if activity_key in p.bad_activities]
    return {"good": good, "bad": bad}


def daily_summary(periods: List[KetikaPeriod], lang: str = "en") -> str:
    """Build a one-paragraph daily fortune overview."""
    baik_count    = sum(1 for p in periods if p.fortune == "baik")
    nahas_count   = sum(1 for p in periods if p.fortune == "nahas")
    neutral_count = sum(1 for p in periods if p.fortune == "sederhana")

    if lang == "zh":
        return (
            f"今日共有 **{len(periods)}** 個時段：\n"
            f"- 吉時 **{baik_count}** 段\n"
            f"- 凶時 **{nahas_count}** 段\n"
            f"- 中平 **{neutral_count}** 段\n\n"
            + ("整體而言，今日吉時較多，適合展開重要事務。"
               if baik_count > nahas_count
               else "今日凶時偏多，建議行事謹慎，避開不利時段。"
               if nahas_count > baik_count
               else "今日吉凶參半，宜擇時而動。")
        )
    return (
        f"Today has **{len(periods)}** periods:\n"
        f"- Auspicious: **{baik_count}**\n"
        f"- Inauspicious: **{nahas_count}**\n"
        f"- Neutral: **{neutral_count}**\n\n"
        + ("Overall, auspicious periods dominate — a good day to undertake "
           "important matters."
           if baik_count > nahas_count
           else "Inauspicious periods dominate today — proceed with caution "
                "and avoid risky undertakings."
           if nahas_count > baik_count
           else "Fortune is balanced today — choose your timing wisely.")
    )

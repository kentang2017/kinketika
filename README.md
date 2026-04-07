# 🌙 Kinketika（堅克提卡）— Malay Time Divination
# 馬來群島傳統時間占卜工具

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit)](https://streamlit.io)

A culturally respectful, bilingual (English / 繁體中文) web application that
presents two classical time-divination systems from the **Malay Archipelago
(Nusantara)** — drawing on traditional manuscripts from the Malay Peninsula,
Sumatra, Java, and South Sulawesi (Bugis-Makassar).

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Ketika Lima** (五時刻) | Five-period system aligned with the five Islamic prayer times |
| **Bintang Tujuh** (七星時刻) | Seven-period system mapped to the seven classical celestial bodies |
| **Wheel Diagram** | Interactive Plotly polar-bar chart in the style of traditional manuscript wheels |
| **Activity Planner** | Select an activity (sailing, marriage, business …) and see recommended / discouraged periods |
| **Daily Fortune Summary** | At-a-glance auspicious / inauspicious / neutral period count |
| **Custom Date & Time** | Query any date-time instead of the current moment |
| **Bilingual UI** | Full English and 繁體中文 interface |

---

## 📖 Cultural Background / 文化背景

### What is *Ketika*?

In Malay tradition, **ketika** (from the Sanskrit *kṛtikā* / Arabic influence)
refers to a system of dividing time into auspicious and inauspicious segments.
These systems appear in traditional Malay manuscripts (*kitab*) and are
consulted before undertaking important activities — voyages, weddings,
house-building, agricultural work, and healing rituals.

The practice synthesises elements from:

- **Islamic cosmology** — planetary hours and prayer-time divisions
- **Hindu-Buddhist heritage** — *muhūrta* and *nakṣatra* traditions
- **Austronesian folk belief** — local spirits, winds, and seasonal knowledge

### Ketika Lima vs Bintang Tujuh

| Aspect | Ketika Lima (五時刻) | Bintang Tujuh (七星時刻) |
|--------|----------------------|--------------------------|
| Periods per day | 5 | 7 |
| Primary mapping | Five Islamic prayer times (Subuh, Zohor, Asar, Maghrib, Isyak) | Seven classical celestial bodies (Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn) |
| Cultural origin | Predominantly Malay Peninsula & Sumatra | Widespread across the Archipelago; strong Bugis-Makassar tradition |
| Fortune categories | Baik (吉), Nahas (凶), Sederhana (中平) | Same three categories |
| Typical use | Daily personal guidance | Detailed activity planning, especially maritime and trade |

### Important Note / 使用注意事項

> 📜 **This app is a cultural-learning and reference tool.**
> Traditional divination should respect the guidance of local
> **Bomoh** (Malay healer-diviners) and **Panrita** (Bugis-Makassar sages).
> Important life decisions should always be combined with rational judgement.
>
> 此應用為文化學習與參考工具。傳統占卜需尊重當地 Bomoh（馬來療癒師）/
> Panrita（武吉士智者）的指導。重要決定請結合理性判斷。

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9+

### Installation

```bash
# Clone the repository
git clone https://github.com/kentang2017/kinketika.git
cd kinketika

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## 📁 Project Structure

```
kinketika/
├── app.py              # Main Streamlit application
├── ketika_data.py      # Data structures — Ketika Lima & Bintang Tujuh
├── wheel_chart.py      # Plotly polar-bar wheel diagram generator
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── .streamlit/
    └── config.toml     # Streamlit theme (warm manuscript palette)
```

---

## 🎨 Design Philosophy

The interface draws on the aesthetics of traditional Malay/Islamic manuscripts:

- **Warm colour palette** — gold (#D4AF37), parchment, deep brown
- **Serif typography** — Playfair Display + Noto Serif TC
- **Ornamental dividers** — inspired by kitab page decorations
- **Colour-coded fortune badges** — green for *baik*, red for *nahas*, amber for *sederhana*

---

## 📚 References & Further Reading

- Mohd. Taib Osman, *Malay Folk Beliefs: An Integration of Disparate Elements* (1989)
- Skeat, W. W., *Malay Magic* (1900; Dover reprint 1967)
- Pelras, Christian, *The Bugis* (1996)
- Winstedt, R. O., *The Malay Magician* (1951)
- Various digitised Malay manuscripts from the British Library and National Library of Malaysia

---

## 📜 License

This project is released for educational and cultural-learning purposes.

---

## 🙏 Acknowledgements

Respect and gratitude to the communities of the Malay Archipelago whose
ancestral wisdom is represented in this tool. This application is offered
in the spirit of cultural preservation and respectful learning.

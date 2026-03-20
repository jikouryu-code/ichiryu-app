import streamlit as st

# ===== ページ設定 =====
st.set_page_config(page_title="一龍聖典", layout="centered")

# ===== 龍画像（あれば表示） =====
try:
    st.image("dragon.png", use_container_width=True)
except:
    pass

# ===== データ（中身は変更しない） =====
DATA = {
    "JP": {
        "title": "一龍聖典",
        "vol": "- 風の巻 -",
        "sub": "四柱推命・基礎事典：【天】の理",
        "categories": {
            "🍃 十干（じっかん：魂の本質）": {
                "甲 (きのえ)": "【木陽：天空を貫く大樹】向上心に溢れる大黒柱。信念という根を深く張り、真っ直ぐに空を目指す宿命です。",
                "乙 (きのと)": "【木陰：風に舞う草花】柔軟性と忍耐力の象徴。仲間と協力し、踏まれても立ち上がる強さを持っています。",
                "丙 (ひのえ)": "【火陽：万物を照らす太陽】圧倒的な存在感。公明正大な生き方で周囲を明るく照らす光の先導者。",
                "丁 (ひのと)": "【火陰：闇を照らす灯火】内面に激しい情熱を秘めた知性。誰かの道を優しく照らす心の救世主。",
                "戊 (つちのえ)": "【土陽：威風堂々たる名山】包容力と安定感の守護者。どっしりと構え、多くの人を惹きつける徳の主。",
                "己 (つちのと)": "【土陰：慈愛の田園】万物を育む育成の天才。地道な努力を積み重ね、人を生かすことで自らも輝きます。",
                "庚 (かのえ)": "【金陽：変革を告げる刀剣】決断力とスピード。自分を厳しく磨き、古い価値観を打ち破る英雄の宿命。",
                "辛 (かのと)": "【金陰：輝きの宝石】高貴なる美意識。試練を磨きに変え、至高の価値を放つ審美の守護者。",
                "壬 (みずのえ)": "【水陽：奔流する大海】自由を愛する開拓者。時代の波を読み解き、大海原を渡る知略の英雄。",
                "癸 (みずのと)": "【水陰：心に染み入る雨】静かな努力で不可能を可能にする持続力。人々の心を潤す癒やしの賢者。"
            }
        }
    }
}

# ===== 英語（中身そのまま使う） =====
DATA["EN"] = DATA["JP"]

# ===== 言語切替 =====
if "lang" not in st.session_state:
    st.session_state.lang = "JP"

col1, col2 = st.columns(2)
with col1:
    if st.button("🇯🇵 日本語"):
        st.session_state.lang = "JP"
with col2:
    if st.button("🇺🇸 English"):
        st.session_state.lang = "EN"

L = DATA[st.session_state.lang]

st.write(L["categories"].keys()) 

# ===== 表示 =====
st.title(L["title"])
st.subheader(L["vol"])
st.markdown(f"**{L['sub']}**")

for cat_name, items in L["categories"].items():
    with st.expander(cat_name):
        for word, desc in items.items():
            st.markdown(f"### {word}")
            st.write(desc)
            st.markdown("---")

st.sidebar.write("Ichiryu龍 監修")

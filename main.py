# my_second_repo0-
import streamlit as st
import random
import time

st.set_page_config(page_title="RPG 캐릭터 게임", page_icon="🎮")

# 🎨 스타일
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}
.card {
    padding: 20px;
    border-radius: 20px;
    background-color: rgba(255,255,255,0.1);
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("🎮 나만의 RPG 캐릭터 게임")
st.write("캐릭터를 만들고 ⚔️ 몬스터와 싸워보세요!")

st.markdown("---")

# 🧠 상태 저장
if "character" not in st.session_state:
    st.session_state.character = None

# 🎯 캐릭터 생성
st.subheader("🧙 캐릭터 생성")

personality = st.selectbox("💭 성격", ["🔥 열정", "❄️ 냉철", "🌪️ 자유", "🌱 따뜻"])
weapon = st.selectbox("⚔️ 무기", ["🗡️ 검", "🏹 활", "🔮 마법", "🛡️ 방패"])

if st.button("🎉 캐릭터 생성"):
    with st.spinner("✨ 생성 중..."):
        time.sleep(1.5)

    st.balloons()

    character = {
        "name": random.choice(["전설의", "어둠의", "빛의", "파괴자"]) + " 전사",
        "personality": personality,
        "weapon": weapon,
        "level": 1,
        "hp": random.randint(80, 120),
        "power": random.randint(50, 100),
        "intelligence": random.randint(50, 100),
        "agility": random.randint(50, 100),
        "exp": 0
    }

    st.session_state.character = character

# 🧾 캐릭터 표시
if st.session_state.character:
    c = st.session_state.character

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.success(f"""
    🏷️ {c['name']}
    
    💭 성격: {c['personality']}
    ⚔️ 무기: {c['weapon']}
    🆙 레벨: {c['level']}
    ❤️ 체력: {c['hp']}
    """)

    st.markdown("### ⚡ 능력치")
    st.progress(c["power"], text=f"💪 힘 {c['power']}")
    st.progress(c["intelligence"], text=f"🧠 지능 {c['intelligence']}")
    st.progress(c["agility"], text=f"🏃 민첩 {c['agility']}")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # 🐲 몬스터 생성
    st.subheader("⚔️ 몬스터 전투")

    monster = {
        "name": random.choice(["🐲 드래곤", "👹 오크", "🧟 좀비", "👻 유령"]),
        "hp": random.randint(60, 120),
        "power": random.randint(40, 100)
    }

    st.warning(f"""
    등장한 몬스터!
    
    👾 {monster['name']}
    ❤️ 체력: {monster['hp']}
    💥 공격력: {monster['power']}
    """)

    # ⚔️ 전투 버튼
    if st.button("⚔️ 전투 시작"):
        with st.spinner("🔥 전투 중..."):
            time.sleep(2)

        # 🎲 전투 계산
        player_score = c["power"] + random.randint(0, 50)
        monster_score = monster["power"] + random.randint(0, 50)

        if player_score > monster_score:
            st.success("🎉 승리했습니다!")
            st.balloons()

            # 경험치 + 레벨업
            c["exp"] += 50

            if c["exp"] >= 100:
                c["level"] += 1
                c["exp"] = 0
                c["power"] += 10
                c["hp"] += 20
                st.info("🆙 레벨업! 능력치 상승!")

        else:
            st.error("💀 패배했습니다...")
            c["hp"] -= 20

            if c["hp"] <= 0:
                st.error("☠️ 캐릭터가 쓰러졌습니다... 다시 생성하세요")
                st.session_state.character = None

    # 🔄 초기화
    if st.button("🔄 새 캐릭터 만들기"):
        st.session_state.character = None
        st.rerun()

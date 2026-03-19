# my_second_repo0-
import streamlit as st
import random

st.set_page_config(page_title="RPG 어드벤처", page_icon="🎮")

# 🎨 UI + 가독성 개선 (핵심)
st.markdown("""
<style>
/* 전체 배경 + 어둡게 덮기 */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1511512578047-dfb367046420");
    background-size: cover;
    background-attachment: fixed;
}

.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.65); /* 🔥 핵심: 어둡게 덮기 */
    z-index: 0;
}

/* 모든 컨텐츠 위로 올리기 */
.main {
    position: relative;
    z-index: 1;
    color: white;
}

/* 카드 UI */
.card {
    background: rgba(0,0,0,0.8);
    padding: 20px;
    border-radius: 20px;
    margin-top: 10px;
    box-shadow: 0 0 15px rgba(0,0,0,0.5);
}

/* 버튼 스타일 */
button {
    border-radius: 12px !important;
    font-weight: bold !important;
}

/* 텍스트 강조 */
h1, h2, h3, h4, p {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🎮 RPG 어드벤처")
st.write("⚔️ 탐험하고 성장하는 나만의 게임")

st.markdown("---")

# 🧠 상태 관리 (안정 핵심)
if "char" not in st.session_state:
    st.session_state.char = None
if "mode" not in st.session_state:
    st.session_state.mode = "idle"
if "enemy" not in st.session_state:
    st.session_state.enemy = None

# 🧙 캐릭터 생성
if st.session_state.char is None:
    if st.button("🎉 캐릭터 생성"):
        st.session_state.char = {
            "name": random.choice(["전설의", "어둠의", "빛의"]) + " 용사",
            "hp": 100,
            "power": random.randint(50, 80),
            "level": 1,
            "gold": 0
        }
        st.balloons()
        st.rerun()

# 🧾 캐릭터 정보
if st.session_state.char:
    c = st.session_state.char

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader(f"🏷️ {c['name']}")
    st.write(f"🆙 레벨: {c['level']} | 💰 골드: {c['gold']}")
    st.progress(max(c["hp"],0), text=f"❤️ 체력 {c['hp']}")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # 🗺️ 탐험
    if st.session_state.mode == "idle":
        if st.button("🌲 탐험하기"):
            event = random.choice(["battle", "treasure", "trap", "heal"])

            if event == "battle":
                st.session_state.enemy = {
                    "hp": random.randint(60, 100),
                    "power": random.randint(40, 80)
                }
                st.session_state.mode = "battle"

            elif event == "treasure":
                gold = random.randint(10, 50)
                c["gold"] += gold
                st.success(f"💰 보물 발견! +{gold}G")

            elif event == "trap":
                damage = random.randint(10, 30)
                c["hp"] -= damage
                st.error(f"💥 함정! -{damage} HP")

            elif event == "heal":
                heal = random.randint(10, 30)
                c["hp"] += heal
                st.success(f"💚 회복! +{heal} HP")

            st.rerun()

    # ⚔️ 전투
    if st.session_state.mode == "battle":
        enemy = st.session_state.enemy

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("⚔️ 전투 중")
        st.write(f"👾 몬스터 HP: {enemy['hp']}")
        st.write(f"💥 공격력: {enemy['power']}")
        st.markdown('</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        # 🗡️ 공격
        if col1.button("🗡️ 공격"):
            player_damage = c["power"] + random.randint(-10, 20)
            enemy["hp"] -= player_damage

            if enemy["hp"] <= 0:
                st.success("🎉 승리!")
                c["gold"] += 30
                c["level"] += 1
                st.session_state.mode = "idle"
                st.session_state.enemy = None
                st.balloons()
            else:
                c["hp"] -= enemy["power"]

            st.rerun()

        # 🏃 도망
        if col2.button("🏃 도망"):
            if random.random() < 0.6:
                st.success("💨 도망 성공!")
                st.session_state.mode = "idle"
                st.session_state.enemy = None
            else:
                st.error("❌ 도망 실패!")
                c["hp"] -= enemy["power"]

            st.rerun()

    # 💀 게임 오버
    if c["hp"] <= 0:
        st.error("☠️ GAME OVER")
        if st.button("🔄 다시 시작"):
            st.session_state.clear()
            st.rerun()

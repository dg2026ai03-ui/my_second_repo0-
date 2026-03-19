# my_second_repo0-
import streamlit as st
import random
import time

st.set_page_config(page_title="RPG 어드벤처", page_icon="🎮")

# 🎨 스타일
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
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

st.title("🎮 RPG 어드벤처: 당신의 선택이 운명을 바꾼다")
st.markdown("---")

# 🧠 상태 저장
if "char" not in st.session_state:
    st.session_state.char = None
if "log" not in st.session_state:
    st.session_state.log = []

# 🧙 캐릭터 생성
st.subheader("🧙 캐릭터 생성")

if st.button("🎉 캐릭터 생성"):
    st.balloons()
    st.session_state.char = {
        "name": random.choice(["전설의", "어둠의", "빛의"]) + " 용사",
        "hp": 100,
        "power": random.randint(50, 80),
        "agility": random.randint(50, 80),
        "level": 1,
        "gold": 0
    }
    st.session_state.log = ["🎮 게임 시작!"]

# 📜 캐릭터 정보
if st.session_state.char:
    c = st.session_state.char

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write(f"🏷️ {c['name']} | 🆙 Lv.{c['level']} | ❤️ {c['hp']} | 💰 {c['gold']}G")
    st.progress(c["hp"], text="체력")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # 🎲 탐험 이벤트
    st.subheader("🗺️ 탐험")

    if st.button("🌲 탐험하기"):
        event = random.choice(["battle", "treasure", "trap", "heal"])

        if event == "battle":
            monster_power = random.randint(40, 90)
            st.session_state.enemy = {"hp": 80, "power": monster_power}
            st.session_state.mode = "battle"
            st.session_state.log.append("👾 몬스터 등장!")

        elif event == "treasure":
            gold = random.randint(10, 50)
            c["gold"] += gold
            st.success(f"💰 보물 발견! +{gold}G")
            st.session_state.log.append("💰 보물 획득")

        elif event == "trap":
            damage = random.randint(10, 30)
            c["hp"] -= damage
            st.error(f"💥 함정! -{damage} HP")
            st.session_state.log.append("💥 함정 발동")

        elif event == "heal":
            heal = random.randint(10, 30)
            c["hp"] += heal
            st.success(f"💚 회복! +{heal} HP")
            st.session_state.log.append("💚 회복 이벤트")

    # ⚔️ 전투 모드
    if "mode" in st.session_state and st.session_state.mode == "battle":
        enemy = st.session_state.enemy

        st.markdown("### ⚔️ 전투 중")
        st.warning(f"👾 몬스터 HP: {enemy['hp']} / 공격력: {enemy['power']}")

        col1, col2, col3 = st.columns(3)

        # 🗡️ 공격
        if col1.button("🗡️ 공격"):
            damage = c["power"] + random.randint(-10, 20)
            enemy["hp"] -= damage

            if enemy["hp"] <= 0:
                st.success("🎉 승리!")
                st.balloons()
                c["gold"] += 30
                c["level"] += 1
                st.session_state.mode = None
            else:
                c["hp"] -= enemy["power"]

        # 🏃 회피
        if col2.button("🏃 회피"):
            if random.random() < 0.5:
                st.success("💨 회피 성공!")
            else:
                st.error("❌ 회피 실패!")
                c["hp"] -= enemy["power"]

        # 🔮 스킬
        if col3.button("🔮 스킬"):
            damage = c["power"] * 1.5
            enemy["hp"] -= damage
            c["hp"] -= 10

    # 💀 게임 오버
    if c["hp"] <= 0:
        st.error("☠️ GAME OVER")
        if st.button("🔄 다시 시작"):
            st.session_state.char = None
            st.rerun()

    # 📜 로그 출력
    st.markdown("### 📜 게임 로그")
    for l in st.session_state.log[-5:]:
        st.write(l)

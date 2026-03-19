# my_second_repo0-
import streamlit as st
import random
import time

st.set_page_config(page_title="캐릭터 생성기", page_icon="🧙‍♂️")

# 🎨 CSS 스타일
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #1e1e2f, #2b2b4f);
    color: white;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}
.card {
    padding: 20px;
    border-radius: 20px;
    background-color: rgba(255,255,255,0.1);
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🧙‍♂️ 나만의 캐릭터 생성기</div>', unsafe_allow_html=True)
st.write("✨ 선택하고 버튼을 누르면 당신만의 캐릭터가 탄생합니다!")

st.markdown("---")

# 🎯 선택
personality = st.selectbox("💭 성격", ["🔥 열정적", "❄️ 냉철", "🌪️ 자유로움", "🌱 따뜻함"])
weapon = st.selectbox("⚔️ 무기", ["🗡️ 검", "🏹 활", "🔮 마법", "🛡️ 방패"])
world = st.selectbox("🌍 세계관", ["🏰 판타지", "🚀 SF", "🌲 자연", "🌌 우주"])

st.markdown("---")

if st.button("🎉 캐릭터 생성하기"):
    
    # 🎬 연출
    with st.spinner("✨ 캐릭터 생성 중..."):
        time.sleep(2)

    st.balloons()

    # 🎲 랜덤 요소
    titles = ["전설의", "어둠의", "빛의", "파괴자", "수호자"]
    abilities = ["🔥 불 지배", "❄️ 시간 정지", "⚡ 번개 소환", "🌿 치유 능력"]
    grades = ["SSS", "SS", "S", "A", "B"]
    
    title = random.choice(titles)
    ability = random.choice(abilities)
    grade = random.choice(grades)

    # ⚡ 능력치
    power = random.randint(50, 100)
    intelligence = random.randint(50, 100)
    agility = random.randint(50, 100)

    # 🖼️ 이미지 (무료 이미지 URL)
    images = [
        "https://cdn.pixabay.com/photo/2017/01/31/13/14/fantasy-2029157_960_720.png",
        "https://cdn.pixabay.com/photo/2016/03/31/19/56/fantasy-1299194_960_720.png",
        "https://cdn.pixabay.com/photo/2017/03/27/14/56/avatar-2179872_960_720.png"
    ]
    image = random.choice(images)

    # 🎭 결과 출력
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.image(image, use_container_width=True)

    st.success(f"""
    🎉 캐릭터 생성 완료!

    🏷️ {title} {personality} 전사  
    🌍 세계: {world}  
    ⚔️ 무기: {weapon}  
    ✨ 능력: {ability}  
    🏆 등급: {grade}
    """)

    st.markdown("### ⚡ 능력치")
    st.progress(power, text=f"💪 힘: {power}")
    st.progress(intelligence, text=f"🧠 지능: {intelligence}")
    st.progress(agility, text=f"🏃 민첩: {agility}")

    st.markdown("### 📖 스토리")
    st.write(f"""
    {world} 세계에서 태어난 당신은 {personality} 성격을 가진 존재입니다.  
    {weapon}을 다루며, {ability} 능력을 사용합니다.  
    사람들은 당신을 '{title} 존재'라 부르며 두려워하거나 존경합니다.
    """)

    st.markdown('</div>', unsafe_allow_html=True)

    # 🎲 재도전 버튼
    if st.button("🔄 다시 생성"):
        st.rerun()

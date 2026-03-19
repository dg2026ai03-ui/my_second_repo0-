# my_second_repo0-
import streamlit as st
import random

st.set_page_config(page_title="나만의 캐릭터 생성기", page_icon="🧙‍♂️")

st.title("🧙‍♂️ 나만의 캐릭터 생성기")
st.subheader("✨ 당신만의 판타지 캐릭터를 만들어보세요!")

st.markdown("---")

# 🎨 선택 요소들
personality = st.selectbox(
    "💭 성격을 선택하세요",
    ["🔥 열정적인", "❄️ 차분한", "🌪️ 자유로운", "🌱 따뜻한"]
)

weapon = st.selectbox(
    "⚔️ 무기를 선택하세요",
    ["🗡️ 검", "🏹 활", "🔮 마법", "🛡️ 방패"]
)

world = st.selectbox(
    "🌍 세계관을 선택하세요",
    ["🏰 중세 판타지", "🚀 미래 SF", "🌲 자연 세계", "🌌 우주"]
)

st.markdown("---")

# 🎲 결과 생성 버튼
if st.button("🎉 캐릭터 생성하기"):
    
    st.balloons()  # 🎈 풍선 효과
    
    # 🎯 랜덤 요소 추가
    special_ability = random.choice([
        "🔥 불을 다루는 능력",
        "❄️ 시간을 멈추는 힘",
        "🌿 자연과 대화하는 능력",
        "⚡ 번개를 소환하는 힘"
    ])
    
    title = random.choice([
        "전설의", "숨겨진", "최강의", "신비로운"
    ])
    
    # 🧙 결과 출력
    st.success(f"""
    🎉 당신의 캐릭터가 완성되었습니다!

    🏷️ 이름: {title} {personality} 전사  
    🌍 세계관: {world}  
    ⚔️ 무기: {weapon}  
    ✨ 특수 능력: {special_ability}
    
    💬 "당신은 세상을 바꿀 운명을 가진 존재입니다!"
    """)

    st.markdown("---")

    # 🎭 추가 설명
    st.info("📖 캐릭터 스토리")
    
    story = f"""
    {world} 세계에서 태어난 당신은 {personality} 성격을 지닌 전사입니다.  
    당신은 {weapon}을(를) 사용하며, {special_ability}을(를) 가지고 있습니다.  
    사람들은 당신을 '{title} 존재'라고 부릅니다.
    """
    
    st.write(story)

    # 🎲 추가 버튼
    if st.button("🔄 다른 캐릭터 다시 만들기"):
        st.rerun()

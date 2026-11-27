from datetime import datetime
from random import choice, randrange
from zoneinfo import ZoneInfo

import streamlit as st


ZODIAC_ANIMALS = (
    ("쥐", "🐭", "재치 있고 기회를 잘 포착해요."),
    ("소", "🐮", "꾸준하고 믿음직스러워요."),
    ("호랑이", "🐯", "용감하고 도전을 즐겨요."),
    ("토끼", "🐰", "다정하고 센스가 넘쳐요."),
    ("용", "🐲", "당당하고 상상력이 풍부해요."),
    ("뱀", "🐍", "차분하고 통찰력이 있어요."),
    ("말", "🐴", "활기차고 자유로워요."),
    ("양", "🐑", "따뜻하고 감수성이 풍부해요."),
    ("원숭이", "🐵", "호기심 많고 재치 있어요."),
    ("닭", "🐔", "꼼꼼하고 자신감이 있어요."),
    ("개", "🐶", "성실하고 의리가 있어요."),
    ("돼지", "🐷", "넉넉하고 긍정적이에요."),
)
KOREA_TIMEZONE = ZoneInfo("Asia/Seoul")


def initialize_player() -> None:
    if "credits" not in st.session_state:
        st.session_state.credits = 0
        st.session_state.last_reward_date = None

    today = datetime.now(KOREA_TIMEZONE).date()
    if st.session_state.last_reward_date != today:
        reward = randrange(50, 501, 5)
        st.session_state.credits += reward
        st.session_state.last_reward_date = today
        st.session_state.today_reward = reward


st.set_page_config(page_title="십이지신 아바타", page_icon="🐉", layout="centered")
initialize_player()

st.title("🐉 십이지신 아바타 게임")
st.caption("오늘의 나만의 수호 동물을 만나고, 매일 접속 보상도 받아 보세요!")

credit_col, reward_col = st.columns(2)
credit_col.metric("보유 크레딧", f"{st.session_state.credits:,} C")
if st.session_state.last_reward_date == datetime.now(KOREA_TIMEZONE).date():
    reward_col.metric("오늘 받은 보상", f"+{st.session_state.today_reward} C")

st.divider()
st.subheader("나만의 아바타 만들기")
st.write("카메라로 전신 사진을 촬영한 뒤 아바타를 생성해 보세요.")
photo = st.camera_input("전신 사진 촬영")

if st.button("✨ 십이지신 아바타 생성", type="primary"):
    if photo is None:
        st.warning("먼저 카메라로 사진을 촬영해 주세요.")
    else:
        st.session_state.avatar_animal = choice(ZODIAC_ANIMALS)
        st.session_state.avatar_photo = photo.getvalue()

if "avatar_animal" in st.session_state:
    animal, emoji, description = st.session_state.avatar_animal
    st.divider()
    st.subheader(f"{emoji} 당신의 수호 동물은 {animal}!")
    st.image(st.session_state.avatar_photo, caption="내 아바타 사진")
    st.info(f"{emoji} {animal}의 기운: {description}")
    st.caption("현재 데모는 사진에 십이지신 캐릭터를 무작위로 지정합니다.")

st.divider()
st.subheader("오늘의 접속 보상")
st.success(f"오늘의 보상으로 **{st.session_state.today_reward} 크레딧**을 받았어요!")
st.caption("보상은 50~500 크레딧 사이에서 5 단위로 지급됩니다.")
st.caption("사진과 크레딧은 현재 브라우저 세션에만 저장되며, 세션이 끝나면 초기화됩니다.")
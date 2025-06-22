import streamlit as st
import random
from datetime import date

st.set_page_config(page_title="RunMate", page_icon="🏃")

words = [
    "努力をしている人間を笑うな。夢を語る人間を笑うな。",
    "諦めなければ失敗じゃない。継続できることも才能の一つだ。",
    "お前がサボっている間に、誰かが努力している。",
    "昨日の自分を超えること、それが本当の成長だ。",
    "才能がなくても、継続は誰にでもできる最強の武器だ。"
]

st.title("🏃 RunMate - 100m記録分析アプリ")

with st.form("run_form"):
    time_sec = st.number_input("タイム（秒）", step=0.1, format="%.2f")
    steps = st.number_input("歩数", step=1)
    weather = st.selectbox("天気", ["晴れ", "曇り", "雨"])
    temp = st.number_input("気温（℃）", step=1)
    start_conf = st.selectbox("スタートの自信", ["◯", "△", "✕"])
    finish_tired = st.selectbox("フィニッシュで疲れたか", ["◯", "△", "✕"])
    submitted = st.form_submit_button("分析する")

if submitted:
    step_length = 100 / steps if steps else 0
    advice = []

    if step_length < 1.6:
        advice.append("歩幅が小さいかもしれません。地面を強く蹴る意識を持ってみましょう。")
    elif step_length > 2.1:
        advice.append("歩幅が大きすぎるとバランスが崩れます。ピッチを意識しましょう。")
    else:
        advice.append("適切な歩幅です。この調子でピッチも意識しましょう。")

    if start_conf == "✕":
        advice.append("スタートの姿勢を改善しましょう。クラウチングスタートのフォームを練習しましょう。")
    elif start_conf == "△":
        advice.append("スタートに少し不安があるようです。スタートダッシュの反応練習をしましょう。")

    if finish_tired == "◯":
        advice.append("終盤にバテやすいなら、持久力アップのインターバルトレーニングを加えましょう。")

    st.header("📊 結果")
    st.write(f"🗓️ 日付：{date.today().isoformat()}")
    st.write(f"⏱️ タイム：{time_sec} 秒")
    st.write(f"👣 歩数：{steps} 歩")
    st.write(f"📏 歩幅：{round(step_length, 2)} m")
    st.write(f"🌤️ 天気：{weather}　🌡️ 気温：{temp} ℃")

    st.subheader("🧠 アドバイス")
    for a in advice:
        st.markdown(f"- {a}")

    st.subheader("💬 励ましの言葉")
    st.success(random.choice(words))

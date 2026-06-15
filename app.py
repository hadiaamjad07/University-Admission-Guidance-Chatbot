import streamlit as st
import re

with open("training_data.txt", "r", encoding="utf-8") as f:
    raw_data = f.read().lower()

sentences = raw_data.split(".")

def clean(text):
    return re.sub(r"[^a-zA-Z ]", "", text.lower()).strip()

def get_answer(query):

    query = clean(query)
    query_words = query.split()

    scored = []

    for sentence in sentences:

        sentence_clean = clean(sentence)

        if len(sentence_clean) < 50:
            continue

        match_count = 0

        for word in query_words:
            if word in sentence_clean:
                match_count += 1

        if match_count >= 2:

            score = match_count / len(sentence_clean.split())

            scored.append(
                (score, sentence.strip())
            )

    scored.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    top = [x[1] for x in scored[:3]]

    if top:
        return "\n\n".join(top)

    return "No exact answer found."

st.set_page_config(
    page_title="University Admission Chatbot",
    page_icon="🎓"
)

st.title("🎓 University Admission Guidance Chatbot")

st.write(
    "Ask questions about admissions, scholarships, universities and education."
)

user_input = st.text_input(
    "Enter your question"
)

if user_input:

    answer = get_answer(user_input)

    st.success(answer)

    st.markdown("---")

    st.caption(
        "University Admission Chatbot"
    )
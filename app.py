import streamlit as st

st.title("No‑Wait Customer Support Bot")

st.subheader("Shop Owner: Paste your FAQ")
faq_text = st.text_area(
    ""
)

st.subheader("Customer: Ask a question")
question = st.text_input("Type your question")

def find_answer(faq, question):
    faq_lines = faq.lower().split("\n")
    question = question.lower()

    for line in faq_lines:
        # very simple keyword matching
        for word in question.split():
            if word in line:
                return line

    return None

if st.button("Get Answer"):
    if faq_text.strip() == "" or question.strip() == "":
        st.warning("Please enter both FAQ and question")
    else:
        answer = find_answer(faq_text, question)

        if answer:
            st.success(answer.capitalize())
        else:
            st.error("Sorry, please contact the shop directly.")

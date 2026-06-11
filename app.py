import os
import streamlit as st

st.set_page_config(
    page_title="Zyro Dynamics HR Assistant",
    page_icon="🤖"
)

st.title("🤖 Zyro Dynamics HR Assistant")

st.markdown(
    '''
    Ask questions about:
    - Leave Policy
    - Work From Home Policy
    - Compensation & Benefits
    - Performance Reviews
    - POSH Policy
    - Travel & Expenses
    '''
)

REFUSAL_MESSAGE = (
    "I can only answer HR-related questions from Zyro Dynamics policy documents."
)

question = st.text_input(
    "Ask your HR question:"
)

if question:

    hr_keywords = [
        "leave",
        "salary",
        "benefit",
        "policy",
        "employee",
        "performance",
        "review",
        "travel",
        "expense",
        "wfh",
        "remote",
        "attendance",
        "posh",
        "onboarding",
        "probation",
        "resignation",
        "compensation"
    ]

    if not any(
        keyword in question.lower()
        for keyword in hr_keywords
    ):
        st.warning(REFUSAL_MESSAGE)

    else:
        st.success(
            "This is a placeholder HR assistant. Connect your RAG pipeline here."
        )

        st.write(
            "Answer will be generated from Zyro Dynamics policy documents."
        )

        st.subheader("Sources")
        st.write("HR Policy Documents")
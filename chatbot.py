import streamlit as st
from fuzzywuzzy import fuzz

# Page configuration
st.set_page_config(page_title="College Helpdesk Chatbot", layout="centered")

# Title & Instruction
st.title("🎓 College Helpdesk Chatbot")
st.write("Ask me anything about college admissions, fees, deadlines, events, or departments!\nOfficial Website: https://www.college.in/")

# --- User Input ---
user_input = st.text_input("💬 Your Question Please:")

# --- FAQ Database ---
faq = {
    "admission deadline": "The admission deadline is July 31, 2025.",
    "hostel fees": "The hostel fees are ₹50,000 per semester including food and lodging.",
    "hod of cse": "Dr. Ramesh Verma is the Head of the Computer Science Department.",
    "placement record": "Our college has a 95% placement rate with top companies like Infosys, TCS, and Amazon.",
    "contact": "You can contact us at helpdesk@college.edu or call +91-9876543210.",
    "library timing": "The library is open from 8 AM to 8 PM on all working days.",
    "scholarship": "Yes, we offer various merit-based and need-based scholarships.",
    "canteen menu": "You can check the weekly canteen menu on the college website — https://www.college.in/.",
    "exam schedule": "The semester exam schedule will be uploaded by mid-November. For more details — https://www.college.in/",
    "departments": "Various departments include AIML, AI, IoT, IT, ECE, EC, Data Science, BioTech, etc. For full list, visit — https://www.college.in/",
    "college events": "We regularly host technical workshops, literary events, sports meets, and national-level seminars."
}

# --- Synonym Mapping ---
synonym_map = {
    "admission info": "admission deadline",
    "exam info": "exam schedule",
    "exam details": "exam schedule",
    "exam time": "exam schedule",
    "exam routine": "exam schedule",
    "hostel charges": "hostel fees",
    "placement stats": "placement record",
    "contact number": "contact",
    "library hours": "library timing",
    "departmental details": "departments"
}

# --- Clickable FAQs ---
st.subheader("📋 Click a question to get an instant answer:")

for question in faq:
    if st.button(f"❓ {question.capitalize()}"):
        st.write("🤖 Chatbot:", faq[question])

# --- Chatbot Logic ---
if user_input:
    user_query = user_input.lower()

    # Normalize with synonyms
    normalized_query = synonym_map.get(user_query, user_query)

    # Fuzzy match logic
    best_match = None
    best_score = 0
    for question in faq:
        score = fuzz.partial_ratio(normalized_query, question)
        if score > best_score:
            best_score = score
            best_match = question

    # Display answer or fallback
    if best_score >= 70:
        response = faq[best_match]
    else:
        response = "Sorry, I don't know the answer yet. Please try asking something else."

    st.write("🤖 Chatbot:", response)

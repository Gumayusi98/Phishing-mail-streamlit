import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 데이터
phishing_emails = [
    "Your account has been suspended click here to verify",
    "Urgent action required your bank account is locked",
    "Win a free iPhone now click this link",
    "Your password has expired reset it immediately",
    "Confirm your identity to avoid account suspension"
]

normal_emails = [
    "Let's meet at 3pm tomorrow",
    "Please review the attached document",
    "Lunch sounds good see you later",
    "Can you send me the report by today",
    "Happy birthday hope you have a great day"
]

texts = phishing_emails + normal_emails
labels = [1]*len(phishing_emails) + [0]*len(normal_emails)

# 모델 학습
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

# UI
st.title("📩 피싱 이메일 탐지기")

user_input = st.text_area("이메일 내용을 입력하세요")

if st.button("분석하기"):
    vec = vectorizer.transform([user_input])
    result = model.predict(vec)

    if result[0] == 1:
        st.error("⚠️ 피싱 이메일로 의심됩니다")
    else:
        st.success("✅ 정상 이메일입니다")

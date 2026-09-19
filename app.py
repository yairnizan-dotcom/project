import streamlit as st
import time

# --- כותרת ראשית של האפליקציה ---
st.title("🎬 CinePredict AI")
st.info("🤖 מערכת פשוטה לחיזוי רווחי סרטים לפי פופולריות")

# --- חלק הקלט מהמשתמש ---
st.header("📝 הזנת פרטי הסרט")

# תיבות קלט פשוטות וברורות
movie_name = st.text_input("שם הסרט:", placeholder="לדוגמה: אווטאר")
popularity = st.number_input("הכנס את מדד הפופולריות של הסרט (מ-1 עד 200):", min_value=1.0, max_value=200.0, value=50.0)

# --- כפתור הפעלה ---
predict_button = st.button("🚀 חזה רווח צפוי")

# --- תיבת התשובה (Answer Box) ---
if predict_button:
    if not movie_name:
        st.warning("⚠️ אנא הכנס את שם הסרט קודם לכן.")
    else:
        # אפקט טעינה קצר בשביל ההרגשה של ה-AI
        with st.spinner('מחשב את הרווח הצפוי...'):
            time.sleep(1)
        
        # חישוב מתמטי פשוט (לדוגמה: כל נקודת פופולריות שווה ל-5 מיליון דולר)
        estimated_revenue = popularity * 3300089.7859529243+11334117.004012793
        
        # יצירת תיבת תשובה מעוצבת ונקייה בעזרת st.success ו-st.metric
        st.success(f"📊 התחזית עבור הסרט: **{movie_name}** מוכנה!")
        
        # שימוש בתיבת מדד (Metric) שמשמשת כתיבת תשובה מצוינת ונקייה
        st.metric(label="💰 רווח משוער בקופות", value=f"${estimated_revenue:,.0f}")
        
        # פירוט קצר מתחת לתיבה
        st.write(f"לפי מודל החיזוי, סרט עם פופולריות של **{popularity}** צפוי להניב רווחים נאים בקולנוע.")

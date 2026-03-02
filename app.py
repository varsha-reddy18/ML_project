import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# ---------------- PAGE CONFIG ----------------
st.set_page_config("Fitness ML Dashboard", layout="wide")

# ---------------- LOAD CSS ----------------
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.markdown('<div class="app-title">🏋 Fitness Progress ML Dashboard</div>', unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
df = pd.read_csv("dataset.csv")

# ---------------- KPI CARDS ----------------
st.markdown('<div class="section-header">📊 Dataset Overview</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"<div class='card'><h3>Total Users</h3><h2>{df.shape[0]}</h2></div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<div class='card'><h3>Avg Calories</h3><h2>{df['daily_calories'].mean():.0f}</h2></div>", unsafe_allow_html=True)

with col3:
    st.markdown(f"<div class='card'><h3>Avg Weight Loss (kg)</h3><h2>{df['weight_loss_kg'].mean():.2f}</h2></div>", unsafe_allow_html=True)

# ---------------- DATA PREVIEW ----------------
st.markdown('<div class="section-header">🔎 Dataset Preview</div>', unsafe_allow_html=True)
st.dataframe(df.head(10))

# ---------------- CORRELATION HEATMAP ----------------
st.markdown('<div class="section-header">🔥 Correlation Heatmap</div>', unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(8,5))
sns.heatmap(df.corr(), annot=True, cmap="magma", ax=ax)
st.pyplot(fig)

# ---------------- FEATURE DISTRIBUTION ----------------
st.markdown('<div class="section-header">📈 Feature Distribution</div>', unsafe_allow_html=True)

feature = st.selectbox("Select Feature", df.columns)

fig, ax = plt.subplots()
sns.histplot(df[feature], kde=True, color="#ff5e62")
st.pyplot(fig)

# ---------------- SCATTER RELATIONSHIP ----------------
st.markdown('<div class="section-header">📊 Relationship With Weight Loss</div>', unsafe_allow_html=True)

x_feature = st.selectbox("Select X Feature", df.columns[:-1])

fig, ax = plt.subplots()
sns.scatterplot(x=df[x_feature], y=df["weight_loss_kg"], color="#ff9966")
plt.xlabel(x_feature)
plt.ylabel("Weight Loss (kg)")
st.pyplot(fig)

# ---------------- MODEL TRAINING ----------------
st.markdown('<div class="section-header">🤖 Model Training</div>', unsafe_allow_html=True)

X = df.drop("weight_loss_kg", axis=1)
y = df["weight_loss_kg"]

# 🔥 FIXED SCALER (Correct Way)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.25, random_state=42
)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# ---------------- MODEL PERFORMANCE ----------------
st.markdown('<div class="section-header">📊 Model Performance</div>', unsafe_allow_html=True)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

st.markdown(
    f"<div class='card'><h3>MSE: {mse:.3f}</h3><h3>R² Score: {r2:.3f}</h3></div>",
    unsafe_allow_html=True
)

# ---------------- FEATURE IMPORTANCE ----------------
st.markdown('<div class="section-header">⭐ Feature Importance</div>', unsafe_allow_html=True)

importance = pd.Series(model.feature_importances_, index=X.columns)
importance = importance.sort_values()

fig, ax = plt.subplots()
importance.plot(kind="barh", color="#ff5e62")
st.pyplot(fig)

# ---------------- PREDICTION PANEL ----------------
st.markdown('<div class="section-header">🚀 Predict Your Progress</div>', unsafe_allow_html=True)

daily_calories = st.slider("Daily Calories", 1500, 3000)
workout_hours = st.slider("Workout Hours", 0.0, 3.0)
protein_intake = st.slider("Protein Intake", 20, 150)
sleep_hours = st.slider("Sleep Hours", 4, 10)
water_intake = st.slider("Water Intake", 1.0, 5.0)
steps_per_day = st.slider("Steps Per Day", 2000, 15000)

if st.button("Predict"):

    input_data = [[daily_calories, workout_hours, protein_intake,
                   sleep_hours, water_intake, steps_per_day]]

    # ✅ Correct usage of SAME scaler
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]

    st.success(f"🔥 Predicted Weight Loss: {prediction:.2f} kg")
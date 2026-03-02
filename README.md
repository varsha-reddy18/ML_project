# Fitness Progress ML Dashboard
### Description:

This interactive ML dashboard helps users track fitness progress, analyze health and activity data, and predict weight loss. Users can explore their data, visualize trends, and get real-time predictions based on lifestyle inputs like calories, workout hours, and sleep.

### Features:

Dataset Overview – View total users, average calories, and average weight loss.

Dataset Preview – Preview the dataset records.

Correlation Heatmap – Visualize relationships between features.

Feature Distribution – Analyze distributions of individual features.

Scatter Plots – Check relationships of features with weight loss.

ML Model Training – Train Random Forest Regression model to predict weight loss.

Model Performance – View metrics like MSE and R² score.

Feature Importance – Identify features impacting weight loss the most.

Real-time Predictions – Predict weight loss using interactive sliders for lifestyle inputs.

### Project Structure:

ML_PROJECT/
|
|--- app.py          # Streamlit frontend & ML model
|--- style.css       # Custom dashboard styling
|--- dataset.csv     # Sample fitness dataset
|--- requirements.txt # Python dependencies
|--- README.md       # Project documentation

Quick Start

Prerequisites

Python 3.8 or higher

Git (optional, for cloning)

Streamlit (pip install streamlit)

1. Clone or Download the Project

Option 1: Clone with Git

git clone https://github.com/varsha-reddy18/ML_project.git
cd ML_PROJECT

Option 2: Download ZIP

Extract the ZIP to your desired folder.

2. Install Dependencies
pip install -r requirements.txt
3. Run the Streamlit Dashboard
streamlit run app.py

The app will open in your browser at http://localhost:8501.

How to Use

Frontend: Streamlit (Python web framework)

Machine Learning: Scikit-learn (Random Forest Regressor)

Data Visualization: Seaborn, Matplotlib

Language: Python 3.8+

Key Components

app.py – Full dashboard with ML model, data visualization, and prediction panel.

style.css – Colorful dashboard styling (dark gradient + modern UI).

dataset.csv – Fitness dataset containing features:

daily_calories

workout_hours

protein_intake

sleep_hours

water_intake

steps_per_day

weight_loss_kg (target)

Troubleshooting

Common Issues:

Module Not Found

Ensure all dependencies are installed: pip install -r requirements.txt

Run commands from the project directory.

Streamlit Not Launching

Make sure you are in the virtual environment.

Check Python version ≥ 3.8.

Future Enhancements

Add multiple ML models and compare performance.

Enable CSV upload for custom datasets.

Add user authentication.

Add predictive dashboards for nutrition and activity recommendations.

Deploy to Streamlit Cloud for public access.

Enable data export (CSV/PDF) of predictions and analytics.

Support

If you encounter any issues or have questions:

Phone: 7842285882

Email: varshareddy1808@gmail.com
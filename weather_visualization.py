import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# ------------------- Configuration -------------------
API_KEY = "9c733c9de07f567605d91f14b6619445"  # Replace with your OpenWeatherMap API key
CITY = "Nashik"  # Change to the desired city
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&units=metric&cnt=7&appid={API_KEY}"

# ------------------- Fetch Weather Data -------------------
response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
else:
    print(f"Error: {response.status_code}")
    exit()

# ------------------- Extract Data -------------------
dates = []
temperatures = []
humidity = []

for forecast in data["list"]:
    dates.append(forecast["dt_txt"])
    temperatures.append(forecast["main"]["temp"])
    humidity.append(forecast["main"]["humidity"])

# Create a Pandas DataFrame
df = pd.DataFrame({"Date": dates, "Temperature": temperatures, "Humidity": humidity})

# ------------------- Data Visualization -------------------
def plot_graphs():
    plt.figure(figsize=(10, 5))
    
    # Temperature Plot
    sns.lineplot(x="Date", y="Temperature", data=df, marker="o", label="Temperature (°C)", color="blue")
    plt.xticks(rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title(f"Temperature Trend for {CITY}")
    plt.legend()
    plt.show()

    # Humidity Plot
    plt.figure(figsize=(10, 5))
    sns.barplot(x="Date", y="Humidity", data=df, palette="Blues")
    plt.xticks(rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Humidity (%)")
    plt.title(f"Humidity Levels for {CITY}")
    plt.show()

# Run visualization
plot_graphs()

# ------------------- Streamlit Dashboard -------------------
st.title(f"Weather Data Visualization for {CITY}")

st.write("### 7-Day Temperature Forecast")
st.line_chart(df.set_index("Date")["Temperature"])

st.write("### 7-Day Humidity Levels")
st.bar_chart(df.set_index("Date")["Humidity"])
 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load Traffic Accident Data
# Replace 'traffic_accidents.csv' with your dataset file
# The CSV should have columns like 'Date', 'Time', 'Location', 'Weather', and 'Accidents'
try:
    df = pd.read_csv('Traffic_accidents.csv')
except FileNotFoundError:
    print("Sample data is being generated as 'tTraffic_accidents.csv' is not found.")
    # Generate synthetic data
    np.random.seed(42)
    df = pd.DataFrame({
        'Date': pd.date_range(start='2024-01-01', periods=100, freq='D'),
        'Time': np.random.choice(['Morning', 'Afternoon', 'Evening', 'Night'], 100),
        'Location': np.random.choice(['Intersection A', 'Intersection B', 'Intersection C'], 100),
        'Weather': np.random.choice(['Clear', 'Rainy', 'Foggy', 'Snowy'], 100),
        'Accidents': np.random.randint(1, 10, 100),
    })

# Preview the dataset
print(df.head())

# Group data for heatmap (Accidents by Time and Location)
heatmap_data = df.pivot_table(index='Location', columns='Time', values='Accidents', aggfunc='sum', fill_value=0)

# Create Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', fmt='d', cbar=True)
plt.title('Traffic Accidents Heatmap by Time and Location', fontsize=16)
plt.xlabel('Time of Day', fontsize=12)
plt.ylabel('Location', fontsize=12)
plt.tight_layout()
plt.show()

# Analyze accidents by weather conditions
weather_accidents = df.groupby('Weather')['Accidents'].sum()

# Plot bar chart for weather analysis
plt.figure(figsize=(8, 5))
sns.barplot(x=weather_accidents.index, y=weather_accidents.values, palette='muted')
plt.title('Total Accidents by Weather Condition', fontsize=16)
plt.xlabel('Weather Condition', fontsize=12)
plt.ylabel('Total Accidents', fontsize=12)
plt.tight_layout()
plt.show()

# Analyze overall trends: Accidents per day
daily_accidents = df.groupby('Date')['Accidents'].sum()

# Plot daily trend
plt.figure(figsize=(12, 6))
plt.plot(daily_accidents.index, daily_accidents.values, marker='o', linestyle='-', color='teal')
plt.title('Daily Traffic Accidents Trend', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Accidents', fontsize=12)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

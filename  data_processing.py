# Group data by season and calculate average count
season_data = train_data.groupby('season')['count'].mean()
print("Average bike rentals per season:")
print(season_data)

# Plot rentals by season
plt.figure(figsize=(8, 5))
sns.barplot(x=season_data.index, y=season_data.values)
plt.title("Average Bike Rentals by Season")
plt.xlabel("Season")
plt.ylabel("Average Count")
plt.show()

# Analyze bike rentals by weather condition
plt.figure(figsize=(8, 5))
sns.boxplot(x='weather', y='count', data=train_data)
plt.title("Bike Rentals by Weather Condition")
plt.xlabel("Weather")
plt.ylabel("Count")
plt.show()

# Analyze bike rentals by hour
plt.figure(figsize=(12, 6))
sns.lineplot(x='hour', y='count', data=train_data, ci=None)
plt.title("Bike Rentals by Hour")
plt.xlabel("Hour")
plt.ylabel("Count")
plt.show()

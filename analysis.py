import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#TASK 1

# Load dataset
df = pd.read_csv("Dataset .csv")

# Display basic info
print(df.head())
print(df.info())

# Split multiple cuisines
df['Cuisines'] = df['Cuisines'].astype(str)

all_cuisines = df['Cuisines'].str.split(', ').explode()

top_cuisines = all_cuisines.value_counts().head(3)

print("Top 3 Cuisines:")
print(top_cuisines)

# Percentage calculation
percentage = (top_cuisines / len(df)) * 100
print("\nPercentage of Restaurants Serving Top Cuisines:")
print(percentage)
#TASK 2

# City with highest number of restaurants
city_count = df['City'].value_counts()
print("City with highest restaurants:", city_count.idxmax())

# Average rating per city
city_avg_rating = df.groupby('City')['Aggregate rating'].mean()

print("\nAverage Rating per City:")
print(city_avg_rating)

# City with highest average rating
print("\nCity with highest average rating:", city_avg_rating.idxmax())

#TASK 3
# Distribution
price_counts = df['Price range'].value_counts()

plt.figure()
price_counts.plot(kind='bar')
plt.title("Price Range Distribution")
plt.xlabel("Price Range")
plt.ylabel("Count")
plt.show()

# Percentage
price_percentage = (price_counts / len(df)) * 100
print(price_percentage)

#TASK 4
# Percentage offering online delivery
online_delivery_percent = (df['Has Online delivery'].value_counts(normalize=True)) * 100
print(online_delivery_percent)

# Compare average ratings
delivery_rating = df.groupby('Has Online delivery')['Aggregate rating'].mean()
print(delivery_rating)



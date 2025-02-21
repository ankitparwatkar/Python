import csv

# Define the number of columns and rows
num_columns = 2500
num_rows = 15

# Create a list of column headers
headers = [f"Attribute{i}" for i in range(1, num_columns + 1)]

# Create sample data
data = []
for i in range(num_rows):
    row = [f"Value{i}_{j}" for j in range(1, num_columns + 1)]
    data.append(row)

# Add some hypothetical influencer names and categories
influencer_names = [f"Influencer{i}" for i in range(1, num_rows + 1)]
categories = ["Fashion", "Travel", "Food", "Fitness", "Technology", "Lifestyle", "Beauty", "Health"]

# Replace some of the values with relevant data
for i in range(num_rows):
    data[i][0] = influencer_names[i]  # Influencer name
    data[i][1] = str(5000000 + i * 100000)  # Followers
    data[i][2] = f"{7.0 + i * 0.5}%"  # Engagement rate
    data[i][3] = str(800 + i * 100)  # Posts
    data[i][4] = categories[i % len(categories)]  # Category

# Write data to CSV file
with open("Influencers.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)

print("CSV file created successfully.")

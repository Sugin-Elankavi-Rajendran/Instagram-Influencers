import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from path import location

# Load the dataset
df = pd.read_csv(location)

# Strip whitespace from the 'Channel Info' column
df['Channel Info'] = df['Channel Info'].str.strip()

# Save the cleaned DataFrame back to a CSV file
# df.to_csv('cleaned_file.csv', index=False)

def convert_shorthand(value):
    if isinstance(value, str):
        value = value.lower().replace(',', '')  # Normalize the string
        if value.endswith('k'):
            return float(value[:-1]) * 1_000
        elif value.endswith('m'):
            return float(value[:-1]) * 1_000_000
        elif value.endswith('b'):
            return float(value[:-1]) * 1_000_000_000
        else:
            try:
                return float(value)
            except ValueError:
                return None  # or handle the error as needed
    return value


df['Followers'] = df['Followers'].apply(convert_shorthand)
df['Avg. Likes'] = df['Avg. Likes'].apply(convert_shorthand)
df['Posts'] = df['Posts'].apply(convert_shorthand)
df['New Post Avg. Likes'] = df['New Post Avg. Likes'].apply(convert_shorthand)
df['Total Likes'] = df['Total Likes'].apply(convert_shorthand)

# df.to_csv('cleaned_numeric_file.csv', index=False)

#######################

# Select only numeric columns for correlation calculation
numeric_df = df.select_dtypes(include=['number'])

# Compute the correlation matrix
correlation_matrix = numeric_df.corr()

# Find the absolute values of the correlation matrix
abs_corr_matrix = correlation_matrix.abs()

# Find the pairs with the highest correlation
# Remove self-correlation (correlation of a feature with itself) by setting those to NaN
abs_corr_matrix = abs_corr_matrix.where(~abs_corr_matrix.eq(1))

# Find the index of the maximum value in the correlation matrix
max_corr = abs_corr_matrix.stack().idxmax()
max_corr_value = abs_corr_matrix.stack().max()

print(f"Most highly correlated pair: {max_corr}")
print(f"Correlation coefficient: {max_corr_value}")


# Plotting the scatter plot for the most highly correlated pair
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.scatterplot(x='Avg. Likes', y='New Post Avg. Likes', data=df)
plt.title('Scatter Plot of Avg. Likes vs. New Post Avg. Likes')
plt.xlabel('Avg. Likes')
plt.ylabel('New Post Avg. Likes')

# Plotting the heatmap of the correlation matrix
plt.subplot(1, 2, 2)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')

plt.tight_layout()
plt.show()

#########################

# Frequency distribution for Influence Score
plt.hist(numeric_df['Influence Score'], bins=20)
plt.title('Influence Score Distribution')
plt.show()

# Frequency distribution for Followers
plt.hist(numeric_df['Followers'], bins=20)
plt.title('Followers Distribution')
plt.show()

# Frequency distribution for Posts
plt.hist(numeric_df['Posts'], bins=20)
plt.title('Posts Distribution')
plt.show()

########################################

# Count of influencers per country
country_counts = df['Country Or Region'].value_counts()

# Plot the bar chart
country_counts.plot(kind='bar')
plt.title('Count of Instagram Influencers by Country')
plt.xlabel('Country')
plt.ylabel('Count')
plt.show()

##########################################

# Normalize the values
df['Followers_Norm'] = df['Followers'] / df['Followers'].max()
df['Avg_Likes_Norm'] = df['Avg. Likes'] / df['Avg. Likes'].max()
df['Total_Likes_Norm'] = df['Total Likes'] / df['Total Likes'].max()

# Create a combined score (simple average of the normalized features)
df['Combined_Score'] = (df['Followers_Norm'] + df['Avg_Likes_Norm'] + df['Total_Likes_Norm']) / 3

# Get the top 10 influencers based on the combined score
top_10_influencers = df.nlargest(10, 'Combined_Score')

# Display the top 10
print(top_10_influencers[['Channel Info', 'Followers', 'Avg. Likes', 'Total Likes', 'Combined_Score']])

##########################################

# Top 10 by Followers
top_followers = df.nlargest(10, 'Followers')

# Top 10 by Average Likes
top_avg_likes = df.nlargest(10, 'Avg. Likes')

# Top 10 by Total Likes
top_total_likes = df.nlargest(10, 'Total Likes')

print("Top 10 by Followers:\n", top_followers)
print("Top 10 by Average Likes:\n", top_avg_likes)
print("Top 10 by Total Likes:\n", top_total_likes)

##############################################

# Followers vs Total Likes
plt.scatter(df['Followers'], df['Total Likes'])
plt.title('Followers vs Total Likes')
plt.xlabel('Followers')
plt.ylabel('Total Likes')
plt.show()

# Followers vs Influence Score
plt.scatter(df['Followers'], df['Influence Score'])
plt.title('Followers vs Influence Score')
plt.xlabel('Followers')
plt.ylabel('Influence Score')
plt.show()

# Posts vs Avg. Likes
plt.scatter(df['Posts'], df['Avg. Likes'])
plt.title('Posts vs Avg. Likes')
plt.xlabel('Posts')
plt.ylabel('Avg. Likes')
plt.show()

# Posts vs Influence Score
plt.scatter(df['Posts'], df['Influence Score'])
plt.title('Posts vs Influence Score')
plt.xlabel('Posts')
plt.ylabel('Influence Score')
plt.show()

#########################################
import pandas as pd

# Load the dataset
df = pd.read_csv(r"F:/guvi/influencer.csv")

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

df.to_csv('cleaned_numeric_file.csv', index=False)

#######################

# Compute the correlation matrix
correlation_matrix = df.corr()

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

#########################

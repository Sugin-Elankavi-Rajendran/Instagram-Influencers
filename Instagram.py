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



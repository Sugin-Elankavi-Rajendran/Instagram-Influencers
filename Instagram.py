import pandas as pd

# Load the dataset
data = pd.read_csv(r"F:/guvi/influencer.csv")

# Function to convert shorthand notation to numeric
def convert_shorthand_to_numeric(value):
    if isinstance(value, str):
        if 'm' in value:
            return float(value.replace('m', '')) * 1e6
        elif 'k' in value:
            return float(value.replace('k', '')) * 1e3
        elif 'b' in value:
            return float(value.replace('b', '')) * 1e9
    return value

# Apply this function to relevant columns
data['Followers'] = data['Followers'].apply(convert_shorthand_to_numeric)
data['Avg. Likes'] = data['Avg. Likes'].apply(convert_shorthand_to_numeric)
data['Posts'] = data['Posts'].apply(convert_shorthand_to_numeric)
data['Total Likes'] = data['Total Likes'].apply(convert_shorthand_to_numeric)


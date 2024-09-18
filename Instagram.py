import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Streamlit title
st.title('Instagram Influencer Data Analysis')

# Upload the dataset
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the dataset
    df = pd.read_csv(uploaded_file)

    # Strip whitespace from the 'Channel Info' column
    df['Channel Info'] = df['Channel Info'].str.strip()

    # Conversion function
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
                    return None
        return value

    # Apply conversion
    df['Followers'] = df['Followers'].apply(convert_shorthand)
    df['Avg. Likes'] = df['Avg. Likes'].apply(convert_shorthand)
    df['Posts'] = df['Posts'].apply(convert_shorthand)
    df['New Post Avg. Likes'] = df['New Post Avg. Likes'].apply(convert_shorthand)
    df['Total Likes'] = df['Total Likes'].apply(convert_shorthand)

    # Show the first few rows of the dataset
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    #######################
    # Correlation Matrix
    st.subheader("Correlation Analysis")

    # Select only numeric columns for correlation calculation
    numeric_df = df.select_dtypes(include=['number'])

    # Compute the correlation matrix
    correlation_matrix = numeric_df.corr()

    # Display the correlation matrix as a heatmap
    st.write("Correlation Heatmap:")
    plt.figure(figsize=(10, 5))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    st.pyplot(plt)

    # Find the absolute values of the correlation matrix
    abs_corr_matrix = correlation_matrix.abs()

    # Remove self-correlation by setting those to NaN
    abs_corr_matrix = abs_corr_matrix.where(~abs_corr_matrix.eq(1))

    # Find the index of the maximum value in the correlation matrix
    max_corr = abs_corr_matrix.stack().idxmax()
    max_corr_value = abs_corr_matrix.stack().max()

    st.write(f"Most highly correlated pair: {max_corr}")
    st.write(f"Correlation coefficient: {max_corr_value}")

    #########################
    # Frequency distribution for various columns
    st.subheader("Frequency Distributions")

    # Influence Score Distribution
    st.write("Influence Score Distribution")
    plt.figure(figsize=(10, 5))
    sns.histplot(numeric_df['Influence Score'], bins=20, kde=True)
    plt.title('Influence Score Distribution with Density Curve')
    st.pyplot(plt)

    # Followers Distribution
    st.write("Followers Distribution")
    plt.figure(figsize=(10, 5))
    sns.histplot(numeric_df['Followers'], bins=20, kde=True)
    plt.title('Followers Distribution with Density Curve')
    st.pyplot(plt)

    # Posts Distribution
    st.write("Posts Distribution")
    plt.figure(figsize=(10, 5))
    sns.histplot(numeric_df['Posts'], bins=20, kde=True)
    plt.title('Posts Distribution with Density Curve')
    st.pyplot(plt)

    #########################
    # Count of influencers per country
    st.subheader("Count of Instagram Influencers by Country")
    country_counts = df['Country Or Region'].value_counts()

    # Display country counts as a bar chart
    st.bar_chart(country_counts)

    ##########################################
    # Normalize the values for Combined Score calculation
    df['Followers_Norm'] = df['Followers'] / df['Followers'].max()
    df['Avg_Likes_Norm'] = df['Avg. Likes'] / df['Avg. Likes'].max()
    df['Total_Likes_Norm'] = df['Total Likes'] / df['Total Likes'].max()

    # Create a combined score (simple average of the normalized features)
    df['Combined_Score'] = (df['Followers_Norm'] + df['Avg_Likes_Norm'] + df['Total_Likes_Norm']) / 3

    # Get the top 10 influencers based on the combined score
    st.subheader("Top 10 Influencers by Combined Score")
    top_10_influencers = df.nlargest(10, 'Combined_Score')
    st.dataframe(top_10_influencers[['Channel Info', 'Followers', 'Avg. Likes', 'Total Likes', 'Combined_Score']])

    ###########################
    # Top 10 by Followers, Avg. Likes, and Total Likes
    st.subheader("Top 10 Influencers by Followers, Avg. Likes, and Total Likes")

    top_followers = df.nlargest(10, 'Followers')
    top_avg_likes = df.nlargest(10, 'Avg. Likes')
    top_total_likes = df.nlargest(10, 'Total Likes')

    st.write("Top 10 by Followers:")
    st.dataframe(top_followers[['Channel Info', 'Followers']])

    st.write("Top 10 by Average Likes:")
    st.dataframe(top_avg_likes[['Channel Info', 'Avg. Likes']])

    st.write("Top 10 by Total Likes:")
    st.dataframe(top_total_likes[['Channel Info', 'Total Likes']])

    ##############################################
    # Feature Relationships
    st.subheader("Feature Relationships")

    # Followers vs Total Likes
    st.write("Followers vs Total Likes")
    plt.figure(figsize=(10, 5))
    sns.regplot(x='Followers', y='Total Likes', data=df, scatter_kws={'s':50}, line_kws={'color':'red'})
    plt.title('Followers vs Total Likes with Regression Line')
    st.pyplot(plt)

    # Followers vs Influence Score
    st.write("Followers vs Influence Score")
    plt.figure(figsize=(10, 5))
    sns.regplot(x='Followers', y='Influence Score', data=df, scatter_kws={'s':50}, line_kws={'color':'red'})
    plt.title('Followers vs Influence Score with Regression Line')
    st.pyplot(plt)

    # Posts vs Avg. Likes
    st.write("Posts vs Avg. Likes")
    plt.figure(figsize=(10, 5))
    sns.regplot(x='Posts', y='Avg. Likes', data=df, scatter_kws={'s':50}, line_kws={'color':'red'})
    plt.title('Posts vs Avg. Likes with Regression Line')
    st.pyplot(plt)

    # Posts vs Influence Score
    st.write("Posts vs Influence Score")
    plt.figure(figsize=(10, 5))
    sns.regplot(x='Posts', y='Influence Score', data=df, scatter_kws={'s':50}, line_kws={'color':'red'})
    plt.title('Posts vs Influence Score with Regression Line')
    st.pyplot(plt)

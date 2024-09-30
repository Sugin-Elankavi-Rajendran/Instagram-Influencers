# Instagram Influencer Data Analysis

This Streamlit app provides an in-depth analysis of Instagram influencer data. It offers interactive insights into various influencer metrics, including followers, likes, and posts, among other attributes. Users can upload a CSV file containing Instagram influencer data and view statistical summaries, correlations, visual distributions, and key rankings.

## Features

1. **Upload CSV File**:
   - Upload your dataset in CSV format, which contains Instagram influencer metrics.
   
2. **Data Preview**:
   - The app shows the first few rows of the uploaded dataset for a quick preview.

3. **Correlation Analysis**:
   - Displays the correlation matrix between numeric features in the dataset.
   - Shows a heatmap visualization of the correlation matrix.
   - Highlights the most highly correlated features.

4. **Frequency Distributions**:
   - Plots the distributions of various columns such as Influence Score, Followers, and Posts.
   - Each plot includes a density curve for better visualization of the data spread.

5. **Count of Influencers by Country**:
   - Provides a bar chart that shows the number of influencers from each country.

6. **Top Influencers Analysis**:
   - Computes a combined score based on normalized features (Followers, Average Likes, Total Likes).
   - Displays the top 10 influencers based on the combined score.
   - Also, lists the top 10 influencers by Followers, Average Likes, and Total Likes.

7. **Feature Relationships**:
   - Visualizes relationships between important features using scatter plots with regression lines.
   - Explores relationships such as:
     - Followers vs Total Likes
     - Followers vs Influence Score
     - Posts vs Average Likes
     - Posts vs Influence Score

## Getting Started

### Prerequisites

Make sure you have the following installed:
- Python 3.7 or above
- Streamlit
- Pandas
- Seaborn
- Matplotlib

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/instagram-influencer-analysis.git
    ```

2. Navigate to the project directory:

  ```
  cd instagram-influencer-analysis
  ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
    ```
4. Running the Application
   
To run the application, use the command:
    ```
    streamlit run app.py
    ```

Replace app.py with the name of your Python file.

### Usage

*   **Upload Data**: Click on the "Upload your CSV file" button and select your influencer dataset.
    
*   **Data Exploration**: View data previews, correlation analyses, frequency distributions, and more.
    
*   **Top Influencers**: Explore the top influencers by different metrics.
    
*   **Relationship Analysis**: View scatter plots and regression lines to understand relationships between features.
    

### Dataset Requirements

Your dataset should be in CSV format and should contain the following columns for optimal analysis:

*   Channel Info: Name or identifier of the influencer.
    
*   Country Or Region: Country of the influencer.
    
*   Followers: Number of followers.
    
*   Avg. Likes: Average number of likes on posts.
    
*   Posts: Number of posts.
    
*   Total Likes: Total number of likes.
    
*   Influence Score: An additional metric indicating influence.
    

The columns should contain numeric values or shorthand notation (e.g., '10k', '1M').

App Functionalities
-------------------

*   **Normalization & Combined Score**:
    
    *   The app normalizes the Followers, Avg. Likes, and Total Likes columns to create a Combined Score to rank influencers more holistically.
        
*   **Correlation & Heatmap**:
    
    *   Explore how different features correlate with each other using visual heatmaps.
        
*   **Interactive Charts**:
    
    *   Use Streamlit’s interactive features to explore the dataset, including heatmaps, bar charts, and scatter plots.

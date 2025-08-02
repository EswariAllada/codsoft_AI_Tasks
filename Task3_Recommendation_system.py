import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Sample user-item rating matrix
# Rows represent users, columns represent movies
# Values are the ratings given by users (0 means no rating)

data = {
    'Movie 1': [5, 3, 0, 1, 4],
    'Movie 2': [4, 0, 0, 1, 2],
    'Movie 3': [1, 1, 0, 5, 4],
    'Movie 4': [1, 0, 0, 4, 4],
    'Movie 5': [0, 1, 3, 4, 5]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data, index=['User 1', 'User 2', 'User 3', 'User 4', 'User 5'])

print("User-Item Rating Matrix:")
print(df)

# Calculate Cosine Similarity between users
user_similarity = cosine_similarity(df)

# Convert the similarity matrix into a DataFrame for easier visualization
user_similarity_df = pd.DataFrame(user_similarity, index=df.index, columns=df.index)

print("\nUser Similarity Matrix:")
print(user_similarity_df)

# Function to recommend movies based on user similarity
def recommend_movies(user_id, num_recommendations=2):
    # Get the similarity scores of the target user with other users
    similarity_scores = user_similarity_df[user_id]

    # Sort the users based on similarity (excluding the user itself)
    similar_users = similarity_scores.sort_values(ascending=False)[1:]

    recommended_movies = []
    for similar_user in similar_users.index:
        # Get the movies that the similar user liked but the target user hasn't rated
        movies_to_recommend = df.loc[similar_user][df.loc[user_id] == 0].index
        recommended_movies.extend(movies_to_recommend)

        # Stop once we have enough recommendations
        if len(recommended_movies) >= num_recommendations:
            break

    return recommended_movies[:num_recommendations]

# Example: Recommend movies for User 1
user_id = 'User 1'
print(f"\nRecommended Movies for {user_id}: {recommend_movies(user_id)}")
#output
#User-Item Rating Matrix:
#        Movie 1  Movie 2  Movie 3  Movie 4  Movie 5
#User 1        5        4        1        1        0
#User 2        3        0        1        0        1
#User 3        0        0        0        0        3
#User 4        1        1        5        4        4
#User 5        4        2        4        4        53

#User Similarity Matrix:
 #         User 1    User 2    User 3    User 4    User 5
#User 1  1.000000  0.735681  0.000000  0.357365  0.625638
#User 2  0.735681  1.000000  0.301511  0.471041  0.721569
#User 3  0.000000  0.301511  1.000000  0.520756  0.569803
#User 4  0.357365  0.471041  0.520756  1.000000  0.919857
#User 5  0.625638  0.721569  0.569803  0.919857  1.000000

#Recommended Movies for User 1: ['Movie 5', 'Movie 5']

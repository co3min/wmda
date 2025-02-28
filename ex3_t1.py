### **Exercise 3: Implementing a Simple Recommendation System**
import pandas as pd

url = "https://files.grouplens.org/datasets/movielens/ml-100k/u.data"
column_names = ["user_id", "movie_id", "rating", "timestamp"]
ratings = pd.read_csv(url, sep="\t", names=column_names, usecols=["user_id", "movie_id", "rating"])

url_movies = "https://files.grouplens.org/datasets/movielens/ml-100k/u.item"
movies = pd.read_csv(url_movies, sep="|", encoding="latin-1", names=["movie_id", "title"], usecols=[0, 1])

# Count how many ratings each user has given
user_counts = ratings["user_id"].value_counts()

# Keep only users who have given at least 10 ratings
valid_users = user_counts[user_counts >= 10].index

# Filter the dataset to keep only these users
filtered_ratings = ratings[ratings["user_id"].isin(valid_users)]

# Compute the average rating per movie 
average_ratings = filtered_ratings.groupby("movie_id")["rating"].mean()

# Compute the number of ratings per movie
ratings_counts = filtered_ratings.groupby("movie_id")["rating"].count()

# Combine into a single DataFrame
movie_stats = pd.DataFrame({"average_rating": average_ratings, "rating_count": ratings_counts})

# Sort movies by popularity first, then by average rating
sorted_movies = movie_stats.sort_values(by=["rating_count", "average_rating"], ascending=[False, False])

# Merge with movie titles
sorted_movies = sorted_movies.merge(movies, on="movie_id")

# Recommend the top 5 most popular movies for new users
top_5_movies = sorted_movies[["title", "rating_count", "average_rating"]].head(5)

# Display the result
print("Top 5 Recommended Movies for New Users:")
print(top_5_movies)
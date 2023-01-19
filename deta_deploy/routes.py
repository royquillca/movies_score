import pandas as pd
from pathlib import Path

file_path = Path("movies_scores.json")
movies = pd.read_json(file_path)


def get_word_count(platform, word):
    mask1 = movies['show_id'].str[0] == platform[0]
    mask2 = movies['title'].str.contains(word)
    count = movies[mask1&mask2].shape[0]
    return {
        'platform': platform,
        'word': word,
        'count': count
    }
# print(get_word_count('netflix','love'))


def get_score_count(platform, score, year):
    mask1 = movies['type'] == 'movie'
    mask2 = movies['show_id'].str[0] == platform[0]
    mask3 = movies['score'] > score
    mask4 = movies['release_year'] == year
    count = movies[mask1&mask2&mask3&mask4].shape[0]
    return {
        'platform': platform, 
        'score': score,
        'year': year,
        'count': count
    }
# print(get_score_count('netflix',85,2010))


def get_second_score(platform):
    mask1 = movies['type'] == 'movie'
    mask2 = movies['show_id'].str[0] == platform[0]
    result = movies[mask1&mask2].sort_values(by=['score', 'title'], ascending=[False, True]).iloc[1]
    type = result.type
    score = result.score
    title = result.title
    return {
        'platform': platform,
        'type': type,
        'score': int(score),
        'title': title
    }
# print(get_second_score('amazon'))


def get_longest(platform,duration_type,year):
    mask1 = movies['show_id'].str[0] == platform[0]
    mask2 = movies['duration_type'] == duration_type
    mask3 = movies['release_year'] == year
    mask4 = movies['type'] == 'movie'
    result = movies[mask1&mask2&mask3&mask4].sort_values(by='duration_int', ascending=False).iloc[0]
    return {
        'title': result.title,
        'platform': platform,
        'duration_type': duration_type,
        'duration_int': int(result.duration_int),
        'year': year,
    }
# print(get_longest('netflix','min',2016))

def get_rating_count(rating):
    mask1 = movies['rating'] == rating
    mask2 = movies['type'] == 'min'
    mask3 = movies['type'] == 'season'
    total_movies_per_rating = movies[mask1].shape[0]
    movies_per_rating = movies[mask1&mask2].shape[0]
    series_per_rating = movies[mask1&mask3].shape[0]
    return {
        'rating': rating,
        'total_movies_per_rating': total_movies_per_rating,
        'movies_per_rating': movies_per_rating,
        'series_per_rating': series_per_rating
    }
# print(get_rating_count('18+'))
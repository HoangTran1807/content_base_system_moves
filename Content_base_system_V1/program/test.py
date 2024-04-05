import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import random

# Đọc dữ liệu từ CSV
movies = pd.read_csv('./Content_base_system_V1/program/tmdb_5000_movies.csv')
# Tạo một vectorizer TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
# Đảm bảo rằng các trường 'overview', 'genres', và 'keywords' không chứa giá trị null
movies['overview'] = movies['overview'].fillna('')
movies['genres'] = movies['genres'].fillna('')
movies['keywords'] = movies['keywords'].fillna('')
# Kết hợp các trường 'overview', 'genres', và 'keywords' thành một chuỗi duy nhất
movies['content'] = movies['overview'] + movies['genres'] + movies['keywords']
# Xây dựng ma trận TF-IDF
tfidf_matrix = tfidf.fit_transform(movies['content'].dropna())
#print('tf-idf matrix: \n',tfidf_matrix[0:5])
# Tính toán độ tương tự cosine
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix) 
print('cosine matrix: \n', cosine_sim.shape)
# Tạo một bản đồ từ tiêu đề phim đến chỉ mục
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()


# Hàm trả về 10 phim tương tự nhất
def get_recommendations(titles, cosine_sim=cosine_sim):
    movie_indices = []

    for title in titles:
        # Lấy chỉ mục của phim từ tiêu đề
        idx = indices[title]

        # Lấy điểm tương tự của tất cả các phim với phim này
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sắp xếp các phim dựa trên điểm tương tự
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Lấy điểm của 10 phim tương tự nhất
        sim_scores = sim_scores[1:11]

        # Lấy chỉ mục phim
        movie_indices.extend([i[0] for i in sim_scores])

    # Trả về 10 phim tương tự nhất cho mỗi tiêu đề phim
    recommended_movies = movies['title'].iloc[movie_indices]
    unique_movies = list(set(recommended_movies))

    # Return 10 random unique movies
    if len(unique_movies) > 10:
        return random.sample(unique_movies, 10)
    else:
        return unique_movies


print(get_recommendations({'Avengers: Age of Ultron', 'The Avengers', 'Iron Man 2', 'Iron Man'}))

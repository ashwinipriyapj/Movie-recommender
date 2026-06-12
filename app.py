from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

movies = pickle.load(open('model.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    idx = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[idx])),
        reverse=True,
        key=lambda x: x[1]
    )
    recommended = []
    for i in distances[1:6]:
        recommended.append(movies.iloc[i[0]].title)
    return recommended

@app.route('/')
def index():
    movie_list = movies['title'].values
    return render_template('index.html', movies=movie_list)

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    selected = request.form.get('movie')
    recommendations = recommend(selected)
    return render_template('index.html',
                           movies=movies['title'].values,
                           recommendations=recommendations,
                           selected=selected)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
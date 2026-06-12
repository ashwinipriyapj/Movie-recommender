# Movie Recommender

A content-based movie recommendation system built with Flask, Pandas, and Scikit-learn.

## How to run locally
pip install -r requirements.txt
python app.py
Visit http://127.0.0.1:5000

## How to run with Docker
docker build -t movie-recommender .
docker run -p 5000:5000 movie-recommender
Visit http://localhost:5000
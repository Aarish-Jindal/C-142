from flask import Flask, jsonify, request, csv
import csv
all_movies = []
with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
liked_movies = []
disliked_movies = []
not_watched_movies = []

app = Flask(__name__)
@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data":all_movies[0],
        "status":"success"
    })

@app.route("/liked-movie", methods = ["POST"])
def liked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(all_movies[0])
    return jsonify({
        "status": "success"

    }),201

@app.route("/disliked-movie", methods = ["POST"])
def disliked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    disliked_movies.append(all_movies[0])
    return jsonify({
        "status": "success"

    }),201

@app.route("/did-not-watch-movie", methods = ["POST"])
def didnotwatch():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(all_movies[0])
    return jsonify({
        "status": "success"

    }),201
if __name__  ==  "__main__":
    app.run()

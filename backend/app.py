from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId
import os

app = Flask(__name__)
app.config["MONGO_URI"] = f"mongodb://{os.environ.get('MONGO_HOST', 'localhost')}:27017/blogdb"
mongo = PyMongo(app)

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = mongo.db.posts.find()
    return jsonify([{**post, '_id': str(post['_id'])} for post in posts])

@app.route('/posts', methods=['POST'])
def add_post():
    post = request.json
    post_id = mongo.db.posts.insert_one(post).inserted_id
    return jsonify({'_id': str(post_id)}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
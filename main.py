from flask import Flask, jsonify, request
from models import db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    post = Post(title=data['title'], content=data['content'], user_id=data['user_id'])
    db.session.add(post)
    db.session.commit()
    return jsonify({'message': 'Post created!', 'post': {'id': post.id}}), 201

@app.route('/posts/<int:post_id>', methods=['GET'])
def read_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify({'title': post.title, 'content': post.content, 'user_id': post.user_id})

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.json
    post = Post.query.get_or_404(post_id)
    post.title = data['title']
    post.content = data['content']
    db.session.commit()
    return jsonify({'message': 'Post updated!'})

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted!'})

if __name__ == '__main__':
    app.run(debug=True)

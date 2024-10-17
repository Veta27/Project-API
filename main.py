from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Временные хранилища для пользователей и постов
users = {}
posts = {}
post_id_counter = 1

# Создать пользователя (если потребуется, для упрощения, не реализовано в данном примере)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = data.get('id')
    if user_id in users:
        return jsonify({'error': 'User already exists'}), 400
    users[user_id] = data
    return jsonify(data), 201

# Создать пост
@app.route('/posts', methods=['POST'])
def create_post():
    global post_id_counter
    data = request.json
    post = {
        'id': post_id_counter,
        'user_id': data['user_id'],
        'content': data['content']
    }
    posts[post_id_counter] = post
    post_id_counter += 1
    return jsonify(post), 201

# Получить пост
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = posts.get(post_id)
    if post is None:
        abort(404)
    return jsonify(post)

# Изменить пост
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = posts.get(post_id)
    if post is None:
        abort(404)
    data = request.json
    post['content'] = data['content']
    return jsonify(post)

# Удалить пост
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = posts.pop(post_id, None)
    if post is None:
        abort(404)
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)

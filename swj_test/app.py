from email import message_from_string
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/memo_2', methods=['POST'])
def write_memo():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']

    doc = {
        'title': title_receive,
        'content': content_receive
    }

    db.memo_ver2.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})


@app.route('/memo_2', methods=['GET'])
def read_memo():
    memos = list(db.memo_ver2.find({}, {'_id': False}))
    return jsonify({'all_memo': memos})


@app.route('/memo_2', methods=['POST'])
def delete_memo():
    title2_receive = request.form['title_give']
    db.memo_ver2.delete_one({'title': title2_receive})
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
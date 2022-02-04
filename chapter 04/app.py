import requests
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/mypage')
# def mypage():
#    return 'This is My Page!'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


# get요청 API 코드

# @app.route('/test', methods=['GET'])
# def test_get():
#     title_receive = request.args.get('title_give')
#     print(title_receive)
#     return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})


# post요청 API 코드

# @app.route('/test', methods=['POST'])
# def test_post():
#    title_receive = request.form['title_give']
#    print(title_receive)
#    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

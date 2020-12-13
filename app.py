from flask import Flask, render_template, request
import json

app = Flask(__name__)


# Ajax的post方法
@app.route('/ajax', methods=['GET'])
def ajax():
    return render_template("js_demo.html")


# Ajax的post方法
@app.route('/ajax/post', methods=['POST'])
def js_post():
    # arguments
    name = request.values['name']
    url = request.values['url']
    print(name + "====" + url)
    condition = {"name": name, "url": url}
    data = {"data": str(condition), "status": "success"}
    return data


# Ajax的GET方法
@app.route('/ajax/get', methods=['GET'])
def js_get():
    # arguments
    condition = request.args.get('name')
    print(condition)
    data = {"data": str(condition), "status": "success"}
    return data


@app.route('/search/')
def search():
    # arguments
    condition = request.args.get('q')
    return '用户提交的查询参数是: {}'.format(condition)


# 默认的试图函数， 只能采用get请求
# 如果你想采用post请求，那么要写明
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':

        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print('username: {}, password: {}'.format(username, password))
        return 'name = {}, password = {}'.format(username, password)


# 动态路由
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# 首页
@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

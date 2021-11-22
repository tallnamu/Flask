# from flask import Flask
# from flask import render_template
# from flask import redirect
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello,World!'
#
#
# @app.route('/test1')
# def test1():
#     return 'test1'
#
#
# @app.route('/test2', methods=['get', 'post'])
# def test2():
#     return 'test2'
#
#
# @app.route('/test3/<tid>')
# def test3(tid):
#     return 'tid is %s' % tid
#
#
# @app.route('/test4')
# @app.route('/test4/<int:tid>')
# def test4(tid=None):
#     return 'test4 tid is %s' % tid
#
#
# @app.route('/template')
# def template():
#     return render_template('template.html')
#
#
# @app.route('/template_with_param')
# def template_with_param():
#     user = 'GGoReb';
#     return render_template(
#         'template_with_param.html', name=user
#     )
#
#
# @app.route("/locals")
# def local():
#     users = ['Flank', 'Steve', 'Alice', 'Bruce']
#     age = 20
#     address_dict = {'a': '서울', 'b': '대전', 'c': '제주'}
#     return render_template('locals.html', **locals())
#
#
# @app.route('/first')
# def first():
#     return render_template('first.html')
#
#
# @app.route('/second')
# def second():
#     return render_template('second.html')
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
#
# app.route("/redirect_url")
#
#
# def redirect_url():
# #     return redirect('/')

from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


@app.route('/')
def student():
    return render_template('info.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)


db = pymysql.connect(host="localhost", user="root", passwd="1234", db="free_board", charset="utf8")
cur = db.cursor()
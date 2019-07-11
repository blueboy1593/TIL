from flask import Flask, render_template, request # 사용자의 요청을 확인할 수 있음.
import requests
app = Flask(__name__)

@app.route('/') # / => root
def index():
    return '반갑습니다'


@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('greeting.html', newname=name)    #어제 했는데 기억이 안나냐 ㅋㅋㅋ


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    age = request.args.get('age')   #age의 변수를 대답받는 내용.
    return f'Pong! age: {age}'
    #render_template('pong.html')


@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/naver')
def naver():
    return render_template('naver.html')


@app.route('/ascii_input')
def ascii_input():  # 사용자가 입력할 수 있는 페이지를 만들겠다는 것.
    return render_template('ascii_input.html')


@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text')
    # Ascii Art API를 활용해서 사용자의 input 값을 변경한다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    result = response.text
    return render_template('ascii_result.html', result=result)



if __name__ == '__main__': 
    app.run(debug=True)

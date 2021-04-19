from flask import Flask , render_template


app = Flask(__name__)

app.debug = True # 개발할때만 True 고 평소엔 False 해킹위험

@app.route('/data', methods=['GET']) # 데코, 기본 경로는 안써도 되고 그 뒤에 연결
# GET쓸땐 methods 생략 가능
def index(): # 함수로 처리
    # return "Hello World!"
    return render_template("index.html", data="Kim") # html 문서로 바꿔줌, html 언어로 바꿔줌 
    #ex) {data} 같은거 html 아니니까 data로 출력 -> 이런 능력 진자2엔진, flask에 기본으로 있음
    #진자2엔진 사용법 중괄호 열고 닫고
# 첫번재 인자로 html파일 경로, 두번째 인자로 전달할 데이터

@app.route('/about')
def about():
    return render_template("about.html", hello="Gary kim")

@app.route('/articles')
def articles():
    return render_template("articles.html", hello="Gary kim")


if __name__ == '__main__': # 위에 다른 코드가 있어도 가장 먼저
    app.run()
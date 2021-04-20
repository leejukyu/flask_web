from flask import Flask , render_template , request, redirect
from data import Articles
import pymysql

app = Flask(__name__)

app.debug = True # 개발할때만 True 고 평소엔 False 해킹위험

db = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '1234',
    db = 'busan'
)


@app.route('/', methods=['GET']) # 데코, 기본 경로는 안써도 되고 그 뒤에 연결
# GET쓸땐 methods 생략 가능
def index(): # 함수로 처리
    cursor = db.cursor()

    # return "Hello World!"
    return render_template("index.html", data="Kim") # html 문서로 바꿔줌, html 언어로 바꿔줌 
    #ex) {data} 같은거 html 아니니까 data로 출력 -> 이런 능력 진자2엔진, flask에 기본으로 있음
    #진자2엔진 사용법 중괄호 열고 닫고
# 첫번재 인자로 html파일 경로, 두번째 인자로 전달할 데이터

@app.route('/about')
def about():
    cursor = db.cursor()

    return render_template("about.html", hello="Gary kim")

@app.route('/articles')
def articles():
    cursor = db.cursor()

    sql = 'SELECT * FROM topic;'
    cursor.execute(sql)
    topics = cursor.fetchall()
    print(topics)
    # articles = Articles() # data.py 의 articles함수 받아오기
    # print(articles[0]['title'])
    return render_template("articles.html", articles = topics) # articles 함수 실행

@app.route('/article/<int:id>') # params <변수명> 
def article(id):
    cursor = db.cursor()

    sql = 'SELECT * FROM topic WHERE id={}'.format(id)
    cursor.execute(sql)
    topic = cursor.fetchone()
    print(topic)
    # articles = Articles()
    # article = articles[id-1]
    # print(articles[id-1])
    return render_template("article.html", article = topic)

@app.route('/add_articles', methods=["GET", "POST"])
def add_articles():
    cursor = db.cursor()

    if request.method == "POST":
        author = request.form['author']
        title = request.form['title']
        desc = request.form['desc']
        sql = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
        input_data = [title,desc,author] # sql 과 순서대로
        cursor.execute(sql, input_data)
        db.commit()
        print(cursor.rowcount)
        # db.close()

        return redirect("/articles")
    # return "<h1>글쓰기페이지</h1>"
    else:
        return render_template("add_articles.html")

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cursor = db.cursor()
    sql = 'DELETE FROM topic WHERE id = %s;'
    # 위에랑 같은거 sql = 'DELETE FROM topic WHERE id = {};'.format(id)

    id = [id]
    cursor.execute(sql, id)
    db.commit()

    return redirect("/articles")



if __name__ == '__main__': # 위에 다른 코드가 있어도 가장 먼저
    app.run()


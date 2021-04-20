import pymysql
# 다르게 쓰면 틀림
db = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '1234',
    db = 'busan'
)

sql = '''
CREATE TABLE `topic` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`title` varchar(100) NOT NULL,
	`body` text NOT NULL,
	`author` varchar(30) NOT NULL,
    `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
	) ENGINE=innoDB DEFAULT CHARSET=utf8;
'''
cursor = db.cursor() # 커리문을 날리는 준비

# cursor.execute(sql)
sql_1 = "INSERT INTO `busan`.`topic` (`title`, `body`, `author`) VALUES ('부산', '부산와서 갈매기를 못봣네', '김태경');"
# # sql_2 = "INSERT INTO `busan`.`users` (`name`, `email`, `username`, `password`) VALUES ('LEE', 'dlwr777@gmail.com', '주경', '12345');"

sql_3 = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
# title = input('제목을 적으세요')
# body = input("내용을 적으세요")
# author = input("누구세요?")
# input_data = [title,body,author ]
# cursor.execute(sql_3,input_data)
# db.commit()
# db.close()

cursor.execute('SELECT * FROM topic;')
# # cursor.execute(sql_2)
# # cursor.execute('SELECT * FROM users;') # excute 커리문 날리기 메소드, 인자값으로 커리문
users = cursor.fetchall() # fetchall 조회한걸 가져오는 걸 return, user로 받기
print(cursor.rowcount,users)

#숙제(sql_2)
# users
#   username : 내 성 (영어로)
#   mail : 내 메일
#   name : 내 이름 (한글로)
#   password:12345
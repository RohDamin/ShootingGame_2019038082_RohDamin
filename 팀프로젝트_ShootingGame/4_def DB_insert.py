# def DB_insert 작성자: 노다민

############ 데이터베이스 관련 ############
con, cur = None, None
data1, data2, data3 = "", "", ""
sql = ""
con = sqlite3.connect("RANKING_CHART")
cur = con.cursor()
# cur.execute("CREATE TABLE scoreTable (id char(4), score INT)") #데이터베이스 파일 생성

def DB_insert(id, score):
    DB_id = id
    DB_score = score
    sql = "INSERT INTO scoreTable VALUES('" + DB_id + "','" + DB_score + "')"
    cur.execute(sql)
    con.commit()
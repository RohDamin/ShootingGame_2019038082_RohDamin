# def DB_check 작성자: 노다민
def DB_check():
    cur.execute("SELECT id, score FROM scoreTable ORDER BY CAST (score AS INTEGER) DESC")
    con.commit()
    draw_text(screen, "Player ID", 35, WIDTH / 2 - 80, 140, BLACK)
    draw_text(screen, "SCORE", 35, WIDTH / 2 + 160, 140, BLACK)
    for i in range(10):
        row = cur.fetchone()
        if row == None:
            break
        DB_id = row[0]
        DB_score = row[1]
        draw_text(screen, str(i + 1), 30, WIDTH / 2 - 230, 200 + i * 35, BLACK)
        draw_text(screen, str(DB_id), 30, WIDTH / 2 - 80, 200 + i * 35, BLACK)
        draw_text(screen, str(DB_score), 30, WIDTH / 2 + 160, 200 + i * 35, BLACK)
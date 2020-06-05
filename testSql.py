# import sqlite3
#
# con, cur = None, None
# data1, data2, data3 = "","",""
# sql = ""
#
# con = sqlite3.connect("C:\\Users\\DaMin\\PycharmProjects\\untitled28_myGame\\testSql.py")
# cur = con.cursor()
#
# while(True):
#     data1 = input("사용자 ID: ")
#     if data1 == "":
#         break;
#     data2 = ("사용자 이름: ")
#     data3 = ("출생년도: ")
#
#     sql = "INSERT INTO testSql.py VALUES('"+data1+"','"+data2+"','"+data3+"')"
#     cur.execute(sql)
#
# con.commit()
# con.close()

import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600, 700))


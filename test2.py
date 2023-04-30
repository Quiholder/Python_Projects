import sqlite3


#create table in database if it does not exist 
conn=sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons(ID INTEGER PRIMARY KEY AUTOINCREMENT, col_fname TEXT)")
    conn.commit()
conn.close()

conn=sqlite3.connect('test.db')

fileList= ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf','myPhoto.jpg')
for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur=conn.cursor()
            cur.execute("INSERT INTO tbl_persons (col_fname) VALUES(?)", (x,))
            print(x)

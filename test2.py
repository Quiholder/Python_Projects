import sqlite3
import os 
fileList=('information.docx', 'Hello.txt', 'myImage/png' \
          'myMovie.mpg', 'World.txt','data.pdf', 'myPhoto.jpg')

#bsolute file path 
fileName='Hello.txt', 'World.txt'
fpath=C:\A\Hello.txt

#concatenate fileName and file path 
abpath=os.path.join(fpath,fileName)
print (abpath)

#create table in database if it does not exist 
conn=sqlite3.connect('test.db')
with conn:
    cur= conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_persons( \
     ID INTERGER PRIMARY KEY AUTOINCREMENT, \
     col.fname TEXT, \
     col.lname TEXT, \
     col.email TEXT \
     )')
    conn.commit()
conn.close()

conn=sqlite3.connect('test.db')

#insert data into the table 
with conn:
    cur= conn.cursor()
    cur.execute('INSERT INTO tbl_persons (col_fname, col_lname, col_email) VALUES (?,?,?)',\
                ('tiffany','holmes','tiff@gmail.com'))
    cur.execute('INSERT INTO tbl_persons (col_fname, col_lname, col_email) VALUES (?,?,?)',\
                ('jake','statefarm','jake@gmail.com'))
    cur.execute('INSERT INTO tbl_persons (col_fname, col_lname, col_email) VALUES (?,?,?)',\
                ('ashley','williams','ash@gmail.com'))
    cur.execute('INSERT INTO tbl_persons (col_fname, col_lname, col_email) VALUES (?,?,?)',\
                ('anthony','blue','blueant@gmail.com'))
        conn.commit()
conn.close()        

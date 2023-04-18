import sqlite3


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

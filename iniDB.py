import sqlite3

conn = sqlite3.connect('test.db')
print "Open DB successfully"
c = conn.cursor()


c.execute('''DROP TABLE board;''')
c.execute('''DROP TABLE post;''')
c.execute('''DROP TABLE user;''')


c.execute('''CREATE TABLE user
        (UID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name text NOT NULL UNIQUE,
        Email text not null,
        Password text not null);''')

c.execute('''CREATE TABLE post
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title text NOT NULL,
        Author text not null,
        Date text not null,
        Content text not null,
        Board text not null,
        Comment text);''')

c.execute('''CREATE TABLE board
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name text NOT NULL,
        Moderator text not null);''')

#for i in range(1000000):
#    username = "user"+ str(i)
#    cursor = c.execute('Insert INTO user("Name","Email","Password")VALUES(?,?,?);',(username,username,username))

print "Table create"
conn.commit()
conn.close()

import re
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
c = 0
for line in fh:
    email = re.findall('^From: \S+@(\S+)', line)
    if len(email) is 0:
        continue
    email = email[0]
    print(email)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))
    row = cur.fetchall()
    if len(row) is 0:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (email,))
    c = c+1
conn.commit()
print(c)

cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10')
rows = cur.fetchall()
for row in rows:
    print(row)


cur.close()

# This file will output a summary report of the company.
# any updates to the database will reflect after you run the file.
# All you have to do is run the file after you have created the database.

import sqlite3

# Return the summary report of the company.
# The report includes:
# 1. A total number of musicians and a list of musicians.
# 2. A total number of albums and a list of albums recorded at Notown.
# 3. A total number of instruments and a list of instruments at Notown.
# 4. A table consists of the name of musicians and the total
#    number of albums written by them.


con = sqlite3.connect('NewtonDB.db')
cur = con.cursor()


print('------------------------------------')
musician_count = cur.execute("SELECT COUNT(*) FROM musicians")
count = musician_count.fetchone()
print('Total number of musicians: ', count)


print('List of musicians:')
cur.execute("SELECT name FROM musicians")
results = cur.fetchall()
for row in results:
    print(row)

print('------------------------------------')
album_count = cur.execute("SELECT COUNT(*) FROM albums")
count = musician_count.fetchone()
print("Total Number of albums", count)

print('List of albums:')
print('album id, title')
cur.execute("SELECT album_id, title FROM albums")
results = cur.fetchall()
for row in results:
    print(row)


print('------------------------------------')
album_count = cur.execute("SELECT COUNT(*) FROM instruments")
count = musician_count.fetchone()
print("Total Number of instruments", count)

print('List of instruments:')
print('instrument id, name')
cur.execute("SELECT in_id, name FROM instruments")
results = cur.fetchall()
for row in results:
    print(row)


print('------------------------------------')
print('Musicians and how many albums they have created:')
cur.execute('''
    SELECT musicians.name, COUNT(musicians_albums.album_id) AS total_albums
    FROM musicians 
    JOIN musicians_albums 
    ON musicians.ssn = musicians_albums.ssn
    GROUP BY musicians.name
''')
results = cur.fetchall()
for row in results:
    print(row)

con.commit()
con.close()

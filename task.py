import sqlite3
import csv

#Create a database
con = sqlite3.connect('NewtonDB.db')

# pointer used to execute SQL and fetch data
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS musicians")
cur.execute("DROP TABLE IF EXISTS instruments")
cur.execute("DROP TABLE IF EXISTS albums")
cur.execute("DROP TABLE IF EXISTS musicians_albums")
cur.execute("DROP TABLE IF EXISTS instruments_albums")

# Create tables
musicians = '''
    CREATE TABLE musicians (
    name text,
    ssn  text,
    PRIMARY KEY(ssn)
);
'''

instruments = '''
    CREATE TABLE instruments(
    in_id text,
    name text,
    musical_key text,
    PRIMARY KEY(in_id)
    );
'''

albums = '''
    CREATE TABLE albums (
    title text,
    album_id text,
    copyright_date text,
    format text,
    PRIMARY KEY (album_id)
    );
'''

musicians_albums = '''
    CREATE TABLE musicians_albums(
        ssn text,
        album_id text,
        
        PRIMARY KEY(ssn, album_id),
        FOREIGN KEY(ssn)
            REFERENCES musicians(ssn),
        FOREIGN KEY (album_id)
            REFERENCES album(album_id)
    );
'''

instruments_albums = '''
    CREATE TABLE instruments_albums(
        album_id text,
        in_id text,
        PRIMARY KEY (album_id, in_id),
        FOREIGN KEY(album_id)
            REFERENCES albums,
        FOREIGN KEY (in_id)
            REFERENCES instruments
    );
'''

cur.execute(musicians)
cur.execute(albums)
cur.execute(instruments)
cur.execute(musicians_albums)
cur.execute(instruments_albums)


# Check if tables were created
def get_all_tables(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())


get_all_tables(cur)

# Extract data from csv files and insert into tables
with open('musician.csv', 'r') as R:
    reader = csv.reader(R)
    next(reader, None)
    for row in reader:
        cur.execute("INSERT INTO musicians (name, ssn) VALUES (?, ?)", (row[0], row[1]))

with open('album.csv', 'r') as A:
    reader = csv.reader(A)
    next(reader, None)
    for row in reader:
        cur.execute("INSERT INTO albums (title, album_id, copyright_date, format) VALUES (?, ?, ?, ?)", (row[0], row[1], row[2], row[3]))

with open('instrument.csv', 'r') as X:
    reader = csv.reader(X)
    next(reader, None)
    for row in reader:
        cur.execute("INSERT INTO instruments (in_id, name, musical_key) VALUES (?, ?, ?)", (row[0], row[1], row[2]))

with open('musician-album.csv', 'r') as R:
    reader = csv.reader(R)
    next(reader, None)
    for row in reader:
        cur.execute("INSERT INTO musicians_albums (ssn, album_id ) VALUES (?, ?)", (row[0], row[1]))

with open('album-instrument.csv', 'r') as B:
    reader = csv.reader(B)
    next(reader, None)
    for row in reader:
        cur.execute("INSERT INTO instruments_albums (album_id, in_id) VALUES (?, ?)", (row[0], row[1]))

# Check it items were inserted
# cur.execute("SELECT * FROM musicians")
# results = cur.fetchall()
# for row in results:
#  print(row)

# cur.execute("SELECT * FROM musicians_albums")
# results = cur.fetchall()
# for row in results:
#  print(row)

con.commit()
con.close()


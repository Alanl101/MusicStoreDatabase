import argparse
import sqlite3

table_structures = {
    'musicians': ('name', 'ssn'),
    'album': ('title', 'album_id', 'copyright_date', 'format'),
    'instruments': ('in_id', 'name', 'musical_key'),
    'musicians_albums': ('ssn', 'album_id'),
    'instruments_albums': ('album_id', 'in_id'),
}


parser = argparse.ArgumentParser(description='Update the database.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--add', action='store_true', help='Add a record to the database')
group.add_argument('--delete', action='store_true', help='Delete a record from the database')
parser.add_argument('--table', required=True, type=str, choices=table_structures.keys(), help='Table to modify')
parser.add_argument('--record', required=True, type=str, help='The record to add or delete as a comma(,) separated string')
args = parser.parse_args()

# Connect to the database
con = sqlite3.connect('NewtonDB.db')
cur = con.cursor()

# Parse the record argument into a tuple
record = tuple(args.record.split(','))

if args.add:
    # If adding a record, use the table structure to format the SQL statement
    columns = ', '.join(table_structures[args.table])
    placeholders = ', '.join('?' * len(record))
    try:
        cur.execute(f"INSERT INTO {args.table} ({columns}) VALUES ({placeholders})", record)
        print(f"Record {args.record} added to table {args.table}.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

elif args.delete:
    # If deleting a record, use the first item in the record as a unique identifier
    # Adjust this to match your actual table structure
    try:
        cur.execute(f"DELETE FROM {args.table} WHERE ssn = ?", (record[0],))
        print(f"Record with ssn {record[0]} deleted from table {args.table}.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Commit changes and close connection
con.commit()
con.close()

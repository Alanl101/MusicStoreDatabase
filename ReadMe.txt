This file will explain how to use the program.
Each file that ends in .py will be a command/file that can be ran.

More about python files:

task.py will build the database via Python and SQLite. Enforcing
all the key/participation constraints. Import the data from the
data clean.zip into the database. It's IMPORTANT to note that
task should only be ran once to create the database from the cvs file.
If you run the task.py after you have used update.py the task.py
will remove any updates not in the csv.

summary.py will return the summary report of the company. The report includes:
1. A total number of musicians and a list of musicians.
2. A total number of albums and a list of albums recorded at Notown.
3. A total number of instruments and a list of instruments at Notown.
4. A table consists of the name of musicians and the total number of albums written by them.

update.py Python file will insert or delete records in the database
you should be able to update your database using a command like this.
    python update.py --add --table musicians --record "Alanl,2828821"
In the first few lines under table_structure you should see how you
should format your entries as in the same way with no spaces just commas
(,) between each entry. Please make sure to fill out every portion of the
record.


Please take note that task.py MUST be ran before running
any other files/commands to build the database if the database doesn't exist
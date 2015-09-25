import sqlite3

"""
This is an example of how to open a SQLite database and perform 
queries against it in python.
"""

# Open a file with the sqlite3 module
conn = sqlite3.connect("example.db")

# Get a cursor. A cursor is the python interface to execute
# quries against the database and retrieve results.
cursor = conn.cursor()

query = """SELECT e.* 
  FROM Run r 
  JOIN Event e on (r.id = e.runId)
  WHERE r.quality = 'GOOD' and e.energy > 1e16
  ORDER BY e.energy desc
"""

cursor.execute(query)

for row in cursor.fetchall():
    print row

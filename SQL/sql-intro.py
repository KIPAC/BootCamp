
import sqlite3
connection = sqlite3.connect("example.db")
cursor = connection.cursor()

try:
    cursor.execute("DROP TABLE Point")
except Exception:
    pass

cursor.execute("""CREATE TABLE Point (
   x NUMBER,
   y NUMBER
)""")

cursor.execute("INSERT INTO Point VALUES (1, 2)")
cursor.execute("INSERT INTO Point VALUES (2, 3)")

cursor.execute("SELECT x, y FROM Point")
print cursor.fetchall()

cursor.execute("SELECT y, x FROM Point")
print cursor.fetchall()

cursor.execute("SELECT * FROM Point")
print cursor.fetchall()

cursor.execute("SELECT * FROM Point WHERE x < 2")
print cursor.fetchall()

cursor.execute("UPDATE Point SET y = 0 WHERE y >= 3")
cursor.execute("DELETE FROM Point WHERE y = 0")
cursor.execute("DELETE FROM Point")
cursor.execute("SELECT * FROM Point")
print cursor.fetchall()

cursor.execute("DROP TABLE Point")


cursor.execute("PRAGMA foreign_keys = ON")

# The following is
try:
    cursor.execute("DROP TABLE Event")
except Exception:
    pass

try:
    cursor.execute("DROP TABLE Run")
except Exception:
    pass

cursor.execute("""CREATE TABLE Run (
    id INTEGER PRIMARY KEY,
    startTime DATETIME,
    quality VARCHAR
)""")

cursor.execute("""CREATE TABLE Event (
    id INTEGER,
    runId INTEGER,
    energy NUMBER,
    triggerTime DATETIME,
    PRIMARY KEY (id, runId),
    FOREIGN KEY(runId) REFERENCES RUN(id)
)""")


cursor.execute("INSERT INTO Run VALUES (1234, datetime('2015-09-22T12:00:00'), 'GOOD')")
cursor.execute("INSERT INTO Event VALUES (1, 1234, 1.2e16, datetime('2015-09-22T12:01:00'))")
cursor.execute("INSERT INTO Event VALUES (2, 1234, 3.1e17, datetime('2015-09-22T12:02:00'))")
cursor.execute("INSERT INTO Event VALUES (3, 1234, 0.8e14, datetime('2015-09-22T12:03:00'))")
cursor.execute("INSERT INTO Event VALUES (4, 1234, 5.9e15, datetime('2015-09-22T12:04:00'))")

cursor.execute("INSERT INTO Run VALUES (4321, datetime('2015-09-23T12:00:00'), 'BAD')")
cursor.execute("INSERT INTO Event VALUES(1, 4321, 4.5e11, datetime('2015-09-23T12:01:00'))")
cursor.execute("INSERT INTO Event VALUES(2, 4321, 8.1e16, datetime('2015-09-23T12:02:00'))")
cursor.execute("INSERT INTO Event VALUES(3, 4321, 0.4e15, datetime('2015-09-23T12:03:00'))")
cursor.execute("INSERT INTO Event VALUES(4, 4321, 5.3e18, datetime('2015-09-23T12:04:00'))")

print
print "All events"
cursor.execute("SELECT * FROM Event")
for row in cursor.fetchall():
    print row

print
print "Run 1234 events after 12:02"
cursor.execute("""SELECT * FROM Event
   WHERE runId = 1234
   AND triggerTime > datetime('2015-09-22T12:02:00')""")
for row in cursor.fetchall():
    print row

print
print "High Energy events in 'GOOD' runs"
cursor.execute("""SELECT e.*
   FROM Run r
   JOIN Event e on (r.id = e.runId)
   WHERE r.quality = 'GOOD' and e.energy > 1e16
   ORDER BY e.energy desc""")
for row in cursor.fetchall():
    print row


cursor.close()
connection.close()

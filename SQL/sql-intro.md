
# Relational Databases

A *database* is an organized collection of data.

A *database management system* (DBMS) provides a user with an
interface for retrieval and manipulation of database. Because a
database isn't typically useful without interfaces, people often use
database and DBMS interchangeably (I will too!)

A *Relational Database* (RDBMS) provides additional interfaces to a user
based on relations in the data which are typically characterized by
*relational algebra*.

After several implementations of databases over many years, some
general standards emerged. The first standards was that of an 
interface for systems based on a relational algebra, an interface in the form
of a programming language. This interface is known as the SQL
language.

### Systems
There are many relational databases. The most popular are SQLite,
MySQL, Oracle, PostgreSQL, and Microsoft SQL Server. SQLite has the
unique distinction of being the most widely deployed database in the
world, as it is on every single iPhone and Android phone in the world. 
SQLite is installed on every Mac and most Linux boxes, and it's a library
included in the base install of python. 

Unlike the other RDBMSs, SQLite doesn't use a client-server architecture, rather
it stores the entire database in a single file. This makes it universally 
accessible across many systems, and since the file format is a standard, it
makes it very easy to share databases as well. It also makes a tutorial like
this possible. So we will use SQLite for this tutorial, but many of
the concepts are portable across the machines.

A word of caution: MySQL is very popular, and while SQL is a standard
(See ANSI SQL-92) that MySQL can cooperate with, the default settings in MySQL 
aren't typically setup to do so. As such, MySQL syntax in tutorials
often deviates from the official SQL standards. In general,
the syntax between PostgreSQL, Oracle, and SQLite are more compatible
with each other.

## SQL Concepts

### Creating a Database

Using SQLite, we want to create an actual database. Since SQLite uses files
and has a command line prompt, let's open a prompt on our machine and supply it a
file path where we will store our database.

```bash
bvan@somehost $ sqlite3 example.db
SQLite version 3.8.5 2014-08-15 22:37:57
Enter ".help" for usage hints.
sqlite> 
```

All changes we perform against the database will now be stored in the
file example.db. SQLite may put a few extra files in the directory 
example.db is in (like example.db-wal and/or *-shm). Those are for recovery,
and they disappear on the clean exit of SQLite.

The next parts of the tutorial will assume you stay in this prompt.
To exit out of the prompt, you can hit Ctrl-D.

### Schema, Tables, Columns and Rows

Databases are primarily composed of *tables*. Tables are typically
defined using a schema described with the *Data Description Language* (DDL), a
subset of the SQL language.

A simple example of a schema would be the definition of a table
describing points. You can execute the following in your SQLite prompt:

```sql
CREATE TABLE Point (
   x NUMBER,
   y NUMBER
);
```

In this example, we've created a table with two fields, known as
*columns*. The first, `x`, defines the x coordinate of a `Point`,
and `y` defines the y coordinate. In both cases, we've defined the
columns to be of type `NUMBER`. The data types that are useable 
is mostly implementation specific and will vary across databases, 
but `NUMBER` for a number (sometimes integer, sometimes floating point)
and `VARCHAR` for a string are fairly universal. `INTEGER`, `DECIMAL`, 
`DATE`, `TIME`, `TIMESTAMP`, and `DATETIME` are also very common, but they
may have slightly different semantics across different systems.

### Queries

A data structure without data isn't much good, so let's insert some
data by executing this in the SQLite prompt:

```sql
INSERT INTO Point VALUES (1, 2);
INSERT INTO Point VALUES (2, 3);
```

We just told SQLite to insert two points, (1, 2), and (2, 3).

This is your first SQL query. Technically speaking, it's another
subset of SQL called the *Data Modification Language* (DML).

There are four main types of DML statements: `INSERT`, `SELECT`, `UPDATE`,
and `DELETE`. They all do about what you'd expect. `SELECT` is the most
common for everyday use, because people usually want to just get a
result from a database:

```sql
SELECT x, y FROM Point;
```

The SQLite prompt returns to us the following:

```bash
1|2
2|3
```

We can reverse the order where that we are presented data:

```sql
SELECT y, x FROM Point;
```

Or, if we're lazy, we can just tell the database to return all columns
it's got. This order is defined by the order they were declared in
`Point`'s schema:

```sql
SELECT * FROM Point;
```

These do about what you might expect (`--` is the line comment delimiter):

```sql
-- Select all columns in Point. This should just return you the data
SELECT * FROM Point WHERE x < 2;
UPDATE Point SET y = 0 WHERE y >= 3;
DELETE FROM Point WHERE y = 0;
DELETE FROM Point; -- We just deleted the rest
SELECT * FROM Point;
```
The last query is to prove there are no rows left in `Point`.

Since there are no rows left, let's just delete the table `Point`.
Before we do that, let's just see what tables exist. From SQLite's prompt, 
you can see what tables are defined by the following command:

```bash
sqlite> .tables
```

This is part of SQLite and isn't actually part of SQL, but most database system's
have prompts which implement a similar feature, it just varies quite a bit. 

Let's remove the table with another DDL statement, the  `DROP` statement:

```sql
DROP TABLE Point;
```

Now we're back to square one, an empty database.

### Relations

What good is an Relational Database without relations?
There's a lot of ways to relate on thing to another. For particle
physics, we often make the relation that a specific set
of events belongs to a specific detector run.

```sql
-- This isn't turned on by default.
PRAGMA foreign_keys = ON;

CREATE TABLE Run (
    id INTEGER PRIMARY KEY,
    startTime DATETIME,
    quality VARCHAR
);

CREATE TABLE Event (
    id INTEGER,
    runId INTEGER,
    energy NUMBER,
    triggerTime DATETIME,
    PRIMARY KEY (id, runId),
    FOREIGN KEY(runId) REFERENCES RUN(id)
);

INSERT INTO Run VALUES (1234, datetime('2015-09-22T12:00:00'), 'GOOD');
INSERT INTO Event VALUES (1, 1234, 1.2e16, datetime('2015-09-22T12:01:00'));
INSERT INTO Event VALUES (2, 1234, 3.1e17, datetime('2015-09-22T12:02:00'));
INSERT INTO Event VALUES (3, 1234, 0.8e14, datetime('2015-09-22T12:03:00'));
INSERT INTO Event VALUES (4, 1234, 5.9e15, datetime('2015-09-22T12:04:00'));

INSERT INTO Run VALUES (4321, datetime('2015-09-23T12:00:00'), 'BAD');
INSERT INTO Event VALUES(1, 4321, 4.5e11, datetime('2015-09-23T12:01:00'));
INSERT INTO Event VALUES(2, 4321, 8.1e16, datetime('2015-09-23T12:02:00'));
INSERT INTO Event VALUES(3, 4321, 0.4e15, datetime('2015-09-23T12:03:00'));
INSERT INTO Event VALUES(4, 4321, 5.3e18, datetime('2015-09-23T12:04:00'));
```

Now, let's find events since 12:02 for run 1234:

```sql
SELECT * FROM Event
   WHERE runId = 1234 AND triggerTime > datetime('2015-09-22T12:02:00');
```

Let's get some high-energy events ordered by decreasing energy, but only from the 'GOOD' run:

```sql
SELECT e.*
   FROM Run r
   JOIN Event e on (r.id = e.runId)
   WHERE r.quality = 'GOOD' and e.energy > 1e16
   ORDER BY e.energy desc;
```

(Note: `r` and `e` are aliases for the table in this example)

What we just did is add a  `JOIN` clause to our `SELECT` statement.
The `JOIN` clause combines records from two (or more) tables using
values common to each. In the example above, I joined all the events
in the `Event` table to each run based on `Run.id`.

The join is the outcome after first taking the Cartesian product of
all records in `Run` with all records in `Event`, and then only
returning the combinations where `Run.id` is equal to `Events.runId`.

There are many types of `JOIN`'s available to you. This specific join
is an `INNER JOIN`. Please see the [Wikipedia Article on
Joins](https://en.wikipedia.org/wiki/Join_(SQL)). 

### Keys, Indexes, and Constraints

If you'll notice in the DDL above, there's a few curious extra parts
in the definitions of both `Run` and `Event` tables.

In the `Run` table, we included a `PRIMARY KEY` after the data type
definition. This tells SQLite that this is to be the primary way we
want to define and address a run. It also tells SQLite that this
number should be unique. We can only have one Run `1234`, for
example. However, we want to be able to identify multiple events
numbered `1` in the `Event` table, in fact, at least one per run. So
rather than identify the Primary Key on just one column, as I did for
`Run`, I told SQLite I will uniquely identify events based both on
their run and their event id.

In practice, it's often useful to go ahead and let the database give
each event a unique, random (or auto-incrementing) ID which has no
semantic meaning as it did in our example. This is useful, if, for
example, you find out events 1 and 3 were actually swapped, and you
want to fix that:

```sql
UPDATE Event SET id=3 WHERE id=1 AND runId = 4321;
UPDATE Event SET id=1 WHERE id=3 AND runId = 4321;
```

This will fail because the first step violates the primary key of the
second step and Databases do things in order (this is actually a core
guarantee called Serializability).

So, in practice, `Event` might actually look like this:

```sql
DROP TABLE Event; 

CREATE TABLE Event (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    eventIndex INTEGER,
    runId INTEGER,
    energy NUMBER,
    triggerTime DATETIME,
    FOREIGN KEY(runId) REFERENCES Run(id)
);

-- Note: We can't use the shorthand anymore because of the autoincrement column
INSERT INTO Event (eventIndex, runId, energy, triggerTime) VALUES (1, 1234, 1.2e16, datetime('2015-09-22T12:01:00'));
INSERT INTO Event (eventIndex, runId, energy, triggerTime) VALUES (2, 1234, 3.1e17, datetime('2015-09-22T12:02:00'));
INSERT INTO Event (eventIndex, runId, energy, triggerTime) VALUES (3, 1234, 0.8e14, datetime('2015-09-22T12:03:00'));
INSERT INTO Event (eventIndex, runId, energy, triggerTime) VALUES (4, 1234, 5.9e15, datetime('2015-09-22T12:04:00'));

INSERT INTO Event (eventIndex, runId, energy, triggerTime) VALUES(1, 4321, 4.5e11, datetime('2015-09-23T12:01:00'));
INSERT INTO Event (eventIndex, runId, energy, triggerTime) VALUES(2, 4321, 8.1e16, datetime('2015-09-23T12:02:00'));
INSERT INTO Event (eventIndex, runId, energy, triggerTime) VALUES(3, 4321, 0.4e15, datetime('2015-09-23T12:03:00'));
INSERT INTO Event (eventIndex, runId, energy, triggerTime) VALUES(4, 4321, 5.3e18, datetime('2015-09-23T12:04:00'));

```

...And the update might look like this, where `id` was automatically
incremented in some way:

```sql
UPDATE Event SET eventIndex=1 WHERE id=7 AND runId = 4321;
UPDATE Event SET eventIndex=3 WHERE id=5 AND runId = 4321;

-- Check it out
SELECT eventIndex, runId, energy, triggerTime FROM Event ORDER BY runId, eventIndex;
```

#### Data integrity

Expanding on the previous definiton of `Event`, there are scenarios
where we might want to delete a run and all events from a run in one
go.

```sql
CREATE TABLE Event (
    id INTEGER PRIMARY KEY,
    eventIndex INTEGER,
    runId INTEGER,
    energy NUMBER,
    triggerTime DATETIME,
    FOREIGN KEY(runId) REFERENCES Run(id) ON DELETE CASCADE
);
```


#### Indexes
Indexes are data structures, like Hash
Tables, Binary Trees, or, more typically
[B-Trees](https://en.wikipedia.org/wiki/B-tree#The_database_problem),
which can drastically speedup the lookup of any given record by
telling SQLite approximately where on disk a given record exists.

One unique property of `PRIMARY KEY` is that it actually generates an
index on `Run.id` which SQLite can consult to find out the exact disk
block where the `Run` record resides. 

In our updated `Event` table, we also have an index on `Event.id` as
well.

That's useful for finding one specific event, but it's not
particularly useful for finding all the events in a given run. The
solution is typically to create an index based on `Event.runId`, which
we also implicitly did by creating the `FOREIGN KEY` relationship. 

But what if we want to quickly find all high energy events in the
`Event` table?

First off, let's see how it will execute:

```sql
EXPLAIN QUERY PLAN SELECT * FROM Event WHERE energy > 1e17;
```

We get:
```bash
0|0|0|SCAN TABLE Event
```

This implies a full table scan, so each time we search the database, we read the *entire* table. That's not efficient.

Let's create an index:

```sql
CREATE INDEX idx_evtEnergy ON Event(Energy);
```

We get the following:

```bash
0|0|0|SEARCH TABLE Event USING INDEX idx_evtEnergy (energy>?)
```

If our event energies were gaussian and we were performing a search for the top 2% of events, the index would allow us to skip reading nearly 98% of the table.

Indexes are really powerful, but they have a storage cost and an
update cost to them, so it's not necessarily useful to create them
everywhere. The reason why they are typically created on `PRIMARY KEY`
and `FOREIGN KEY` relationships is because it's assumed a user may want
to do a `JOIN` with them.

You can 

## Transactions

The second standard was a set of generally accepted
guarantees these databases should implement so that they behave
predictably after some smart guy defined them. These properties are
summarized as [ACID](https://en.wikipedia.org/wiki/ACID). You can read up on this yourself, but the implications
is that you typically execute SQL queries inside a *transactions*.

When is a transaction good?

In our previous example, say we wanted to add a run, then add all the
events of a run to a database. We wanted to do this all at once or
none at all, and it takes a few hours for your program to update
the database of all the runs.

With a transaction, you can *atomically* update both the `Run` table
and the `Event` table at once.

So the following statement:

```sql
BEGIN TRANSACTION;
INSERT INTO Run VALUES (4321, datetime('2015-09-23T12:00:00'), 'BAD');
INSERT INTO Event VALUES(1, 4321, 4.5e11, datetime('2015-09-23T12:01:00'));
INSERT INTO Event VALUES(2, 4321, 8.1e16, datetime('2015-09-23T12:02:00'));
INSERT INTO Event VALUES(3, 4321, 0.4e15, datetime('2015-09-23T12:03:00'));
INSERT INTO Event VALUES(4, 4321, 5.3e18, datetime('2015-09-23T12:04:00'));
COMMIT;
```

... Is either executed completely or not at all.

Without a transaction, it's conceivable your program could die halfway
through and you would end up effectively executing the following:

```sql
INSERT INTO Run VALUES (4321, datetime('2015-09-23T12:00:00'), 'BAD');
INSERT INTO Event VALUES(1, 4321, 4.5e11, datetime('2015-09-23T12:01:00'));
```

In this case, it might appear that Run `4321` only had one event.

Transactions make some things simpler, but that occasionally comes at
a cost. In SQLite, that cost isn't so great due to internal
engineering, but it can be much higher in certain databases.

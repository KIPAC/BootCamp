DROP TABLE Event;
DROP TABLE Run;

-- SQLite actually turns foreign keys off by default
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
INSERT INTO Event VALUES(1, 1234, 1.0e17, datetime('2015-09-22T12:01:00'));
INSERT INTO Event VALUES(2, 1234, 1.2e16, datetime('2015-09-22T12:02:00'));
INSERT INTO Event VALUES(3, 1234, 0.8e14, datetime('2015-09-22T12:03:00'));
INSERT INTO Event VALUES(4, 1234, 5.9e15, datetime('2015-09-22T12:04:00'));


INSERT INTO Run VALUES (4321, datetime('2015-09-23T12:00:00'), 'BAD');
INSERT INTO Event VALUES(1, 4321, 4.5e11, datetime('2015-09-23T12:01:00'));
INSERT INTO Event VALUES(2, 4321, 8.1e16, datetime('2015-09-23T12:02:00'));
INSERT INTO Event VALUES(3, 4321, 0.4e15, datetime('2015-09-23T12:03:00'));
INSERT INTO Event VALUES(4, 4321, 5.3e18, datetime('2015-09-23T12:04:00'));


-- Remove old Run Entries
DELETE FROM Run;
-- Remove old table;
DROP TABLE Event;

-- Add autoincrement support to Event
CREATE TABLE Event (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    eventIndex INTEGER,
    runId INTEGER,
    energy NUMBER,
    triggerTime DATETIME,
    FOREIGN KEY(runId) REFERENCES Run(id) ON DELETE CASCADE
);

INSERT INTO Run VALUES (1234, datetime('2015-09-22T12:00:00'), 'GOOD');

-- Note: We can't use the shorthand anymore because of the autoincrement column
INSERT INTO Event (eventIndex, runId, energy, triggerTime) VALUES (1, 1234, 1.2e16, datetime('2015-09-22T12:01:00'));
INSERT INTO Event (eventIndex, runId, energy, triggerTime) VALUES (2, 1234, 3.1e17, datetime('2015-09-22T12:02:00'));
INSERT INTO Event (eventIndex, runId, energy, triggerTime) VALUES (3, 1234, 0.8e14, datetime('2015-09-22T12:03:00'));
INSERT INTO Event (eventIndex, runId, energy, triggerTime) VALUES (4, 1234, 5.9e15, datetime('2015-09-22T12:04:00'));

INSERT INTO Run VALUES (4321, datetime('2015-09-23T12:00:00'), 'BAD');
INSERT INTO Event (eventIndex, runId, energy, triggerTime) VALUES(1, 4321, 4.5e11, datetime('2015-09-23T12:01:00'));
INSERT INTO Event (eventIndex, runId, energy, triggerTime) VALUES(2, 4321, 8.1e16, datetime('2015-09-23T12:02:00'));
INSERT INTO Event (eventIndex, runId, energy, triggerTime) VALUES(3, 4321, 0.4e15, datetime('2015-09-23T12:03:00'));
INSERT INTO Event (eventIndex, runId, energy, triggerTime) VALUES(4, 4321, 5.3e18, datetime('2015-09-23T12:04:00'));


-- Try previous queries again
SELECT * FROM Event WHERE runId = 1234 and triggerTime > datetime('2015-09-22T12:02:00');

-- But we want all events from all good runs!
SELECT e.*
   FROM Run r
   JOIN Event e on (r.id = e.runId)
   WHERE r.quality = 'GOOD';

-- Add an index
CREATE INDEX idx_evtEnergy ON Event(Energy);

-- Delete bad runs (cascades into Event table)
DELETE FROM Run WHERE quality = 'BAD';

-- Proof Bad run events are gone!
SELECT * FROM Event;


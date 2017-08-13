PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE log (dt datetime not null, json text not null);
CREATE INDEX dt on log(dt);
COMMIT;

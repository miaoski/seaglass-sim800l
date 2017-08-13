# -*- coding: utf8 -*-
from time import sleep
import gps
import gsm
import json
import sqlite3

db = sqlite3.connect('seaglass.sq3')
cur = db.cursor()

print 'IMEI =', gsm.getIMEI()

while True:
    xs = gps.readGLL()
    netscan = gsm.doCNETSCAN()
    ceng = gsm.getCENG()
    if netscan:
        xs['netscan'] = netscan
    if ceng:
        xs['ceng'] = ceng
    print json.dumps(xs, indent=4)
    cur.execute("INSERT INTO log VALUES (datetime('now'), ?)", (json.dumps(xs),))
    db.commit()
    sleep(30)

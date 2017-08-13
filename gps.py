# -*- coding: utf8 -*-
import serial
from time import sleep

gps = serial.Serial('/dev/ttyS0', 9600, timeout=60)

# $GPGLL,2501.70189,N,12130.08138,E,144048.00,A,D*63

def switch(x):
    dot = x.find('.')
    if dot == -1:
        return None
    abc  = int(x[:dot-2])
    de   = int(x[dot-2:dot])
    fghi = int(x[dot+1:])
    return abc + (de / 60.0) + (fghi / 600000.0)

def readGLL():
    gps.flushInput()
    while True:
        x = gps.readline().strip()
        if not x.startswith('$GPGLL'):
            continue
        xs = x.split(',')
        if xs[6] != 'A':
            sleep(1)
            continue
        if xs[2] == 'N':
            longitude = switch(xs[1])
        else:
            longitude = -switch(xs[1])
        if xs[4] == 'E':
            latitude = switch(xs[3])
        else:
            latitude = -switch(xs[3])
        utc = '%s:%s:%s' % (xs[5][0:2], xs[5][2:4], xs[5][4:6])
        return {'longitude': longitude, 'latitude': latitude, 'utc': utc}

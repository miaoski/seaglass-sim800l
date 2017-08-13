Make Yourself a SeaGlass
========================

I am trying to make myself a [SeaGlass](https://seaglass.cs.washington.edu/)
with components that I have.  I use what you easily find in
[Ruten](http://www.ruten.com.tw), i.e.,

- SIM-800L GSM MODEM
- VK2828U7G5LF GPS module

To be very honest, Telit GT-864 QUAD/PY is what you need, if you really want to
make a valid comparison.  Telit MODEM returns more useful information.  It
simply doesn't hurt to use what I have on hand and see where I can go.  Hence,
use at your own risk.


Schematics
==========

To be added.


Run
===

To create the SQLite database (I used it to prevent sudden power loss), run
`sqlite3 seaglass.sq3 < schema.sql`.  SSH and do `nohup python main.py`.  If
you feel comfortable, put it into `rc.local`.


License
=======

MIT License.

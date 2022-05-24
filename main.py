#!/usr/bin/env python
# -*- coding: utf-8 -*-


from functions import createTweetsFile, createTweetsDB, dumpTweetsDB1, dumpTweetsDB2, closeTweetsDBs

# createTweetsFile()

cursor, db = createTweetsDB()
dumpTweetsDB1(cursor)
dumpTweetsDB2(cursor)
closeTweetsDBs(db)
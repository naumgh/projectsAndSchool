#!/usr/bin/env python3

import psycopg2

def main():
    dbconn = psycopg2.connect(host='studentdb.csc.uvic.ca', user='johnwick',
        password='have.a.nice.day')
    cursor = dbconn.cursor()

    cursor = dbconn.cursor()
    cursor.arraysize = 500
    cursor.execute("select shrt_desc, ndb_no from food_des order by shrt_desc")

    batch_num = 1
    while True:
        batch = cursor.fetchmany()
        if not batch:
            break
        print ("BATCH # %d" % (batch_num))
        for row in batch:
            print ("Desc: %s; Database #: %s" % (row[0], row[1]))

        batch_num = batch_num + 1


    cursor.close()
    dbconn.close()


if __name__ == "__main__": main()

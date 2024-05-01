#!/usr/bin/env python3

import psycopg2

def main():
    dbconn = psycopg2.connect(host='studentdb.csc.uvic.ca', user='johnwick',
        password='have.a.nice.day')
    cursor = dbconn.cursor()

    cursor.execute("select pub, price, beer from sells")
    for row in cursor.fetchall():
        print("Sells data: %s %s %s" % (row[0], row[1], row[2].rstrip()))

    cursor.close()
    dbconn.close()


if __name__ == "__main__": main()

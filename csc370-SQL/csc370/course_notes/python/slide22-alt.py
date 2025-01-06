#!/usr/bin/env python3

import psycopg2

def main():
    dbconn = psycopg2.connect(host='studentdb.csc.uvic.ca', user='johnwick',
        password='have.a.nice.day')
    cursor = dbconn.cursor()

    cursor.execute("select pub, price, beer from sells where price > 5")
    row = cursor.fetchone()
    if (row):
        print("Sells data:", row[0], ' || ',  row[1], ' || ', row[2].rstrip())
        print("Types: ", type(row[0]), type(row[1]), type(row[2]))

    cursor.close()
    dbconn.close()


if __name__ == "__main__": main()

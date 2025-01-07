#!/usr/bin/env python3

import psycopg2

def main():
    dbconn = psycopg2.connect(host='studentdb.csc.uvic.ca', user='johnwick',
        password='have.a.nice.day')
    cursor = dbconn.cursor()

    cursor.execute("select price, pub, beer from sells")
    print (cursor.description[0].name)
    print (cursor.description[0].type_code)
    print (cursor.description[2].name)
    print (cursor.description[2].type_code)

    cursor.close()
    dbconn.close()


if __name__ == "__main__": main()

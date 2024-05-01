#!/usr/bin/env python3

import psycopg2

def main():
    dbconn = psycopg2.connect(host='studentdb.csc.uvic.ca', user='johnwick',
        password='have.a.nice.day')
    cursor = dbconn.cursor()

    cursor.execute("""
    select pub, beer
    from sells
    where price < 5
    """)
    result = cursor.fetchall()                  # Does work.
    print (result)

    cursor.execute("analyze verbose sells")
    result = cursor.fetchall()                  # Doesn't work.
    print (result)


    cursor.close()
    dbconn.close()


if __name__ == "__main__": main()

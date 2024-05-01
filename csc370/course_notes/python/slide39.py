#!/usr/bin/env python3

from decimal import Decimal
from psycopg2 import connect, Date

def main():
    dbconn = connect(host='studentdb.csc.uvic.ca', user='johnwick',
        password='have.a.nice.day')
    cursor = dbconn.cursor()

    query_string = cursor.mogrify("""
                insert into orders (orderdate, customerid,
                    netamount, tax, totalamount)
                    values (%s, %s, %s, %s, %s)""",
    [Date(2020,3,31), 12345, Decimal("899.95"), 8.875, Decimal("979.82")])

    print (query_string)


    cursor.close()
    dbconn.close()


if __name__ == "__main__": main()

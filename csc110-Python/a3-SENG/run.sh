#!/bin/sh
#./icsout3 --start=2021/2/14 --end=2021/2/14 --file=one.ics
./icsout3 --start=2021/2/14 --end=2021/2/14 --file=one.ics |diff test01.txt -
./icsout3 --start=2021/4/18 --end=2021/4/21 --file=two.ics | diff test02.txt -
./icsout3 --start=2021/2/1 --end=2021/3/1 --file=many.ics |diff test03.txt -
./icsout3 --start=2021/4/22 --end=2021/4/23 --file=two.ics |diff test04.txt -
./icsout3 --start=2021/2/1 --end=2021/2/1 --file=diana-devops.ics |diff test05.txt -
#./icsout3 --start=2021/2/1 --end=2021/2/1 --file=diana-devops.ics
./icsout3 --start=2021/2/2 --end=2021/2/2 --file=diana-devops.ics |diff test06.txt -
#./icsout3 --start=2021/2/1 --end=2021/2/8 --file=diana-devops.ics 
./icsout3 --start=2021/2/1 --end=2021/2/8 --file=diana-devops.ics |diff test07.txt -
#./icsout3 --start=2021/2/8 --end=2021/2/15 --file=diana-devops.ics 
./icsout3 --start=2021/2/8 --end=2021/2/15 --file=diana-devops.ics |diff test08.txt -
./icsout3 --start=2021/2/1 --end=2021/3/1 --file=diana-devops.ics |diff test09.txt -
./icsout3 --start=2021/1/1 --end=2021/4/30 --file=diana-devops.ics|diff test10.txt -
#./icsout3 --start=2021/1/1 --end=2021/4/30 --file=diana-devops.ics
./icsout3 --start=2021/5/1 --end=2021/6/1 --file=mlb.ics|diff test11.txt -
./icsout3 --start=2021/5/1 --end=2021/8/1 --file=mlb.ics|diff test12.txt -
./icsout3 --start=2020/12/1 --end=2021/4/30 --file=mlb.ics|diff test13.txt -
./icsout3 --start=2021/8/1 --end=2021/10/1 --file=f1.ics |diff test14.txt -
./icsout3 --start=2021/1/1 --end=2021/12/31 --file=f1.ics |diff test15.txt -

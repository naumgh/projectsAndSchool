/*
 * A2Tester.java
 *
 * This tester includes the tests we used to grade your assignment
 * The actual grading will have been done with different values than
 *   shown here but the tests will have been the same.
 */
public class A2Tester{
    
    private static int testPassCount = 0;
    private static int testCount = 0;
    
    public static void main (String[] args) {
        
        dateConstructorGetterTests();
        dateSetterGetterTests();
        dateEqualsTests();
        dateToStringTests();
      
        
        timeConstructorGetterTests();
        
        timeSetterGetterTests();
        
        timeEqualsTests();
        
        timeIsBeforeTests();
        
        timeAddTimeTests();
        
        timeToStringTests();
        
        examConstructorGetterTests();
        examSetterGetterTests();
        
        examIsOverlap();
       
        examToStringTests();
        
        
        System.out.println("Passed " + testPassCount + "/" + testCount + " tests");
    }
    
    public static void displayResults (boolean passed, String testName) {
        /* There is some magic going on here getting the line number
         * Borrowed from:
         * http://blog.taragana.com/index.php/archive/core-java-how-to-get-java-source-code-line-number-file-name-in-code/
         */
        testCount++;
        if (passed)
        {
            System.out.println ("Passed test: " + testCount);
            testPassCount++;
        }
        else
        {
            System.out.println ("Failed test: " + testName + " at line "
                                + Thread.currentThread().getStackTrace()[2].getLineNumber());
            //System.exit(1);
        }
    }
    
    public static void dateConstructorGetterTests() {
        
        // TODO:
        // uncomment the following to test your implementation
        
         
         Date noParams = new Date();
         displayResults (noParams.getMonth().equals("January"), "Date() Constructor Getter Test -month");
         displayResults (noParams.getDay()   == 1, "Date() Constructor Getter Test -day");
         displayResults (noParams.getYear()  == 1582, "Date() Constructor Getter Test -year");
         
         Date d20190131 = new Date("January",31,2019);
         displayResults (d20190131.getMonth().equals("January"), "Date(1,31,2019) Constructor Getter Test -month");
         displayResults (d20190131.getDay()   == 31, "Date(\"January\",31,2019) Constructor Getter Test -day");
         displayResults (d20190131.getYear()  == 2019, "Date(\"January\",31,2019) Constructor Getter Test -year");
         
         Date d20521015 = new Date("October",15,2052);
         displayResults (d20521015.getMonth().equals("October"), "Date(\"October\",15,2052) Constructor Getter Test -month");
         displayResults (d20521015.getDay()   == 15, "Date(\"October\",15,2052) Constructor Getter Test -day");
         displayResults (d20521015.getYear()  == 2052, "Date(\"October\",15,2052) Constructor Getter Test -year");
         
        
    }
    
    public static void dateSetterGetterTests() {
        
        // TODO:
        // uncomment the following to test your implementation
        
         Date d1 = new Date("January",31,2018);
         
         d1.setYear(2019);
         d1.setMonth("February");
         d1.setDay(10);
         
         displayResults (d1.getMonth().equals("February"), "Date setMonth(\"February\") Test");
         displayResults (d1.getDay()   == 10, "Date setDay(10) Test");
         displayResults (d1.getYear()  == 2019, "Date setYear(2019) Test");
         
         d1.setYear(1956);
         d1.setMonth("November");
         d1.setDay(23);
         
         displayResults (d1.getMonth().equals("November"), "Date setMonth(\"November\") Test");
         displayResults (d1.getDay()   == 23, "Date setDay(22) Test");
         displayResults (d1.getYear()  == 1956, "Date setYear(1956) Test");
         
    }
    
    public static void dateEqualsTests() {
        
        // TODO:
        // uncomment the following to test your implementation
        
         Date d         = new Date("January",15,2018);
         Date dEqual    = new Date("January",15,2018);
         Date dYrDiff   = new Date("January",15,2019);
         Date dMthDiff  = new Date("February",15,2018);
         Date dDayDiff  = new Date("January",10,2018);
         Date dDefault  = new Date();
         
         displayResults (d.equals(d), "Date Equals Tests - same object");
         
         displayResults (d.equals(dEqual), "Date Equals Tests - different objects, equal date");
         displayResults (dEqual.equals(d), "Date Equals Tests - different objects, equal date");
         
         displayResults (d.equals(dYrDiff) == false, "Date Equals Tests - different objects, years differ");
         displayResults (!dMthDiff.equals(d), "Date Equals Tests - different objects, months differ");
         displayResults (!d.equals(dDayDiff), "Date Equals Tests - different objects, days differ");
         displayResults (!dDefault.equals(dDayDiff), "Date Equals Tests - different objects, all fields differ");
         
    }
    
    
    public static void dateToStringTests() {
        
        // TODO:
        // uncomment the following to test your implementation
        
         Date d1 = new Date("November",1,2008);
         Date d2 = new Date("March",23,2000);
         
         displayResults (d1.toString().equals("November 1, 2008"), "Date toString Test November 1, 2008");
         displayResults (d2.toString().equals("March 23, 2000"), "Date toString Test March 23, 2000");
         
    }
    
    
    
    public static void timeConstructorGetterTests() {
        
        // TODO:
        // uncomment the following to test your implementation
         
         Time noParams = new Time();
         displayResults (noParams.getHour() == 0, "Time() Constructor Getter Test -hour");
         displayResults (noParams.getMinute()   == 0, "Time() Constructor Getter Test -minute");
         
         Time t1834 = new Time(18,34);
         displayResults (t1834.getHour() == 18, "Time(18,34) Constructor Getter Test -hour");
         displayResults (t1834.getMinute()   == 34, "Time(18,34) Constructor Getter Test -minute");
         
         Time t04 = new Time(0,4);
         displayResults (t04.getHour() == 0, "Time(0,4) Constructor Getter Test -hour");
         displayResults (t04.getMinute()   == 4, "Time(0,4) Constructor Getter Test -minute");
         
    }
    
    public static void timeSetterGetterTests() {
        
        // TODO:
        // uncomment the following to test your implementation
        
         Time t1 = new Time(18,34);
         
         t1.setHour(15);
         t1.setMinute(45);
         
         displayResults (t1.getHour() == 15, "Time setHour(15) Test");
         displayResults (t1.getMinute() == 45, "Date setMinute(45) Test");
         
         t1.setHour(7);
         t1.setMinute(23);
         
         displayResults (t1.getHour() == 7, "Time setHour(7) Test");
         displayResults (t1.getMinute() == 23, "Date setMinute(23) Test");
         
        
    }
    
    public static void timeEqualsTests() {
        // TODO:
        // uncomment the following to test your implementation
        
        Time t              = new Time(10,15);
        Time tEqual         = new Time(10,15);
        Time tMinuteDiff    = new Time(10,35);
        Time tHourDiff      = new Time(21,15);
        Time tDefault       = new Time();
        
        displayResults (t.equals(t), "Time Equals Tests - same object");
        
        displayResults (t.equals(tEqual), "Time Equals Tests - different objects, equal date");
        displayResults (tEqual.equals(t), "Time Equals Tests - different objects, equal date");
        
        displayResults (t.equals(tMinuteDiff) == false, "Time Equals Tests - different objects, minutes differ");
        displayResults (!tMinuteDiff.equals(t), "Time Equals Tests - different objects, minutes differ");
        displayResults (!t.equals(tHourDiff), "Time Equals Tests - different objects, hours differ");
        displayResults (!tDefault.equals(tHourDiff), "Time Equals Tests - different objects, all fields differ");
        
    }
    
    public static void timeIsBeforeTests() {
        
        // TODO:
        // uncomment the following to test your implementation
        
         Time t1a         = new Time(10,34);
         Time t1Same      = new Time(10,34);
         Time t1Before1a  = new Time(10,30);
         Time t2Before1a  = new Time(9,36);
         
         Time t1After1a   = new Time(10,36);
         Time t2After1a   = new Time(12,34);
         Time t3After1a   = new Time(11,36);
         Time t4After1a   = new Time(14,23);
         
         displayResults (!t1Same.isBefore(t1a), "Time isBefore Tests - different objects, equal time");
         displayResults (!t1a.isBefore(t1Same), "Time isBefore Tests - different objects, equal time");
         
         displayResults (t1Before1a.isBefore(t1a), "Time isBefore Tests - minute is before");
         displayResults (t2Before1a.isBefore(t1a), "Time isBefore Tests - hour is before");
         
         displayResults (!t1After1a.isBefore(t1a), "Time isBefore Tests - minute is after");
         displayResults (!t2After1a.isBefore(t1a), "Time isBefore Tests - hour is after");
         displayResults (!t3After1a.isBefore(t1a), "Time isBefore Tests - minute is same, hour is after");
         displayResults (!t4After1a.isBefore(t1a), "Time isBefore Tests - hour is after, minute is not");
         
    }
    
    public static void timeAddTimeTests() {
        
        // TODO:
        // uncomment the following to test your implementation
        
         Time t923  = new Time(9,23);
         t923.addTime(20);
         displayResults (t923.equals(new Time(9,43)), "Time addTime Tests - t923.addTime(20)");
         
         Time t1034  = new Time(10,34);
         t1034.addTime(30);
         displayResults (t1034.equals(new Time(11,4)), "Time addTime Tests - t1034.addTime(30)");
         
         Time t2245  = new Time(22,45);
         t2245.addTime(90);
         displayResults (t2245.equals(new Time(0,15)), "Time addTime Tests - t2245.addTime(90)");
         
    }
    
    
    
    public static void timeToStringTests() {
        
        // TODO:
        // uncomment the following to test your implementation
        
         Time t1 = new Time(10,23);
         Time t2 = new Time(21,12);
         
         displayResults (t1.toString().equals("10:23am"), "Time toString Test Time(10,23)");
         displayResults (t2.toString().equals("9:12pm"), "Time toString Test Time(21,12)");
         
    }
    
    
    public static void examConstructorGetterTests() {
        
        // TODO:
        // uncomment the following to test your implementation
        
         Exam eNoLocationDuration = new Exam(new Date("January",31,2019), new Time(9,0));
         displayResults (eNoLocationDuration.getDate().equals(new Date("January",31,2019)),
         "new Exam(new Date(\"January\",31,2019), new Time(9,0)) Constructor Getter Test - date");
         displayResults (eNoLocationDuration.getLocation().equals("TBA"),
         "new Exam(new Date(\"January\",31,2019), new Time(9,0)) Constructor Getter Test - location");
         displayResults (eNoLocationDuration.getStartTime().equals(new Time(9,0)),
         "new Exam(new Date(\"January\",31,2019), new Time(9,0)) Constructor Getter Test - startTime");
         displayResults (eNoLocationDuration.getDuration() == 180,
         "new Exam(new Date(\"January\",31,2019), new Time(9,0)) Constructor Getter Test - duration");
         
         
         Date d20190131 = new Date("January",31,2019);
         Time t1234 = new Time(12,34);
         
         Exam eWithAllArgs = new Exam(d20190131, "MAC 101", t1234, 120);
         displayResults (eWithAllArgs.getDate().equals(new Date("January",31,2019)),
         "new Exam(d20190131, \"MAC 101\", t1234, 120)) Constructor Getter Test - date");
         displayResults (eWithAllArgs.getLocation().equals("MAC 101"),
         "new Exam(d20190131, \"MAC 101\", t1234, 120)) Constructor Getter Test - location");
         displayResults (eWithAllArgs.getStartTime().equals(new Time(12,34)),
         "new Exam(d20190131, \"MAC 101\", t1234, 120)) Constructor Getter Test - startTime");
         displayResults (eWithAllArgs.getDuration() == 120,
         "new Exam(d20190131, \"MAC 101\", t1234, 120)) Constructor Getter Test - duration");
         
        
    }
    
    public static void examSetterGetterTests() {
        
        // TODO:
        // uncomment the following to test your implementation
        
         Exam e1 =  new Exam(new Date("January",31,2019), new Time(9,0));
         Date d20190131 = new Date("January",31,2019);
         Time t1234 = new Time(12,34);
         
         e1.setDate(d20190131);
         e1.setLocation("ECS 128");
         e1.setStartTime(t1234);
         e1.setDuration(210);
         
         displayResults (e1.getDate().equals(new Date("January",31,2019)),
         "Exam setDate(d20190131) Test");
         displayResults (e1.getLocation().equals("ECS 128"),
         "Exam setLocation(\"ECS 128\") Test");
         displayResults (e1.getStartTime().equals(new Time(12,34)),
         "Exam setStartTime(t1234) Test");
         displayResults (e1.getDuration() == 210,
         "Exam setDuration(210) Test");
         
         Date d19350618 = new Date("June",18,1935);
         Time t2348 = new Time(23,48);
         
         e1.setDate(d19350618);
         e1.setLocation("SUB 008");
         e1.setStartTime(t2348);
         e1.setDuration(160);
         
         displayResults (e1.getDate().equals(new Date("June",18,1935)),
         "Exam setDate(d19350618) Test");
         displayResults (e1.getLocation().equals("SUB 008"),
         "Exam setLocation(\"SUB 008\") Test");
         displayResults (e1.getStartTime().equals(new Time(23,48)),
         "Exam setStartTime(t2348) Test");
         displayResults (e1.getDuration() == 160,
         "Exam setDuration(160) Test");
         
    }
    
    public static void examIsOverlap() {
        
        // TODO:
        // uncomment the following to test your implementation
        
         Date d20200315a = new Date("March",15,2020);
         Date d20200315b = new Date("March",15,2020);
         Date d20180315 = new Date("March",15,2018);
         
         Time t1530a = new Time(15,30);
         Time t1530b = new Time(15,30);
         Time t1330 = new Time(13,30);
         Time t1730 = new Time(17,30);
         
         Exam e1 = new Exam(d20200315a, "ECS 125", t1530a, 60);
         displayResults (e1.isOverlap(e1), "Exam isOverlap Test same exam - true");
         
         Exam e1SameDayTimeDuration = new Exam(d20200315b, "ECS 125", t1530b, 60);
         displayResults (e1.isOverlap(e1SameDayTimeDuration), "Exam isOverlap Test e1SameDayTimeDuration - true");
         displayResults (e1SameDayTimeDuration.isOverlap(e1), "Exam isOverlap Test e1SameDayTimeDuration - true");
         
         Exam e1SameDayTime = new Exam(d20200315b, "ECS 125", t1530b, 30);
         displayResults (e1.isOverlap(e1SameDayTime), "Exam isOverlap Test e1SameDayTime - true");
         displayResults (e1SameDayTime.isOverlap(e1), "Exam isOverlap Test e1SameDayTime - true");
         
         Exam e1SameDayNoOverlapBackToBack= new Exam(d20200315b, "ECS 125", t1330, 120);
         displayResults (!e1.isOverlap(e1SameDayNoOverlapBackToBack), "Exam isOverlap Test e1SameDayNoOverlapBackToBack - false");
         displayResults (!e1SameDayNoOverlapBackToBack.isOverlap(e1), "Exam isOverlap Test e1SameDayNoOverlapBackToBack - false");
         
         Exam e1SameDayOverlapMidBefore  = new Exam(d20200315b, "ECS 125", t1330, 150);
         displayResults (e1.isOverlap(e1SameDayOverlapMidBefore), "Exam isOverlap Test e1SameDayOverlapMidBefore - true");
         displayResults (e1SameDayOverlapMidBefore.isOverlap(e1), "Exam isOverlap Test e1SameDayOverlapMidBefore - true");
         
         Exam e1SameDayOverlapEndBefore  = new Exam(d20200315b, "ECS 125", t1330, 300);
         displayResults (e1.isOverlap(e1SameDayOverlapEndBefore), "Exam isOverlap Test e1SameDayOverlapEndBefore - true");
         displayResults (e1SameDayOverlapEndBefore.isOverlap(e1), "Exam isOverlap Test e1SameDayOverlapEndBefore - true");
         
         Exam e1SameDayNoOverlapBefore   = new Exam(d20200315b, "ECS 125", t1330, 60);
         displayResults (!e1.isOverlap(e1SameDayNoOverlapBefore), "Exam isOverlap Test e1SameDayNoOverlapBefore - false");
         displayResults (!e1SameDayNoOverlapBefore.isOverlap(e1), "Exam isOverlap Test e1SameDayNoOverlapBefore - false");
         
         Exam e1After  = new Exam(d20200315b, "ECS 125", t1730, 60);
         displayResults (!e1.isOverlap(e1After), "Exam isOverlap Test e1After - false");
         displayResults (!e1After.isOverlap(e1), "Exam isOverlap Test e1After - false");
         
         // change e1 duration
         e1.setDuration(121);
         displayResults (e1.isOverlap(e1After), "Exam isOverlap Test e1After overlap start - true");
         displayResults (e1After.isOverlap(e1), "Exam isOverlap Test e1After overlap start - true");

         e1.setDuration(150);
         displayResults (e1.isOverlap(e1After), "Exam isOverlap Test e1After overlap mid - true");
         displayResults (e1After.isOverlap(e1), "Exam isOverlap Test e1After overlap mid - true");
         
         e1.setDuration(300);
         displayResults (e1.isOverlap(e1After), "Exam isOverlap Test e1After overlap all - true");
         displayResults (e1After.isOverlap(e1), "Exam isOverlap Test e1After overlap all - true");
         
         
         // change e1 date - non of these should be overlapping now
         e1.setDate(d20180315);
         displayResults (!e1.isOverlap(e1SameDayTimeDuration), "Exam isOverlap Test e1SameDayTimeDuration e1 date changed - false");
         displayResults (!e1.isOverlap(e1SameDayTime), "Exam isOverlap Test e1SameDayTime e1 date changed - false");
         displayResults (!e1.isOverlap(e1SameDayNoOverlapBackToBack), "Exam isOverlap Test e1SameDayOverlapStartBefore e1 date changed - false");
         displayResults (!e1.isOverlap(e1SameDayOverlapMidBefore), "Exam isOverlap Test e1SameDayOverlapMidBefore e1 date changed - false");
         displayResults (!e1.isOverlap(e1SameDayOverlapMidBefore), "Exam isOverlap Test e1SameDayOverlapEndBefore e1 date changed - false");
         
         
    }
    
    public static void examToStringTests() {
        
        // TODO:
        // uncomment the following to test your implementation
        
         Date d20200315 = new Date("March",15,2020);
         Date d20180614 = new Date("June",14,2018);
         
         
         Time t1730 = new Time(17,30);
         Time t900 = new Time(9,0);
         
         Exam e0 = new Exam(d20200315, "ECS 125", t1730, 60);
         Exam e1 = new Exam(d20180614, "MAC 1016", t900, 120);
         
         displayResults (e0.toString().equals("March 15, 2020: ECS 125: 5:30pm-6:30pm"), "Exam toString Test on new Exam(d20200315b, \"ECS 125\", t1730, 60)");
         displayResults (e1.toString().equals("June 14, 2018: MAC 1016: 9:0am-11:0am"), "Exam toString Test on new Exam(d20180315, \"MAC 1016\", t900, 120)");
         
        
    }
    
}

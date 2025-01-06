import java.util.Random;
/*
 * A4Tester.java
 *
 * The auto grading of your assignment will include tests with different values.
 *
 */
public class A4Tester {
    
    private static int testPassCount = 0;
    private static int testCount = 0;
    public static int  stressTestSize = 20000;
    
    public static void main (String[] args) {
        
        try
        {
        examListTestOne();
         
		examListTestTwo();
           
        examListResizeTest();
            
            examListRemoveAtTest();
            
            examListStressTest();
            examListRemoveAllOnDateTest();
           examScheduleTest();
            
            
            
            //            teamTest();
        }
        catch (Exception e)
        {
            System.out.println("Your code threw an Exception.");
            System.out.println("Perhaps a stack trace will help:");
            e.printStackTrace(System.out);
        }
        
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
        }
    }
    
    public static void examListTestOne() {
        
        System.out.println("ExamArrayList testing: constructor, add, get, find in max 1 element list");
        
        ExamListInterface l = new ExamArrayList();
        Time t0630 = new Time(6,30);
        Date d20200215 = new Date("February", 15,2020);
        Exam e = new Exam("CSC 115", d20200215, "ECS 125", t0630, 120);
        
        displayResults(l.size() == 0, "list constructor, size");
        l.add(e);
        
        //System.out.println(e);
        
        displayResults(l.size() == 1, "list constructor + add 1 element");
        displayResults(l.get(0) == e, "list get 1 element list");
        displayResults(l.find("CSC 110") == -1, "list find not there, 1 element list");
        displayResults(l.find("CSC 115") == 0, "list find is there, 1 element list");
        
    }
    
    public static void examListTestTwo() {
        
        System.out.println("ExamArrayList testing: add, get, find, remove");
        
        ExamListInterface l = new ExamArrayList();
        Time t0630 = new Time(6,30);
        Time t0820 = new Time(8,20);
        Time t0920 = new Time(9,20);
        Time t1600 = new Time(16,00);
        
        Date d20200215 = new Date("February", 15, 2020);
        Date d20180528 = new Date("May", 28, 2018);
        Date d20210201 = new Date("February", 01, 2021);
        Date d20180512 = new Date("May", 12, 2018);
        
        Exam e1 = new Exam("PSYC 101", d20200215, "ECS 125", t0630, 120);
        Exam e2 = new Exam("MATH 100", d20180528, "DSB 108", t0820, 60);
        Exam e3 = new Exam("CSC 110", d20210201, "MAC 1016", t0920, 270);
        Exam e4 = new Exam("ECON 100", d20180512, "ECS 125", t1600, 60);
        
        l.add(e1);
        l.add(e2);

        displayResults(l.size() == 2, "add + size, 2 element list");
        Exam eptr = l.get(0);
        Exam remaining;
        
        if (eptr == e1)
            remaining = e2;
        else
            remaining = e1;
        
        l.removeAtPos(0);
        displayResults(l.find(remaining.getCourse()) != -1, "remove + find, 1 element list");
       // System.out.println(l.size());
       // System.out.println(l.find(remaining.getCourse()));
        displayResults(l.size() == 1, "remove + size, 2 element list");
        displayResults(l.get(0) == remaining, "remove + get, 2 element list");
        
        l.removeAtPos(0);
        displayResults(l.size() == 0, "remove + size, 1 element list");
        //System.out.println(l.find(remaining.getCourse().toString()));
      //  System.out.println(l.find(remaining.getCourse()));
        displayResults(l.find(remaining.getCourse()) == -1, "remove + find empty list");
        
    }
    
    public static void examListResizeTest() {
        
        System.out.println("ExamArrayList testing resizing, add, find");
        ExamListInterface l = new ExamArrayList();
        
        int monthNum = 5500000;
        int courseNum = 6600000;
        for (int i = 0; i < 100; i++) {
            Date d = new Date(Integer.toString(monthNum+i), i, i);
            l.add(new Exam(Integer.toString(courseNum+i), d));
        }
        
        System.out.println(l.size());
        displayResults(l.size() == 100, "add + size, 100 elements");
        
        boolean passed = true;
        
        for (int i = 99; i >= 0; i--) {
            Date d = new Date(Integer.toString(monthNum+i), i, i);
            System.out.println(l.find(Integer.toString(courseNum+i)));
            if (l.find(Integer.toString(courseNum+i)) == -1)
                passed = false;
            
        }
        displayResults(passed, "find, 100 elements");
    }
    
    public static void examListRemoveAtTest() {
        
        System.out.println("ExamArrayList testing resizing, add, find, removeAtPos");
        ExamListInterface l = new ExamArrayList();
        
        int monthNum = 5500000;
        int courseNum = 6600000;
        int numElements = 100;
        for (int i = 0; i < numElements; i++) {
            Date d = new Date(Integer.toString(monthNum+i), i, i);
            l.add(new Exam(Integer.toString(courseNum+i), d));
        }
        
        int pos = l.find(Integer.toString(courseNum+10));
        Exam toRemove = l.get(pos);
        String course = new String(toRemove.getCourse());
        
        l.removeAtPos(pos);
        numElements--;
        displayResults(l.size() == numElements, "add, removeAt + size");
        displayResults(l.find(course) == -1, "add, removeAt + find");
        
        Random r = new Random();
        int numRemove = 5;
        for (int i=0; i<numRemove; i++) {
            pos = r.nextInt(numElements); // random number between 0 and numElements-1 inclusive
            toRemove = l.get(pos);
            course = new String(toRemove.getCourse());
            
            displayResults(l.find(course) == pos, "add + size, 100 elements");
            l.removeAtPos(pos);
            numElements--;
            displayResults(l.size() == numElements, "add + size, 100 elements");
            displayResults(l.find(course) == -1, "add + size, 100 elements");
            
        }
        
    }
    
    public static void examListStressTest() {
        
        System.out.println("ExamArrayList stress test.");
        
        ExamListInterface list = new ExamArrayList();
        
        int monthNum = 5500000;
        int courseNum = 6600000;
        for (int i = 0; i < stressTestSize; i++) {
            Date d = new Date(Integer.toString(monthNum+i), i, i);
            list.add(new Exam(Integer.toString(courseNum+i), d));
        }
        
        displayResults(list.size() == stressTestSize, "add + size, >10000 elements");
        
        boolean passed = true;
        
        for (int i = (stressTestSize - 1); i >= 0; i--)
            if (list.find(Integer.toString(courseNum+i)) == -1)
                passed = false;
        
        displayResults(passed, "find, >10000 elements");
        
        passed = true;
        for (int i = (stressTestSize - 1); i > 0; i--) {
            Exam toRemove = list.get(0);
            list.removeAtPos(0);
            
            if (list.find(new String(toRemove.getCourse())) != -1) {
                passed = false;
                break;
            }
            
            if (list.size() != i) {
                passed = false;
                break;
            }
        }
        displayResults(passed, "remove + find, >10000 elements");
        
    }
    
    public static void examListRemoveAllOnDateTest() {
        
        System.out.println("ExamArrayList testing removeAllOnDate");
        ExamListInterface list = new ExamArrayList();
        
        int monthNum = 5500000;
        int courseNum = 6600000;
        int numElements = 3;
        for (int i = 0; i < numElements; i++) {
            Date d = new Date(Integer.toString(monthNum+i), i, i);
            list.add(new Exam(Integer.toString(courseNum+i), d));
        }
        
        Date dateToRemove = new Date(Integer.toString(monthNum+0), 0, 0);
        String courseToRemove = Integer.toString(courseNum+0);
        displayResults((list.find(courseToRemove) != -1), "element to remove is in list");
        list.removeAllOnDate(dateToRemove);
        displayResults((list.size() == 2 &&
                        (list.find(courseToRemove) == -1)), "element removed from list");
        
        
        Date d = new Date(Integer.toString(monthNum+3), 3, 3);
        list.add(new Exam(Integer.toString(courseNum+3), d));
        d = new Date(Integer.toString(monthNum+1), 1, 1);
        list.add(new Exam(Integer.toString(courseNum+1), d));
        d = new Date(Integer.toString(monthNum+1), 1, 1);
        list.add(new Exam(Integer.toString(courseNum+1), d));
        
        dateToRemove = new Date(Integer.toString(monthNum+1), 1, 1);
        courseToRemove = Integer.toString(courseNum+1);
        displayResults(list.size() == 5 && (list.find(courseToRemove) != -1), "element to remove is in list");
        list.removeAllOnDate(dateToRemove);
        displayResults((list.size() == 2 &&
                        (list.find(courseToRemove) == -1)), "element removed from list");
        
        
        list = new ExamArrayList();
        numElements = 15;
        for (int i = 0; i < numElements; i++) {
            d = new Date(Integer.toString(monthNum+10), 10, 10);
            list.add(new Exam(Integer.toString(courseNum+10), d));
        }
        
        dateToRemove = new Date(Integer.toString(monthNum+10), 10, 10);
        courseToRemove = Integer.toString(courseNum+10);
        displayResults(list.size() == numElements && (list.find(courseToRemove) != -1), "element to remove is in list");
        list.removeAllOnDate(dateToRemove);
        displayResults((list.size() == 0 &&
                        (list.find(courseToRemove) == -1)), "element removed from list");
        
    }
    
    
    public static void examScheduleTest() {
        
        System.out.println("ExamSchedule testing - uncomment tests");
        
        Time t0630 = new Time(6,30);
        Time t0820 = new Time(8,20);
        Time t0920 = new Time(9,20);
        Time t1600 = new Time(16,00);
        Time t1020 = new Time(10,20);
        
        Date d20200215  = new Date("February", 15, 2020);
        Date d20180528a = new Date("May", 28, 2018);
        Date d20210201  = new Date("February", 01, 2021);
        Date d20180512  = new Date("May", 12, 2018);
        Date d20180528b = new Date("May", 28, 2018);
        
        Exam e1 = new Exam("PSYC 101", d20200215, "ECS 125", t0630, 120);
        Exam e2 = new Exam("MATH 100", d20180528a, "DSB 108", t0820, 60);
        Exam e3 = new Exam("CSC 110", d20210201, "MAC 1016", t0920, 270);
        Exam e4 = new Exam("ECON 100", d20180512, "ECS 125", t1600, 60);
        Exam e5 = new Exam("MATH 200", d20180528b, "ECS 108", t1020, 90);
        
        
        ExamSchedule schedule = new ExamSchedule("V00123456");
        
        displayResults(schedule.getSid().equals("V00123456"), "constructor without initial exam added  + getName");
        //System.out.println();
        displayResults(schedule.getExamCount() == 0, "constructor without initial exam added + getExamCount");
        schedule.setSid("V00999999");
        displayResults(schedule.getSid().equals("V00999999"), "setName + getName");
        
        schedule = new ExamSchedule("V00111111", e1);
        displayResults(schedule.getSid().equals("V00111111"), "constructor with exam + getName");
        displayResults(schedule.getExamCount() == 1 , "constructor with exam + getExamCount");
        
        //            System.out.println("before addExams e2,e3: \n" + schedule);
        Exam[] examsToAdde2e3 = {e2, e3};
        schedule.addExams(examsToAdde2e3);
        //            System.out.println("after addExams e2,e3: \n" + schedule);
        displayResults(schedule.getExamCount() == 3 , "addExams + getExamCount");
        
        schedule.removeExam("ECON 100");
        displayResults(schedule.getExamCount() == 3 , "removeExam not found + getExamCount");
        
        Exam[] examsToAdde4e5 = {e4, e5};
        schedule.addExams(examsToAdde4e5);
        displayResults(schedule.getExamCount() == 5 , "addExams + getExamCount");
        
        schedule.removeExam("ECON 100");
        displayResults(schedule.getExamCount() == 4 , "removeExam found + getExamCount");
        
        //            System.out.println("before clear day: \n" + schedule);
        schedule.clearDay("May", 28, 2018);
        //            System.out.println("after clear day: \n" + schedule);
        displayResults(schedule.getExamCount() == 2 , "clearDay + getExamCount");
        
        
    }
    
}

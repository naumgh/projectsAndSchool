import java.util.Arrays;
/*
 * A3Tester.java
 *
 * A partial test program for Assignment 3.
 *
 * While this program includes many test cases,
 * it is INTENTIONALLY not a comprehensive set of tests.
 * You should add your own tests to test cases not considered.
 *
 * The auto grading of your assignment will include different and additional tests.
 *
 */
public class A3Tester {
    
    private static int testPassCount = 0;
    private static int testCount = 0;
    
    private static Time t0630 = new Time(6,30);
    private static Time t0820a = new Time(8,20);
    private static Time t0820b = new Time(8,20);
    private static Time t1600 = new Time(16,00);
    
    private static Date d20200215 = new Date("February", 15,2020);
    private static Date d20180528 = new Date("May", 28,2018);
    private static Date d20210201 = new Date("February", 01,2021);
    private static Date d20180528b = new Date("May", 28,2018);
    
    private static Exam e1 = new Exam(d20200215, "ECS 125", t0630, 120);
    private static Exam e2 = new Exam(d20180528, "DSB 108", t0820a, 60);
    private static Exam e3 = new Exam(d20210201, "MAC 1016", t0820b, 270);
    private static Exam e4 = new Exam(d20180528b, "ECS 125", t1600, 60);
    
    public static void main (String[] args) {
        
        getAllExamLocationsTest();
        getExamDurationTest();
        addExamTest();
        countExamsOnDateTest();
        removeExamsWithDateTest();
        getEarliestTimeExamTest();
        
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
    
    public static void getAllExamLocationsTest() {
        
        // TODO:
        // uncomment the following to test your implementation:
        
        
         Exam[] examsEmpty = {};
         Exam[] exams4 = {e1, e2, e3, e4};
         
         String[] result;
         String[] expectedEmpty = {};
         String[] expected4 = {"ECS 125", "DSB 108", "MAC 1016", "ECS 125"};
         
         result = ExamArrayOperations.getAllExamLocations(examsEmpty);
         displayResults (Arrays.equals(result, expectedEmpty), "getAllExamLocations - empty array");
         
         result = ExamArrayOperations.getAllExamLocations(exams4);
         displayResults (Arrays.equals(result, expected4), "getAllExamLocations - non-empty array");
         
    }
    
    public static void getExamDurationTest() {
        // TODO:
        // uncomment the following to test your implementation:
        
        
         Exam[] examsEmpty = {};
         Exam[] exams4 = {e1, e2, e4, e3 };
         
         int result;
         
         result = ExamArrayOperations.getExamDuration(examsEmpty, "ECS 125");
         displayResults (result==0, "getExamDuration - empty array");
         
         result = ExamArrayOperations.getExamDuration(exams4, "ECS 125");
         displayResults (result==120, "getExamDuration - non-empty array, 1st element");
         
         result = ExamArrayOperations.getExamDuration(exams4, "DSB 108");
         displayResults (result==60, "getExamDuration - non-empty array, middle element");
         
         result = ExamArrayOperations.getExamDuration(exams4, "MAC 1016");
         displayResults (result==270, "getExamDuration - non-empty array, last element");
         
    }
    
    public static void addExamTest() {
        
        // TODO:
        // uncomment the following to test your implementation:
        
        
         Exam[] examsEmpty = {};
         Exam[] exams3 = {e1, e2, e4};
         
         Exam[] expectedEmpty = {e1};
         Exam[] expected3     = {e1, e2, e4, e3 };
         
         Exam[] result;
         
         result = ExamArrayOperations.addExam(examsEmpty, e1);
         displayResults (Arrays.equals(result, expectedEmpty), "addExam - empty array");
         
         result = ExamArrayOperations.addExam(exams3, e3);
         displayResults (Arrays.equals(result, expected3), "addExam - non-empty array");
         
    }
    
    public static void countExamsOnDateTest() {
        // TODO:
        // uncomment the following to test your implementation:
        
        
         Exam[] examsEmpty = {};
         Exam[] exams4 = {e1, e2, e4, e3};
         
         int result;
         
         result = ExamArrayOperations.countExamsOnDate(examsEmpty, new Date("February", 15, 2020));
         displayResults (result==0, "countExamsOnDate - empty array -- 0");
         
         result = ExamArrayOperations.countExamsOnDate(exams4, new Date("February", 15, 2020));
         displayResults (result==1, "countExamsOnDate - non-empty array front -- 1");
         
         result = ExamArrayOperations.countExamsOnDate(exams4, new Date("May", 28, 2018));
         displayResults (result==2, "countExamsOnDate - non-empty array mutliple -- 2");
         
         result = ExamArrayOperations.countExamsOnDate(exams4, new Date("February", 01, 2021));
         displayResults (result==1, "hasExamTest - non-empty array end -- 1");
         
         result = ExamArrayOperations.countExamsOnDate(exams4, new Date("February", 15, 2030));
         displayResults (result==0, "countExamsOnDate - non-empty array none-- 0");
         
    }
    
    public static void removeExamsWithDateTest() {
        // TODO:
        // uncomment the following to test your implementation:
        
        
         Exam[] examsEmpty = {};
         Exam[] exams4 = {e1, e2, e4, e3};
         
         
         Exam[] result;
         Exam[] expectedEmpty = {};
         Exam[] expected4RemoveFront = {e2, e4, e3};
         Exam[] expected4RemoveMultiple = {e1, e3};
         Exam[] expected4RemoveBack = {e1, e2, e4};
         Exam[] expected4RemoveNone = {e1, e2, e4, e3};
         
         result = ExamArrayOperations.removeExamsWithDate(examsEmpty, new Date("February", 15, 2020));
         displayResults (Arrays.equals(result, expectedEmpty), "removeExamsWithDate - empty array -- 0 removed");
         
         result = ExamArrayOperations.removeExamsWithDate(exams4, new Date("February", 15, 2020));
         displayResults (Arrays.equals(result, expected4RemoveFront), "removeExamsWithDate - non-empty array front -- 1 removed");
         
         result = ExamArrayOperations.removeExamsWithDate(exams4, new Date("May", 28, 2018));
         displayResults (Arrays.equals(result, expected4RemoveMultiple), "removeExamsWithDate - non-empty array mutliple -- 2 removed");
         
         result = ExamArrayOperations.removeExamsWithDate(exams4, new Date("February", 01, 2021));
         displayResults (Arrays.equals(result, expected4RemoveBack), "removeExamsWithDate - non-empty array end -- 1 removed");
         
         result = ExamArrayOperations.removeExamsWithDate(exams4, new Date("February", 15, 2030));
         displayResults (Arrays.equals(result, expected4RemoveNone), "removeExamsWithDate - non-empty array none-- 0 removed");
         
    }
    
   
   public static void getEarliestTimeExamTest() {
        // TODO:
        // uncomment the following to test your implementation:
        
        
         Exam[] exams1 = {e1};
         Exam[] examsMultiple = {e2,e3,e4};
         Exam[] examsFront = {e1, e2, e3, e4};
         Exam[] examsEnd = {e4, e2, e3, e1};
         Exam[] examsMiddle = {e3, e4, e2};
         
         Exam result;
         
         result = ExamArrayOperations.getEarliestTimeExam(exams1);
         displayResults (result==e1, "getEarliestTimeExam - one element array");
         
         result = ExamArrayOperations.getEarliestTimeExam(examsMultiple);
         displayResults (result==e2, "getEarliestTimeExam - >1 earliest");
         
         result = ExamArrayOperations.getEarliestTimeExam(examsFront);
         displayResults (result==e1, "getEarliestTimeExam - in front");
         
         result = ExamArrayOperations.getEarliestTimeExam(examsEnd);
         displayResults (result==e1, "getEarliestTimeExam - at end");
         
         result = ExamArrayOperations.getEarliestTimeExam(examsMiddle);
         displayResults (result==e3, "getEarliestTimeExam - middle");
         
    }
    
}

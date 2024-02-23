/*
 * A6Tester.java
 *
 * A partial test program for Assignment 6.
 *
 * While this program includes many test cases,
 * it is INTENTIONALLY not a comprehensive set of tests.
 * You should add your own tests to test cases not considered.
 *
 * The auto grading of your assignment will include different and additional tests.
 *
 */
public class A6Tester {
    
    private static int testPassCount = 0;
    private static int testCount = 0;
    public static int  stressTestSize = 5000;
    
    public static String listType = "recursive";
    
    public static void main (String[] args) {
        if (args.length == 1)
            listType = args[0];
        
        try {
            
            
            listTestOne();
             testToStringReverse();
            testGetPositionOfVal();
           testSumDivisibleEvenPositions();
              testRemoveValue();
          listStressTest();
            
        } catch (Exception e) {
            
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
    
    public static IntegerList createList() {
        
        if (listType.equals("linked")){
            return new IntegerLinkedList();
        } else if (listType.equals("recursive")){
            return new RecursiveIntegerLinkedList();
        } else {
            System.out.println("list type specified not supported");
            return null;
        }
    }
    
    public static void listTestOne() {
        System.out.println("testing basic functionality of addFront, addBack, size and getAtPosition");
        IntegerList list = createList();
        
        displayResults(list.size() == 0, "list constructor, size");
        list.addFront(4);
        System.out.println(list.toString());
        displayResults(list.size() == 1, "list constructor + add 1 element");
        list.addFront(7);
        System.out.println(list.toString());
        displayResults(list.size() == 2, "list constructor + add 1 element");
        displayResults(list.getAtPosition(0) == 7, "list get 2 element list");
        displayResults(list.getAtPosition(1) == 4, "list get 2 element list");
        
        list.addBack(11);
        System.out.println(list.toString());
        list.addBack(23);
       System.out.println(list.toString());
        list.addFront(15);
        displayResults(list.size() == 5, "list size + addFront+ addBack - 5 elements");
        System.out.println(list.toString());
        displayResults(list.getAtPosition(0) == 15, "list get 5 element list");
        displayResults(list.getAtPosition(1) == 7, "list get 5 element list");
        displayResults(list.getAtPosition(2) == 4, "list get 5 element list");
        displayResults(list.getAtPosition(3) == 11, "list get 5 element list");
        displayResults(list.getAtPosition(4) == 23, "list get 5 element list");
        
        list = createList();
        list.addBack(11);
        list.addBack(23);
        displayResults(list.size() == 2, "list size + addBack - 2 elements");
        displayResults(list.getAtPosition(0) == 11, "list get 2 element list");
        displayResults(list.getAtPosition(1) == 23, "list get 2 element list");
        
        list.addFront(15);
        displayResults(list.size() == 3, "list size + addBack + addFront - 3 elements");
        displayResults(list.getAtPosition(0) == 15, "list get 3 element list");
        displayResults(list.getAtPosition(1) == 11, "list get 3 element list");
        displayResults(list.getAtPosition(2) == 23, "list get 3 element list");
        
    }
    
    public static void testToStringReverse() {
        System.out.println("testing toString and reverse methods");
        IntegerList list1 = createList();
        list1.addFront(4);
        list1.addFront(7);
        list1.addBack(11);
        list1.addBack(23);
        list1.addFront(15);
        
        IntegerList list2 = createList();
        list2.addBack(11);
        list2.addBack(23);
        list2.addFront(15);
        list2.addFront(14);
        list2.addBack(12);
        
                System.out.println("list1 fwd: " + list1);
                System.out.println("list1 rev: " + list1.reverse());
                System.out.println("list2 fwd: " + list2);
               System.out.println("list2 rev: " + list2.reverse());
        //System.out.println(list1.toString());
        displayResults(list1.toString().equals("15 7 4 11 23"), "using addBack + addFront to test toString");
        displayResults(list2.toString().equals("14 15 11 23 12"), "using addBack + addFront to test toString");
        
        
        displayResults(list1.reverse().equals("23 11 4 7 15"), "using addBack + addFront to test toString");
        displayResults(list2.reverse().equals("12 23 11 15 14"), "using addBack + addFront to test toString");
        //System.out.println(list1.reverse());
    }
    
    
    public static void testGetPositionOfVal() {
        
        System.out.println("List testing: add, getAtPosition, getPositionOfVal");
        
        IntegerList list = createList();
        
        list.addFront(34);
        list.addFront(22);
        
        System.out.println(list.size());
        displayResults((list.size() == 2) && (list.getAtPosition(0) == 22) && (list.getAtPosition(1) == 34), "addFront + size +get, 2 element list");
        
        displayResults((list.getPositionOfVal(100) == -1), "addFront +getPositionOfVal, 2 element list - not found");
        displayResults((list.getPositionOfVal(22) == 0), "addFront +getPositionOfVal, 2 element list -  found");
        displayResults((list.getPositionOfVal(34) == 1), "addFront +getPositionOfVal, 2 element list -  found");
        System.out.println(list.getPositionOfVal(34));
        System.out.println(list.getPositionOfVal(22));

        list.addBack(22);
        list.addFront(2);
        list.addBack(22);
        
        displayResults((list.getPositionOfVal(34) == 2), "addFront +getPositionOfVal, 2 element list -  found");
        displayResults((list.getPositionOfVal(22) == 1), "addFront +getPositionOfVal, 2 element list -  found");
        
    }
    
    public static void testSumDivisibleEvenPositions() {
        
        System.out.println("List testing: sumDivisble, sumEvenPosition");
        
        IntegerList emptyList = createList();
        
        int[] arrayAllDivisibleBy3 = {9, 3, -6, 18};
        IntegerList listAllDivisibleBy3 = createList();
        addArray(arrayAllDivisibleBy3, listAllDivisibleBy3, true);
        
        int[] arrayNoneDivisibleBy2 = {-1, 3, -7, 17, 9};
        IntegerList listNoneDivisibleBy2 = createList();
        addArray(arrayNoneDivisibleBy2, listNoneDivisibleBy2, true);
        
        int[] arraySomeDivisibleBy5 = {3, -10, -6, 25, 34, 45};
        IntegerList listSomeDivisibleBy5 = createList();
        addArray(arraySomeDivisibleBy5, listSomeDivisibleBy5, true);
        
        int sumResult;
        
        sumResult = emptyList.sumDivisible(9);
        displayResults(sumResult == 0, "sumDivisible, emptyList");
        
        sumResult = listAllDivisibleBy3.sumDivisible(3);
        System.out.println(sumResult);

        displayResults(sumResult == (9 + 3 + -6 + 18), "sumDivisible, all Divisible");
        System.out.println(sumResult);
        System.out.println(listAllDivisibleBy3);
        

        sumResult = listNoneDivisibleBy2.sumDivisible(2);
        displayResults(sumResult == 0, "sumDivisible, none Divisible");
        
        sumResult = listSomeDivisibleBy5.sumDivisible(5);
        displayResults(sumResult == (-10 + 25 + 45), "sumDivisible, some Divisible");
        
        
        sumResult = emptyList.sumEvenPositionElements();
        displayResults(sumResult == 0, "sumEvenPositionElements, emptyList");
        
        sumResult = listAllDivisibleBy3.sumEvenPositionElements();
        System.out.println(listAllDivisibleBy3);
        displayResults(sumResult == (9 + -6), "sumEvenPositionElements, length 4");
        
        sumResult = listNoneDivisibleBy2.sumEvenPositionElements();
        displayResults(sumResult == (-1 + -7 + 9), "sumEvenPositionElements, length 5");
        
        sumResult = listSomeDivisibleBy5.sumEvenPositionElements();
        displayResults(sumResult == (3 + -6 + 34), "sumEvenPositionElements, length 6");
        
    }
    
    private static void addArray (int[] a, IntegerList l, boolean addBack) {
        for (int i=0;i<a.length;i++) {
            if (addBack)
                l.addBack(a[i]);
            else
                l.addFront(a[i]);
        }
    }
    
    
    public static void testRemoveValue() {
        
        System.out.println("IntegerList removeValue");
        
        IntegerList list = createList();
        list.removeValue(5);
        displayResults(list.size() == 0, "removeValue empty list");
        
        int num = 10;
        int p0 = num+0;
        int p1 = num+2;
        int p2 = num+1;
        int p3 = num+2;
        int p4 = num+1;
        int p5 = num+1;
        int p6 = num+4;
        int p7 = num+5;
        
        int[] vals = {p0, p1, p2, p3, p4, p5, p6, p7};
        addArray(vals, list, true);
        
        list.removeValue(p0);
        
        System.out.println(list);
        System.out.println(list.size());
        displayResults(list.size() == 7, "removeValue one element at front");
        displayResults(list.getPositionOfVal(p0) == -1, "removeValue one element at front");
        
        String sFwd = list.toString();
        String sRev = list.reverse();
        String foward = p1 + " " + p2 + " " + p3 + " " + p4 + " "  + p5 + " "  + p6 + " "  + p7;
        String reverse = p7 + " "  + p6 + " "  + p5 + " " + p4 + " " + p3 + " " + p2 + " "  + p1;
        displayResults(sFwd.equals(foward), "removeValue one element at front");
        System.out.println(list.toString());
        System.out.println(list.reverse());
        displayResults(sRev.equals(reverse), "removeValue one element at front");
        
        
        list.removeValue(p7);
        System.out.println(list);
        System.out.println(list.size());
        displayResults(list.size() == 6, "removeValue one element at end");
        displayResults(list.getPositionOfVal(p7) == -1, "removeValue one element at end");
        
        sFwd = list.toString();
        sRev = list.reverse();
        foward = p1 + " " + p2 + " " + p3 + " " + p4 + " "  + p5 + " "  + p6;
        reverse = p6 + " "  + p5 + " " + p4 + " " + p3 + " " + p2 + " "  + p1;
        displayResults(sFwd.equals(foward), "removeValue one element at end");
        displayResults(sRev.equals(reverse), "removeValue one element at end");
        
        
        list.removeValue(p2);
        
        displayResults(list.size() == 3, "removeValue multiple elements not at ends");
        displayResults(list.getPositionOfVal(p2) == -1, "removeValue multiple elements not at ends");
        
        System.out.println(list);

        sFwd = list.toString();
        sRev = list.reverse();
        foward = p1 + " " + p3 + " " + p6;
        reverse = p6 + " " + p3 + " " + p1;
        displayResults(sFwd.equals(foward), "removeValue multiple elements not at ends");
        displayResults(sRev.equals(reverse), "removeValue multiple elements not at ends");
        
        
        list.removeValue(p6);
        
        displayResults(list.size() == 2, "removeValue 1 element at end");
        displayResults(list.getPositionOfVal(p6) == -1, "removeValue 1 element at end");
        
        sFwd = list.toString();
        sRev = list.reverse();
        foward =  p1 + " " + p3;
        reverse = p3 + " " + p1;
        System.out.println(foward.toString());
        displayResults(sFwd.equals(foward), "removeValue 1 element at end");
        displayResults(sRev.equals(reverse), "removeValue 1 element at end");
        
        list.removeValue(p1);
        
        displayResults(list.size() == 0, "removeValue multiple elements to make empty");
        displayResults(list.getPositionOfVal(p1) == -1, "removeValue multiple elements to make empty");
        
        sFwd = list.toString();
        sRev = list.reverse();
        foward = "";
        reverse = "";
        displayResults(sFwd.equals(foward), "removeValue multiple elements to make empty");
        displayResults(sRev.equals(reverse), "removeValue multiple elements to make empty");
        
        list.removeValue(5);
        displayResults(list.size() == 0, "removeValue empty list");
        
    }
    
    
    
    
    public static void listStressTest() {
        IntegerList     list = createList();
        
        System.out.println("Stress test");
        
        for (int i=0;i<stressTestSize;i++) {
            list.addFront(i);
            list.addBack(i);
        }
        displayResults(list.size() == stressTestSize*2, "added stressTestSize*2 elements");
        
        boolean passed = true;
        int num = 0;
        while (num<stressTestSize && passed) {
            
            if ( list.getAtPosition(num) != ((stressTestSize-1) - num) ) {
                passed = false;
            }
            
            if ( list.getAtPosition(num+stressTestSize) != num ) {
                passed = false;
            }
            num++;
        }
        displayResults(passed, "getAtPosition stressTestSize*2 elements");
        
        
        passed = true;
        num = 0;
        while (num<stressTestSize && passed) {
            list.removeValue(num);
            if (list.getPositionOfVal(num) != -1)
                passed = false;
            num++;
        }
        displayResults(passed, "remove + getAtPosition stressTestSize values");
        displayResults(list.size() == 0, "removed stressTestSize*2 elements");
        
        
    }
}

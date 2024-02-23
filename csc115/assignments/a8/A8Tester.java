/*
 * A8Tester.java
 *
 * A test program for Assignment 8.
 *
 */

import java.util.Random;

public class A8Tester {
    private static int testPassCount = 0;
    private static int testCount = 0;
    public static boolean  	testHeapSolution = true;
    
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
    
    
    public static void testOne () {
        
        PriorityQueue 	q = createNewPriorityQueue();
        
        System.out.println("Basic testing of size, isEmpty");
        displayResults (q.size() == 0, "size on empty Q");
        
        displayResults (q.isEmpty(), "isEmpty on empty Q");
        
        q.insert(2);
        System.out.println(q.toString());
        displayResults (q.size() == 1, "size on 1 element Q");
        displayResults (!q.isEmpty(), "isEmpty on 1 element Q");

        
        q.insert(9);
        System.out.println(q.toString());
        displayResults (q.size() == 2, "size on 2 element Q");
        
        
        q.insert(12);
        System.out.println(q.toString());
        displayResults (q.size() == 3, "size on 3 element Q");

        q.insert(8);
        System.out.println(q.toString());
        displayResults (q.size() == 4, "size on 4 element Q");
     
    }
    
    
    public static void testTwo()
    {
        
        PriorityQueue q = createNewPriorityQueue();
        
        System.out.println("Basic testing of removeLow");
        q.insert(8);

        q.insert(9);

        q.insert(10);
        System.out.println(q);
        int result;
        result = ((Integer)q.removeLow()).intValue();
                 
                System.out.println("res: " + result + ":" + q);
        displayResults(result == 8, "remove on multiple element Q");
        displayResults(q.size() == 2, "remove + size on multiple element Q");
        


        result = ((Integer)q.removeLow()).intValue();
            System.out.println("res: " + result + ":" + q);
        displayResults(result == 9, "remove on multiple element Q");
        displayResults(q.size() == 1, "remove + size on multiple element Q");
        
         

        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 10, "remove + size on 1 element Q");
        displayResults(q.isEmpty(), "remove + isEmpty on 1 element Q");
        
        q = createNewPriorityQueue();
        q.insert(3);
        q.insert(2);
        q.insert(1);

        System.out.println(q);
        
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 1, "insert + remove on multiple element Q");
        displayResults(q.size() == 2, "insert + remove + size on multiple element Q");
        
        System.out.println(q);

        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 2, "insert + remove on multiple element Q");
        displayResults(q.size() == 1, "insert + remove + size on multiple element Q");
        
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 3, "insert + remove on 1 element Q");
        displayResults(q.isEmpty(), "insert + remove + size on 1 element Q");
         
    }
    public static void testExceptions()
    {
        
        PriorityQueue q = createNewPriorityQueue(2);
        
        System.out.println("Testing of exceptions");
        
        try {
            q.removeLow();
            displayResults(false, "exception should have been thrown");
        } catch (HeapFullException e) {
            displayResults(false, "different exception should have been thrown");
        } catch (HeapEmptyException e) {
            displayResults(true, "HeapEmptyException should be thrown");
        }
        q.insert(10);
        q.insert(9);
        try {
            q.insert(8);
            if(testHeapSolution)
                displayResults(false, "exception should have been thrown in heap solution");
            else
                displayResults(true, "exception should not have been thrown in linked version");
        } catch (HeapEmptyException e) {
            displayResults(false, "different exception should have been thrown");
        } catch (HeapFullException e) {
            displayResults(true, "HeapFullException should be thrown");
        }
        
    }
    public static void testThree() {
        
        PriorityQueue q = createNewPriorityQueue();
        String result;
        
        System.out.println("Testing of removeLow with Strings");
        q.insert("abc");
        q.insert("def");
        q.insert("ghi");
        
        result = ((String)q.removeLow());
        displayResults(result.equals("abc"), "insert/remove Strings");
        displayResults(q.size() == 2, "insert/remove Strings");
        
        result = ((String)q.removeLow());
        displayResults(result.equals("def"), "insert/remove Strings");
        displayResults(q.size() == 1, "insert/remove Strings");
        
        result = ((String)q.removeLow());
        displayResults(result.equals("ghi"), "insert/remove Strings");
        displayResults(q.isEmpty(), "insert/remove Strings");
        
        q = createNewPriorityQueue();
        q.insert("ghi");
        q.insert("def");
        q.insert("abc");
        
        result = ((String)q.removeLow());
        displayResults(result.equals("abc"), "insert/remove Strings");
        displayResults(q.size() == 2, "insert/remove + size Strings");
        
        result = ((String)q.removeLow());
        displayResults(result.equals("def"), "insert/remove Strings");
        displayResults(q.size() == 1, "insert/remove + size Strings");
        
        result = ((String)q.removeLow());
        displayResults(result.equals("ghi"), "insert/remove Strings");
        displayResults(q.isEmpty(), "insert/remove + isEmpty Strings");
        
    }
    
    public static void testFour()
    {
        
        PriorityQueue q = createNewPriorityQueue();
        int result;
        
        System.out.println("Testing duplicates.");
        q.insert(4);
        q.insert(1);
        q.insert(1);
        q.insert(5);
        q.insert(0);
        //        System.out.println("q after insert 4 1 1 5 0:" + q);
        
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 0, "add duplicates + remove single");

        q.insert(4);
        q.insert(1);
        q.insert(4);
        q.insert(4);

        q.insert(0);
        q.insert(5);
        q.insert(0);
        q.insert(5);

        
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 0, "add duplicates + remove duplicates");
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 0, "add duplicates + remove duplicates");
        
        
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 1, "add duplicates + remove duplicates");
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 1, "add duplicates + remove duplicates");
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 1, "add duplicates + remove duplicates");
        
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 4, "add duplicates + remove duplicates");
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 4, "add duplicates + remove duplicates");
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 4, "add duplicates + remove duplicates");
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 4, "add duplicates + remove duplicates");
        
        
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 5, "add duplicates + remove duplicates");
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 5, "add duplicates + remove duplicates");
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 5, "add duplicates + remove duplicates");
        
        displayResults(q.isEmpty(), "insert/remove + isEmpty");
         
    }
    
    
    public static void testFive()
    {
        
        PriorityQueue q = createNewPriorityQueue();
        int result;
        System.out.println("Testing insert mixed with removeLow.");
        
        q.insert(2);
        q.insert(0);
        q.insert(5);
        q.insert(7);
  
        result = ((Integer)q.removeLow()).intValue();
        displayResults( result == 0, "inserts + remove");

        q.insert(4);
        
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 2, "inserts + remove + insert + remove");

        q.insert(11);
        q.insert(2);
        q.insert(3);
        q.insert(1);

        
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 1, "inserts + remove");
        
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 2, "inserts + remove");

        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 3, "inserts + remove");
        
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 4, "inserts + remove");

        q.insert(1);
        
        result = ((Integer)q.removeLow()).intValue();
        displayResults(result == 1, "inserts + remove");
        displayResults(q.size() == 3, "inserts + remove + size");
         
    }
    
    public static boolean testRandomArray (int count)
    {
        // These tests are effectively sorting the random values
        //
        // For the heap, this is O (n log n)
        // For the linked list, this is O (n^2)
        PriorityQueue q = createNewPriorityQueue(count);
        
        System.out.println("Testing size: " + count);
        Random r = new Random();
        
        for ( int i = 0; i < count; i++ ) {
            int val = r.nextInt(1000000);
            q.insert (val);
        }
        
        int oldVal = 0; //biggest possible value val could be
        int i = 0;
        while (!q.isEmpty()) {
            int val = (int)((Integer)q.removeLow()).intValue(); // or a bug
            if ( val < oldVal )
                return false;
            oldVal = val;
            i++;
        }
        return true;
        
    }
    
    public static void stressTest() {
        /*
        
        System.out.println("Stress Tests.");
        displayResults(testRandomArray(100), "inserts + removes");
        displayResults(testRandomArray(10000), "inserts + removes");
        displayResults(testRandomArray(100000), "inserts + removes");
        
        //This takes too long using the linked list.
        if (testHeapSolution)
            displayResults(testRandomArray(1000000), "inserts + removes");
         */
    }
    
    public static PriorityQueue createNewPriorityQueue()  {
        if (testHeapSolution) {
            return new HeapPriorityQueue();
        }
        else {
            return new LinkedPriorityQueue();
        }
    }
    
    public static PriorityQueue createNewPriorityQueue(int size)  {
        if (testHeapSolution) {
            return new HeapPriorityQueue(size);
        }
        else {
            return new LinkedPriorityQueue();
        }
    }
    
    public static void testPassenger ()
    {
        
        System.out.println("Testing Passenger creation, compareTo and equals.");
        Passenger p1 = new Passenger(3, "LeBron James", "GHN123", new Time(12,24));
        Passenger p2 = new Passenger(0, "Lizzo", "HA192B", new Time(12,24));
        Passenger p3 = new Passenger(3, "Serena Williams", "ABN456", new Time(12,24) );
        Passenger p4 = new Passenger(0, "S. Williams", "ABN456", new Time(9,14) );
        
        displayResults(p1.compareTo(p2) > 0, "testing Passenger compareTo");
        displayResults(p2.compareTo(p1) < 0, "testing Passenger compareTo");
        displayResults(p1.compareTo(p1) == 0, "testing Passenger compareTo");
        displayResults(p1.compareTo(p3) == 0, "testing Passenger compareTo");
        displayResults(p1.compareTo(p4) > 0, "testing Passenger compareTo");
        displayResults(p4.compareTo(p1) < 0, "testing Passenger compareTo");
        displayResults(p3.equals(p4), "testing Passenger equals");
        
    }
    
    public static void testBoardingGate()
    {
        
        System.out.println("Testing adding/removing passengers from BoardingGate.");
        Passenger p1 = new Passenger(3, "LeBron James", "GHN123", new Time(12,24));
        Passenger p2 = new Passenger(4, "Lizzo", "HA192B", new Time(12,24));
        Passenger p3 = new Passenger(3, "Serena Williams", "ABN456", new Time(12,24));
        Passenger p4 = new Passenger(1, "Kyle Lowry", "GHN123", new Time(12,24));
        Passenger p5 = new Passenger(4, "Justin Trudeau", "XCV92B", new Time(10,24));
        Passenger p6 = new Passenger(0, "Bianca Andrescu", "TENNI5", new Time(12,24));

        BoardingGate gate = new BoardingGate();
        displayResults(gate.numPassengersWaiting() == 0, "testing BoardingGate constructor + numPassengersWaiting");

        gate.addPassenger(p1);
        gate.addPassenger(p2);
        gate.addPassenger(p3);
        gate.addPassenger(p4);
        gate.addPassenger(p5);

        displayResults(gate.numPassengersWaiting() == 5, "testing BoardingGate addPassenger + numPassengersWaiting");
        Passenger nextP = gate.nextPassenger();
//        System.out.println(nextP);
        displayResults(p4.equals(nextP), "testing BoardingGate addPassenger + numPassengersWaiting");

        gate.addPassenger(p6);
        displayResults(gate.numPassengersWaiting() == 5, "testing BoardingGate addPassenger + numPassengersWaiting");

        nextP = gate.nextPassenger();
        displayResults(p6.equals(nextP), "testing BoardingGate addPassenger + nextPassenger");
        nextP = gate.nextPassenger();
        displayResults(p1.equals(nextP), "testing BoardingGate addPassenger + nextPassenger");
        displayResults(gate.numPassengersWaiting() == 3, "testing BoardingGate addPassenger + numPassengersWaiting");

        nextP = gate.nextPassenger();
        displayResults(p3.equals(nextP), "testing BoardingGate addPassenger + nextPassenger");
        nextP = gate.nextPassenger();
        displayResults(p5.equals(nextP), "testing BoardingGate addPassenger + nextPassenger");
        nextP = gate.nextPassenger();
        displayResults(p2.equals(nextP), "testing BoardingGate addPassenger + nextPassenger");
        displayResults(gate.numPassengersWaiting() == 0, "testing BoardingGate addPassenger + numPassengersWaiting");
        
        nextP = gate.nextPassenger();
        displayResults(nextP == null, "testing BoardingGate nextPassenger - no more ppassengers");

        BoardingGate smallPlane = new BoardingGate(2);
        smallPlane.addPassenger(p1);
        smallPlane.addPassenger(p2);

        try {
            smallPlane.addPassenger(p3);
            displayResults(true, "testing BoardingGate addPassenger to full BoardingGate - should get here without exception");
        } catch (HeapFullException e) {
            displayResults(false, "testing BoardingGate addPassenger to full BoardingGate - should not get here");
        }
         
    }
    
    public static void main (String[] args) {
        if (args.length != 0 && args[0].equals("linked")) {
            testHeapSolution=false;
        }
        
        System.out.println("Testing " + (testHeapSolution ? "Heap" : "Linked" ) + " implementation.");
        testOne();
        testTwo();
        testExceptions();
        testThree();
        testFour();
        testFive();
        stressTest();
        
        System.out.println("Testing Application using Priority Queue.");
        testPassenger();
        testBoardingGate();
        
        System.out.println("Passed " + testPassCount + "/" + testCount + " tests");
    }
}

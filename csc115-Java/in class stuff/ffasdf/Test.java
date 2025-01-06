public class Test {
    public static void main (String[] args) {
        
        IntegerLinkedList emptyList = new IntegerLinkedList();
//        // Q0. write and test a recursive method that will
//        //  print the absolute values of all elements in the list
//        System.out.println("abs, list was:\n" + emptyList);
//        emptyList.abs();
//        System.out.println("abs emptyList, should print an empty line:\n" + emptyList);
//
//        IntegerLinkedList myList0 = new IntegerLinkedList();
//        myList0.addBack(-10);
//        myList0.addBack(9);
//        myList0.addBack(-3);
//        myList0.addBack(12);
//
//        System.out.println("abs, list was:\n" + myList0);
//        myList0.abs();
//        System.out.println("abs, should print 10 9 3 12:\n" + myList0);
//
//        
//        // Q1. write and test a recursive method that will
//        //  sum all of the elements in the list
//        
        int result = emptyList.sum(); 
        System.out.println("sum emptyList, should print 0: " + result);
        IntegerLinkedList myList1 = new IntegerLinkedList();     
        myList1.addBack(-10); 
        myList1.addBack(9);
        myList1.addBack(-3);
        myList1.addBack(12); 
        result = myList1.sum();
        System.out.println("sum emptyList, should print " + (-10 + 9 + -3 + 12) + ": " + result);
        
        
        // Q2. write and test a recursive method that will
        //  find and return the largest number in the list
        //  assume there is at least one element in the list
        IntegerLinkedList myList2a = new IntegerLinkedList();
        myList2a.addBack(10);
        int max = myList2a.max();
        System.out.println("max emptyList, should print 10: " + max);

        IntegerLinkedList myList2b = new IntegerLinkedList();
        myList2b.addBack(-10);
        myList2b.addBack(-9);
        myList2b.addBack(-3);
        myList2b.addBack(-12);

        max = myList2b.max();
        System.out.println("max should print -3: " + max);
        
        myList2b.addBack(3);
        max = myList2b.max();
        System.out.println("max should print 3: " + max);
        
        myList2b.addFront(40);
        max = myList2b.max();
        System.out.println("max should print 40: " + max);
        
        
        // Q3. write and test a recursive method that will
        //  determine whether all elements are above a given threshold
        boolean above = emptyList.allAbove(10);
        System.out.println("allAbove emptyList, should print true: " + above);
        
        IntegerLinkedList myList3 = new IntegerLinkedList();
        myList3.addBack(40);
        myList3.addBack(10);
        myList3.addBack(9);
        myList3.addBack(3);
        myList3.addBack(12);
        myList3.addBack(3);
        
        // myList has: 40 10 9 3 12 3
        above = myList3.allAbove(3);
        System.out.println("allAbove should print false: " + above);
        
        above = myList3.allAbove(0);
        System.out.println("allAbove should print true: " + above);
        
        
//        // Q4. write and test a recursive method that will
//        //  print the values at a given position
//        IntegerLinkedList myList4 = new IntegerLinkedList();
//        myList4.addBack(-10);
//        myList4.addBack(7);
//        myList4.addBack(-3);
//        myList4.addBack(12);
//        myList4.addBack(1);
//        myList4.addBack(14);
//        
//        System.out.println("printAtPosition, should print -10: ");
//        myList4.printAtPosition(0);
//        System.out.println("printAtPosition, should print -3: ");
//        myList4.printAtPosition(2);
//        System.out.println("printAtPosition, should print 14:");
//        myList4.printAtPosition(5);
//        
//        
//        // Q5. write and test a recursive method that will
//        //  determine whether a list is strictly decreasing by 1
//        //  ie. 5 4 3 2 is strictly decreasing by 1
//        //  ie. 5 3 2 1 is NOT strictly decreasing by 1
//        boolean isDecreasing = emptyList.isStrictlyDecreasing();
//        System.out.println("emptyList, should print true: " + isDecreasing);
//        
//        IntegerLinkedList myList5a = new IntegerLinkedList();
//        myList5a.addBack(-10);
//        
//        isDecreasing = myList5a.isStrictlyDecreasing();
//        System.out.println("isStrictlyDecreasing list -10, should print true: " + isDecreasing);
//        
//        IntegerLinkedList myList5b = new IntegerLinkedList();
//        myList5b.addBack(3);
//        myList5b.addBack(5);
//        myList5b.addBack(6);
//        myList5b.addBack(7);
//        
//        isDecreasing = myList5b.isStrictlyDecreasing();
//        System.out.println("isStrictlyDecreasing list 3 5 6 7, should print false: " + isDecreasing);
//        
//        IntegerLinkedList myList5c = new IntegerLinkedList();
//        myList5c.addBack(7);
//        myList5c.addBack(7);
//        myList5c.addBack(5);
//        myList5c.addBack(4);
//        
//        isDecreasing = myList5c.isStrictlyDecreasing();
//        System.out.println("isStrictlyDecreasing list 7 7 5 4, should print false: " + isDecreasing);
//        
//        IntegerLinkedList myList5d = new IntegerLinkedList();
//        myList5d.addBack(7);
//        myList5d.addBack(6);
//        myList5d.addBack(5);
//        myList5d.addBack(4);
//        
//        isDecreasing = myList5d.isStrictlyDecreasing();
//        System.out.println("isStrictlyDecreasing list 7 6 5 4, should print true: " + isDecreasing);
//        
        
    }
}

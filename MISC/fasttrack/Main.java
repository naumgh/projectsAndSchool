public class Main {
    public static void main(String[] args) {

        System.out.println("Hello, World!");

        // object types: String, Integer, Double, Character, Boolean, Long, Short, Byte
        // (heap)
        // function and method calls are allocated on the stack
        // objects are allocated on the heap and are referenced by a pointer on the
        // stack
        // any object created on the heap has global access
        // garbage colletion runs on the heap

        int x = 5;

        // stack:
        // [int x = 5, String helloWorld]

        // heap:
        // [String Pool:
        // String helloWorld = "what's up?" (memory address 0x1234 given to println,
        // VALUE stored inside object)]

        String helloWorld = "what's up?";
        char y = 'a';
        System.out.println(x);
        System.out.println(y);
        System.out.println(helloWorld);

        // java operators: arithmatic (usually infix)
        System.out.println(x % 2);
        System.out.println(++x); // prefix increment
        System.out.println(x++); // postfix increment
        // these two incements are not the same, the first one increments x before
        // printing it, the second one increments x after printing it

        // assgnment operators: =, +=, -=, *=, /=, %=
        x += 5;
        x -= 5;
        x /= 5;
        x *= 5;
        x %= 5;

        // comparison operators: ==, !=, >, <, >=, <= (equals)
        // logical operators: &&, ||, !
        // bitwise operators: &, |, ^, ~, <<, >>, >>> (unsigned right shift)

        // branching logic: if, else if, else, switch

        int totalSugarInGlass = 0;
        int sugar = 2;
        int maxSugar = 10;
        /*
         * if (sugar <= maxSugar) {
         * totalSugarInGlass += sugar;
         * } else if (sugar == maxSugar) {
         * totalSugarInGlass += maxSugar;
         * } else {
         * System.out.println("we only allow 10tsp of sugar in a glass");
         * }
         * System.out.println("total sugar in glass: " + totalSugarInGlass);
         * 
         * // looping logic: for, while, do while
         * 
         * while (totalSugarInGlass < maxSugar) {
         * totalSugarInGlass += sugar;
         * System.out.println("total sugar in glass: " + totalSugarInGlass);
         * }
         * 
         * do {
         * totalSugarInGlass += sugar;
         * System.out.println("total sugar in glass: " + totalSugarInGlass);
         * } while (totalSugarInGlass < maxSugar);
         * 
         * 
         * // for loop
         * // dont need any local varaibles in beginning of the loop
         * for ( ; totalSugarInGlass < maxSugar;
         * totalSugarInGlass += sugar) {
         * System.out.println("total sugar in glass: " + totalSugarInGlass);
         * }
         * 
         * // arrays object type, not a primitive type. refrences memory address in the
         * heap
         * //stack[numbers = 0x1234]
         * // heap[numbers = {0:1, 1:2, 2:3, 3:4, 4:5}] built in arrays are of static
         * size
         */
        int[] numbers = new int[5]; // creating objects on the heap
        numbers[0] = 4;
        // System.out.println("numbers: " + numbers); // prints the memory address of
        // the array object
        int count = 0;
        for (int i = 0; i < numbers.length; i++, count++) {
            numbers[i] = count;
        }

        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }
        // newish java 8 array syntax:

        // this is stupid, but it works:
        int[] numbersNewSyntax = new int[] { 1, 2, 3, 4, 5 }; // creating objects on
        int max = (int) (Math.random() * 10) + 1;
        int current_number = 6;
        for (int i = 0; i < max; i++, current_number++) {
            int temp[] = new int[numbersNewSyntax.length + 1];
            for (int j = 0; j < numbersNewSyntax.length; j++) {
                temp[j] = numbersNewSyntax[j];
            }
            temp[temp.length - 1] = current_number;
            numbersNewSyntax = temp;
        }

        for (int i = 0; i < numbersNewSyntax.length; i++) {
            System.out.println(numbersNewSyntax[i] + "here");
        }

        System.out.println("numbersNewSyntax: " + numbersNewSyntax); // prints the
        numbersNewSyntax = new int[] { 1, 2, 3, 4, 5, 6, 7 }; // creating objects on the heap
        System.out.println("numbersNewSyntax: " + numbersNewSyntax); // allocates to new memeory address who knew?
        add(5, 6); // calls the add method, which is a static method in this class arguments are
                   // passed by
        concat("hello", "world"); // calls the concat method, which is a static method in this class
    }

    public static int add(int a, int b) { // static method, can be called without creating an object of the class
        // a and b would be considered 'parameter variables' in this case
        return a + b;
    }

    public static String concat(String a, String b) {
        return a + b;
    }

}
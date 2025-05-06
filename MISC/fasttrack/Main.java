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

        //java operators: arithmatic (usually infix)
        System.out.println(x % 2);
        System.out.println(x++);


    }

}
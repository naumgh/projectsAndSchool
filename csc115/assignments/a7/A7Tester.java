public class A7Tester {
    private static int testPassCount = 0;
    private static int testCount = 0;
	
	public static void main(String[] args) {
        try {
            
            stackTest();
			calculatorTest();
            
        } catch (Exception e) {
            
            System.out.println("Your code threw an Exception.");
            System.out.println("Perhaps a stack trace will help:");
            e.printStackTrace(System.out);
        }
        System.out.println("Passed " + testPassCount + "/" + testCount + " tests");
	}
	
    public static void stackTest() throws StackException {
        System.out.println("testing basic functionality of Stack");
        StackArray<Integer> stack = new StackArray<>(10);
		
        displayResults(stack.isEmpty(), "initial stack is empty");
		
		stack.push(4);
		displayResults(!stack.isEmpty(), "stack is not empty after push");
		displayResults(stack.peek()==4 && !stack.isEmpty(), "stack has right element and is not empty after peek");
		displayResults(stack.pop()==4 && stack.isEmpty(), "stack has right element and is  empty after pop");
		
		stack.push(5);
		stack.push(6);
		stack.push(7);
		displayResults(stack.pop()==7 && !stack.isEmpty(), "stack has right element and is empty not after pop");
		displayResults(stack.pop()==6 && !stack.isEmpty(), "stack has right element and is empty not after pop");
		displayResults(stack.pop()==5 && stack.isEmpty(), "stack has right element and is empty after pop");
		
		
		stack.push(5);
		stack.push(6);
		stack.push(7);
		stack.popAll();
		
        displayResults(stack.isEmpty(), "popall stack is empty");
		stack.push(1);
		stack.push(2);
		stack.push(3);
		stack.push(4);
		stack.push(5);
		stack.push(6);
		stack.push(7);
		stack.push(8);
		stack.push(9);
		stack.push(10);
		
		try {
			stack.push(11);
			displayResults(false, "stack should through exception when it is full");
			
		} catch (StackException e) {
			displayResults(true, "stack should through exception when it is full");
		}
		
    }
	
    public static void calculatorTest() throws Exception{
		String[] e1 = {"1", "1", "+"};
		String[] e2 = {"15", "7", "1", "1", "+", "-", "/", "3", "*", "2", "1", "1", "+", "+", "-"};
		String[] e3 = {"15", "7", "1", "1", "3", "5", "7", "9", "3", "+", "+", "+", "+", "+", "+", "+", "+" };
		String[] e4 = {"1", "+", "1"};
		String[] e5 = {"1", "&", "1"};
		String[] e6 = {"2147483647", "10", "+"};
		String[] e7 = {"-2147483647", "10", "-"};
		String[] e8 = {"30", "0", "/"};
		RPNCalculator c = new RPNCalculator(4);
		
		try {
			displayResults(c.calculate(e1)==2, "1 1 + should be 2" );
			//System.out.println(e1.toString());
			displayResults(c.calculate(e2)==5, "calculate(e2) should be 5" );
		} catch (Exception e) {
			throw e;
			//throw new RuntimeException("Unexpected exception");
		}
		
		try {
			c.calculate(e3);
			displayResults(true, "calculate(e3) should not throw an exception");
		} catch (CalculatorException e) {
			displayResults(false, "calculate(e3) should not throw an exception");
		}
		
	    c = new RPNCalculator(4);
		
		try {
			c.calculate(e4);
			displayResults(false, "calculate(e4) should throw an exception: Invalid Expression");
		} catch (CalculatorException e) {
			displayResults(e.getMessage().equals("Invalid expression"), "calculate(e4) should throw an exception: Invalid Expression");
		}
		
		try {
			c.calculate(e5);
			displayResults(false, "calculate(e5) should throw an exception: Invalid Token");
		} catch (CalculatorException e) {
			displayResults(e.getMessage().equals("Invalid token"), "calculate(e5) should throw an exception: Invalid Token");
		}
		
		try {
			c.calculate(e6);
			displayResults(false, "calculate(e6) should throw an exception: Integer Overflow");
		} catch (CalculatorException e) {
			displayResults(e.getMessage().equals("integer overflow"), "calculate(e6) should throw an exception: Integer Overflow");
		}
		
		try {
			c.calculate(e7);
			displayResults(false, "calculate(e7) should throw an exception: Integer Underflow");
		} catch (CalculatorException e) {
			displayResults(e.getMessage().equals("integer underflow"), "calculate(e7) should throw an exception: Integer Underflow");
		}
		
		try {
			c.calculate(e8);
			displayResults(false, "calculate(e8) should throw an exception: Division By Zero");
		} catch (CalculatorException e) {
			displayResults(e.getMessage().equals("division by zero"), "calculate(e8) should throw an exception: Division By Zero");
		}
		
	}
		
	
    
    public static void displayResults (boolean passed, String testName) {
        /* There is some magic going on here getting the line number
         * Borrowed from:
         * http://blog.taragana.com/index.php/archive/core-java-how-to-get-java-source-code-line-number-file-name-in-code/
         */
        testCount++;
        if (passed)
        {
            System.out.println ("Passed test: " + testCount + ": " + testName);
            testPassCount++;
        }
        else
        {
            System.out.println ("Failed test: " + testName + " at line "
                                + Thread.currentThread().getStackTrace()[2].getLineNumber());
        }
    }
}
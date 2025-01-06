import java.math.BigInteger; 
// imported for you, so you can use BigInteger objects to detect integer over/underflows
// delete if you want to do this differently

public class RPNCalculator{
	private Stack<String> stack;
	private int size;
	
	public RPNCalculator (int initSize) {
// create a new StackArray of Strings 


		stack = new StackArray<>(initSize);
		this.size = initSize;
		

// and set the size field to the provided parameter initSize
	}
	 
	public int calculate(String[] expression) throws CalculatorException{
		String stringreturnvalue;
		String operand1;
		String operand2;
		
		for(int x = 0; x < expression.length; x++){
			if(expression[x].equals("+") || expression[x].equals("-") || expression[x].equals("/") || expression[x].equals("*")){
				
				try{
					 operand1 = stack.pop();
					 operand2 = stack.pop();
					this.size -= 1;
				}

				catch(StackException q){
					throw new CalculatorException("Invalid expression");
				}	
				
				try{
					stringreturnvalue = compute(expression[x], operand1, operand2);
					stack.push(stringreturnvalue);
					this.size += 1;
				}
				
				catch(StackException e){
					Stack<String>tmp1 = new StackArray<>(size);
					Stack<String>tmp2 = new StackArray<>(size * 2);
					System.out.println("test");
					

					for(int z = 0; z < size; z++){
						try{
							String val0 = stack.pop();
							tmp1.push(val0);
						}

						catch(StackException uuu){

						}
						
					}

					for(int y = 0; y < size; y++){
						try{
							String val1 = tmp1.pop();
							tmp2.push(val1);
						}

						catch(StackException z1){

						}

						
					}
				}

			}else{
					
				try{
					//System.out.println(expression[x]);
					try{
						Integer.parseInt(expression[x]);
					}

					catch(Exception abcd){
						throw new CalculatorException("Invalid token");
					}
						stack.push(expression[x]);
						this.size += 1;
					//this.size -= 1;
				}

				catch(StackException f){
					Stack<String>tmp1 = new StackArray<>(size);
					Stack<String>tmp2 = new StackArray<>(size * 2);
					for(int z = 0; z < size; z++){
						
						try{
							String val0 = stack.pop();
							tmp1.push(val0);
						}
							
						catch(StackException e){

						}

					}

					for(int y = 0; y < size; y++){
						
						try{
							String val1 = tmp1.pop();
							tmp2.push(val1);
						}
						catch(StackException g){

						}
					}

					stack = tmp2;
					try { stack.push(expression[x]);} catch (StackException nn) {}
				}
			

			}
		}
		
		try{
			int retaurn = Integer.parseInt(stack.pop());
			return retaurn;
		}

		catch(Exception ggggg){

		}
		
		//String popped = 

		//compute(operator, operand1, operand2);

		// implement the main calculation algorithm here
		
		// remember: you can use Integer.parseInt(s) to convert a string to an integer
		return 0;
		//System.out.println(return_value);
		//return 0; // this line is only here to this compiles - replace with algorithm
	} 
	
	// remember: you can define private helper methods. That improves code-readability
	// for example: we recommend that you define a private "compute" method that carries out
	// one primitive computation
	
	
	private String compute (String operator, String operand1, String operand2) throws CalculatorException{ 
		int compute = 0;

		
		

		if(operator.equals("+")){
	

			compute = Integer.parseInt(operand2) + Integer.parseInt(operand1);
			
			 if(compute < 0){
		    	throw new CalculatorException("integer overflow");
		    }

		   /*
		    if(compute > 0 && operand2 < 0 || operand1 < 0){
		    	throw new CalculatorException("integer underflow");
		    }
		*/

		/*
		catch(InvalidTokenException e){
			return "integer overflow"; 
		}
		
		*/
		}else if(operator.equals("-")){
			compute = Integer.parseInt(operand2) - Integer.parseInt(operand1);
		
			 if(compute > 0 && Integer.parseInt(operand2) < 0 && Integer.parseInt(operand1) > 0){
			 	throw new CalculatorException("integer underflow");
			 }else if(compute < 0 && Integer.parseInt(operand2) < 0 && Integer.parseInt(operand1) < 0)
			 	throw new CalculatorException("integer overflow");
		 /*   
		    if(compute < 0 && operand2 > 0 || operand1 > 0){
		    	throw new CalculatorException("integer overflow");
		    }

		   */

		}else if(operator.equals("/")){
			if(!(operand1.equals("0"))){
				compute = Integer.parseInt(operand2) / Integer.parseInt(operand1);	

				
			}else{
				throw new CalculatorException("division by zero");
			}

		}else if (operator.equals("*")){
			compute = Integer.parseInt(operand2) * Integer.parseInt(operand1);
		}else{
			throw new CalculatorException("Invalid token");
		}

		

		//int compute = Integer.parseInt(operand1) + operator + Integer.parseInt(operand2);
		String str_compute = "";
		str_compute = Integer.toString(compute);
		return str_compute;

	}
	
	
}
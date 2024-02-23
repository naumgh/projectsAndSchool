public class StackArrayBased implements Stack {
    private static final int INIT_SZ = 4;
    private char[] data;
    private int top;
    // notice there is no count
   // private int count;

    public StackArrayBased() { 
        data = new char[INIT_SZ];
        top = -1;
        //count = INIT_SZ;
    }

    public int size() {
       
        return this.top + 1;
    }

    public boolean isEmpty() {
        return this.top == -1;
        
    }

    public void push(char val) {
    
        if(top + 1 == data.length){
            doubleArray();
        }

            
      data[++top] = val; 
    }

    public void doubleArray(){
        char [] newArray;

        newArray = new char[data.length * 2];
        for(int i = 0; i < data.length; i++){
            newArray[i] = data[i];
        }
        data = newArray;
    }


    public char pop() {
        char x = 'a';                        
        if(isEmpty()){
            throw new RuntimeException("f in chat bois");
        }
        
        x = data[top];
    

        top--;
        return x;
    }


    public char peek() {

        return 'a';
    }


    public void makeEmpty() {

    }

    public String toString() {
        String result = "{";


        result += "}";
        return result;
    }
}


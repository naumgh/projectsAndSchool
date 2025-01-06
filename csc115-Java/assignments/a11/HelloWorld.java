public class HelloWorld{
    public static void variablePractice(){
	int x = 3;
	int y = 5;
	double z = 2.7;

	System.out.println("x:" + x);
	System.out.println("x/y:" + x/y);
	System.out.println("x + y:" + x + y);
	System.out.println("x + y:" +(x + y));

	double d;
	
	d = x;
	System.out.println("d:" + d);
	d = z;
    }

    public static void main(String[] args){
        System.out.println("Hello World.");
        variablePractice();
    }
}
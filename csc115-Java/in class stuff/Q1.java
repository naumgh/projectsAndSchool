public class Q1 {

	public static void main(String args[]) {
		int[] a = {2, 3, 4};
		int v = 3;
		
		System.out.println("a: ");
		
		for(int i=0; i<a.length; i++)
			System.out.println(a[i]);
		
		System.out.println();
		foo(a, v);

		System.out.println("a: ");
		
		for(int i=0; i<v; i++)
		System.out.println(a[i]);
		System.out.println();
	}


	public static int foo(int[] a, int v) {

		v--;
		for(int i=1; i<v; i++)
			a[i] *= v;
		
		System.out.println("a: ");
		
		for(int i=0; i<v; i++)
			System.out.println(a[i]);
		
		System.out.println();
		
		return v;
	}
}
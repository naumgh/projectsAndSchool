public class longest_sequence {
	
	public static void main(String[] args) {
		
		int[] data = {2, 3, 1, 7};
		
		int count = 4;
		
		foo( data );
		
		System.out.println(data[0]);
		
		
		System.out.println(data[3]);
		
		
		System.out.println(count);
		
		}
		
		
		public static int foo(int[] array) {
			
			
			
			int count = 0;
			
			for (int i = 0; i < array.length; i++) {  // the remainder when dividing array[i] by 2// For example://  3 % 2 is 1//  4 % 2 is 0
			if (array[i] % 2 != 0) {
				
				array[i] *= 2;count++;
				
				} 
				
				
			}
			
			
			return count;
			
			}
			
}
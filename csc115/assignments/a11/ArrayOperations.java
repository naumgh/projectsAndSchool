import java.lang.Math;

/*
 * ArrayOperations
 * DO NOT use builtin java Arrays mehthods
 * A class with basic array methods to
 *  - print the values in an array
 *  - calculate the product of the values in an array
 *  - calculate the minimum of the values in an array
 *  - calculate the maximum of the values in an array
 *  - determine the equality to 2 arrays
 *  -
 *
 */
public class ArrayOperations {
    /*
     * printArray
     *
     * Purpose: prints all the values in the array to the console
     *  example format:  {1,2,3,4}
     *
     * Parameters: an array of integers
     *
     * Returns: void
     *
     */
    public static void printArray ( int[] array ) {
        System.out.print("{");
        for(int i=0; i<array.length; i++) {
            
            System.out.print(array[i]);
            if(i<array.length-1)
                System.out.print(",");
        }
        
        System.out.println("}");
    }
    
    /*
     * arrayProduct
     *
     * Purpose: computes the product of all values in the input array
     *  NOTE: product of 3 numbers n1, n2 and n3 = n1*n2*n3
     *  NOTE: product of no numbers = 1
     *
     * Parameters: an array of integers
     *
     * Returns: product of all values in the array
     *
     */
    public static int arrayProduct ( int[] array ) {
        int product = 1;
        for(int q = 0; q < array.length; q++){
            product *= array[q];
        }
        // TODO...
        
        return product;
    }
    
    /*
     * arrayMax
     *
     * Purpose: finds the maximum value in the input array
     *
     * Parameters: an array of integers
     *
     * Preconditions:
     *  array contains at least one element
     *
     * Returns: maximum value in the array
     *
     */
    public static int arrayMax ( int[] array ){
       int max_value = 0;  
            for(int x = 0; x < array.length; x++){
            
               if(array[x] > max_value){
                   max_value = array[x];
        
                }
       
        }   

       return max_value;
    }
    
    
    // TODO...
    
    /*
     * arrayMin
     *
     * Purpose: finds the minimum value in the input array
     *
     * Parameters: an array of integers
     *
     * Preconditions:
     *  array contains at least one element
     *
     * Returns:  minimum value in the array
     *
     */
    public static int arrayMin( int[] array ){
            int min_value = 1000;
            for(int x = 0; x < array.length; x++){
               
               if(array[x] < min_value){
                   min_value = array[x];
        
                }
       
        }   

       return min_value;
    }
    
    
    
    
    // TODO...
    
    
    /*
     * arraysEqual
     *
     * Purpose: determines whether the two arrays are equal
     *      where equal means array1 and array2 are the same length
     *      and the contain the same values in the same order
     *
     * Parameters: two arrays of integers
     *
     * Returns: true if the are equal, false otherwise
     *
     *
     *
     */
    
    public static boolean arraysEqual(int [] array1, int [] array2){
        
        boolean troof = false;
    
        
        int a1 = array1.length;
        int a2 = array2.length;
        if(a1 != a2){
            return troof;
        }
        for(int x = 0; x < array1.length; x++){
            if(array1[x] == array2[x]){
                troof = true;
            }else{
                troof = false;
                return troof;
                
            }
            
        }
        return troof;
    }
        
        
        
        
    
    // TODO...
    
    /*
     * arrayRange
     *
     * Purpose: determines the range of values in inputArray
     *  as the lowest value and the highest value in the inputArray
     *
     * Parameters: int[] - array of integers
     *
     * Preconditions:
     *    inputArray contains at least one element
     *
     * Returns: int[] - a 2 element array with the lowest and highest values
     *  found in inputArray at index 0 and 1 respectively of the result array
     *
     */
    public static int[] arrayRange(int [] array0){
        int new_array[] = new int[2];
        int max_array = arrayMax(array0);
        int min_array = arrayMin(array0);
        
        new_array[0] = min_array;
        new_array[1] = max_array;
        
        return new_array;
        
        
        
    }
    
    
    // TODO...
    
    /*
     * areAllAbove
     *
     * Purpose: determines whether all values in array are above threshold
     *
     * Parameters: int[] - array of integers
     *             int - threshold that numbers must be above
     *
     * Returns: boolean - true is all are above, false otherwise
     *
     */
    // TODO...
    public static boolean areAllAbove(int[] array, int t){
            boolean troof = false;
            for(int x = 0; x < array.length; x++){
            if(array[x] > t){
                troof = true;
              
            }else{
                troof = false;
                return troof;
            
            }
        }
        return troof;
    }
            
            
           
            
        
    

    /*
     * contains
     *
     * Purpose: determines whether the values in lookingFor are strictly
     *  contained in searchArray in the same order
     *
     * Parameters: int[] - array of integers being looked for
     *             int[] - array of integers being looked in
     *
     * Returns: boolean - true is all are above, false otherwise
     *
     */
    
    public static boolean contains(int [] lookfor, int [] lookin){
        for(int a = 0; a < lookin.length; a++){
            for(int x = 0; x < lookfor.length; x++){
                try {
                    if(lookin[a] == lookfor[x]){
                        if(lookin[a+1] == lookfor[x+1]){
                            if(lookin[a+2] == lookfor[x+2]){
                            return true;
                        }
                    }
                    
                }   
            }
            catch(ArrayIndexOutOfBoundsException exception){
                return false;
            }

            }
        
        }
        return false;
    } 
}
    


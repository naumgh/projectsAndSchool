/*
 * HeapPriorityQueue.java
 *
 * An implementation of a minimum PriorityQueue using a heap.
 * based on the implementation in "Data Structures and Algorithms
 * in Java", by Goodrich and Tamassia
 *
 * This implementation will throw a Runtime, HeapEmptyException
 *	if the heap is empty and removeLow is called.
 *
 * This implementation will throw a Runtime, HeapFullException
 *	if the heap is full and insert is called.
 *
 */

public class HeapPriorityQueue implements PriorityQueue {
    
    protected final static int DEFAULT_SIZE = 10000;

    protected Comparable[] storage;
    protected int currentSize;

    /* constructor
     *
     * PURPOSE:
     *  initializes storage to new Comparable[] of DEFAULT_SIZE
     *      and initializes currentSize to 0
     *
     * PARAMETERS:
     *  none
     */

    public HeapPriorityQueue(){
    	storage = new Comparable[DEFAULT_SIZE];
    	this.currentSize = 0;
    }

    
    /* constructor
     *
     * PURPOSE:
     *  initializes storage to new Comparable[] of given size
     *      and initializes currentSize to 0
     *
     * PARAMETERS:
     *  int size
     */
    public HeapPriorityQueue(int size){
    	//this.pos = 1;
    	storage = new Comparable[size];
    	this.currentSize = 0;
    }
    	

    /*
	 * PURPOSE:
	 *	Adds element into the PriorityQueue at the position
	 *	according to the element's priority 	.
	 *
	 * PRECONDITIONS:
	 *	None.
	 *
	 * RETURNS:
	 *	None.
	 *
	 * Examples:
	 * 	If q contains elements that would be accessed in the 
	 * 	following order:  {5,13,21} after q.insert(20) returns,
	 * 	then q will contain elements that will be accessed
	 * 	in the following order: {5,13,20,21}.
	 *
	 */
 	public void insert ( Comparable element ) throws HeapFullException{
		
	

		System.out.println("Current size:" + currentSize);
		System.out.println("sotrage length:" + storage.length);
 		if(currentSize >= storage.length){
 			throw new HeapFullException();
 		
 		}
 			if(currentSize == 0){
 				storage[0] = element;
 			}else{
 				int newl = 0;
				while((currentSize > newl) && (element.compareTo(storage[newl]) >= 0)) {
               		newl++;
            	}
 			
			
	

		Comparable[] copy = new Comparable[storage.length];
		for(int i = 0; i < newl; i++){
		
			copy[i] = storage[i];

		}
		

		copy[newl] = element;
		for(int i = newl; i < currentSize; i++){
			copy[i + 1] = storage[i];

		}
		storage = copy;
		

		
		}

	
		
		currentSize++;
	}



 		 			
 	
 	
 	
 	 /*
	 * PURPOSE:
	 *	Remove highest priority element from the PriorityQueue, 
	 *	where the smallest value will be of highest priority.
	 *
	 * PRECONDITIONS:
	 *	None.
	 *
	 * RETURNS:
	 *	Comparable - the highest priority object in the Queue
	 *
	 * Examples:
	 * 	If q contains elements that would be accessed in the 
	 * 	following order:  {5,13,21},  q.removeLow() returns 5,
	 * 	and then q will contain elements that will be accessed
	 * 	in the following order: {13,21}.
	 *
	 */
	public Comparable removeLow ()throws HeapEmptyException{
		//Comparable smallest_value = Integer.MAX_VALUE - 1;
		//Comparable a[] = new Comparable[DEFAULT_SIZE];

		if(isEmpty()){
			throw new HeapEmptyException();
		}else{

		
		Comparable smallest_value = storage[0];
		Comparable [] a = new Comparable[storage.length];


		for(int x = 1; x < currentSize; x++){
			a[x-1] = storage[x];
		}
		storage = a;
		currentSize -= 1;
		
		return smallest_value;
	}
		
		//return smallest_value;
	}
	
	 /*
	 * PURPOSE:
	 *	Determines if the PriorityQueue is empty or not.
	 *
	 * PRECONDITIONS:
	 *	none
	 *
	 * RETURNS:
	 *	true if PriorityQueue is empty, false otherwise.
	 *
	 */
	public boolean isEmpty(){

		
		if(currentSize > 0){
			return false;
		}else{
			return true;
		}
	}
	
	 /*
	 * PURPOSE:
	 *	Determines number of elements in the PriorityQueue.
	 *
	 * PRECONDITIONS:
	 *	None.
	 *
	 * RETURNS:
	 *	the size of the PriorityQueue.
	 *
	 */			
	public int	size (){
		return this.currentSize;
	}



    /*
     * PURPOSE:
     *    constructs a String representation of the elements in storage
     *      ordered by their position in storage NOT by priority 
     *
     * PARAMETERS:
     *    None.
     *
     * RETURNS:
     *    String - the String representation
     *
     */
    public String toString() {
        String s = "";
        String sep = "";
        for(int i=0;i<currentSize;i++) {
            s+= sep + storage[i];
            sep = " ";
        }
        return s;
    }

}

public class StudentLinkedList implements StudentList{
	private StudentNode head;
	private StudentNode tail;
    private int count;



	public StudentLinkedList(){
		this.head = head;
		this.count = 0;

	}


	 /*
     * Purpose: adds Student s to back of this list
     * Parameters: Student - s
     * Returns: nothing
     */
    public void add(Student s){
      //  StudentNode tail = new StudentNode();
      //  StudentNode curr = new StudentNode();
        
        if(count == 0){
            head = new StudentNode(s);
        }else if(count == 1){
       

        tail = new StudentNode(s);
        head.setNext(tail);

        }else{
            StudentNode current = new StudentNode(s);
            tail.setNext(current);
            tail = current;
            
        }
    
        count++;
    }
    
    /*
     * Purpose: returns the number of elements in this list
     * Parameters: none
     * Returns: int - the number of elements
     */
    public int size(){
    	return count;
    }
    
    /*
     * Purpose: returns a String reprensentation of the elements
     *      in this list separated by newlines
     * Parameters: none
     * Returns: String - the representation
     */
    public String toString(){
    	String s = "";
    	
    	StudentNode cur = head;

    	
    		for(int i = 0; i < count; i++){
                s += cur.getData().toString() + "";
                cur = cur.getNext();
            }
    			
    	
        return s;
    }
    
    /*
     * Purpose: removes the first element in the list
     * Parameters: none
     * Returns: nothing
     */
    public void removeFront(){
    	if(head == null){
    		head = null;
    	}

    	//Node temp = head;
    	head = head.next;
    	count--;

    	//return head;
    }
    
    /*
     * Purpose: determines whether a Student which is equivalent to s
     *      is contained in this list
     * Parameters: Student - s
     * Returns: boolean - true if a Student matching s is found,
     *  false otherwise
     */
    public boolean contains(Student s){
        boolean b = true;
        StudentNode cur = head;
        while(cur != null){
            if(cur.getNext().equals(s)){
                b = true;
                cur = cur.getNext();
            }
        }
    	

        return b;
    }






}
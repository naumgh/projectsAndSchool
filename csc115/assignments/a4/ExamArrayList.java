 public class ExamArrayList implements ExamListInterface {
    
    private static final int INITIAL_CAPACITY = 2;
    
    private Exam[] storage;  // holds Exams, each with a unique course
    private int numExams;
    
    /*
     *
     * Purpose:
     *    Initialize a new instance of PlayerList
     *
     */
    public ExamArrayList() {
        // You must allocate an array to be able
        // to hold INITIAL_CAPACITY Exam objects
        // You must set numExams to be 0
        storage = new Exam[INITIAL_CAPACITY];
		numExams = 0;
		
		
		
    }
    
	 /* get
     *
     * Purpose: returns the element at position
     *
     * Parameters: int - position
     *
     * Pre-Conditions:
     *     for a ExamList x:
     *    position >= 0 AND
     *    position < x.size()
     *
     * Returns: Exam - the Exam at position
     *
     */
	public Exam get (int position){
		//System.out.println(position);
          return storage[position];
			
	}
    

    
    /* size
     *
     * Purpose: returns the number of elements in the list
     *
     * Parameters: none
     *
     * Returns: int - the number of elements
     *
     */
    public int size(){		
		
		
		return numExams;
	}
    
    /* add
     *
     * Purpose: add Exam e to the Examlist
     *  more space is allocated for the Examlist if necessary
     *  to add e to the list
     *
     * Parameters: Exam e
     *
     * Returns: nothing
     *
     */
    public void add (Exam e){ 

        if(numExams + 1 > this.storage.length){    
           

            Exam [] newerexam = new Exam[numExams+10];

            for(int i = 0; i < numExams; i++){
                
                newerexam[i] = storage[i];
               // numExams++;
                
            }
           
           storage = newerexam;
                  
        }
        storage[numExams] = e;
        numExams++;
    }
   

    /*
        if(numExams == 0){
            storage[0] = e;
            numExams++;
        }else if(numExams == 1){
             storage[1] = e;
             numExams++;
        }
           
   */     
      //  storage[1] = 2
       // numExams += 1;
        
        
	
	
    
    /* find
     *
     * Purpose: return the position where Exam with given course is in the Examlist,
     *  if Exam with course is not found, returns -1
     *
     * Parameters: String course
     *
     * Pre-Conditions: course is not null
     *
     * Returns: int - position of Exam with course, -1 if it does not exist
     *
     */
    public int find (String course){

        for(int i = 0; i < numExams; i++){
            if(storage[i].getCourse().equals(course)){
                return i;
            }
        }

        return -1;
    }
        
     
    
    /* removeAtPos
     *
     * Purpose: removes the element at position
     *
     * Parameters: int - position
     *
     * Pre-Conditions:
     *    for a ExamList x:
     *        position >= 0 AND
     *        position < x.size()
     *
     * Returns: nothing
     *
     */
    public void removeAtPos (int position){
	   for(int i = position; i < numExams-1; i++){
            storage[i] = storage[i+1];

       }
       storage[numExams-1]=null;
       numExams--;
   }

       
    
    /* removeAllOnDate
     *
     * Purpose: removes all Exams that are on given date
     *    from this ExamList
     *
     * Parameters: Date date
     *
     * Pre-Conditions: date is not null
     *
     * Returns: nothing
     *
     */
    public void removeAllOnDate (Date date){
		for(int i = 0; i < numExams; i++){
            if(storage[i].getDate().equals(date)){
                removeAtPos(i);
                i--;
            }
        }
	}
    
    
    /* toString
     *
     * Purpose: return a String representing the forward traversal
     *  with a space after each element
     *
     * Parameters: none
     *
     * Returns: String - the forward list representation
     *
     */
    public String toString() {
        String s = "";
        
        for(int i=0; i<numExams; i++) {
            s += storage[i];
            if(i != (numExams-1))
                s += " ";
        }
        
        return s;
    }

}

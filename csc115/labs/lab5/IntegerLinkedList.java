public class IntegerLinkedList {
    
    
    private IntegerNode	head;
    private int		    count;
    
    
    public IntegerLinkedList() {
        head = null;
        count = 0;
    }
    /*
     *
     * Purpose: returns the size of this IntegerList
     *
     * Parameters: none
     *
     * Returns: int - the size
     *
     */
    public int size() {
        return count;
    }
    
    /*
     *
     * Purpose: adds element with i to the front of this Integerlist
     *
     * Parameters: int - i
     *
     * Returns: nothing
     *
     */
    public void addFront (int i) {
        IntegerNode n = new IntegerNode(i, head);
        
        head = n;
        
        count++;
        
    }
    
    
    /*
     *
     * Purpose: returns a String representation of this IntegerList
     *
     * Parameters: none
     *
     * Returns: String - the String representation
     *
     */
    public String toString() {
        String s = "";
        IntegerNode tmp = head;
        
        while (tmp!=null) {
            s += tmp.getElement();
            if(tmp.next!=null)
                s += " ";
            tmp = tmp.next;
        }
        
        return s;
    }
    
    /*
     *
     * Purpose: adds 1 to every element in this IntegerList
     *
     * Parameters: none
     *
     * Returns: nothing
     *
     */
    public void addOne() {
        IntegerNode tmp = head;
        
        while (tmp!=null) {
            int valPlusOne = tmp.getElement() + 1;
            tmp.setElement(valPlusOne);
            tmp = tmp.next;
        }
    }
    
    /*
     *
     * Purpose: recursively adds 1 to every element in this IntegerList
     *
     * Parameters: none
     *
     * Returns: nothing
     *
     */
    public void addOneRecursive() {
        addOneRecursiveHelper(head);
    }
    
    /*
     *
     * Purpose: recursively adds 1 to IntegerNode n and every element following n
     *
     * Parameters: IntegerNode - n
     *
     * Returns: nothing
     *
     */
    private void addOneRecursiveHelper(IntegerNode n) {
        if (n==null) {
            return;
        } else {
            
            // get data in current node and add 1 to it
            int valPlusOne = n.getElement() + 1;
            // set element in current node to valPlusOne
            n.setElement(valPlusOne);
            
            // add one to the elements in the  REST of the list
            addOneRecursiveHelper(n.next);
        }
    }
    
    /*
     *
     * Purpose: recursively doubles every element in this IntegerList
     *
     * Parameters: none
     *
     * Returns: nothing
     *
     */
    // ToDo: implement and test this method
    public void doubleAtOddElements(){
        doubleAtOddElementsHelper(head);
        //return;
    }   



    /*
     *
     * Purpose: recursively doubles every odd element in this IntegerList
     *  By "odd element" we mean the Node's element is an odd number
     *  NOT that it is at an odd position in the list
     *
     * Parameters: none
     *
     * Returns: nothing
     *
     */
    // ToDo: implement and test this method
    private void doubleAtOddElementsHelper(IntegerNode n){
        //IntegerNode n = head.next;

        //if 
       // int county = 0;
        if(n == null){
            return;
        }else if(n.getElement() % 2 == 0){
            
            n = n.next;

        }else if(n.getElement() % 2 != 0){
            //head = head.get
            
            int valxd = n.getElement() * 2;
            n.setElement(valxd);
            //n = n.next;
            //System.out.println(valxd);
            //current = head.getNext();
            doubleAtOddElementsHelper(n.next); 
        }
        
        return;
   
    } 
    
    /*
     *
     * Purpose: recursively sums every element in this IntegerList
     *
     * Parameters: none
     *
     * Returns: int - the sum
     *
     */
    public int sum() {
        return sum(head);
    }
    
    
    /*
     *
     * Purpose: recursively sums element in IntegerNode n and every element following n
     *
     * Parameters: IntegerNode - n
     *
     * Returns: int - the sum
     *
     */
    public int sum(IntegerNode n) {
        if (n==null) {
            return 0;
        } else {
            int first = n.getElement();
            int sumRest = sum(n.next);
            
            return first + sumRest;
        }
    }
    
    /*
     *
     * Purpose: recursively computes the product of every element in this IntegerList
     *  Note: the product of an empty list is 1
     *
     * Parameters: none
     *
     * Returns: int - the product
     *
     */
    // ToDo: implement and test this method
    
    
    
    /*
     *
     * Purpose: recursively doubles every element at an odd postion in this IntegerList
     *  the first  element in this list is at position 0 (is not odd)
     *  the second element in this list is at position 1 (is odd)
     *  the third  element in this list is at position 2 (is not odd)
     *  ...
     *
     * Parameters: none
     *
     * Returns: nothing
     *
     */
    public void doubleOddPositionValues() {
        doubleOddPositionValues(head, 0);
    }
    
    /*
     *
     * Purpose: recursively doubles element in IntegerNode n if n is at odd position
     *  and every element after n at odd positions
     *
     * Parameters: IntegerNode - n, int - position
     *
     * Returns: nothing
     *
     */
    public void doubleOddPositionValues(IntegerNode n, int position) {
        if (n==null) {
            return;
        } else {
            if (position % 2 != 0) {
                int doubleVal = n.getElement() * 2;
                n.setElement(doubleVal);
            }
            doubleOddPositionValues(n.next, position+1);
        }
    }
    
    
    /*
     *
     * Purpose: recursively determines whether every element in this IntegerList
     *      is sorted in ascending order
     *      {1, 2, 2, 5} is sorted in ascending order
     *      {3, 2, 2, 5} is not sorted in ascending order
     *
     * Parameters: none
     *
     * Returns: boolean - true if sorted, false otherwise
     *
     */
    // ToDo: implement and test this method
    
    
    
    
    
    
    /*
     *
     * Purpose: recursively determines whether all elements in this IntegerList are negative
     *
     * Parameters: none
     *
     * Returns: boolean - true if all negative, false otherwise
     *
     */
    // ToDo: implement and test this method
    
    
    
}


public class IntegerLinkedList implements IntegerList {


    private IntegerNode	head;
    private IntegerNode tail;
    private int		    count;

    public IntegerLinkedList(){
        this.head = null;
        this.tail = null;
        this.count = 0;
    }

   // public IntegerLinkedList(int count){
    //    this.count = 0;
        // }

 //   public IntegerLinkedList(){

 //   }

 /* Parameters: (int) val
     * Purpose:  add val to the front of the list
     * Returns:  nothing
     */
    public void addFront (int val){
        if(count == 0){
            
            IntegerNode new_head = new IntegerNode(val);
            tail = new_head;
            head = tail;
        }else if(count == 1){
            head = new IntegerNode(val);
            tail.setPrev(head);
            head.setNext(tail);
        }else{
            IntegerNode cur = new IntegerNode(val);
            head.setPrev(cur);
            cur.setNext(head);
            head = cur;
        }

        count++;
    }

    /* Parameters: (int) val
     * Purpose:  add val to the back of the list
     * Returns:  nothing
     */
    public void addBack (int val){
        if(count == 0){
            IntegerNode new_head = new IntegerNode(val);
            tail = new_head;
            head = tail;
        }else if(count == 1){
            tail = new IntegerNode(val);
            head.setNext(tail);
            tail.setPrev(head);
        }else{
            IntegerNode current = new IntegerNode(val);
            tail.setNext(current);
            current.setPrev(tail);
            //head.setPrev(current);
            tail = current;
        }

        count++;
    }
    
    /* Parameters: none
     * Purpose:  get the size of the list
     * Returns:  (int) the size
     */
    public int size (){
        return this.count;
    }
    
    /*
     *
     * Purpose: returns the element at position
     *
     * Parameters: int - position
     *
     * Pre-Conditions:
     *     for a IntegerList x:
     *    position >= 0 AND
     *    position < x.size()
     *
     * Returns: int - the int at position
     *
     */
    public int getAtPosition (int position){
       IntegerNode current = head;
    
        for(int i = 0; i < count; i++){
            if(i == position){
                return current.getElement();
            }else{
                current = current.getNext();
            }
        }
        return -1;
    }

    
    
    /*
     *
     * Purpose: return the position where i is in the list,
     *  if i is not found returns -1
     *
     * Parameters: int - i
     *
     * Returns: int - position of i, -1 if i does not exist
     *
     */
    public int getPositionOfVal (int i){
        IntegerNode current = new IntegerNode(i);
        IntegerNode moveit = head;
        try{
        for(int q = 0; q < count; q++){
             
                if(current.getElement() == moveit.getElement() && moveit != null && current != null){

                //System.out.println("it's working");
                    return q;
                }

            moveit = moveit.getNext();
        }

    }
        catch(Exception e){
            return -1;
        }
        return -1;
    }
    
    /*
     *
     * Purpose: computes the sum of only elements in this list
     *      which hold values that are divisible by given divisor
     *
     * Parameters: none
     *
     * Returns: int - the sum
     *
     */
    public int sumDivisible (int divisor){
        IntegerNode visor = head;
        int sum = 0;
        for(int i = 0; i < count; i++){
            if(visor.getElement() % divisor == 0){
                System.out.println(visor.getElement());
                sum = sum + visor.getElement();
                visor = visor.getNext();
        

            
               
        }else if(visor.getElement() % divisor != 0){
            visor = visor.getNext();

        }
    }
        System.out.println(sum);
        return sum;
        
    }
    
    /*
     *
     * Purpose: computes the sum of only elements in this list
     *    at even positions within the list where, the the first
     *    element of the list is considered to be at position 0.
     *
     * Parameters: none
     *
     * Returns: int - the sum
     *
     */
    public int sumEvenPositionElements(){
        IntegerNode visor = head;
        int sum = 0;

        for(int i = 0; i < count; i++){
            if(i % 2 == 0 || i == 0){
                sum = sum + visor.getElement();

            }
            visor = visor.getNext();
        }
        return sum;
    }
    

    /*
     *
     * Purpose: remove all elements with i from the list
     *   The number of occurances of i can be >= 0
     *
     * Parameters: int - i
     *
     * Returns: nothing
     *
     */
    public void removeValue(int i){
    
        IntegerNode current = head;
       if(count != 0){
       for(int q = 0; q < count; q++){
            if(q == 0 && head.getElement() == i){
                head = head.getNext();
                head.setPrev(null);
                count--;
            }else if(q == count-1 && tail.getElement() == i){
                tail = tail.getPrev();
                tail.setNext(null);
                count--;
            }else if(q == 1 && current.getElement() == i){
               if(current.getNext().getElement() != i){
                    head.setNext(current.getNext());
                    current.getNext().setPrev(head);
                    count--;
               }
                
            }else if(q > 1 && current.getElement() == i){
                if(current.getNext().getElement() != i){
                    current.getPrev().setNext(current.getNext());
                    current.getNext().setPrev(current.getPrev());
                    count--;
               }else if(current.getNext().getElement() == i){
                    current.getPrev().setNext(current.getNext().getNext());
                    current.getNext().getNext().setPrev(current.getPrev());
                    count--;
               }
            count--;
            }
        current = current.getNext();
      if(head.getElement() == i){
                count--;
                head = null;
                tail = null;
                
            }
       }
       
   }
       // return;
    }



    /*
     *
     * Purpose: return a String representing the forward
     *  traversal of this list with a space between each element
     *
     * Parameters: none
     *
     * Returns: String - the forward list representation
     *
     */
    public String toString(){
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
     * Purpose: return a String representing the reverse
     *  traversal of this list with a space between each element
     *
     *
     * Returns: String - the reverse list representation
     *
     */
    public String reverse() {
        String s = "";
        IntegerNode tmp = tail;

        while (tmp!=null) {
            s += tmp.getElement();
            if(tmp.prev!=null)
                s += " ";
            tmp = tmp.prev;
        }

        return s;

    }
    
 

}
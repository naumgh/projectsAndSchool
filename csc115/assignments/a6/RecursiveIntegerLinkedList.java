public class RecursiveIntegerLinkedList implements IntegerList {
    
    private IntegerNode    head;
    private IntegerNode    tail;
    private int		count;

    public RecursiveIntegerLinkedList(){
        this.head = null;
        this.tail = null;
        this.count = 0;
    }

 
 


 /* Parameters: (int) val
     * Purpose:  add val to the front of the list
     * Returns:  nothing
     */
       public void addFront (int v){
        if(count == 0){
            
            IntegerNode new_head = new IntegerNode(v);
            tail = new_head;
            head = tail;
        /*

        }else if(count == 1){
            head = new IntegerNode(v);
            tail.setPrev(head);
            head.setNext(tail);

            */
        }else{
            IntegerNode cur = new IntegerNode(v);
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




   public void addBack (int i){
        if(count == 0){
            IntegerNode new_head = new IntegerNode(i);
            tail = new_head;
            head = tail;
        /*
        }else if(count == 1){
            tail = new IntegerNode(i);
            head.setNext(tail);
            tail.setPrev(head);
            */
        }else{
            IntegerNode current = new IntegerNode(i);
            tail.setNext(current);
            current.setPrev(tail);
            //head.setPrev(current);
            tail = current;
        }

        count++;
    }



        /*

        IntegerNode nn = new IntegerNode(i);
        if (head == null) {
            head = nn;
        } else {
            //IntegerNode temp = head;
            if(nn.next == null){
                tail = nn.next;
            }else{
                nn=nn.next;
            } 
           // addBack();
            
            
        }
        count ++;
        //return;
    }
    */
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
    public int getAtPosition(int position){
        return getAtPosition(position, head);
        

    }


    public int getAtPosition (int position, IntegerNode new_head){
       // IntegerNode c = new IntegerNode(position)
        if(new_head == null){
            return -1;
        }

        if(position == 0){
            return new_head.getElement();
        }else{
            position--;
        }


        
        return getAtPosition(position, new_head.next);
        
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
        return getPositionOfVal(i, head, 0);
    }

    public int getPositionOfVal(int i, IntegerNode n, int counter){
        if(n == null){
            return -1;
        }

        if(n.getElement() == i){
            return counter;
        }else{
            return getPositionOfVal(i, n.next, counter+1);
        }
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
   
    public int sumDivisible(int divisible){
        return sumDivisible(0, head, divisible);
    }

    public int sumDivisible(int sum, IntegerNode n, int divisible){
        if(n == null){
            return sum;
        }else{
   
            if(n.getElement() % divisible == 0 && n != null){
                return sumDivisible(sum + n.getElement(), n.next, divisible);
            }else if (n.getElement() % divisible != 0 && n != null){
                return sumDivisible(sum, n.next, divisible);
            
            }
        
        }
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
        return sumEvenPositionElements(head, 0, 0);
    }


    public int sumEvenPositionElements(IntegerNode q, int sum, int counter){
        if(q == null){
            return sum;
        }else{
           if(counter % 2 == 0){
                return sumEvenPositionElements(q.next, sum + q.getElement(), counter+1);
           }else{
                return sumEvenPositionElements(q.next, sum, counter+1);
           }
        }
       // return sum;
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
   /*
    public void removeValue(int i){
        removeValue(i, 0, head, tail);
    }
*/  
    public void removeValue(int i){
        
        /*
        IntegerNode z = new IntegerNode(900);
        z.setNext(head);

        removeValue(i, z);
        */
        removeValue(i, head);
        return;
    }
 
    
    public void removeValue(int i, IntegerNode c){
        if(c == null){
            return;
        }else{
            if(c.getElement() == i){
                if(count == 1){
                    head = null;
                    tail = null;
                    count--;
                }else{
                    if(c == head){
                        head = c.next;
                        c.setPrev(null);
                        head.setPrev(null);
                        count--;
                    }else if(c == tail){
                        tail = c.prev;
                        c.setNext(null);
                        tail.setNext(null);
                        count--;
                    }else{
                        c.prev.setNext(c.next);
                        c.next.setPrev(c.prev);
                        count--;
                    }
                }
               
            }

               // count--;
                removeValue(i, c.next);
        }
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

        return toString(head);
    }
    private String toString(IntegerNode n){
        if (n == null) {
            return "";
        } else {
            int firstVal = n.getElement();
            IntegerNode rest = n.next;
            if(rest != null){
                return firstVal + " " + toString(rest);
            }else{
                return firstVal + "" + toString(rest);
            }
            

        }
        
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



    public String reverse(){

        return reverse(tail);
    }
    private String reverse(IntegerNode n){
        if (n == null) {
            return "";
        } else {
            int firstVal = n.getElement();
            IntegerNode rest = n.prev;
            if(rest != null){
                return firstVal + " " + reverse(rest);
            }else{
                return firstVal + "" + reverse(rest);
            }
        }
        //return"";
    }
 

}
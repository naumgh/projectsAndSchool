public class IntegerLinkedList implements IntegerList{
    
    private int count;
    private Node head;
    
    public IntegerLinkedList() {
        
        count = 0;
        head = null;
    }
    

    public void print_list_recursive(){
        print_list_recursive(head);
    }

    private void print_list_recursive(Node cur){
        if(cur == null){
            System.out.println();
            return;
        }else{
            int firstVal = cur.getValue();
            System.out.println(firstVal + " ");


            Node rest = cur.next;
            print_list_recursive(rest); //print the rest of list



        }
    }


    public void abs(){
        abs(head);
    }

    private void abs(Node cur){
        if(cur == null){
            System.out.println("");
        }else{
            int firstVal = cur.getValue();
            //firstVal = 0 + firstVal;
            if(firstVal < 0){
                firstVal *= -1;
                cur.setValue(firstVal);

                System.out.println(firstVal * -1);
            }
            Node rest = cur.next;
            abs(rest); 
        }
    }

    /* Parameters: int i
     * Purpose:  add i to the front of the list
     * Returns:  nothing
     */
    public void addFront (int i){
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
    
    /* Parameters: int i
     * Purpose:  add i to the back of the list
     * Returns:  nothing
     */
    public void addBack (int i){
        Node nn = new Node(i);
        if (head == null) {
            head = nn;
        } else {
            Node tmp = head;
            while (tmp.next != null) {
                tmp = tmp.next;
            }
            tmp.next = nn;
        }
        count++;

    }
    
    /* Parameters: nothing
     * Purpose:  get the size of the list
     * Returns:  int size
     */
    public int size (){
        return count;
    }
    
    /* Parameters: int position
     * Purpose:  get the int value at specified position in the list
     * Returns:  int the int value
     * Precondition: 0 <= position < list.size()
     */
    public int get (int position){
        Node tmp = head;
        
        for(int i=0; i<position; i++)
            tmp = tmp.next;
        
        return tmp.getValue();
    }
    
    /* Parameters: none
     * Purpose:  returns a string representing the list
     * Returns:  (String) the representation
     */
    public String toString(){
//        String s = "";
//
//        Node tmp = head;
//        while(tmp != null) {
//            s = s + tmp.getValue() + " ";
//            tmp = tmp.next;
//        }
//
//        return s;
        return toString(head);
    }
 
    /* Parameters: Node n
     * Purpose:  returns a string representing the list pointed to by n
     * Returns:  String the representation
     */
    public String toString(Node n){
        if (n == null) {
            return "";
        } else {
            int firstVal = n.getValue();
            Node rest = n.next;
            return firstVal + " " + toString(rest);
        }
    }
    
    /* Parameters: int val
     * Purpose:  remove val from the list
     * Returns:  nothing
     */
    public void remove (int val){
        Node tmp = head;
        Node prev = null;
        while(tmp!=null) {
            if(tmp.getValue() == val) {
                removeNode(prev, tmp);
            } else {
                prev = tmp;
            }
            tmp = tmp.next;
        }
    }
    
    /* Parameters: Node prev, Node n
     * Purpose:  remove n from this list,
     *  make prev point to n's next and n.next's prev point to prev
     * Postcondition: n.next and n.prev are unchanged
     * Returns:  nothing
     */
    private void removeNode (Node prev, Node n){
        // TODO...
    }
    
    /* Parameters: none
     * Purpose:  prints all values in this list
     * Returns:  nothing
     */
    public void printValues() {
        printValues(head);
    }
    
    /* Parameters: Node n
     * Purpose:  prints all values in list pointed to by n
     * Returns:  nothing
     */
    private void printValues(Node n) {
        if (n==null) {
            System.out.println();
        } else {
            Node first = n;
            int firstVal = first.getValue();
            Node rest = n.next;
            
            System.out.print(firstVal + " ");
            printValues(rest);
        }
    }



}

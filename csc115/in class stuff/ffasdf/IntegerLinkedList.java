import java.lang.Math;

public class IntegerLinkedList implements IntegerList{
    
    private int count;
    private Node head;
    
    public IntegerLinkedList() {
        
        count = 0;
        head = null;
    }
    public boolean allAbove(int threshold) {
        return allAbove(head, threshold);
    }
    
    private boolean allAbove(Node curHead, int threshold) {
        if (curHead==null) {
            return true;
        } else {
            Node first = curHead;
            int firstVal = first.getValue();
            Node rest = curHead.next;
            
            if (firstVal<=threshold)
                return false;
            boolean restAllAbove = allAbove(rest, threshold);
            return restAllAbove;
        }
    }
        //could write the above method as:
//    private boolean allAbove(Node curHead, int threshold) {
//        if (curHead==null) {
//            return true;
//        } else {
//            return (curHead.getValue()>threshold) &&
//                    allAbove(curHead.next, threshold);
//        }
//    }
    
    public int max() {
        return max (head);
    }
    
    private int max(Node curHead) {
        if (curHead == null) {
            return Integer.MIN_VALUE;
        } else {
            Node first = curHead;
            int firstVal = first.getValue();
            Node rest = curHead.next;

            int maxOfRest = max(rest);
            if (firstVal>maxOfRest)
                return firstVal;
            else
                return maxOfRest;
        }
    }
    //could write the above method as:
//    private int max(Node curHead) {
//        if (curHead == null) {
//            return Integer.MIN_VALUE;
//        } else {
//            return Math.max(curHead.getValue(), max(curHead.next));
//        }
//    }
    public int sum() {
        
        return sum(head);
    }
    
    private int sum(Node curHead) {
        if (curHead==null) {
            return 0;
        } else {
            Node first = curHead;
            int firstVal = first.getValue();
            Node rest = curHead.next;

            int sumOfRest = sum(rest); // sum of the rest of the values

            return firstVal + sumOfRest;
        }

    }

    
     //could write the above method as:
//    private int sum(Node curHead) {
//        if (curHead==null) {
//            return 0;
//        } else {
//            return curHead.getValue() + sum(curHead.next);
//        }
//    }
    
    public void abs() {
        abs(head);
        
    }
    
    private void abs (Node curHead) {
        if (curHead == null) {
            return;
        } else {
            Node first = curHead;
            int firstVal = first.getValue();
            Node rest = curHead.next;
            
            if (firstVal < 0)
                first.setValue(firstVal*-1);
            
            abs(rest);// change all -ve to +ve in REST
        }
        
    }
    
    
    /* Parameters: int i
     * Purpose:  add i to the front of the list
     * Returns:  nothing
     */
    public void addFront (int i){
        Node nn = new Node(i);
        if (head != null)
            nn.next = head;
        head = nn;
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

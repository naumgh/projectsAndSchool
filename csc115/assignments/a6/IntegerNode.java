/*
 * IntegerNode.java
 *
 * An implementation of a node class for a doubly-linked list of integers.
 *
 * Your textbook uses the following coding conventions for setting the value of
 * a node's next and prev values
 *
 *    n.next = null;
 *    n.prev.next = otherNode;
 *
 * Rather than:
 *
 *    n.setNext(null);
 *    n.getPrev().setNext(otherNode);
 *
 * Therefore I have not set next and prev to be private
 * contrary to what we have said about keeping data fields private...
 *
 * In this assignment, and on exams, you are free to use whichever
 * method you find most comfortable.
 *
 */

public class IntegerNode {
	IntegerNode	next;
	IntegerNode	prev;
	int		    e;


	public IntegerNode (Integer e) {
		this.e = e;
		next = null;
        prev = null;
	}

	public IntegerNode (Integer e, IntegerNode next, IntegerNode prev) {
		this.e = e;
		this.next = next;
        this.prev = prev;
	}

	public IntegerNode getNext()	{
		return next;
	}
	
	public void setNext (IntegerNode next) {
		this.next = next;
	}

	public IntegerNode getPrev() {
		return prev;
	}
	
	public void setPrev (IntegerNode prev) {
		this.prev = prev;
	}

	public int getElement() {
		return e;
	}
	
	public void setElement (Integer e) {
		this.e = e;
	}
    
    public String toString() {
        return "e: " + e ;
    }
}


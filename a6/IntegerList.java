public interface IntegerList {
    
    /*
     *
     * Purpose: add i to the front of this list
     *  more space is allocated if necessary
     *  to add ito the list
     *
     * Parameters: int - i
     *
     * Returns: nothing
     *
     */
    void addFront (int i);
    
    /*
     *
     * Purpose: add i to the back of this list
     *  more space is allocated if necessary
     *  to add it to the list
     *
     * Parameters: int - i
     *
     * Returns: nothing
     *
     */
    void addBack (int i);
    
    /*
     *
     * Purpose: returns the number of elements in this list
     *
     * Parameters: none
     *
     * Returns: int - the number of elements
     *
     */
    int size ();
    
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
    int getAtPosition (int position);
    
    
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
    int getPositionOfVal (int i);
    
    
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
    int sumDivisible (int divisor) ;
    
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
    int sumEvenPositionElements() ;
    

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
    void removeValue(int i) ;
    

    
    
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
    String toString();
    
    /*
     *
     * Purpose: return a String representing the reverse
     *  traversal of this list with a space between each element
     *
     * Parameters: none
     *
     * Returns: String - the reverse list representation
     *
     */
    String reverse();
    
    
}

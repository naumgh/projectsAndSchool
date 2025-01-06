public interface ExamListInterface {
        
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
    Exam get (int position);
    

    
    /* size
     *
     * Purpose: returns the number of elements in the list
     *
     * Parameters: none
     *
     * Returns: int - the number of elements
     *
     */
    int size();
    
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
    void add (Exam e);
    
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
    int find (String course);
    
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
    void removeAtPos (int position) ;
    
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
    void removeAllOnDate (Date date) ;
    
    /* toString
     *
     * Purpose: return a String representing the forward traversal
     *  with a space between each element
     *
     * Parameters: none
     *
     * Returns: String - the forward list representation
     *
     */
    String toString();
    
}

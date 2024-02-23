/*
 * Exam class representing a scheduled exam
 */
public class Exam {

    // TODO add Exam attributes/fields..

    /* Exam
     * Purpose: Initialize this instance of Exam with parameter values
     *  location is set to "TBA", duration is set to default 180 minutes
     *
     * Parameters: Date date, Time startTime
     *
     */
    // TODO...
    


    /* Exam
     * Purpose: Initialize this instance of Exam with parameter values
     *
     * Parameters: Date date, String location, Time startTime, int duration
     *
     */
    // TODO...
    

    

    /* getDate
     * Purpose: Returns the date associated with this Exam
     *
     * Parameters: nothing
     *
     * Returns: Date - date associated with this Exam
     */
    // TODO...
    


    /* setDate
     * Purpose: sets the date associated with this Exam to parameter value
     *
     * Parameters: Date date
     *
     * Returns: nothing
     */
    // TODO...
    


    /* getLocation
     * Purpose: Returns the location associated with this Exam
     *
     * Parameters: nothing
     *
     * Returns: String - location associated with this Exam
     */
    // TODO...
    


    /* setLocation
     * Purpose: sets the location associated with this Exam to parameter value
     *
     * Parameters: String location
     *
     * Returns: nothing
     */
    // TODO...
    


    /* getStartTime
     * Purpose: Returns the startTime associated with this Exam
     *
     * Parameters: nothing
     *
     * Returns: Time - startTime associated with this Exam
     */
    // TODO...
    


    /* setStartTime
     * Purpose: sets the startTime associated with this Exam to parameter value
     *
     * Parameters: Time startTime
     *
     * Returns: nothing
     */
    // TODO...
    

    
    /* getDuration
     * Purpose: Returns the duration associated with this Exam
     *
     * Parameters: nothing
     *
     * Returns: int - duration associated with this Exam
     */
    // TODO...
    


    /* setDuration
     * Purpose: sets the duration associated with this Exam to parameter value
     *
     * Parameters: int duration
     *
     * Precondition: duration >= 60
     *
     * Returns: nothing
     */
    // TODO...
    



    /* isOverlap
     * Purpose: determines whether the date and time of this Exam
     *  overlaps with the other Exam date and time
     *
     * Parameters: Exam - other
     *
     * Precondition: other is not null
     *
     * Returns: boolean - true if this Exam overlaps with other, false otherwise
     *
     * HINT: instructor made use of addTime method in the Time class
     *  Be careful how you use it as it is an instance method that updates the instance data
     */
    // TODO...
    


    /* toString
     * Purpose: returns a String representing this Exam formated as:
     *  date: location: startTime-endTime
     *
     * Parameters: nothing
     *
     * Returns: String - a representation of this Exam
     *
     * Example:
     *  Exam e = new Exam(new Date("October",25,2019), "ECS 125", new Time(9,30), 120);
     *  e.toString() returns "October 25, 2019: ECS 125: 9:30am-11:30am"
     *
     * HINT: instructor made use of addTime method in the Time class
     *  Be careful how you use it as it is an instance method that updates the instance data
     */
    // TODO...
    

}

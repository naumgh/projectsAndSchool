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
    Date date;
    String location;
    Time startTime;
    int duration;


    /* Exam
     * Purpose: Initialize this instance of Exam with parameter values
     *
     * Parameters: Date date, String location, Time startTime, int duration
     *
     */
    // TODO...
    
    public Exam(Date d, Time sT){
        date = d;
        location = "TBA";
        startTime = sT; 
        duration = 180;
    }
    
    public Exam(Date date, String location, Time startTime, int duration){
        this.date = date;
        this.location = location;
        this.startTime = startTime;
        this.duration = duration;
    }

    

     
    /* getDate
     * Purpose: Returns the date associated with this Exam
     *
     * Parameters: nothing
     *
     * Returns: Date - date associated with this Exam
     */
    // TODO...
    public Date getDate(){
        return date;
        
    }


    /* setDate
     * Purpose: sets the date associated with this Exam to parameter value
     *
     * Parameters: Date date
     *
     * Returns: nothing
     */
    // TODO...
    public void setDate(Date d){
        date = d;
   
    }


    /* getLocation
     * Purpose: Returns the location associated with this Exam
     *
     * Parameters: nothing
     *
     * Returns: String - location associated with this Exam
     */
    // TODO...
    
    public String getLocation(){
        return location;
    }


    /* setLocation
     * Purpose: sets the location associated with this Exam to parameter value
     *
     * Parameters: String location
     *
     * Returns: nothing
     */
    // TODO...
    
    public void setLocation(String locate){
        location = locate;
    }

    /* getStartTime
     * Purpose: Returns the startTime associated with this Exam
     *
     * Parameters: nothing
     *
     * Returns: Time - startTime associated with this Exam
     */
    // TODO...
    public Time getStartTime(){
        return startTime;
    }


    /* setStartTime
     * Purpose: sets the startTime associated with this Exam to parameter value
     *
     * Parameters: Time startTime
     *
     * Returns: nothing
     */
    // TODO...
    
    public void setStartTime(Time start){
        startTime = start;
    }
    
    /* getDuration
     * Purpose: Returns the duration associated with this Exam
     *
     * Parameters: nothing
     *
     * Returns: int - duration associated with this Exam
     */
    // TODO...
    public int getDuration(){
        return duration;
    }


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
    public void setDuration(int d){
       duration = d;
       
        
    }



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
    public boolean isOverlap(Exam other){
        //int first = this.startTime.addTime(this.duration);
        //int second = other.getStartTime().addTime(other.getDuration());
        Time s1 = new Time(startTime.getHour(),startTime.getMinute());
        Time t = other.getStartTime();
        
        Time s2 = new Time(t.getHour(),t.getMinute());
        
        //System.out.println(s1);
        //System.out.println(s2);
        if(this.date.equals(other.getDate()) && this.startTime.equals(other.getStartTime())){
            return true;
        }else if(this.date.equals(other.getDate())){
           if(s2.isBefore(s1)){
                s2.addTime(other.getDuration());
               // System.out.println("s2 = " + s2);
           if(s2.isBefore(s1) || s2.equals(s1)){
                return false;
            }
          return true;
        }
            if(s1.isBefore(s2)){
             s1.addTime(duration);
             //System.out.println("s1 = " + s1);
            if(s1.isBefore(s2) || s1.equals(s2)){
                return false;
            
            }
           return true;
        
            
            //System.out.println(this.startTime);
            //System.out.println(other.getStartTime());
            
        }else{
            //System.out.println("skipping");
            return false;
        }
        
    
    }
    return false;
}
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
    
    public String toString(){
        
        String start = this.startTime.toString();
        this.startTime.addTime(this.duration);
        //System.out.println(this.date + ": " + this.location + ": " + start + "-" + this.startTime);
        return this.date + ": " + this.location + ": " + start + "-" + this.startTime;
    }
    

}

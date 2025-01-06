/*
 * Time class
 *  represents time on a 24 hour clock in hours and minutes
 *  from 0:0 to 23:59
 */
public class Time{

    // TODO: add Time attributes/fields..

    /* Time
     * Purpose: Initialize this instance of Time with values for a time of 0:0
     *
     * Parameters: nothing
     */
    // TODO...
    int hours;
    int minuets;

    public Time(){
        this(0,0);
        
    }
    
    public Time(int hours, int minuets){
        this.hours = hours;
        this.minuets = minuets;
        
    }
    
    
    /* Time
     * Purpose: Initialize this instance of Time with parameter values
     *
     * Parameters: int hour, int minute
     *
     * Precondition: hour and minute specify a valid time on a 24 hour clock
     */
    // TODO...
    

    public int getHour(){
        return hours;
        
    }

    /* getHour
     * Purpose: Returns the hour associated with this Time
     *
     * Parameters: nothing
     *
     * Returns: (int) - hour associated with this Time
     */
    // TODO...
    

    public void setHour(int h){
        hours = h;
    }

    /* setHour
     * Purpose: sets the hour associated with this Time to parameter value
     *
     * Parameters: int hour
     *
     * Precondition: 0 <= hour <= 23
     *
     * Returns: nothing
     */
    // TODO...
    
     public int getMinute(){
        return minuets;
        
    }

    /* getMinute
     * Purpose: Returns the minute associated with this Time
     *
     * Parameters: nothing
     *
     * Returns: (int) - minute associated with this Time
     */
    // TODO...
    

    public void setMinute(int m){
        minuets = m;
    }
    /* setMinute
     * Purpose: sets the minute associated with this Time to parameter value
     *
     * Parameters: int minute
     *
     * Precondition: 0 <= minute <= 59
     *
     * Returns: nothing
     */
    // TODO...
    


    public boolean equals(Time Other){
        if(this.hours == Other.getHour() && this.minuets == Other.getMinute()){
            return true;
        }else{
            return false;
        }
    }

    /* equals
     * Purpose: determines whether the hour and minute of
     *  this instance of Time is equal to other's hour and minute
     *
     * Parameters: Time other
     *
     * Precondition: other is not null and is a valid 24 hour clock time
     *
     * Returns: boolean - true if this Time equals other Time, false otherwise
     */
    // TODO...
    

    
    /* isBefore
     * Purpose: determines whether this instance of Time
     *   is strictly less that of other Time
     *
     * Parameters: Time other
     *
     * Precondition: other is not null and is a valid 24 hour clock Time
     *
     * Returns: boolean - true if this Time is before other Time, false otherwise
     */
    // TODO...
    public boolean isBefore(Time Other){
        
        if(this.hours > Other.getHour()){
            return false;
        }
        
        else if(this.hours == Other.getHour() && this.minuets >= Other.getMinute()){
            
            return false;
        }
        return true;
        
        
    }


    
    
    public void addTime(int m){
        int current_min = this.getMinute();
        int current_hour = this.getHour();
        int min_set = current_min + m;
        int min_multiplier = (int)min_set/60;
        int hour_set = current_hour + min_multiplier;
        
        
         
           if(min_set > 60){
            setHour(hour_set);
            setMinute(min_set - 60 * min_multiplier);
            //System.out.println(hour_set);
            //System.out.println(min_set - 60 * min_multiplier);
            
        
        }else{
           setMinute(min_set); 
        }
        if(hour_set > 23){
            setHour(hour_set - 24);
            //System.out.println(hour_set - 24);
        
            }
      
        
        
    }
    /* addTime
     * Purpose: updates the values of this Time's hour and minute
     *  by adding the given minutes.
     *  The updated time is a valid 24 hour clock Time
     *
     * Parameters: int minutes
     *
     * Precondition: minutes >= 0
     *
     * Example:
     *  Time t = new Time(23, 30);
     *  t.addTime(70) will change t's hour to 0 and minute to 40
     *  This is because 23:30 == 11:30pm,
     *  we add 70 minutes (1 hr, 10 minutes) => 12:40am = 0:40 on 24 hour clock
     *  RECALL 00:00 is 12:00am which is midnight
     */
    // TODO...
    

    public String toString(){
        int updated_hours = this.hours - 12;
        if(this.hours > 11){
            //System.out.println(this.hours + ":" + this.minuets + "pm");
            
            if(this.hours >= 13){
                //System.out.println(updated_hours + ":" + this.minuets + "pm");
                String thirteen = updated_hours + ":" + this.minuets +"pm";
                return thirteen;
            }   
            String twelve = this.hours + ":" + this.minuets +"pm";
            return twelve;
        }
        else{
            //System.out.println(this.hours + ":" + this.minuets + "am");
            String am = this.hours + ":" + this.minuets +"am";
            return am;
            
        }
    }

    /* toString
     * Purpose: returns a String representing this Time formated as:
     *  hour:minute am/pm
     *
     * Parameters: nothing
     *
     * Returns: String - a representation of this Time
     *
     * Example:AAAAAAAA
     *  Time t = new Time(22, 2)
     *  t.toString() returns "10:2pm"
     *  NOTICE: ignore that the leading 0 is not printed in the minutes
     *  Time t = new Time(0, 22)
     *  t.toString() returns "0:22am"
     *  NOTICE: we are representing 0:00am as 0:0am, not 12:00am to simplify
     */
    // TODO...
    

}

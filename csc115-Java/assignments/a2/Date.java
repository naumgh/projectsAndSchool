/*
 * Date class
 *  represents a date in the Gregorian calendar (used in most of the world).
 *  started in year 1582
 */
public class Date {
    
    // TODO add Date attributes/fields...
    
    /* Date
     * Purpose: Initialize this instance of Date with values for: January 1, 1582
     *
     * Parameters: nothing
     */
    // TODO...
    String month;
    int day;
    int year;
    
    
    
    /* Date
     * Purpose: Initialize this instance of Date with parameter values
     *
     * Parameters: String month, int day, int year
     *
     * Precondition: month, day and year specify a valid date
     *  in the Gregorian calendar.
     */
    // TODO...
    
    
    public Date(){
        this("January", 1, 1582);
        
        
    }
    public Date(String month, int day, int year){
        this.month = month;
        this.day = day;
        this.year = year;
        
        
    }
    
    

    /* getMonth
     * Purpose: Returns the month associated with this Date
     *
     * Parameters: nothing
     *
     * Returns: (String) - month associated with this Date
     */
    // TODO...
    public String getMonth(){
        return month;
        
    }
    

    
    /* setMonth
     * Purpose: sets the month associated with this Date to parameter value
     *
     * Parameters: String month
     *
     * Precondition: month with this Date's day and year specify a valid date
     *  in the Gregorian calendar.
     *
     * Returns: nothing
     */
    // TODO...
    public void setMonth(String m){
        month = m;
        //System.out.println(month);
    
    }
    


    /* getDay
     * Purpose: Returns the day associated with this Date
     *
     * Parameters: nothing
     *
     * Returns: (int) - day associated with this Date
     */
    // TODO...
    public int getDay(){
        return day;
        
    }


    /* setDay
     * Purpose: sets the day associated with this Date to parameter value
     *
     * Parameters: int day
     *
     * Precondition: day with this Date's month and year specify a valid date
     *  in the Gregorian calendar.
     *
     * Returns: nothing
     */
    // TODO...
    
    public void setDay(int d){
        day = d;
        //System.out.println(day);
        
        
    }

    /* getYear
     * Purpose: Returns the year associated with this Date
     *
     * Parameters: nothing
     *
     * Returns: int - year associated with the date
     */
    // TODO...
    public int getYear(){
        return year;
        
    }


    /* setYear
     * Purpose: sets the year associated with this Date to parameter value
     *
     * Parameters: int year
     *
     * Precondition: year with this Date's day and month specify a valid date
     *  in the Gregorian calendar.
     *
     * Returns: nothing
     */
    // TODO...
    public void setYear(int y){
        year = y;
        //System.out.println(year);
        
    }


    /* equals
     * Purpose: determines whether the month, day and year of
     *  this instance of Date is equal to other's month, day, year
     *
     * Parameters: Date other
     *
     * Precondition: other is not null and is a valid Gregorian date
     *
     * Returns: true if this Date equals other date, false otherwise
     */
    // TODO...
    public boolean equals(Date other){
        if(this.month == other.getMonth() && this.day == other.getDay() && this.year == other.getYear()){
            return true;
        }else{
            return false;
        }
    }
    



    /* toString
     * Purpose: returns a String representing this Date formated as:
     *  month day, year
     *
     * Parameters: nothing
     *
     * Returns: String - a representation of this Date
     *
     * Example:
     *  Date d = new Date("January", 25, 2019)
     *  d.toString() returns "January 25, 2019"
     */
    // TODO...
    public String toString(){
       
        return this.month + " " + this.day + "," + " " + this.year;
    }
    

}

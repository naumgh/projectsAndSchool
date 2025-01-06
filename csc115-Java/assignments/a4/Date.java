/*
 * Date class
 *  represents a date in the Gregorian calendar (used in most of the world).
 *  started in year 1582
 */
public class Date {
    
    private String month;
    private int day;
    private int year;
    
    
    /*
     * Purpose: Initialize this instance of Date with values for: January 01, 1582
     *
     * Parameters: nothing
     */
    public Date () {

        this.month = "January";
        this.day   = 1;
        this.year  = 1582;
    }

	/*
     * Purpose: Initialize this instance of Date with parameter values
     *
     * Parameters: String month, int day, int year
     *
     * Precondition: month, day and year specify a valid date
     *  in the Gregorian calendar.
     */
	public Date (String month, int day, int year) {

        this.month = month;
        this.day   = day;
        this.year  = year;
	}

    /*
     * Purpose: Returns the month associated with this Date
     *
     * Parameters: nothing
     *
     * Returns: (String) - month associated with this Date
     */
    public String getMonth() {
        return month;
    }
    
    /*
     * Purpose: sets the month associated with this Date to parameter value
     *
     * Parameters: String month
     *
     * Precondition: month with this Date's day and year specify a valid date
     *  in the Gregorian calendar.
     *
     * Returns: nothing
     */
	public void setMonth (String month) {
		this.month = month;
	}

    /*
     * Purpose: Returns the day associated with this Date
     *
     * Parameters: nothing
     *
     * Returns: (int) - day associated with this Date
     */
    public int getDay () {
        return day;
    }

    /*
     * Purpose: sets the day associated with this Date to parameter value
     *
     * Parameters: int day
     *
     * Precondition: day with this Date's month and year specify a valid date
     *  in the Gregorian calendar.
     *
     * Returns: nothing
     */
    public void setDay (int day) {
        this.day = day;
    }

    /*
     * Purpose: Returns the year associated with this Date
     *
     * Parameters: nothing
     *
     * Returns: int - year associated with the date
     */
    public int getYear () {
        return year;
    }

    /*
     * Purpose: sets the year associated with this Date to parameter value
     *
     * Parameters: int year
     *
     * Precondition: year with this Date's day and month specify a valid date
     *  in the Gregorian calendar.
     *
     * Returns: nothing
     */
    public void setYear (int year) {
        this.year = year;
    }

    /*
     * Purpose: determines whether the month, day and year of
     *  this instance of Date is equal to other's month, day, year
     *
     * Parameters: Date other
     *
     * Precondition: other is not null and is a valid Gregorian date
     *
     * Returns: true if this Date equals other date, false otherwise
     */
    public boolean equals (Date other) {
        return  other.getMonth().equals(month) &&
                other.getDay()   == day &&
                other.getYear()  == year;
    }


    /*
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
	public String toString() {
			return month + " " + day + ", " + year;
	}
}

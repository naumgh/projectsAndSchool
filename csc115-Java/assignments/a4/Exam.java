/*
 * Exam class representing a scheduled exam
 */
public class Exam {

    private String course;      // name of course being examined
	private Date date;          // date of the exam
    private String location;    // location of the exam
    private Time startTime;     // time exam starts
    private int duration;       // number of minutes the exam is

    
    /*
     * Purpose: Initialize this instance of Exam with parameter values
     *  location is set to "TBA", duration is set to default 180 minutes
     *
     * Parameters: String course, Date date, Time startTime
     *
     */
    public Exam (String course, Date date) {
        this.course     = course;
        this.date       = date;
        this.location   = "TBA";
        this.startTime  = new Time(9,00);
        this.duration   = 180;
    }
    
    
    /*
     * Purpose: Initialize this instance of Exam with parameter values
     *  location is set to "TBA", duration is set to default 180 minutes
     *
     * Parameters: String course, Date date, Time startTime
     *
     */
    public Exam (String course, Date date, Time startTime) {
        this.course     = course;
        this.date       = date;
        this.location   = "TBA";
        this.startTime  = startTime;
        this.duration   = 180;
    }

    /*
     * Purpose: Initialize this instance of Exam with parameter values
     *
     * Parameters: String course, Date date, String location, Time startTime, int duration
     *
     */
    public Exam (String course, Date date, String location, Time startTime, int duration) {
        this.course     = course;
        this.date       = date;
        this.location   = location;
        this.startTime  = startTime;
        this.duration   = duration;
    }
    
    /*
     * Purpose: Returns the course associated with this Exam
     *
     * Parameters: nothing
     *
     * Returns: String - course associated with this Exam
     */
    public String getCourse () {
        return course;
    }

    /*
     * Purpose: sets the course associated with this Exam to parameter value
     *
     * Parameters: String course
     *
     * Returns: nothing
     */
    public void setCourse(String course) {
        this.course = course;
    }
    
    /*
     * Purpose: Returns the date associated with this Exam
     *
     * Parameters: nothing
     *
     * Returns: Date - date associated with this Exam
     */
    public Date getDate () {
        return date;
    }

    /*
     * Purpose: sets the date associated with this Exam to parameter value
     *
     * Parameters: Date date
     *
     * Returns: nothing
     */
	public void setDate(Date date) {
		this.date = date;
	}

    /*
     * Purpose: Returns the location associated with this Exam
     *
     * Parameters: nothing
     *
     * Returns: String - location associated with this Exam
     */
    public String getLocation () {
        return location;
    }

    /*
     * Purpose: sets the location associated with this Exam to parameter value
     *
     * Parameters: String location
     *
     * Returns: nothing
     */
    public void setLocation (String location) {
        this.location = location;
    }

    /*
     * Purpose: Returns the startTime associated with this Exam
     *
     * Parameters: nothing
     *
     * Returns: Time - startTime associated with this Exam
     */
    public Time getStartTime () {
        return startTime;
    }

    /*
     * Purpose: sets the startTime associated with this Exam to parameter value
     *
     * Parameters: Time startTime
     *
     * Returns: nothing
     */
    public void setStartTime (Time startTime) {
        this.startTime = startTime;
    }
    
    /*
     * Purpose: Returns the duration associated with this Exam
     *
     * Parameters: nothing
     *
     * Returns: int - duration associated with this Exam
     */
    public int getDuration () {
        return duration;
    }

    /*
     * Purpose: sets the duration associated with this Exam to parameter value
     *
     * Parameters: int duration
     *
     * Precondition: duration >= 60
     *
     * Returns: nothing
     */
    public void setDuration (int duration) {
        this.duration = duration;
    }


    /*
     * Purpose: determines whether the Date and Time of this Exam
     *  overlaps with the other Exam
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
    public boolean isOverlap (Exam other) {
        if (!this.getDate().equals(other.getDate()))
            return false;
        
        Time thisStartTime = this.getStartTime();
        Time thisEndTime = new Time(thisStartTime.getHour(), thisStartTime.getMinute());
        thisEndTime.addTime(duration);
        
        Time otherStartTime = other.getStartTime();
        Time otherEndTime = new Time(otherStartTime.getHour(), otherStartTime.getMinute());
        otherEndTime.addTime(other.getDuration());

        
        return  otherStartTime.isBefore(thisEndTime) &&
            thisStartTime.isBefore(otherEndTime);
    }

    /*
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
	public String toString() {
        Time endTime = new Time(startTime.getHour(), startTime.getMinute());
        endTime.addTime(duration);
        
        return course + ": " + date + ": " + location + ": " + startTime + "-" + endTime;
	}
}

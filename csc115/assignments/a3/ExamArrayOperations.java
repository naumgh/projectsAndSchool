import java.lang.Math;

/*
 * ExamArrayOperations
 */
public class ExamArrayOperations {
    
    /*
     * getAllExamLocations
     *
     * Purpose: creates a new array of the locations of all of the exams in the given array
     *
     * Parameters: Exam[] - array
     *
     * Returns: String[] - new array of Exam locations
     *
     */
    // TODO:
	
	public static String[] getAllExamLocations(Exam[] array){
		String[] locations = new String[array.length];
		
		for(int i = 0; i < array.length; i++){
			//System.out.println(array[i].getLocation());
			locations[i] = array[i].getLocation();
		}
		
		//System.out.println(array.toString());
		
		return locations;
	}
    
    
    /*
     * getExamDuration
     *
     * Purpose: gets the duration of the Exam in the given array that is
     *  at the given location.
     * If there is more than one exam at the given location,
     *  it gets the location of the first encountered in the given array.
     *
     * Parameters: Exam[] - array, String - location
     *
     * Returns: int - the duration of the Exam or 0 if Exam location is not found
     *
     */
    // TODO:
	public static int getExamDuration(Exam[] array, String location){
		int duration = 0;
		
		for(int i = 0; i < array.length; i++){
			//if(array.length == 0){
				//duration = 0;
				//return duration;
			//}
			
			//System.out.println(array[i].getLocation());
			
			
			if(location == array[i].getLocation()){
				return array[i].getDuration();
			}
			
		}
		return duration;
	}
	
    
    
    /*
     * addExam
     *
     * Purpose: creates a new array 1 longer than input array and copies all Exam references
     *  from input array to new array and puts e at the end of new array
     *
     * Parameters: Exam[] - array, Exam - e
     *
     * Preconditions:  e is not null
     *
     * Returns:  Exam[] - the new array
     *
     */
    // TODO:
	public static Exam[] addExam(Exam [] array, Exam e){
		Exam[] return_e = new Exam[array.length + 1];
		
		for(int i = 0; i < array.length; i++){
			//System.out.println(array[i]);
			return_e[i] = array[i];
		}
		return_e[array.length] = e;
		
		return return_e;
	}
    
    
    
    /*
     * countExamsOnDate
     *
     * Purpose: counts the number of Exams in array with specified Date
     *
     * Parameters: Exam[] - array, Date - date
     *
     * Returns: int - the count
     *
     */
    // TODO:
	public static int countExamsOnDate(Exam[] array, Date d){
		int count =0;
		for(int i = 0; i < array.length; i++){
			//System.out.println(array[i].getDate());
			if(array[i].getDate().toString().equals(d.toString())){
				count += 1;
			}
		}
		//System.out.println(count);
		return count;
	}
    
    
    
    /*
     * removeExamsWithDate
     *
     * Purpose: if input array has Exams with the given date,
     *      returns a new array with only those Exams with the given date.
     *  The size of the new array must match the number of Exams
     *      without the given date in the given array.
     *  If the given array does not have Exam with given date,
     *      it returns input array unchanged.
     *
     * Parameters: Exam[] - array, Date date
     *
     * Returns: Exam[] - new array
     *
     */
    // TODO:
    public static Exam[] removeExamsWithDate(Exam[] array, Date date){
		Exam[] copy_array = new Exam[array.length];
		int length = 0;
		
		for(int i = 0; i < array.length; i++){
			if(!(array[i].getDate().equals(date))){
				//System.out.println(copy_array[length]);
				copy_array[length] = array[i];
				length++;
			}
		}
		if(length == 0 || length == array.length){
			return array;
		}
		Exam[] new_array = new Exam[length];
		while(length >= 0){
		if(copy_array[length] != null){
			new_array[length]=copy_array[length];
		}
		length--;
		
	}
		return new_array;
	}
    
    /*
     * getEarliestTimeExam
     *
     * Purpose: get the Exam from array that has the earliest startTime
     *  If there is more than one Exam that is the earliest,
     *  use the first occurance of the earliest in array
     *
     * Parameters: Exam[] - array
     *
     * Precondition: array is not empty
     *
     * Returns: Exam - oldest Exam
     *
     */
    // TODO:
    
	
	public static Exam getEarliestTimeExam(Exam[] array){
		Exam min = array[0];
		int small = 0;
		for(int y = 1; y < array.length; y++){			
			if(array[small].getStartTime().isBefore(array[y].getStartTime())){
					
					min = array[small];
				//	System.out.println(min);
				if(array[small].getStartTime().equals(array[y].getStartTime())){
					min = array[small];
			//		System.out.println(min);
				}
			
			}		
		
			if(array[y].getStartTime().isBefore(array[small].getStartTime())){
			min = array[y];
			}
			//if(){
				
				}
		//System.out.println(min);
				return min;
			
	}
		
	
  
    
	}


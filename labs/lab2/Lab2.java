/*
 * Lab2.java
 *
 * A class of static methods that operate on Students
 *
 */
public class Lab2 {
    
    /*
     *
     * Purpose: determines which of Students s1 and s2
     *  have the higher grade
     *
     * Parameters: Student - s1, Student - s2
     *
     * Precondition: s1 and s2 are not null
     *
     * Returns: Student - the Student with the higher grade,
     *  s1 if they have the same grade
     *
     */
    public static Student getHigherGradeStudent(Student s1, Student s2) {
        // ToDo: implement getHigherGradeStudent
      
		int grade1 = s1.getGrade();
		int grade2 = s2.getGrade();
	  
	   if(grade1 == grade2){
			//System.out.println(grade1);
			//System.out.println(grade2);
			return s1;
		}else if(grade1 > grade2){
			//System.out.println(grade1);
			//System.out.println(grade2);
			return s1;
        }else{
			return s2;
		}
		//return null;
	}

    
    
    /*
     *
     * Purpose: determines whether the grade of Student s
     *  is above the threshold
     *
     * Parameters: Student - s, int - threshold
     *
     * Returns: boolean - true if grade is above threshold,
     *          false otherwise
     *
     */
    // ToDo: implement isGradeAbove
    
    public static boolean isGradeAbove(Student S, int threshold){
		int grade = S.getGrade();
		System.out.println(grade);
		if(grade > threshold){
			return true;
		}else{
			return false;
		}
	}
    
    /*
     *
     * Purpose: creates an array sIDs of all Students in students
     *
     * Parameters: Student[] - students
     *
     * Returns: String[] - array of sIDs
     *
     */
    // ToDo: implement getClasslist
    public static String[] getClasslist(Student[] stud){
		String[] new_student_data= new String[stud.length];
		for(int i = 0; i < stud.length; i++){
			new_student_data[i] = stud[i].getSID();
			
			
		}
		//System.out.println(new_student_data);
		System.out.println(new_student_data);
		return new_student_data;
	}
    
	
    /*
     *
     * Purpose: counts the number of Students in students
     *  with grade above threshold
     *
     * Parameters: Student[] - students, int threshold
     *
     * Returns: int - the count
     *
     */
    // ToDo: implement countAbove
    // HINT: you should be using the isGradeAbove method!
    
    public static int countAbove(Student[] S, int threshold){
		int count = 0;
		//int grade = S.getGrade();
		for(int i = 0; i < S.length; i++){
			//Student grade = S[i].getGrade();
			if(isGradeAbove(S[i], threshold) == true){
				count += 1;
			}
		}
		
		return count;
	}
    
    /*
     *
     * Purpose: calculates the average grade of Students in students,
     *  does NOT include students with 0 grade in calculation
     *  average is 0.0 if students is empty or all students have 0 grade
     *
     * Parameters: Student[] - students
     *
     * Returns: double - the average grade
     *
     */
    // ToDo: implement getClassAverage
    // HINT: you can use the isGradeAbove method again
    public static double getClassAverage(Student[] S){
		int total = 0;
		int num_students = 0;
		//int grade = S.getGrade();
		for(int i = 0; i < S.length; i++){
			System.out.println(S[i]);
			int grade = S[i].getGrade();
			if(grade == 0){
				num_students -= 1;
			}
			total += grade;
			num_students += 1;
		}
		System.out.println(total);
		System.out.println(num_students);
		System.out.println((double)total/num_students);
		return (double)total/num_students;
	}
    
    /*
     *
     * Purpose: creates a new array 1 longer than students
     *  and adds all students and s to the new array
     *
     * Parameters: Student[] - students, Student s
     *
     * Returns: Student[] - the new array
     *
     */
    // ToDo: implement registerStudent
	
	public static Student[] registerStudent(Student[] S, Student s){
		Student[] to_return = new Student[S.length + 1];
		for(int i = 0; i < S.length; i++){
			to_return[i] = (S[i]);
			//to_return[S.length] = s;
		}
		
		System.out.println(to_return);
		return to_return;
	}

    
}

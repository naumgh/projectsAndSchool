import java.lang.Math;
import java.util.Scanner;

/*
 * ExpenseCalculator
 *
 * A class with basic expense calculations methods
 *
 */
public class ExpenseCalculator {
    
    // Calculation constants:
    private static final double GST                 = 5.0;   // Good and Service tax rate
    private static final double HOTEL_TAX           = 8.0;   // Hotel tax rate
    private static final double LOW_MILEAGE_RATE    = 0.24;  // $ per km mileage rate
    private static final double HIGH_MILEAGE_RATE   = 0.48;  // $ per km mileage rate
    private static final int    MILEAGE_LIMIT       = 100;   // The low mileage limit
    
    
    private static final int    DAYS_PER_WEEK       = 7;    // 7 days in a week
    private static final int    DAILY_FOOD_RATE     = 65;   // daily food expense rate
    private static final int    WEEKLY_FOOD_RATE    = 345;  // weekly food expense rate
    private static final int    FOOD_RATE_CUT       = 10;   // % deducted from food reimbursement reimbursment
    
    // Array access constants:
    protected static final int KMS_DRIVE_INDEX      = 0;
    protected static final int HOTEL_COST_INDEX     = 1;
    protected static final int NUM_DAYS_INDEX       = 2;
    
    
    
    /*
     * calcMileage
     *
     * Purpose: calculates the mileage cost given the number of km driven
     * NOTE:LOW_MILEAGE_RATE applied to kms up to and including 100 kms
     *      HIGH_MILEAGE_RATE applied to kms over MILEAGE_LIMIT kms
     *
     * Parameters:  double - the number of kms driven
     *
     * Preconditions: kms >=0
     *
     * Returns: double - the amount of calculated mileage expense
     *
     */
    // TODO...
    public static double calcMileage(double kms){
        double mileage_expense = 0.0;
        
        if(kms <= MILEAGE_LIMIT){
            mileage_expense = kms * LOW_MILEAGE_RATE;
        }else{
           mileage_expense = MILEAGE_LIMIT * LOW_MILEAGE_RATE +(kms-MILEAGE_LIMIT) * HIGH_MILEAGE_RATE;
        }
        
        return mileage_expense;
    }
    /*
     * calcHotel
     *
     * Purpose: calculates the hotel cost given the rate ad
     *
     * Parameters:  double - nightly rate of the hotel, int - number of days of travel
     *
     * Preconditions: numNights >= 0
     *
     * Returns: double - the amount of calculated hotel expense
     *
     */
    // TODO...
    
    public static double calcHotel(double rate, int num_nights){
        double cost = rate * (num_nights);
        
        double tax = cost * (GST + HOTEL_TAX)/100;
                
        return cost + tax;
    }
    /*
     * calcFood
     *
     * Purpose: calculates the food cost given the number of days of travel
     *  NOTE: if travel is 7 or more days uses WEEKLY_FOOD_RATE
     *          with for less than full weeks
     *          ie. if travel is 9 days, rate will be:
     *          one week at WEEKLY_FOOD_RATE + 2/7 of the WEEKLY_FOOD_RATE
     *        less than 7 days uses DAILY_FOOD_RATE
     *        if travel is more than 4 weeks, the total reimbursment will
     *          be reduced by the percent defined in FOOD_RATE_CUT
     *
     * Parameters:  int - number of days of travel
     *
     * Preconditions: the number of days is >= 1
     *
     * Returns: double - the amount of calculated food expense
     *
     */
    
    public static double calcFood(double num_days){
           double expense = 0.0;
                
          if (num_days>=DAYS_PER_WEEK ){
              
              expense = (num_days/DAYS_PER_WEEK) * WEEKLY_FOOD_RATE;
                      
            }else{
                expense = (int)num_days * (int)DAILY_FOOD_RATE;
            }    
          if (num_days/DAYS_PER_WEEK > 4){
                expense *= (1 - (double)FOOD_RATE_CUT/100);
            }                           
            return expense;    
    }
    // TODO...
    
    
    /*
     * calcTotalExpense
     *
     * Purpose: calculates the expenses for a person as:
     *   the sum of mileage, hotel and food costs
     *   NOTE: hotel is not needed for the last day of travel
     *
     * Parameters:  double[] - an array of data from a single person at the following indices:
     *              [KMS_DRIVE_INDEX]  - the number of kms they drove
     *              [HOTEL_COST_INDEX] - the cost of the hotel per night
     *              [NUM_DAYS_INDEX]   - the number of days they were traveling
     *
     * Preconditions: data must be of length 3 with expected values at indices listed above
     *
     * Returns: double - total expenses for a person with the given data
     *
     */
    public static double calcTotalExpense(double[] data){
        double mileage = calcMileage(data[KMS_DRIVE_INDEX]);
        double hotel = calcHotel(data[HOTEL_COST_INDEX],(int)(data[NUM_DAYS_INDEX])-1);
        double food = (int)calcFood(data[NUM_DAYS_INDEX]);
                
        double result = mileage + hotel + food;
                    
        return result;
    }
    // TODO...
    
    
    /*
     * calcAllExpenses
     *
     * Purpose: calculates the expenses for each person in a population
     *   and stores the result in the corresponding index of the 1D result array
     *
     * Parameters:  double[][] - a 2D array of data for a populution where,
     *                each row represents a person in the population and
     *                each column of a row has the following data for that individual:
     *                  [KMS_DRIVE_INDEX]  - the number of kms they drove
     *                  [HOTEL_COST_INDEX] - the cost of the hotel per night
     *                  [NUM_DAYS_INDEX]   - the number of days they were traveling
     *
     *  NOTE: the decimal portion of the values stored in the result array will be truncated
     *
     * Preconditions: the data array must have 3 columns and
     *      the length of the 1D result array must be
     *      equal to the number of rows in the data array
     *
     * Returns: int[] - a 1D array to store the total expense for each individual
     *
     */
     public static int [] calcAllExpenses(double[][]data){  
         
         int [] expense_results = new int[(data.length)];
         for(int index = 0; index < data.length; index++){
             expense_results[index] = (int)calcTotalExpense(data[index]);
         }
         
        
        // expense_results.append(int(calc_total_expense(person)))
        
         return expense_results;

        
      // expense_results.append(int(calc_total_expense(person))) 
        //return expense_results;  
    }
    
 }

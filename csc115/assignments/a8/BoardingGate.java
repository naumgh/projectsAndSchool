/*
 * represents a transit boarding gate (train, airplane, etc.)
 */

public class BoardingGate {
    
    private PriorityQueue passengers;
    private int currentSize;
    //protected final static int DEFAULT_SIZE = 10000;
    
    /* constructor
     *
     * PURPOSE:
     *  initialize passengers to the default capacity of a HeapPriorityQueue
     *
     * PARAMETERS:
     *  none
     */

    public BoardingGate(){
    	this.passengers = new HeapPriorityQueue();
        currentSize = 0;

    }

    
    /* constructor
     *
     * PURPOSE:
     *  initialize passengers to a new HeapPriorityQueue of given size
     *
     * PARAMETERS:
     *  int size - capacity of passengers
     */
    public BoardingGate(int size){
    	this.passengers = new HeapPriorityQueue(size);
        currentSize = 0;

    }


    
    /* addPassenger
     * PURPOSE:
     *  add given Passenger p to passengers and
     *  prints a notification message if the Triage is full
     *
     * PARAMETERS:
     *  Passenger p - Passenger to be added
     *
     * RETURNS:
     *  None.
     */

    public void addPassenger(Passenger p){
    	try{
    		currentSize += 1;
            passengers.insert(p);
    	}catch(HeapFullException v){
    		System.out.println("Triage is full");
            //throw new HeapFullException();
    	}

    }

    
    
    /* numPassengersWaiting
     * PURPOSE:
     *  returns the number of Passengers in passengers waiting to board
     *
     * PARAMETERS:
     *  None.
     *
     * RETURNS:
     *  int - number of passengers waiting to board
     */

    public int numPassengersWaiting(){
    	return passengers.size();

    }

    
    
    /* nextPassenger
     *
     * PURPOSE:
     *  removes and returns the next Passenger from passengers
     *
     * PARAMETERS:
     *  None.
     *
     * RETURNS:
     *  Passenger - the next Passenger, null if there is no more Passengers.
     */

    public Passenger nextPassenger(){
    	try{
            if(passengers.size() == 0){
                return null;
            }else{
                Passenger to_return = (Passenger)passengers.removeLow();
                return to_return;
            }
        }catch(HeapEmptyException a){
            throw new HeapEmptyException();
        }
    }


}


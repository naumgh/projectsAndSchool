import java.util.*;

public class HashMap<K extends Comparable<K>, V> {

    private int                 tableSize;
    private List<Entry<K,V>>    table;
    private int                 count;
    private static final int    NUM_ENTRIES = 33;

    public HashMap() {
        // TODO: finish this....
        table = new LinkedList<Entry<K,V>>(tableSize);
        tableSize = 101;
        count = 0;

    }

    /*
     * Purpose: Check to see if key is stored in the map.
     * Pre-conditions: None.
     * Returns: true if key is in the map, false otherwise.
     */
    public boolean containsKey(K key) {
        // TODO:



        return false;
    }

    /*
     * Purpose: Return the value stored at key in the map
     * Pre-conditions: None.
     * Returns: the value stored at key.
     * Throws: KeyNotFoundException if key is not in the map.
     */
    public V get (K key) throws KeyNotFoundException {
        // TODO:



        return null;
    }

    /*
     * Purpose: Return a List of Entry types which contain the
     *    key/value pairs of every entry in the map.
     * Pre-conditions: None.
     * Returns: An instance of List with all the key/value pairs in
     *    the map.
     */
    /*
     Java API for Iterator hasNext method:
     boolean hasNext()
     Returns true if the iteration has more elements. (In other words, returns true if next() would return an element rather than throwing an exception.)

     Java API for Iterator next method:
     E next()
     Returns the next element in the iteration.
     Throws:     NoSuchElementException - if the iteration has no more elements
     */
    public List<Entry<K,V> >    entryList() {
        List <Entry<K,V>> returnList = new LinkedList<Entry<K,V> >();
        ListIterator<Entry<K,V>> iter = table.listIterator();

        // TODO:




        return returnList;
    }

    /*
     * Purpose: Insert the key/value pair into the map.
     *    If the key already exists in the map, instead
     *    update the entry to include the new value.
     * Pre-conditions: None.
     */
    public void put (K key, V value){
        // TODO:



    }

    /*
     * Purpose: Return the number of elements in the Map.
     * Pre-conditions:  None.
     * Returns:the number of elements in the map, 0 if empty.
     */
    public int size() {
        return count;
    }

    /*
     * Purpose: Remove all elements from the map.
     * Pre-conditions: None.
     */
    public void clear() {
    }

    public static void main(String[] args) {

        // Q1. What will the following code output?
        // SEE: https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html
        List<Integer> l = new ArrayList<Integer>(20);  // create a new ArrayList of initial capacity 20
        l.add(600);  // add 600 to end of the list
        System.out.println("l: " + l);

        // Q2. if we uncomment the following lines of code how will the output change?
        l.add(5, 500);
        System.out.println("l: " + l);

        
        // Q3. Implement the constructor and put method with no collision resolution
        HashMap<Integer, String> map = new HashMap<Integer, String>();
        
        Random r = new Random(128);    // by hardcoding the seed, we get the same numbers every time
        for(int i=0; i<NUM_ENTRIES; i++) {
            map.put(r.nextInt(1000), String.valueOf(i)); // key is random number between 0,1000
        }

        System.out.println("table: " + map.table);
        
        // Q4. Implement the entryList method
//        System.out.println(map.entryList());
        
        // implement and test the remaining methods
    }

}




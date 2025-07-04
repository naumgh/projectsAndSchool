package com.cooksys.ftd.assignments.control;

import com.cooksys.ftd.assignments.control.util.MissingImplementationException;

/**
 * The Fibonacci sequence is simply and recursively defined: the first two elements are `1`, and
 * every other element is equal to the sum of its two preceding elements. For example:
 * <p>
 * [1, 1] =>
 * [1, 1, 1 + 1]  => [1, 1, 2] =>
 * [1, 1, 2, 1 + 2] => [1, 1, 2, 3] =>
 * [1, 1, 2, 3, 2 + 3] => [1, 1, 2, 3, 5] =>
 * ...etc
 */
public class Fibonacci {

    /**
     * Calculates the value in the Fibonacci sequence at a given index. For example,
     * `atIndex(0)` and `atIndex(1)` should return `1`, because the first two elements of the
     * sequence are both `1`.
     *
     * @param i the index of the element to calculate
     * @return the calculated element
     * @throws IllegalArgumentException if the given index is less than zero
     */
    public static int atIndex(int i) throws IllegalArgumentException {
    	//common leetcode question
    	if(i < 0) {
    		throw new IllegalArgumentException("given index is less than 0");
    	}
    	
    	//base case (used to be):
    	if(i == 0 || i == 1) {
    		return 1;
    	}
    	/*
    	return(atIndex(i-1) + atIndex(i-2));
    	*/
    	//recursive stack got WAY too big (took over 5 minutes to run tests), trying iteration now...
    	int prev = 1;
    	int current = 1;
    	
    	for(int start_of_fib_sequence = 0; start_of_fib_sequence <= i-2; start_of_fib_sequence++) {
    		int next = prev + current;
    		prev = current;
    		current = next;
    	}
    	return current;
    }

    /**
     * Calculates a slice of the fibonacci sequence, starting from a given start index (inclusive) and
     * ending at a given end index (exclusive).
     *
     * @param start the starting index of the slice (inclusive)
     * @param end   the ending index of the slice(exclusive)
     * @return the calculated slice as an array of int elements
     * @throws IllegalArgumentException if either the given start or end is negative, or if the
     *                                  given end is less than the given start
     */
    public static int[] slice(int start, int end) throws IllegalArgumentException {
        int[] res = new int[end-start];
    	if(start < 0 || end < 0 || end < start) {
        	throw new IllegalArgumentException("start or end cannot be less than 0, or end is less than start");
        }
        
        for(int i = start; i < end; i++) {
        	res[i-start] = atIndex(i);
        }
        /*
        for(int i = 0; i < res.length; i++) {
        	System.out.println(res[i]);
        }
        */
        return res;
    }

    /**
     * Calculates the beginning of the fibonacci sequence, up to a given count.
     *
     * @param count the number of elements to calculate
     * @return the beginning of the fibonacci sequence, up to the given count, as an array of int elements
     * @throws IllegalArgumentException if the given count is negative
     */
    public static int[] fibonacci(int count) throws IllegalArgumentException {
    	if(count < 0) {
    		throw new IllegalArgumentException("count must be positive");
    	}
    	int[] res = new int[count];
    	
    	for(int i = 0; i < count; i++) {
    		res[i] = atIndex(i);
    	}
    	return res;
    }
}

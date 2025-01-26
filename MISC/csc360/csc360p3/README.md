Naum Hoffman
V00927502
3/14/2022

p2B MTS

Description: A program that uses threads, mutexes and condition variables to simulate an automated control system for trains

note: major differences between p2a and p2b algorithms

to run: 
make mts.c
./mts [INPUT FILE]


Relevant functions:
	1. File Access:
		-fopen
		-fscanf
		-fclose
	2. Thread functions:
		-pthread_create
		-pthread_exit
		-pthread_join
	3. Mutex functions
		-pthread_mutex_init
		-pthread_mutex_lock
		-pthread_mutex_unlock
	4. Condition variable functions
		-pthread_cond_init
		-pthread_cond_wait
		-pthread_cond_broadcast
		-pthread_cond_signal

current psuedocode:
	create train struct
	create node struct (set up priority queue) and initialize east and west station
		-for pro queue create these fucntions: pop(), newnode(), peek(), push(), isempty
	
	create train thread function
		-usleep(loading time)
		-mutex lock
		-add train to pri queue
		-if train going west, pushed to weststation pq
		-if train going east, pushed to eaststation pq
		-mutex unlock
		-signal dispatch ready
		-mutex lock
		-wait for track signal
		-once track ready, output train on track
		-usleep(crossing time)
		-print train off track
		-dispatch track and destroy convar, exit thread

	create dispatch function
		-check and wait for ready trains
		- dispatcher finds/signal the next train to cross
            - If there is a single train ready, dispatch (train in one of the stations)
            - If there are multiple loaded trains, the one with the higher priority crosses
            - If there is more than one train with the same priority
                - If with the same direction, check the loading_time
                 - If with the same loading time, dispatch the first in the input file (based on train_id)
                - if with opposite directions, dispatch the one opposite from the last dispatched
        - wait until the crossing finishes
        - Pop the dispatched train from the station
        - end if all trains have crossed

    int main function(input_file):
        - Read input file, parse line-by-line, store into train_struc
        - Create train thread with train_thread function and train_struc
        - join threads
		
	
	
	


-Previous p2a Alorithm:
	In load function:
	Initialize station mutex
	Load train
	If train is loaded, get station mutex, put into array, sort array, release station mutex	
	Print train loaded
	In Dispatch function:
	Initialize dispatch mutex
	Using additional array, sort east station and west station trains
	Get dispatch mutex, dispatch train according to east or west station in array, pop train from array
	when used.
	Release dispatch matrix.
	In main:
	Parse stdin file and initialize station arrays
	Load()
	Dispatch()


refrences: priority queues inspired by https://www.geeksforgeeks.org/priority-queue-using-linked-list/
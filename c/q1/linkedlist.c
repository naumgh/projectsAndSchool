/*
 * This program will use list.c to create linked lists and store animal related scientific information. 
 * Proper MEMORY MANAGEMENT is required.
 * Complete implementation of the code per instructions below. 
 * You may add a helper function, although it is not required.
 * You CANNOT modify or delete any of the code given.
 * You CANNOT use any libraries, other than the ones included here.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"
#include "list.c"
#include "emalloc.c"

#define MAX_LINE_LEN 80

/*
 * SECTION 01
 * Complete the implementation of section 01 in list.c FIRST. 
 * NOTE that the function add_to_position CANNOT CALL functions add_front OR add_end
 *
 * SECTION 02
 * Then proceed to section 02 in list.c. 
 * NOTE that function add_front MUST CALL THE FUNCTION add_to_position.
 * 
 * SECTION 03
 * Next, proceed to section 03 in this file. 
 * 
 * SECTION 04 (BONUS SECTION in list.c)
 * This is a bonus section and is not required. 
 * Implement Section 04 in list.c
 * NOTE that function add_end MUST CALL THE FUNCTION add_to_position.
 *
 * SECTION 05 (BONUS SECTION)
 * This is a bonus section and is not required
 *
 */


int main(int argc, char *argv[]) {
    
    node_t *list = NULL;    
    list = add_at_position(list, "S1", "G1", "N1", 0);
    list = add_at_position(list, "S2", "G2", "N2", 1);
    list = add_at_position(list, "S3", "G3", "N3", 0);    
    list = add_at_position(list, "S4", "G4", "N4", 0);    
    list = add_at_position(list, "S5", "G5", "N5", 0);
    list = add_at_position(list, "S6", "G6", "N6", 5);
    list = add_at_position(list, "S7", "G7", "N7", 2);
    list = add_at_position(list, "S8", "G8", "N8", 4);


    
    exit(0); 

}

/*
 * SECTION 03 (2 marks)
 * Note the calls to the add_at_position function in the main.
 * When the code is run in main(), after which add_at_position() call is S3 at index 3?

 * To answer this question, write the order of function calls in main that would have to execute.
 */

//the function call at 2 pushes the node at s3 to 3
WRITE YOUR ANSWER TO SECTION 03 HERE



/*
 * SECTION 05 (BONUS) (2 marks)
 * After executing main(), what is the order of nodes inside "list", starting at index 0?
 */


WRITE YOUR ANSWER TO SECTION 05 HERE



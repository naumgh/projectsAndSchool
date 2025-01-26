/*
 *
 * Implement code per instructions in section 01, 02 and 04 below.
 * All code provided MUST REMAIN UNCHANGED. 
 * NOTE: There is no SECTION 03 in this file. 
 * 
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "emalloc.h"
#include "list.h"


void print_node(node_t *p) {
        
    if (p != NULL) {          
        printf("%s ,", p->species);        
        
    } else {
        printf("Empty\n");
    }    
}

node_t *new_node(char *sp, char *gn, char *nm) {
    assert( sp != NULL);
    assert( gn != NULL);    
    assert( nm != NULL);

    node_t *temp = (node_t *)emalloc(sizeof(node_t));

    temp->species = strdup(sp);
    temp->genus = strdup(gn);
    temp->name = nm;    
    temp->next = NULL;

    return temp;
}

/*
 * SECTION 01 (8 marks)
 * Complete the implementation of "add_at_position" function to add a node to the linked list at the index "position". 
 * You CANNOT change the function definition
 * INDEXING STARTS AT 0
 * Function must work for all use cases and not just the cases shown in the main
 */

node_t * add_at_position(node_t *head, char* species, char* genus, char* name, int key){
    node_t *new_node = (node_t *)malloc(sizeof(node_t));
    if(new_node == NULL){
        return head;
    }
    new_node->species = species;
    new_node -> genus = genus;
    new_node -> name = name;

    if(head == NULL || key <= 0){
        new_node -> next = head;
        return new_node;
    } 

    node_t * currentNode = head;

    while(currentNode->next != NULL && --key > 0){
        currentNode = currentNode->next;
    }
    new_node -> next = currentNode -> next;
    currentNode -> next = new_node;

    return head;
}




/*
 * SECTION 02 (2 marks)
 * Complete the implementation of the add_front function that adds a node to the front of the linked list 
 * being passed in by the pointer list. 
 * It is REQUIRED that you use the add_at_position function from SECTION 01. 
 * 0 marks will be awarded if add_at_position is not used.
 */

void add_front(node_t * list, char * species, char * genus, char *name){
    node_t *new_node = (node_t *)malloc(sizeof(node_t));
    list -> species = species;
    list -> genus = genus;
    list -> name = name;

    add_at_position(list, species, genus, name, 1);
   
    
    return list;
}


/*
 * SECTION 04 (BONUS) (3 marks)
 * Complete the implementation of the add_end function that adds a node to the end of the linked list 
 * being passed in by the pointer list
 * It is REQUIRED to use the add_at_position function. 
 * 0 marks will be awarded if add_at_position is not used.
 * Marks awarded only if SECTIONS 01 and 02 are completed. 
 */



node_t *peek_front(node_t *list) {
    node_t *list = NULL;
    char*genus;
    char*species;
    char*name;
    x = getCount()
    add_at_position();
    return list;
}






/*
 * icsout3.c
 *
 * Starter file provided to students for Assignment #3, SENG 265,
 * Spring 2021.
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "emalloc.h"
#include "ics.h"
#include "listy.h"

//#define DEBUG	0

#define MAX_LINE_LEN 132
#define MAX_EVENTS 500
#define MAX_CHAR 1000
#define EVENT_LINE 80
#define EVENT_NUM 256
#define MAX_CHAR_NUM  256
#define MAX_CONTENT_CHAR_NUM 512
#define MAX_FILE_SIZE 8192*1000
#define MAX_STRUCT_SIZE 48

char *title = NULL;
char *content1 = NULL;
char *date = NULL;
static int total_num = 0;
int *total = NULL;
char *file_buf = NULL;

struct vevent{
	char begin[MAX_STRUCT_SIZE];
	char dtstart[MAX_STRUCT_SIZE];
	char dtend[MAX_STRUCT_SIZE];
	char rrule[MAX_STRUCT_SIZE];
	char location[MAX_STRUCT_SIZE];
	char summary[MAX_STRUCT_SIZE];
	char end[MAX_STRUCT_SIZE];
};

void print_event(node_t *n, void *arg) {
    assert(n != NULL);
    event_t *event = n->val;
    node_t * temp = NULL;
char buf[1024];

	for( temp = n ; temp != NULL; temp = temp->next1)
	{
		event = temp->val;
		if(event->title_flag != 1)
		{
			printf("%s\n------------------------\n",event->title);
		}
        	printf("%s%s {{%s}}\n", event->dt,event->summary, event->location);
		free(event);
		free(temp);
	}

}


#ifdef DEBUG

/*
 * Just showing the use of the linked-list routines.
 */

void _demo() {
    event_t *temp_event = NULL;
    node_t  *temp_node  = NULL;
    node_t  *head = NULL;

    /* Add one event, without an RRULE */

    temp_event = emalloc(sizeof(event_t));
    strncpy(temp_event->dtstart, "20210306T120000", 17);
    strncpy(temp_event->dtend, "20210306T160000", 17);
    strncpy(temp_event->summary, "summary 1", SUMMARY_LEN);
    strncpy(temp_event->location, "location 1", LOCATION_LEN);
    temp_event->rrule[0] = '\0';
    temp_node = new_node(temp_event);
    head = add_front(head, temp_node);

    /* Add a second event, with an RRULE */

    temp_event = emalloc(sizeof(event_t));
    strncpy(temp_event->dtstart, "20210307T093000", 17);
    strncpy(temp_event->dtend, "20210307T102000", 17);
    strncpy(temp_event->summary, "uvwxyz 1234567", SUMMARY_LEN);
    strncpy(temp_event->location, "abcde 1234567", LOCATION_LEN);
    strncpy(temp_event->rrule, "yada RULE yada UNTIL yada", RRULE_LEN);
    temp_node = new_node(temp_event);
    head = add_front(head, temp_node);

    /* Print the list of events. */

    apply(head, print_event, NULL);

    /* Free up the memory. This is done rather deliberately
     * and manually. A full-featured function might better
     * serve for this. Asserts are liberally used here as they
     * express state that *must* be true if all of the code is
     * correctly working.
     */

    temp_node = head;
    assert(temp_node != NULL);
    head = remove_front(head);
    temp_event = temp_node->val;
    assert(temp_event != NULL);
    free(temp_event);
    free(temp_node);

    temp_node = head;
    assert(temp_node != NULL);
    head = remove_front(head);
    temp_event = temp_node->val;
    assert(temp_event != NULL);
    free(temp_event);
    free(temp_node);
   
    assert(head == NULL); 
    
}

#endif

/*
 * Function dt_format.
 *
 * Given a date-time, creates a more readable version of the
 * calendar date by using some C-library routines. For example,
 * if the string in "dt_time" corresponds to:
 *
 *   20190520T111500
 *
 * then the string stored at "formatted_time" is:
 *
 *   May 20, 2019 (Mon).
 *
 */

void dt_format(char *formatted_time, const char *dt_time, const int len)
{
    struct tm temp_time;
    time_t    full_time;
    char      temp[5];

    /*  
     * Ignore for now everything other than the year, month and date.
     * For conversion to work, months must be numbered from 0, and the 
     * year from 1900.
     */  
    memset(&temp_time, 0, sizeof(struct tm));
    sscanf(dt_time, "%4d%2d%2d",
        &temp_time.tm_year, &temp_time.tm_mon, &temp_time.tm_mday);
    temp_time.tm_year -= 1900;
    temp_time.tm_mon -= 1;
    full_time = mktime(&temp_time);
    strftime(formatted_time, len, "%B %d, %Y (%a)", 
    localtime(&full_time));
}


/*
 * Function dt_increment:
 *
 * Given a date-time, it adds the number of days in a way that
 * results in the correct year, month, and day. For example,
 * if the string in "before" corresponds to:
 *
 *   20190520T111500
 *
 * then the datetime string stored in "after", assuming that
 * "num_days" is 100, will be:
 *
 *   20190828T111500
 *
 * which is 100 days after May 20, 2019 (i.e., August 28, 2019).
 *
 */

void dt_increment(char *after, const char *before, int const num_days)
{
    struct tm temp_time, *p_temp_time;
    time_t    full_time;
    char      temp[5];

    memset(&temp_time, 0, sizeof(struct tm));
    sscanf(before, "%4d%2d%2d", &temp_time.tm_year,
        &temp_time.tm_mon, &temp_time.tm_mday);
    temp_time.tm_year -= 1900;
    temp_time.tm_mon -= 1;
    temp_time.tm_mday += num_days;

    full_time = mktime(&temp_time);
    after[0] = '\0';
    strftime(after, 9, "%Y%m%d", localtime(&full_time));
    strncpy(after + 8, before + 8, MAX_LINE_LEN - 8); 
    after[MAX_LINE_LEN - 1] = '\0';
}


int time_stamps(char * time,char * out_buf,int flag)
{
	char out_buf1[8];
	char out_buf2[8];

	memset(out_buf1,0,8);
	memset(out_buf2,0,8);
	memcpy(out_buf1,time+9,2);
	memcpy(out_buf2,time+11,2); 

	if(strncmp(time + 9,"1200",4) < 0)
	{
		if(out_buf1[0] == 0x30)
			out_buf1[0] = 32;

		if(flag == 0)
			sprintf(out_buf,"%2s:%2s AM ",out_buf1,out_buf2);
		else 
			sprintf(out_buf + 9,"to %2s:%2s AM: ",out_buf1,out_buf2);
			
	}else{
		if(out_buf1[0] == '1' && out_buf1[1] != '2')
		{
			out_buf1[0] = 32; //blank
			out_buf1[1] = out_buf1[1] - 0x2;
		}else if (out_buf1[0] == '2' && out_buf1[1] >= '2')
		{
			out_buf1[0] = '1';
			out_buf1[1] = out_buf1[1] - 2;
		}else if(out_buf1[0] == '2' && out_buf1[1] < '2')
		{
			out_buf1[0] = 32;
			out_buf1[1] = out_buf1[1] + 8;
		}
		if(flag == 0)
			sprintf(out_buf,"%2s:%2s PM ",out_buf1,out_buf2);
		else
			sprintf(out_buf + 9,"to %2s:%2s PM: ",out_buf1,out_buf2);
	}
}


node_t  *head = NULL;

int event_print(struct vevent * tmp_vevent)
{
	char time_A[MAX_LINE_LEN];
	char time_B[MAX_LINE_LEN];
	char output[MAX_LINE_LEN];
	static int flag_num = 0;
	int flag_same = 0;
	int i = 0;
	int tmp_total_num = 0;
	char out_buf1[8];
	char out_buf2[8];
	char out_buf[64];
	char time1_buf[64] = {0};
	char time2_buf[64] = {0};


	event_t *temp_event = NULL;
    	node_t  *temp_node  = NULL;
	node_t  *temp = NULL;
	node_t  *tmp = NULL;


	memset(time_A, '\0', MAX_LINE_LEN);
	memset(time_B, '\0', MAX_LINE_LEN);
	memset(output, '\0', MAX_LINE_LEN);
	memset(out_buf1, '\0', 8);
	memset(out_buf2, '\0', 8);
	memset(out_buf, '\0', 64);
	memset(time1_buf, '\0', 64);
	memset(time2_buf, '\0', 64);
	time_stamps(tmp_vevent->dtstart,out_buf,0);
	time_stamps(tmp_vevent->dtend,out_buf,1);

    	temp_event = emalloc(sizeof(event_t));
	strncpy(temp_event->dtstart,tmp_vevent->dtstart,17 +1);
    	strncpy(temp_event->dtend, tmp_vevent->dtend,17 +1);
    	strncpy(temp_event->dt,out_buf, strlen(out_buf) +1);

	//printf("out_buf:%s.\n", out_buf);
	sprintf(out_buf + strlen(out_buf),"%s ",tmp_vevent->summary);
	//printf("out_buf:%s.\n", out_buf);
	sprintf(out_buf + strlen(out_buf),"{{%s}}",tmp_vevent->location);
	//printf("out_buf:%s.\n", out_buf);	
	strncpy(time_A, tmp_vevent->dtstart, MAX_LINE_LEN +1);
	dt_format(output, time_A, MAX_LINE_LEN);	
	
	memcpy(date + total_num * MAX_CHAR_NUM,tmp_vevent->dtstart,8 + 1);

	memset(temp_event->title, '\0', 80);
	memcpy(temp_event->title,output,strlen(output) + 1);
	//printf("title:%s.\n", temp_event->title);

	temp_event->title_flag = 0;
#if 1
	for(temp = head;temp != NULL;temp= temp->next)
	{
		if(strncmp(temp->val->dtstart,tmp_vevent->dtstart,8) == 0)
		{
			temp_event->title_flag = 1;
			break;

		}

	} 
#endif

	memset(temp_event->summary, '\0', 80);
	memset(temp_event->location, '\0', 80);
    	strncpy(temp_event->summary,tmp_vevent->summary,strlen(tmp_vevent->summary) + 1);
*(temp_event->summary + strlen(tmp_vevent->summary) + 1) = '\0';

    	strncpy(temp_event->location,tmp_vevent->location, strlen(tmp_vevent->location) + 1);
*(temp_event->location + strlen(tmp_vevent->location) + 1) = '\0';
    	temp_event->rrule[0] = '\0';

	if(temp_event->title_flag == 1)
	{
    		temp_node = new_node1(temp_event);
	    	//head = add_end(head, temp_node);
	    	add_end1(temp, temp_node);
#if 0
			//printf("tmp_vevent->dtstart iiiiiis %s , temp->val1->dtstart is %s, %d\n",tmp_vevent->dtstart, temp->val->dtstart, strncmp(tmp_vevent->dtstart,temp->val->dtstart,15));
		//	temp = temp->next;

    			//apply(head, print_event, NULL);

		

				if(strncmp(tmp_vevent->dtstart,temp->val->dtstart,15) < 0) {
					 event_t tmp_t;
					//t = *temp;
					//temp->val = tmp_vevent->;
					//temp->next = t.next;
					//*temp_node = t;

					add_end1(temp,temp_node);
					memset(tmp_t.dtstart,0,17);
					memset(tmp_t.summary,0,80);
					memset(tmp_t.location,0,80);
					memset(tmp_t.title,0,80);
					memset(tmp_t.dt,0,32);

					memcpy(tmp_t.dtstart,temp->val->dtstart,17);
					memcpy(tmp_t.summary,temp->val->summary,80);
					memcpy(tmp_t.location,temp->val->location,80);
					memcpy(tmp_t.title,temp->val->title,80);
					memcpy(tmp_t.dt,temp->val->dt,32);
					//tmp_t.title_flag = temp->val->title_flag;
//printf("0location: %s, %s\n", tmp_t.location, tmp_t.summary);


					memset(temp->next1->val->dtstart,0,17);	
					memset(temp->next1->val->summary,0,80);
					memset(temp->next1->val->location,0,80 );
					memset(temp->next1->val->title,0,80 );
					memset(temp->next1->val->dt,0,32);

					memcpy(temp->next1->val->dtstart,tmp_t.dtstart,17);
					memcpy(temp->next1->val->summary,tmp_t.summary,80);
					memcpy(temp->next1->val->location,tmp_t.location,80);
					memcpy(temp->next1->val->title,tmp_t.title,80);
					memcpy(temp->next1->val->dt,tmp_t.dt,32);
					temp->next1->val->title_flag = 1;
//printf("1location: %s, %s\n", temp->next1->val->location, temp->next1->val->summary);
					
#if 1
					memset(temp->val->dtstart,0,17);	
					memset(temp->val->summary,0,80);
					memset(temp->val->location,0,80 );
					memset(temp->val->title,0,80 );
					memset(temp->val->dt,0,32);

					memcpy(temp->val->dtstart,tmp_vevent->dtstart,17);
					memcpy(temp->val->summary,tmp_vevent->summary,80);
					memcpy(temp->val->location,tmp_vevent->location,80);
					memcpy(temp->val->title,output,80);
					memcpy(temp->val->dt,out_buf,22);
					temp->val->title_flag = 0;
//printf("2location: %s, %s, %s\n", temp->val->location, temp->val->summary, temp->val->dt);
#endif

			}else {



					int temp_flag = 0;
					for(tmp = temp ;;tmp= tmp->next1)
					{
					//	printf("cmp: tmp_vevent->dtstart is %s ,tmp->val->dtstart is %s, %d  \n",tmp_vevent->dtstart,tmp->next1->val->dtstart,strncmp(tmp_vevent->dtstart,tmp->next1->val->dtstart,8));

						if(tmp->next1 != NULL)
						{
							if(strncmp(tmp_vevent->dtstart,tmp->next1->val->dtstart,15) > 0)
							{
								if(tmp->next1->next1 == NULL)
									break;
								continue;
							}else if(strncmp(tmp_vevent->dtstart,tmp->next1->val->dtstart,15) < 0)
							{
								temp_flag = 1;
								break;
							}else if(tmp->next1 == NULL){
								break;
							}
						}else{
								temp_flag = 2;
								break;
						}
					}

					if(temp_flag == 1)
						insert_node(tmp,temp_node);
					else if(temp_flag == 2)
						add_end1(tmp,temp_node);
					else
						insert_node(tmp->next1,temp_node);


		
			}
		
#endif	
	}
	else
	{
    		temp_node = new_node(temp_event);
		if(head != NULL)
		{

			//printf("0tmp_vevent->dtstart is %s , head->val->dtstart is %s\n",tmp_vevent->dtstart, head->val->dtstart);
			if(head->next == NULL)
			{
				if(strncmp(tmp_vevent->dtstart,head->val->dtstart,8) < 0)
					head = add_front(head,temp_node);
				else
					head = add_end(head,temp_node);	
			}else{
			int temp_flag = 0;


			if(strncmp(tmp_vevent->dtstart,head->val->dtstart,8) < 0)
			{
					head = add_front(head,temp_node);
			}else{
						

					temp_flag = 0;

					for(tmp = head ;;tmp= tmp->next)
					{
//						printf("tmp_vevent->dtstart is %s ,tmp->val->dtstart is %s, %d  \n",tmp_vevent->dtstart,tmp->val->dtstart,strncmp(tmp_vevent->dtstart,tmp->val->dtstart,8));
						if(strncmp(tmp_vevent->dtstart,tmp->next->val->dtstart,8) > 0)
						{
							if(tmp->next->next == NULL)
								break;
							continue;
						}else if(strncmp(tmp_vevent->dtstart,tmp->next->val->dtstart,8) < 0)
						{
							temp_flag = 1;
							break;
						}else if(tmp->next == NULL){
							break;
						}
					}
					if(temp_flag == 1)
						insert_node(tmp,temp_node);
					else
						insert_node(tmp->next,temp_node);
				}
			}
		
		}else{
			head = add_front(head,temp_node);
		}
	}
}


void print_events(int from_yy, int from_mm, int from_dd, int to_yy, int to_mm, int to_dd)
{
	struct vevent vevent_t;
	char * tmp_buf = NULL;
	char * tmp = NULL;
	int i = 0;
	char * p_dtstart = NULL;
	char * p_dtend = NULL;
	char * p_rrule = NULL;
	char * p_location = NULL;
	char * p_summary = NULL;
	char * p_end = NULL;
	char * p_until = NULL;
	char * p_byday = NULL;
	char time_A[MAX_LINE_LEN];
	char time_B[MAX_LINE_LEN];
	char output[MAX_LINE_LEN];
	char time_before[32];
	char time_after[32];
	int freq_flag = 0;
	int flag_num = 0;


	memset(time_A,0,MAX_LINE_LEN);
	memset(time_B,0,MAX_LINE_LEN);
	memset(output,0,MAX_LINE_LEN);
	memset(time_before,0,32);
	memset(time_after,0,32);

	sprintf(time_before,"%02d%02d%02d",from_yy,from_mm,from_dd);
	sprintf(time_after,"%02d%02d%02d",to_yy,to_mm,to_dd);
	
	tmp_buf = file_buf;

	if(strncmp("BEGIN:VCALENDAR",tmp_buf,strlen("BEGIN:VCALENDAR")) == 0)
	{
		tmp_buf += strlen("BEGIN:VCALENDAR");
	}else{
		printf("The file format is WRONG \n");
	}

	for( ; ; )
	{
		p_dtstart = NULL;
		p_dtstart = strstr(tmp_buf, "DTSTART:");

		if(p_dtstart == NULL)
			break;
		
		p_dtend = strstr(tmp_buf, "DTEND:");
		p_dtstart += strlen("DTSTART:");
		memset(vevent_t.dtstart,0,48);
		memcpy(vevent_t.dtstart,p_dtstart,p_dtend - p_dtstart - 1);		       

		p_rrule = strstr(tmp_buf,"RRULE:");
		p_location = strstr(tmp_buf,"LOCATION:");		

		if(p_rrule != NULL)
		{
			p_dtend += strlen("DTEND:"); 
			memset(vevent_t.dtend,0,48);
			memcpy(vevent_t.dtend,p_dtend,p_rrule - p_dtend - 1);		      
			p_rrule += strlen("RRULE:");
			memset(vevent_t.rrule,0,48);
			memcpy(vevent_t.rrule,p_rrule,p_location - p_rrule - 1);	
		}else{
			
			p_dtend += strlen("DTEND:"); 
			memset(vevent_t.dtend,0,48);
			memcpy(vevent_t.dtend,p_dtend,p_location - p_dtend - 1);		      
			memset(vevent_t.rrule,0,48);
		}

		p_summary = strstr(tmp_buf,"SUMMARY:");
		p_location += strlen("LOCATION:");
		memset(vevent_t.location,0,48);
		memcpy(vevent_t.location,p_location,p_summary - p_location - 1);	

		p_end = strstr(tmp_buf,"END:VEVENT");
		p_summary += strlen("SUMMARY:");
		memset(vevent_t.summary,0,48);
		memcpy(vevent_t.summary,p_summary,p_end - p_summary -1);
		tmp_buf += p_end - tmp_buf +strlen("END:VEVENT");;

		if(strncmp(vevent_t.rrule,"FREQ=WEEKLY",strlen("FREQ=WEEKLY")) == 0)
		{
			for ( ; ; )
			{
				if (strncmp(vevent_t.dtstart,time_after, 8) <= 0 && strncmp(vevent_t.dtstart,vevent_t.rrule + 18,8) <= 0 )
				{
					if(strncmp(vevent_t.dtstart,time_before, 8) >= 0)
						event_print(&vevent_t);

					strncpy(time_A, vevent_t.dtstart, MAX_LINE_LEN);
					dt_format(output, time_A, MAX_LINE_LEN);		

	    				dt_increment(time_B, time_A, 7);
    					dt_format(output, time_B, MAX_LINE_LEN);
					memcpy(vevent_t.dtstart,time_B,strlen(time_B));
				}else{	
						break;
				}

			}
			}else{
			if (strncmp(vevent_t.dtstart,time_after, 8) <= 0 && strncmp(vevent_t.dtstart,time_before, 8) >= 0)
				event_print(&vevent_t);
		}

		

	}

}


int main(int argc, char *argv[])
{
    int from_y = 0, from_m = 0, from_d = 0;
    int to_y = 0, to_m = 0, to_d = 0;
    char *filename = NULL;
    int i; 
    int len;
file_buf = (char *)emalloc(MAX_FILE_SIZE);
title = (char *)emalloc(EVENT_NUM * MAX_CHAR_NUM);
content1 = (char *)emalloc(EVENT_NUM * MAX_CONTENT_CHAR_NUM);
date = (char *)emalloc(EVENT_NUM * MAX_CHAR_NUM);
total = (char *)emalloc(EVENT_NUM);


    for (i = 0; i < argc; i++) {
        if (strncmp(argv[i], "--start=", 7) == 0) {
            sscanf(argv[i], "--start=%d/%d/%d", &from_y, &from_m, &from_d);
        } else if (strncmp(argv[i], "--end=", 5) == 0) {
            sscanf(argv[i], "--end=%d/%d/%d", &to_y, &to_m, &to_d);
        } else if (strncmp(argv[i], "--file=", 7) == 0) {
            filename = argv[i]+7;
        }
    }

    if (from_y == 0 || to_y == 0 || filename == NULL) {
        fprintf(stderr, 
            "usage: %s --start=yyyy/mm/dd --end=yyyy/mm/dd --file=icsfile\n",
            argv[0]);
        exit(1);
    }


		memset(file_buf,0,3*1024);

	FILE *fp = fopen(filename, "r" );

	if(fp == NULL)
	{
		printf("Fopen %s error \n",filename);
		return -1;
	}

	fseek(fp, 0, SEEK_END);   
 
	len = ftell(fp);
	
	fseek(fp, 0, SEEK_SET);

	fread(file_buf, len, 1, fp);

	
	print_events(from_y,from_m,from_d,to_y,to_m,to_d);


    	apply(head, print_event, NULL);

    	fclose(fp);
/* 
 * Showing some simple usage of the linked-list routines.
 */

#ifdef DEBUG
    _demo();
#endif

free(file_buf);
free(title);
free(content1);
free(date);
free(total);

    exit(0);
}

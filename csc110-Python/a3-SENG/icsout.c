#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>

#define MAX_LINE_LEN 132
#define MAX_EVENTS 500
#define MAX_CHAR 1000
#define EVENT_LINE 80
#define EVENT_NUM 256
#define MAX_CHAR_NUM  256
#define MAX_CONTENT_CHAR_NUM 512
#define MAX_FILE_SIZE 8192
#define MAX_STRUCT_SIZE 48

char title[EVENT_NUM][MAX_CHAR_NUM] = {0};
char content1[EVENT_NUM][MAX_CONTENT_CHAR_NUM] ={0};
char date[EVENT_NUM][MAX_CHAR_NUM] ={0};
static int total_num = 0;
int total[EVENT_NUM] = {0};
char file_buf[MAX_FILE_SIZE] = {0};

struct vevent{
	char begin[MAX_STRUCT_SIZE];
	char dtstart[MAX_STRUCT_SIZE];
	char dtend[MAX_STRUCT_SIZE];
	char rrule[MAX_STRUCT_SIZE];
	char location[MAX_STRUCT_SIZE];
	char summary[MAX_STRUCT_SIZE];
	char end[MAX_STRUCT_SIZE];
};

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

	time_stamps(tmp_vevent->dtstart,out_buf,0);
	time_stamps(tmp_vevent->dtend,out_buf,1);

	sprintf(out_buf + strlen(out_buf),"%s ",tmp_vevent->summary);
	sprintf(out_buf + strlen(out_buf),"{{%s}}",tmp_vevent->location);	
	strncpy(time_A, tmp_vevent->dtstart, MAX_LINE_LEN);
	dt_format(output, time_A, MAX_LINE_LEN);	
	
	memcpy(date[total_num],tmp_vevent->dtstart,8);

#if 1
	for(i =0; i < total_num ;i ++)
	{
		if(strncmp(date[i],tmp_vevent->dtstart,8) == 0)
		{
			tmp_total_num = i;
			flag_same  = 1;
				break;
		}
	}
#else


#endif
	

#if 0
	if(flag_same == 1)
	{
		sprintf(content1[tmp_total_num] +total[tmp_total_num] * EVENT_LINE,"%s\n",out_buf);
		total[tmp_total_num]++;
		
	}else{
		sprintf(title[total_num] + strlen(title[total_num]),"%s\n-----------------------\n",output);
		sprintf(content1[total_num] + total[total_num] * EVENT_LINE,"%s\n",out_buf);
		total[total_num] ++;
		total_num ++;
	}
#endif
}

void sort_event2(void)
{
	int i,j;
	char * p;
	char temp[512];
	p = temp;
	int temp_num = 0;
	int num =0;

	for(num = 0; num < EVENT_NUM; num ++)
	{
		if(total[num] > 1)
		{
		for ( i = 0; i < total[num] -1; i++)
			for (j = 0;j < total[num] - i -1; j++)
			{
				if (strncmp(content1[num] + j * EVENT_LINE  + 6,content1[num] + (j+1) * EVENT_LINE + 6, 2) > 0 \
				|| (strncmp(content1[num] + j * EVENT_LINE  + 6,content1[num] + (j+1) * EVENT_LINE + 6, 1) == 0 &&\
					strncmp(content1[num] + j * EVENT_LINE,content1[num] + (j+1) * EVENT_LINE, 2) >  0))
				{
					memset(p,0,512);
					memcpy(p,content1[num] + j * EVENT_LINE,EVENT_LINE);
					memset(content1[num] + j* EVENT_LINE,0,EVENT_LINE);
					memcpy(content1[num] + j * EVENT_LINE,content1[num] + (j +1) * EVENT_LINE,EVENT_LINE);
					memset(content1[num] + (j + 1) * EVENT_LINE,0,EVENT_LINE);
					memcpy(content1[num] + (j + 1) * EVENT_LINE,p,EVENT_LINE);
				}			
			}
		}
	}

}



void sort_event(void)
{
	int i,j;
	char * p;
	char temp[512];
	p = temp;
	int temp_num = 0;
	int num = 0;

	
	if(total_num <= 1)
		return ;
	
	for ( i = 0; i < total_num -1; i++)
		for (j = 0;j < total_num - i -1; j++)
			if (strncmp(date[j],date[j+1],8) > 0)
			{
				memcpy(p,date[j],strlen(date[j]));
				memcpy(date[j],date[j+1],strlen(date[j +1]));
				memcpy(date[j+1],p,strlen(p));


				memset(p,0,256);
				memcpy(p,title[j],strlen(title[j]));
				memset(title[j],0,256);
				memcpy(title[j],title[j+1],strlen(title[j +1]));
				memset(title[j+1],0,256);
				memcpy(title[j+1],p,strlen(p));

				memset(p,0,512);
				memcpy(p,content1[j],MAX_CONTENT_CHAR_NUM);
				memset(content1[j],0,MAX_CONTENT_CHAR_NUM);
				memcpy(content1[j],content1[j+1],MAX_CONTENT_CHAR_NUM);
				memset(content1[j+1],0,MAX_CONTENT_CHAR_NUM);
				memcpy(content1[j+1],p,MAX_CONTENT_CHAR_NUM);

				temp_num = total[j];
				total[j] = total[j+1];
				total[j+1] = temp_num;

			}

}

void print_all_event(void)
{
	//printf("############################# %d \n",total_num);
	sort_event();
	sort_event2();

	int i = 0;
	int j = 0;
	for( i = 0 ; i < total_num; i++)
	{
		printf("%s",title[i]);

		if(total[i] > 1)
		{
			for(j = 0; j < total[i];j++)
				printf("%s",content1[i] + j * EVENT_LINE);
		}else
			printf("%s",content1[i]);

		if( i != total_num -1)
			printf("\n");
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
    int i = 0; 
    int len = 0;
    int j = 0;

    for (i = 0; i < argc; i++) {
        if (strncmp(argv[i], "--start=", 8) == 0) {
            sscanf(argv[i], "--start=%d/%d/%d", &from_y, &from_m, &from_d);
        } else if (strncmp(argv[i], "--end=", 6) == 0) {
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

	memset(file_buf,0,8192);
	memset(total,0,256);

	for(i =0; i < 256;i ++)
		for(j = 0; j < 512;j ++)
		{
			content1[i][j] = '\0';
		}
			

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
	print_all_event();

    	fclose(fp);

	return 0;

    /* Starting calling your own code from this point. */

	exit(0);
}


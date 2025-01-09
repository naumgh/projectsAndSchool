#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define MAX_LINE_LEN 132
#define MAX_EVENTS 500


void print_events(int from_yy, int from_mm, int from_dd, 
    int to_yy, int to_mm, int to_dd)
{

}
struct MyTest{
    char freq[132];
    char wkst[132];
    char until[132];
    char byday[132];
    char location[132];
    char summary[132];
    int startMinute;
    int startHour;
    int startYear;
    int startMonth;
    int startDay;
    int isAmFlag;
    

    int endMinute;
    int endHour;
    int endYear;
    int endMonth;
    int endDay;
    int isAmFlag2;

    int untilMinute;
    int untilHour;
    int untilYear;
    int untilMonth;
    int untilDay;
    int isFlagUntil;
    
    
}event1; 

/*
//struct MyTest event1;

void printLocationTest(struct MyTest event1){
    printf("%s", event1.location[0]);
}
*/

void printSummaryLocation(){
    printf("%s%s\n", "Location: ", event1.location);
    printf("%s%s\n", "Summary: ", event1.summary);
}
void printDateTest(){
    printf("%s%d\n","Start Hour:",event1.startHour);
    printf("%s%d\n","Start Minute:",event1.startMinute);
    printf("%s%d\n", "Start Year:",event1.startYear);
    printf("%s%d\n", "Start Month:",event1.startMonth);
    printf("%s%d\n", "Start day:",event1.startDay);
    printf("%s%d\n", "AmFlag:", event1.isAmFlag);
    printf("\n");
    printf("%s%d\n","Start Hour:",event1.endHour);
    printf("%s%d\n","Start Minute:",event1.endMinute);
    printf("%s%d\n", "Start Year:",event1.endYear);
    printf("%s%d\n", "Start Month:",event1.endMonth);
    printf("%s%d\n", "Start day:",event1.endDay);
    printf("%s%d\n", "AmFlag:", event1.isAmFlag2);

    
     
}
void checkTimeEvents(){


}
void calculateUntil(char*token){
   char*year = strtok(token, "T");
   char*time = strtok(NULL,";");
   int yearInt = atoi(year);
   int timeInt = atoi(time);
   int day;
   int month;
   int y;
   int minute;
   int hour;
   int isAmFlag = 1;
   //printf("%d", timeInt);

   if(timeInt >=120000){
      timeInt = timeInt-120000;
      isAmFlag = 0;
   }else{
        timeInt = timeInt;
   }
   //timeInt = timeInt/1000;
   minute = timeInt/10;
   minute = minute % 100;
   timeInt = timeInt - minute;
   hour = timeInt;
   hour = hour/10000;
   day = yearInt % 100;
   yearInt = yearInt-day;
   yearInt = yearInt/100;
   month = yearInt % 100;
   yearInt = yearInt-month;
   yearInt = yearInt/100;
   y = yearInt;

       event1.untilHour=hour;
       event1.untilMinute=minute;
       event1.untilYear=y;
       event1.untilMonth=month;
       event1.untilDay=day;
       event1.isFlagUntil = isAmFlag;


}
void takeSummary(char*token){
     strcpy(event1.summary, token);  
}
void endDataDump(){
    return;
}
void takeLocation(char*token){
    strcpy(event1.location, token);

}
void doSomething(char**ptr){
    for(int i = 0; i < 5; i++){
        printf("%s",ptr[i]);
    }
}
void printRRULE(){
    printf("%s\n", event1.freq);
    printf("%s\n", event1.wkst);
    printf("%s\n", event1.until);
    printf("%s\n", event1.byday);
}


void parseRule(char *token){
    char * split = strtok(token, ";");
    char * token1;
    char * token2;
    char *parse[132];
    char **ptr = parse;
    int r = 0;

    while(split != NULL){
        ptr[r] = split;
        r++;
        split = strtok(NULL, ";");
        
    }
    for(int i = 0; i < 4; i++){
        printf("%s\n", ptr[i]);
        token1 = strtok(ptr[i], "=");
        token2 = strtok(NULL, "\n");
        if(strcmp(token1, "FREQ") == 0){
            strcpy(event1.freq, token2);     
        }else if(strcmp(token1, "WKST")==0){
            strcpy(event1.wkst, token2);
        }else if(strcmp(token1, "UNTIL")==0){
            strcpy(event1.until, token2);
            calculateUntil(token2);
        }else{
            if(strcmp(token1, "BYDAY")==0){
                strcpy(event1.byday, token2);
            }

        }
    }


}

void calculate_date_start(char*token,int s){//time is done, thank fuck
   char*year = strtok(token, "T");
   char*time = strtok(NULL,";");
   int yearInt = atoi(year);
   int timeInt = atoi(time);
   int day;
   int month;
   int y;
   int minute;
   int hour;
   int isAmFlag = 1;
   //printf("%d", timeInt);

   if(timeInt >=120000){
      timeInt = timeInt-120000;
      isAmFlag = 0;
   }else{
        timeInt = timeInt;
   }
   //timeInt = timeInt/1000;
   minute = timeInt/10;
   minute = minute % 100;
   timeInt = timeInt - minute;
   hour = timeInt;
   hour = hour/10000;
   day = yearInt % 100;
   yearInt = yearInt-day;
   yearInt = yearInt/100;
   month = yearInt % 100;
   yearInt = yearInt-month;
   yearInt = yearInt/100;
   y = yearInt;
   //event1
                        //we have hour, minute, year, month, day all in
//   printf("%d\n", hour);
/*
   printf("%d\n", minute);
   printf("%d\n", y);
   printf("%d\n", month);
*/
 //  printf("%d\n", day);
   
   if(s == 0){
       event1.startHour=hour;
       event1.startMinute=minute;
       event1.startYear=y;
       event1.startMonth=month;
       event1.startDay=day;
       event1.isAmFlag= isAmFlag;
   }else{
        event1.endHour = hour;
        event1.endMinute = minute;
        event1.endYear = y;
        event1.endMonth = month;
        event1.endDay = day;
        event1.isAmFlag2 = isAmFlag;
   }
}

void analyze_buffer(char buffer[]){
    /*
    we have a few options to consider, and it's gonna be a pain in the ass to parse but if we see BEGIN: END: DTSTART: DTEND: RRULE: LOCATION: SUMMARY: we split until and put in array until we don't see it again 
    */
    
    int strcmpZero;
    char * token1 = strtok(buffer, ":"); 
    char * token2 = strtok(NULL, "\n");
    //printf("%s\n","here are the buffers");
    //printf("%s\n", token1);
    //printf("%s\n", token2);
    
    if(strcmp(token1, "BEGIN") == 0){       
        //startDataDump();
    /*
    now i have to differentiate between the different events and parse those accordintly 
*/                                                                    
    }else if(strcmp(token1, "END") == 0){
       if(token2 == "VEVENT"){
           checkTimeEvents();
       }else if(token2 == "VCALENDAR"){
            exit(1);
       }
    }else if(strcmp(token1, "DTSTART")==0){
        calculate_date_start(token2, 0);
        //printDateTest();
    }else if(strcmp(token1, "DTEND")==0){
        calculate_date_start(token2,1);
        //printDateTest(); 
    //}else if(strcmp(strcmpZero, "RRULE")==0){

    }else if(strcmp(token1, "LOCATION")==0){
        takeLocation(token2);
        //printLocationTest(event1);
    }else if(strcmp(token1, "SUMMARY")==0){
       takeSummary(token2);
       //printSummaryLocation();

    }else if(strcmp(token1, "RRULE") == 0){
        parseRule(token2);
        printRRULE();
    }else{
        return;
    }

}

int main(int argc, char *argv[])
{
    int from_y = 0, from_m = 0, from_d = 0;
    int to_y = 0, to_m = 0, to_d = 0;
    char *filename = NULL;
    int i; 

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

    FILE *fp = fopen(filename, "r");

    if(fp == NULL){
        printf("the file does not exist");
        exit(1);
    }
  

    char buffer[256];
    char n = '\n';
    //event1.test = 0;
    while(fgets(buffer, sizeof(buffer), fp) != NULL){
    //    printf("%s\n", buffer);
        analyze_buffer(buffer);
        print_events(from_y, from_m, from_d, to_y, to_m);
    }

    exit(0);
}

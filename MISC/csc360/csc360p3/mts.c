#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <time.h>

pthread_mutex_t mutex1;
void * loadingTrain(void* arg){
	printf("train created\n");
}

void * dispatcher(void * arg){
	printf("dispatcher created\n");
}



typedef struct node{
	int train_number;
	char priority;
	int loading_time;
	int crossing_time;
	char * status;
	struct node * next;


} Node;

Node * newNode(int tnumber, char prio, int load_t, int cross_t, char*stat){
	Node * t = (Node*)malloc(sizeof(Node));
	t->train_number = tnumber;
	t->priority = prio;
	t->loading_time = load_t;
	t->crossing_time = cross_t;
	t->status = stat;

	return t;
	

}




int main(int argc, char * argv[]){
	//step1, open file
	FILE * fp;
	char delim[] = " ";
	fp = fopen(argv[1],"r");
	int line = 0;
	int count = 0;
	char input[512];
	while(fgets(input, 512, fp)){
		line++;
		printf("LINE:%d -> %s", line,input);
		char * ptr = strtok(input,delim);
		
		if(line > count){
		   count = line;
		}


		while(ptr != NULL){
			printf("%s\n", ptr);
			ptr = strtok(NULL, delim);
		}

	}
	printf("%d\n", count); 
	pthread_t train[count];
	pthread_mutex_init(&mutex1, NULL);

	for(int i = 0; i < count; i++){
		if (pthread_create(&train[i], NULL, &loadingTrain, NULL) != 0){
			perror("couldn't create thread");
		}	    
	}

	for(int i = 0; i < count; i++){
		if(pthread_join(train[i], NULL) != 0){
			perror("could not join thread");
		}
	}

	pthread_mutex_destroy(&mutex1);
	fclose(fp);
	return 0;

}


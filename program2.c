#include <stdio.h>
#include <string.h>

void dummy(const char *data){

	char buf[128];
	unsigned short len = strlen(data);
	if(len>128){
		puts("Bad Dog!");
	}	
	else {
		sprintf(buf, data);
		printf("Copied your string\n");
	}
	
}

int main(int argc, char **argv){
	
	dummy(argv[1]);
	return 0;
}


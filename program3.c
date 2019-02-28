
#include <stdio.h>
#include <string.h>

void dummy(const char *data){

	char buf[400];
	sprintf(buf, data);
	printf("Copied your string\n");	
}

int main(int argc, char **argv){
	
	dummy(argv[1]);
	return 0;
}

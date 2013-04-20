#include <stdio.h>

int main(int argc, char **argv)
{
	if (argc<2) {
		puts("Usage: ./pass <password>");
		return 0;
	}
	int i;
	String a = "hi";
	String b = "hi";	
	if (argv[1]!="hi") {
		puts(argv[1]);
		puts(a==b);
		return 1;
	}
	
	puts("Right");
	return 1;
}

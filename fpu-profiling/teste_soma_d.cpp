#include<cstdio>
#include<cmath>
#include <cstdlib>     /* srand, rand */
#include <time.h>       /* time */

double random_float(double min, double max)    
{    
    return ((double) rand()) / (double) RAND_MAX;    
}

int main(int argc, char** argv){
	srand (time(NULL));
	int N = atoi(argv[1]);

	double a, b;
	for(int i = 0; i < N; i++){
		a = random_float(0,1);
		b = random_float(0,1);
		printf("%f\n", a+b);
	}

	return 0;
}

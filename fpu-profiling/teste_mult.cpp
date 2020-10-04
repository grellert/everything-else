#include<cstdio>
#include<cmath>
#include <cstdlib>     /* srand, rand */
#include <time.h>       /* time */

float random_float(float min, float max)    
{    
    return ((float) rand()) / (float) RAND_MAX;    
}

int main(int argc, char** argv){
	srand (time(NULL));
	int N = atoi(argv[1]);
	
	float a, b;
	for(int i = 0; i < N; i++){
		a = random_float(0,1);
		b = random_float(0,1);
		printf("%f\n", a*b);
	}

	return 0;
}

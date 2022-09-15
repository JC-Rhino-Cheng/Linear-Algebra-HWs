#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "mmm.h"

float A[SIZE][SIZE], B[SIZE][SIZE], C[SIZE][SIZE], D[SIZE][SIZE];

int main() {
	for (auto i = 0; i < SIZE; i++) {
		for (auto j = 0; j < SIZE; j++) {
			A[i][j] = rand() % 10;
			B[i][j] = rand() % 10;
		}
	}

	clock_t t1 = clock();
	matrixmul(A, B, C);
	clock_t t2 = clock();
	matrixmul_block(A, B, D, 4);
	clock_t t3 = clock();

	double d1 = ((double)(t2 - t1)) / CLOCKS_PER_SEC;
	double d2 = ((double)(t3 - t2)) / CLOCKS_PER_SEC;

	printf("%f, %f, diff= %f\n", d1, d2, verify(C, D));

	return 0;
}

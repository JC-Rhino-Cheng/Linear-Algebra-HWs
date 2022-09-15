#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "mmm.h"

float A[SIZE][SIZE], B[SIZE][SIZE], C[SIZE][SIZE], D[SIZE][SIZE];

int main() {
	for (auto i = 0; i < SIZE; i++) {
		for (auto j = 0; j < SIZE; j++) {
			///*
			A[i][j] = rand() % 10;
			B[i][j] = rand() % 10;
			//*/
			/*
			A[i][j] = i + j;
			B[i][j] = (SIZE - 1) * 2 - (i + j);
			*/
			
        }
    }
	/*
	const auto t1 = clock();
    matrixmul(A, B, C);
	const auto t2 = clock();
    //matrixmul_block(A, B, D, 4);
	matrixmul_block2(A, B, D, 32,64);
	const auto t3 = clock();

	double d1 = ((double)(t2 - t1)) / CLOCKS_PER_SEC;
	double d2 = ((double)(t3 - t2)) / CLOCKS_PER_SEC;

    printf("%f, %f, diff= %f\n", d1, d2, verify(C, D));
	*/
	
	for (auto p = 1 << 2; p <= 1 << 8; p = p << 1) for (auto q = 1 << 2; q <= 1 << 8; q = q << 1) {
		double total_time = 0;
		for (auto i = 0; i < 10; i++) {
			const auto t1 = clock();
			matrixmul_block2(A, B, D, p, q);
			const auto t2 = clock();

			double duration = ((double)(t2 - t1)) / CLOCKS_PER_SEC;
			total_time += duration;
		}
		printf("p = %d, q = %d, time = %f\n", p, q, total_time / 10);
		
	}
	
	//system("pause");
}
#include "mmm.h"

// compute C = A*B
void matrixmul(float A[][SIZE], float B[][SIZE], float C[][SIZE]) {
	// i: row index for C
	// j: col index for C
	// k: iteration index


	for (auto i = 0; i < SIZE; i++) {
		for (auto j = 0; j < SIZE; j++) {
			C[i][j] = 0;
			for (auto k = 0; k < SIZE; k++) C[i][j] += A[i][k] * B[k][j];
		}
	}
}

// compute C = A*B using blocking
void matrixmul_block(float A[][SIZE], float B[][SIZE], float C[][SIZE], int bSize) {
	for (auto bi = 0; bi < SIZE; bi += bSize) {// bi: block row index for C
		for (auto bj = 0; bj < SIZE; bj += bSize) {// bj: block col index for C
			// clean C's value
			for (auto i = bi; i < bi + bSize; i++) {// i: row index for block
				for (auto j = bj; j < bj + bSize; j++) {// j: col index for block
					C[i][j] = 0.0;
				}
			}
			// compute the block submatrix C[bi][bj]
			for (auto bk = 0; bk < SIZE; bk += bSize) {// bk: block index
				for (auto i = bi; i < bi + bSize; i++) {// i: row index for block
					for (auto j = bj; j < bj + bSize; j++) {// j: col index for block
						for (auto k = bk; k < bk + bSize; k++) {// k: iteration index
							C[i][j] += A[i][k] * B[k][j];
						}
					}
				}
			}
		}
	}
}


// compute C = A*B using blocking
void matrixmul_block2(float A[][SIZE], float B[][SIZE], float C[][SIZE], int p, int q) {
	// your implementation here
}


// verify the correctness of the result
double verify(float X[][SIZE], float Y[][SIZE]) {
	double accum = 0.0;

	for (auto i = 0; i < SIZE; i++) {
		for (auto j = 0; j < SIZE; j++) {
			float diff = X[i][j] - Y[i][j];
			accum += diff < 0 ? -diff : diff;
		}
	}

	return accum;
}

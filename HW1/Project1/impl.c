#include "mmm.h"

// compute C = A*B
void matrixmul(float A[][SIZE], float B[][SIZE], float C[][SIZE]) {
	for (auto i = 0; i < SIZE; i++) {// i: row index for C
		for (auto j = 0; j < SIZE; j++) {// j: col index for C
			C[i][j] = 0;
			for (auto k = 0; k < SIZE; k++) C[i][j] += A[i][k] * B[k][j];// k: iteration index
		}
	}

	return;
}

// compute C = A*B using blocking
void matrixmul_block(float A[][SIZE], float B[][SIZE], float C[][SIZE], int bSize) {

	for (auto bi = 0; bi < SIZE; bi += bSize) {// bi: block row index for C
		for (auto bj = 0; bj < SIZE; bj += bSize) {// bj: block col index for C

			// clean C's value //不太重要，只是把值全搞回0。
			for (auto i = bi; i < bi + bSize; i++) {// i: rol index for block
				for (auto j = bj; j < bj + bSize; j++) {// j: col index for block
					C[i][j] = 0.0;
				}
			}

			// compute the block submatrix C[bi][bj]
			for (auto bk = 0; bk < SIZE; bk += bSize) {// bk: block index
				for (auto i = bi; i < bi + bSize; i++) {// i: rol index for block
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
	//n = Np=Mq

	/*//先分別透過p、q，來求出N、M
	auto N = SIZE / p;
	auto M = SIZE / q;*/
	//ex: 8 = (N=2)4 = (M=4)2。但是兩個submatrix(NxM=2x4, 和 MxN = 4x2)算出來會是NxN = 2x2

	for (auto bi = 0; bi < SIZE; bi += /*N*/p) {// bi: block row index for C
		for (auto bj = 0; bj < SIZE; bj += /*N*/p) {// bj: block col index for C

			// clean C's value //不太重要，只是把值全搞回0。
			for (auto i = bi; i < bi + /*N*/p; i++) {// i: rol index for block
				for (auto j = bj; j < bj + /*N*/p; j++) {// j: col index for block
					C[i][j] = 0.0;
				}
			}

			// compute the block submatrix C[bi][bj]
			for (auto bk = 0; bk < SIZE; bk += /*M*/q) {// bk: block index
				for (auto i = bi; i < bi + /*N*/p; i++) {// i: rol index for block
					for (auto j = bj; j < bj + /*N*/p; j++) {// j: col index for block
						for (auto k = bk; k < bk + /*M*/q; k++) {// k: iteration index
							C[i][j] += A[i][k] * B[k][j];
						}
					}
				}
			}
		}
	}

}


// verify the correctness of the result
double verify(float X[][SIZE], float Y[][SIZE]) {
	float diff = 0.0;
	double accum = 0.0;

	for (auto i = 0; i < SIZE; i++) {
		for (auto j = 0; j < SIZE; j++) {
			diff = X[i][j] - Y[i][j];
			accum += diff < 0 ? -diff : diff;
		}
	}

	return accum;
}

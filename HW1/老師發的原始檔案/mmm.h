#define SIZE 1024
#define BLKSIZE 8

// compute C = A*B
void matrixmul(float A[][SIZE], float B[][SIZE], float C[][SIZE]);

// compute C = A*B using blocking
void matrixmul_block(float A[][SIZE], float B[][SIZE], float C[][SIZE], int bSize);

// compute C = A*B using blocking
void matrixmul_block2(float A[][SIZE], float B[][SIZE], float C[][SIZE], int p, int q);

// verify the correctness of the result
double verify(float X[][SIZE], float Y[][SIZE]);

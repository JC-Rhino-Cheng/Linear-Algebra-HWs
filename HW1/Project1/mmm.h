#define SIZE 1024

// compute C = A*B //最普通最暴力的矩陣乘法演算法。不太重要。
void matrixmul(float A[][SIZE], float B[][SIZE], float C[][SIZE]);

// compute C = A*B using blocking
void matrixmul_block(float A[][SIZE], float B[][SIZE], float C[][SIZE], int bSize);

// compute C = A*B using blocking
void matrixmul_block2(float A[][SIZE], float B[][SIZE], float C[][SIZE], int p, int q);

// verify the correctness of the result //只是在確認兩種算法的差異到底有多大，照理講應該是0。不太重要。
double verify(float X[][SIZE], float Y[][SIZE]);

#define SIZE 1024

// compute C = A*B //�̴��q�̼ɤO���x�}���k�t��k�C���ӭ��n�C
void matrixmul(float A[][SIZE], float B[][SIZE], float C[][SIZE]);

// compute C = A*B using blocking
void matrixmul_block(float A[][SIZE], float B[][SIZE], float C[][SIZE], int bSize);

// compute C = A*B using blocking
void matrixmul_block2(float A[][SIZE], float B[][SIZE], float C[][SIZE], int p, int q);

// verify the correctness of the result //�u�O�b�T�{��غ�k���t���쩳���h�j�A�Ӳz�����ӬO0�C���ӭ��n�C
double verify(float X[][SIZE], float Y[][SIZE]);

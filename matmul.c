#define N 512

float A[N][N], B[N][N], C[N][N];

void matrix_multiply() {
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      float acc = C[i][j];
      for (int k = 0; k < N; ++k) {
        acc += A[i][k] * B[k][j];
      }
      C[i][j] = acc;
    }
  }
}

int main() {
  matrix_multiply();
  return 0;
}
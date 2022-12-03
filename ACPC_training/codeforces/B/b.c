#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int fib[16] = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987};
    int num;
    scanf("%d", &num);
    char* hi = (char*)calloc(num + 1, sizeof(char));
    memset(hi, 111, num);
    for (int i = 0; i<16;i++){
        if (fib[i] > num) break;
        hi[fib[i]-1] = 'O';
    }
    hi[num] = '\0';
    printf("%s\n", hi);
    free(hi);
    return 0;
}
#include <stdio.h>

int main() {
    int n, i = 1;
    long long int bal;
    // scanf("%d %d",&n, &bal);
    n = 11;
    bal = 2147483648;
    // bal = bal % (int)(((float)n/2)*(2 + n - 1));
    while (1){
        if (bal>=i){
            bal-=i;
        } else{
            printf("%d\n", bal);
            break;
        }
        i+=1;
        if (i>n) {
            i=1;
        }

    }

    return 0;
}
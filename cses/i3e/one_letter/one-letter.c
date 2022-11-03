#include <stdio.h>
#include <string.h>
#define SIZE 100000


int main() {
    int n;
    scanf("%d\n", &n);
    int s, count=0;
    char cur;
    char final[n];
    while(n--){
        // printf("%d\n",SIZE);
        char hi[SIZE];
        scanf("%s", hi);
        s = 200;
        for (int i =0;i<strlen(hi);i++){
            if (hi[i] < s) {
                s = hi[i];
                cur = hi[i];
            }
        }
        final[count] = cur;
        count++;
    }
    printf("%s\n", final);

}
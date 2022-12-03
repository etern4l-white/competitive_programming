#include <stdio.h>


int gen(n){
    
}
int main() {
    long long int start, finish, summ = 0, lucky_index = 0;
    scanf("%lld %lld", &start, &finish);



    for (long long i = start; i<=finish;i++){
        while (1) {
            if (org[lucky_index] >= i) {
                summ+=org[lucky_index];
                break;
            } else{
                lucky_index+=1;
            }
        }
    }
    printf("%lld\n", summ);
    return 0;
}
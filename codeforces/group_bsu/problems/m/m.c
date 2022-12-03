#include <stdio.h>

int get_sum_digits(int num){
    int sum = 0;
    while(num>0){
        sum+=num%10;
        num/=10;
    }
    return sum;
}

int main() {
    int l, d, x;
    scanf("%d\n%d\n%d", &l, &d, &x);
    // printf("%d\n%d\n%d", l, d, x);
    int n = l, m = d, temp;
    while(n<=d){
        temp = get_sum_digits(n);
        if (temp == x) {
            break;
        }
        n++;
    }


    while(m>=l){
        temp = get_sum_digits(m);
        if (temp == x) {
            break;
        }
        m--;
    }

    printf("%d\n%d\n", n, m);
    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// #include <time.h>
// #include <stdint.h>


// int64_t timespecDiff(struct timespec *timeA_p, struct timespec *timeB_p)
// {
//   return ((timeA_p->tv_sec * 1000000000) + timeA_p->tv_nsec) -
//            ((timeB_p->tv_sec * 1000000000) + timeB_p->tv_nsec);
// }



int see_if_happy(int number) {
    int sum = 0, cur, counter = 0, old = number;
    if (number == 1){
        return 1;
    }
    while(counter<10000){
        // printf("%d --> ", number);
        sum = 0;
        // printf("%d\n", counter);
        
        
        while(number>0){
            cur = number%10;
            sum+=cur*cur;
            number/=10;
        }
        
        number = sum;
        // printf("|%d|%d|", sum, number);
        if (number == old){
            return 0;
        }
        if (number == 1){
            return 1;
        }
        counter++;
    }
    // printf("\n\n");
    return 0;
}


int main() {
    // struct timespec start, end;
    // clock_gettime(CLOCK_MONOTONIC, &start);




    int a, b, sum=0;
    scanf("%d %d", &a, &b);
    for(a;a<=b;a++){
        // printf("%d\n", a);
        if (see_if_happy(a)) {
            sum+=1;
            // printf("------------%d\n", a);
        }
    }
    printf("%d\n", sum);


    // GKWsDJMfLKEiot
    // clock_gettime(CLOCK_MONOTONIC, &end);
    // uint64_t timeElapsed = timespecDiff(&end, &start);
    // printf("%u\n", timeElapsed/1000);
    return 0;
}
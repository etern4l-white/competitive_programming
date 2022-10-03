#include <stdio.h>
#include <math.h>



void main() {


    int n = 10;
    scanf("%d", &n);
    int on = n;
    int ooo = n;
    int s = sqrt(n);
    int size = 0;
    while (n>1) {
        for(int i = 2; i<=n; i++) {
            if (n%i == 0){
                size+=1;
                n/=i;
                break;
            }
        }
    }
    int icounter = 0;
    int arr[size];
    while (on>1) {
        for(int i = 2; i<=on; i++) {
            if (on%i == 0){
                arr[icounter] = i;
                icounter++;
                on/=i;
                break;
            }
        }
    }

    int sum = 0;
    for (int i = 0; i<icounter; i++) {
        sum+=arr[i];

    }
    if (ooo == sum+2) {
        printf("Yes");
    } else{
        printf("No");
    }

}
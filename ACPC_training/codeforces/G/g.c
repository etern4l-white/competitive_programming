#include <stdio.h>



int main() {
    int n, s = 0;
    scanf("%d", &n);

    for(int i = 1; i<n+1;i++) {
        int arr[10] = {0};
        int cur_sum = 0, intt = i;
        while(intt > 0) {
            arr[(intt%10)] = 1;
            intt/=10;
            // printf("%d\n", intt);
        }
        for (int j = 0; j<10;j++){
            // printf("%d, ", arr[j]);
            cur_sum+= arr[j]>0;
        }
        // printf("\n");
        if (cur_sum <3) {
            s++;
        }

    }
    printf("%d\n", s);



    return 0;
}
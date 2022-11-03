#include <stdio.h>



int  main() {
    int n, q, p, d, res;
    scanf("%d %d", &n, &q);
    int di[n];
    for (int i = 0;i<n; i++){
        scanf("%d ", &di[i]);
    }
    // char str[q*]
    for(int i = 0; i<q;i++) {
        scanf("%d %d", &p, &d);
        res = p;
        if (res == di[res-1]){
            printf("%d\n", res);
            continue;
        }
        while(d>0) {
            res = di[res-1];
            d-=1;
        }
        printf("%d\n", res);
    }
    return 0;
}

// OMG THIS STILL DOESN'T WORK -- TIME LIMIT EXCEEDED.

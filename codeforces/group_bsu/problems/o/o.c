#include <stdio.h>
#include <math.h>

int main() {
    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; i++) {
        long long int n;
        scanf("%lld", &n);
        long long int sum = (n / 2) * (2 + n - 1);
        int l = (int)log2(n);

        for (int j = 0; j <= l; j++) {
            sum -= 2 * (long long int)powl(2, j);
        }
        printf("%lld\n", sum);
        long long int sum2 = 0;
        for (int j = 1; j <= n; j++) {
            if (log2(j) == (int)log2(j)) {
                sum2 -= j;
            } else {
                sum2 += j;
            }
        }

        if (sum != sum2) {
            printf("%d\n", n);
            printf("%lld %lld\n", sum, sum2);
        }
    }

    return 0;
}

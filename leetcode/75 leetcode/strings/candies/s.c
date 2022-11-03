#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize){
    bool* l = (bool*)malloc(candiesSize*sizeof(bool));
    printf("%d\n", sizeof(l));
    int i =0;
    int m = INT_MIN;
    for(int j = 0;j<candiesSize;j++){
        m = candies[i]>m?candies[i]:m;
    }
    while(i<candiesSize){
        l[i] = candies[i]+extraCandies>m?true:false;
        i++;
    }
    return l;
}

void main() {
    int hi[5] = {2,3,5,1,3};
    kidsWithCandies(hi, 5, 3, 5);
}
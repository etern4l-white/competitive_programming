int gcd(int a, int b){
    return b==0?a:gcd(b, a%b);
}

int findGCD(int* nums, int numsSize) {
    int s = nums[0], b = nums[0];
    for(int i =0;i<numsSize;i++){
        s = nums[i]<s?nums[i]:s;
        b = nums[i]>b?nums[i]:b;
    }
    return gcd(s, b);
}

void main() {
    int n = 5;
    int nums[] = {7,5,6,8,3};
    printf("%d\n", findGCD(nums, n));
}
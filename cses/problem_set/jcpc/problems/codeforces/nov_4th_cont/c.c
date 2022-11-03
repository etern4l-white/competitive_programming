#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void main () {
    int n, p=0, even_len = 0, odd_len = 0;
    scanf("%d", &n);
    char** arr = (char**)malloc(sizeof(char*)*n);
    int lens[n];
    for(int i = 0;i<n;i++) {
        char* word = (char*)malloc(sizeof(char)*6);
        scanf("%5s", word);
        arr[i] = word;
        lens[i] = strlen(word);
        if (lens[i]%2==0){
            even_len++;
        } else {
            odd_len++;
        }
    }
    
    char** even = (char**)malloc(even_len*sizeof(char*));
    char** odd = (char**)malloc(odd_len*sizeof(char*));
    

    int even_counter = 0, odd_counter = 0;
    for(int i =0;i<n;i++){
        if (lens[i]%2==0){
            even[even_counter] = arr[i];
            even_counter++;
        } else{
            odd[odd_counter] = arr[i];
            odd_counter++;
        }
    }
    int all =0, temp, cur_sum = 0;
    for(int i =0;i<even_counter;i++){
        // printf("%s--\n", even[i]);
        for (int j =0;j<even_counter;j++){
            all = 0;
            cur_sum = 0;
            temp = atoi(even[i]);
            printf("%d, ",temp);
            while(temp){
                cur_sum+=temp%10;
                temp/=10;
            }

            all = cur_sum;
            cur_sum = 0;
            temp = atoi(even[j]);
            printf("%d\n", temp);
            while(temp){
                cur_sum+=temp%10;
                temp/=10;
            }
            printf("%d %d\n", cur_sum, all);
            if (cur_sum == all) {
                p++;
            }
        }

    }


    all =0; temp = 0; cur_sum = 0;

    for(int i =0;i<odd_counter;i++){
        // printf("%s--\n", even[i]);
        for (int j =0;j<odd_counter;j++){
            cur_sum = 0;
            temp = atoi(odd[i]);
            printf("%d, ",temp);
            while(temp){
                cur_sum+=temp%10;
                temp/=10;
            }
            all = cur_sum;
            cur_sum = 0;
            temp = atoi(odd[j]);
            printf("%d\n",temp);
            while(temp){
                cur_sum+=temp%10;
                temp/=10;
            }
            printf("%d %d\n", cur_sum, all);
            if (cur_sum == all) {
                p++;
            }
        }

    }

    printf("%d-----------------------------\n", p);


    // for(int i = 0;i<n;i++){
    //     printf("%d\n", strlen(arr[i]));
    //     free(arr[i]);
    // }

    for(int i =0;i<n;i++){
        free(arr[i]);
    }
    free(arr);


}
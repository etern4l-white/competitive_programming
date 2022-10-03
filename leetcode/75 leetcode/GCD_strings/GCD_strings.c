#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* delete_string(char* org, char* rep, int rep_len) {
    char* strr = strdup(org);
    char* substrr = strdup(rep);
    char* first_point = strstr(strr, substrr);
    while (first_point != NULL) {
        char* new_str = (char*)calloc(rep_len+1, sizeof('a'));
        strncat(new_str, strr, first_point - strr);
        strcat(new_str, first_point + rep_len);
        // printf("%s\n", new_str);
        free(strr);
        strr = strdup(new_str);
        // printf("%s\n", strr);
        first_point = strstr(strr, substrr);
        // printf("%s\n", strr);
        free(new_str);
    }
    // printf("Returned -- %s\n", strr);
    return strr;

}

char * gcdOfStrings(char * str1, char * str2){
    
    int l1 = strlen(str1), l2 = strlen(str2);
    char* small = l1>=l2?strdup(str2):strdup(str1);
    char* big = l1<l2?strdup(str2):strdup(str1);
    // printf("Small : %s\nBig: %s\n", small, big);
    int ls = strlen(small), lb = strlen(big), i = 0, kernel_size = ls;
    while (kernel_size > 0) {
        while (i<ls-kernel_size+1) {
            // printf("asdf\n");
            char* kernel = (char*)calloc(kernel_size+1, sizeof('a'));
            strncpy(kernel, i + small, kernel_size);
            // if 
            char* b = delete_string(big, kernel, kernel_size);
            char* s = delete_string(small, kernel, kernel_size);
            // printf("%s\n", kernel);
            if (strlen(b) == 0 && strlen(s) == 0){
                
                return kernel;
            }
            free(kernel);
            i++;
        }
        kernel_size--;
    }
    char* kernel = "";
    return kernel;
}

void main () {
    char* str1 = "ABCDEF";char* str2="ABC";
    printf("%s\n", gcdOfStrings(str1, str2));


}
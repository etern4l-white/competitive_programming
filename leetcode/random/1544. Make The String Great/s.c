#include <string.h>
#include <stdlib.h>
#include <stdio.h>


char* makeGood(char* s) {
    char* str = strdup(s);
    int l, is = 1, ist = 0, v;
    l = strlen(str);
    char* stack = (char*)calloc(l, sizeof(char));
    stack[0] = str[0];
    while (is<l){
        if (is > 0) {
            v = str[is] - stack[ist];
            if (v == 32 || v == -32){
                stack[ist] = '\0';
                ist--;
            } else {
                ist++;
                stack[ist] = str[is];
            }
            
        } else {
                ist++;
                stack[ist] = str[is];
        }
        is++;
    }
    char res[ist-1];
    strcpy(res, stack);
    free(stack);
    // printf("%d\n", ist);
    stack = (char*)calloc(ist, sizeof(char));
    stack = strdup(res);
    return stack;

}



int main() {

    printf("%s\n", makeGood("leEeetcode"));
    return 0;
}
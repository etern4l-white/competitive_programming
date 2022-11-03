#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#define AP "abcdefghijklmnopqrstuvwxyz"


void main() {
    int n, r;
    char* raw = (char*)malloc(300*sizeof(char));
    scanf("%d", &n);
    int decrypt = !strstr(raw, " the ") == NULL;

    for(int i=0;i<n;i++){
        scanf("%d", &r);
        scanf("%s", raw);
        for(int j = 0;j<strlen(raw);j++){
            if (raw[j]!=' ') {
                if (decrypt)
                raw[j] = strchr(AP, (strchr(AP, raw[j])+(26-r))[0]);
                else
                raw[j] = strchr(AP, (strchr(AP, raw[j])+(r))[0]);
            }
        }
        printf("%s\n", raw);
        scanf("%s", NULL);
    }
    free(raw);



}
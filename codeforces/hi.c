#include <stdlib.h>
#include <string.h>
#include <stdio.h>


/*


st = input()
l = input()
s = 0
ss = 0
i = []
while True:
    try:
        ss = st.index(l, ss) + 1
        i.append(ss)
        s+=1
    except:
        break
if s > 0:
    print(s)
    print(' '.join([str(x) for x in i]))
else:
    print("Not found")


*/

void main() {
    int st, l, s= 0, ss= 0;
    int i;
    char* str = "khaled";
    printf("%s\n", str);
    char* tok = strtok(str, "a");
    printf("opyui\n");
    printf("%d\n", strtok(str, "a"));
    // printf("%d\n", strtok("asdfa", "a"));

}
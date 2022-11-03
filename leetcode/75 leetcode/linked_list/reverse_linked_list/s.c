#include <stdlib.h>

// Definition for singly-linked list->
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* hi;
    if (!head) return hi;
    hi->val = head->val;
    hi->next = NULL;
    while (!head->next) {
        head = head->next;
        struct ListNode* hey;
        hey->val = head->val;
        hey->next = head;
    }
    return hi;
}
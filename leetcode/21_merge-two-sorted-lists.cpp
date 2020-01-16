
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (!l1 or !l2) {
            if (!l1) {return l2;}
            else {return l1;}
            
        } else {
            ListNode* l = new ListNode(0);
            ListNode* head = l;
            while (l1 && l2) {
                if (l1->val <= l2->val) {
                    l->next = l1;
                    l1 = l1->next;
                } else {
                    l->next = l2;
                    l2 = l2->next;
                }
                l = l->next;
            }
            if (!l1) {
                l->next = l2;
                while (l2->next) {
                    l->next = l2;
                    l2 = l2->next;
                    l = l->next;
                }
            } else {
                l->next = l1;
                while (l1->next) {
                    l->next = l1;
                    l1 = l1->next;
                    l = l->next;
                }
            }
            return head->next;
        }
    }
};

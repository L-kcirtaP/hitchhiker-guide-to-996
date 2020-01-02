/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }
        ListNode* second = head->next;
        ListNode* dummy = new ListNode(-1);
        ListNode *ptr = dummy;
        ListNode *ret = ptr;
        while (head->next && second->next) {
            ptr->next = new ListNode(second->val);
            ptr = ptr->next;
            ptr->next = new ListNode(head->val);
            ptr = ptr->next;
            head->next = second->next;
            head = head->next;
            if (head->next) {
                second->next = head->next;
                second = second->next;
            } else {
                ptr->next = new ListNode(head->val);
                cout << "return in while." << endl;
                return ret->next;
            }
        }
        ptr->next = new ListNode(second->val);
        ptr = ptr->next;
        ptr->next = new ListNode(head->val);
        return ret->next;
    }
};

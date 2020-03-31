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
    ListNode* sortList(ListNode* head) {
	    if (!head) return NULL;

        ListNode* tail = head;
        while (tail->next) {
            tail = tail->next;
        }

        this->sortListCore(head, tail);
        return head;
	}

    void sortListCore(ListNode* start,ListNode* end) {
        if (start == end) return;

        ListNode *p1_prev, *p1, *p2;
        p1_prev = start;
        p1 = start->next;
        p2 = start->next;

        while (p2 != end->next) {
            if (p2->val <= start->val) {
            	int tmp = p1->val;
            	p1->val = p2->val;
            	p2->val = tmp;
                if (p1 != end) {
                    p1 = p1->next;
                    p1_prev = p1_prev->next;
                }
            }
            p2 = p2->next;
        }

        if (p1 == end and p1->val < start->val) {
        	int tmp = p1->val;
        	p1->val = start->val;
        	start->val = tmp;
        }

        this->sortListCore(start, p1_prev);
        this->sortListCore(p1, end);
    }
};
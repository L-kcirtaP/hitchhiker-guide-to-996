/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {
 }
 * };
 */
class Solution {
public:

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // 从head开始每一位累加，用flag表示是否需要进位
        if (l1 == nullptr && l2 == nullptr) {
            return nullptr;
        }

        ListNode* head = new ListNode(0);
        ListNode* p = head;
        int flag = 0;
        // 逐位相加，注意进位
        while (l1 != nullptr && l2 != nullptr) {
            ListNode* node = new ListNode(0);
            int num = l1->val + l2->val + flag;
            node->val = num % 10;
            flag = num >= 10 ? 1 : 0;

            l1 = l1->next;
            l2 = l2->next;
            p->next = node;
            p = p->next;
        }

        // 如果l1比l2长
        while (l1 != nullptr && l2 == nullptr) {
            ListNode* node = new ListNode(0);
            int num = l1->val + flag;
            node->val = num % 10;
            flag = num >= 10 ? 1 : 0;

            l1 = l1->next;
            p->next = node;
            p = p->next;
        }

        //  如果l2比l1长
        while (l2 != nullptr && l1 == nullptr) {
            ListNode* node = new ListNode(0);
            int num = l2->val + flag;
            node->val = num % 10;
            flag = num >= 10 ? 1 : 0;

            l2 = l2->next;
            p->next = node;
            p = p->next;
        }

        // 注意l1和l2全部遍历完后，仍然有可能出现flag为1的情况，此时需要继续添加一个node
        if (flag == 1) {
            ListNode* node = new ListNode(1);

            p->next = node;
            p = p->next;
        }

        return head->next;
    }


};

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2)
{
    if(list1 == NULL) return list2;
    if(list2 == NULL) return list1;

    struct ListNode *temp1 = list1;
    struct ListNode *temp2 = list2;

    struct ListNode *head = malloc(sizeof(struct ListNode));
    struct ListNode *temp = head;

    while(temp1 != NULL && temp2 != NULL)
    {
        if(temp1->val < temp2->val)
        {
            temp->val = temp1->val;
            temp1 = temp1->next;
        }
        else
        {
            temp->val = temp2->val;
            temp2 = temp2->next;
        }

        if(temp1 != NULL || temp2 != NULL)
        {
            temp->next = malloc(sizeof(struct ListNode));
            temp = temp->next;
        }
    }

    while(temp1 != NULL)
    {
        temp->val = temp1->val;
        temp1 = temp1->next;

        if(temp1 != NULL)
        {
            temp->next = malloc(sizeof(struct ListNode));
            temp = temp->next;
        }
    }

    while(temp2 != NULL)
    {
        temp->val = temp2->val;
        temp2 = temp2->next;

        if(temp2 != NULL)
        {
            temp->next = malloc(sizeof(struct ListNode));
            temp = temp->next;
        }
    }

    temp->next = NULL;

    return head;
}
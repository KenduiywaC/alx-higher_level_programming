#include <stdlib.h>
#include "lists.h"

/**
* check_cycle - Checks if a singly-linked list contains a cycle.
* @list: A singly-linked list.
*
* Return: If there is no cycle - 0.
*         If there is a cycle - 1.
*/
int check_cycle(listint_t *list)
{
listint_t *girl, *boy;

if (list == NULL || list->next == NULL)
return (0);

girl = list->next;
boy = list->next->next;

while (girl && boy && boy->next)
{
if (girl == boy)
return (1);

girl = boy->next;
boy = boy->next->next;
}

return (0);
}

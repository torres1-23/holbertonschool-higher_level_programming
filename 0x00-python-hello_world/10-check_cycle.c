#include "lists.h"
/**
 * check_cycle - checks if a list has a cycle or not
 * @list: pointer to list structure
 * Return: 0 if list has no cycle, else 1.
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list;

	if (list)
	{
		while (list->next && head->next->next)
		{
			if (list == head)
				return (1);
		}
	}
	return (0);
}

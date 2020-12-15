#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head node.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int num[1024], i, cont = 0, l = 0;

	if (*head)
	{
		for (i = 0; tmp; i++)
		{
			cont++;
			num[i] = tmp->n;
			tmp = tmp->next;
		}
		if (cont % 2 != 0)
			return (0);
		while (num[l])
			l++;
		l--;
		for (i = 0; i < l; i++)
		{
			if (num[i] != num[l--])
				return (0);
		}
		return (1);
	}
	return (0);
}

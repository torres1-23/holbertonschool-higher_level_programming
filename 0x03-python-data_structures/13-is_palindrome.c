#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head node.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int num[40], i, j;

	if (*head == NULL || !head)
		return (1);
	for (i = 0; tmp; i++)
		tmp = tmp->next;
	tmp = *head;
	for (j = 0; j < i; j++)
	{
		num[j] = tmp->n;
		tmp = tmp->next;
	}
	for (j = 0; j < i; j++)
	{
		if (num[j] != num[i - 1])
			return (0);
		i--;
	}
	return (1);
}

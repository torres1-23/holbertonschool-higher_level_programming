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
	int *num = NULL, i, j;

	if (head || head*)
	{
		for (i = 1; tmp->next; i++)
			tmp = tmp->next;
		num = malloc(sizeof(int) * i);
		if (!num)
			return (-1);
		tmp = *head;
		for (j = 0; j < i; j++)
		{
			num[j] = tmp->n;
			tmp = tmp->next;
		}
		for (j = 0; j < i; j++)
		{
			if (num[j] != num[i - 1])
			{
				free(num);
				return (0);
			}
			i--;
		}
		free(num);
	}
	return (1);
}

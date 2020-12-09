#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts node in a sorted list
 * @head: head pointer to list.
 * @number: integer to insert.
 * Return: pointer to new node or NULL if fails.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *new, *tmp1;
	int i, cont = 0;

	tmp = *head;
	tmp1 = *head;
	if (head)
	{
		while (tmp)
		{
			if (tmp->n < number)
			{
				tmp = tmp->next;
				cont++;
			}
			else
				break;
		}
		if (!tmp)
			return (NULL);
		for (i = 0; i < cont - 1; i++)
			tmp1 = tmp1->next;
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		tmp1->next = new;
		new->n = number;
		new->next = tmp;
		return (tmp);
	}
	return (NULL);
}

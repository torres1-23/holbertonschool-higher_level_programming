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
	listint_t *tmp = NULL, *new = NULL, *tmp1 = NULL;
	int i, cont = 0;

	tmp = *head, tmp1 = *head;
	if (head)
	{
		while (tmp)
		{
			if (tmp->n < number)
				tmp = tmp->next, cont++;
			else
				break;
		}
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);
		for (i = 0; i < cont - 1; i++)
			tmp1 = tmp1->next;
		if (cont == 0)
		{
			*head = new;
			new->next = tmp;
		}
		else if (!tmp)
		{
			tmp1->next = new;
			new->next = NULL;
		}
		else
		{
			tmp1->next = new;
			new->next = tmp;
		}
		new->n = number;
		return (tmp);
	}
	return (NULL);
}

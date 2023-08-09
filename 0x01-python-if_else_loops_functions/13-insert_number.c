#include "lists.h"
/**
 * insert_node - Inserts number into linked list
 * @head: A pointer the head
 * @number: The number
 * Return: NULL if function fails
 * or a pointer to new node (niu)
 */

listint_t *insert_node(listint_t **head, int number)
{

	listint_t *nd = *head, *niu;

	niu = malloc(sizeof(listint_t));
	if (niu == NULL)
		return (NULL);
	niu->n = number;
	if (nd == NULL || nd->n >= number)
	{
		niu->next = nd;
		*head = niu;
		return (niu);
	}
	while (nd && nd->next && nd->next->n < number)
		nd = nd->next;
	niu->next = nd->next;
	nd->next = niu;
	return (niu);
}

#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * rev_slistint - Reverses a singly-linked listint_t list.
 * @h: A pointer to the starting node of the list to reverse.
 * Return: A pointer to the head of the reversed list.
 */

listint_t *rev_slistint(listint_t **h)
{

	listint_t *nd = *h, *next, *previous = NULL;

	while (nd)
	{
		next = nd->next;
		nd->next = previous;
		previous = nd;
		nd = next;
	}
	*h = previous;
	return (*h);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 * Return: 0 if linked list not a palindrome
 * 1 if otherwise
 */

int is_palindrome(listint_t **head)
{

	listint_t *temp, *r, *m;
	size_t size = 0, j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}
	temp = *head;
	for (j = 0; j < (size / 2) - 1; j++)
		temp = temp->next;
	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);
	temp = temp->next->next;
	r = rev_slistint(&temp);
	m = r;
	temp = *head;
	while (r)
	{
		if (temp->n != r->n)
			return (0);
		temp = temp->next;
		r = r->next;
	}
	rev_slistint(&m);
	return (1);
}

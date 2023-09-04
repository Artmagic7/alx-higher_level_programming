#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - The singly linked list
 * @n: The integer
 * @next: pointing to next node
 *
 * Description: Structure of singly linked list node
 * for project Holberton
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
int check_cycle(listint_t *list);
void free_listint(listint_t *head);

#endif /* LISTS_H */

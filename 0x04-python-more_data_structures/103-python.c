#include <stdio.h>
#include <Python.h>
/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object
 * Return: no return
 */

void print_python_bytes(PyObject *p)
{

	char *str;
	long int s, j, l;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", s);
	printf("  trying string: %s\n", str);
	if (s >= 10)
		l = 10;
	else
		l = s + 1;
	printf("  first %ld bytes:", l);
	for (j = 0; j < l; j++)
		if (str[j] >= 0)
			printf(" %02x", str[j]);
		else
			printf(" %02x", 256 + str[j]);
	printf("\n");
}

/**
 * print_python_list - Prints list information
 * @p: Python Object
 * Return: no return
 */

void print_python_list(PyObject *p)
{

	long int s, j;
	PyListObject *l;
	PyObject *o;

	s = ((PyVarObject *)(p))->ob_size;
	l = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", l->allocated);
	for (j = 0; j < s; j++)
	{
		o = ((PyListObject *)p)->ob_item[j];
		printf("Element %ld: %s\n", j, ((o)->ob_type)->tp_name);
		if (PyBytes_Check(o))
			print_python_bytes(o);
	}
}

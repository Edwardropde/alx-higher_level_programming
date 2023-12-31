#include <Python.h>
/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */

void print_python_list_info(PyObject *p)
{

	int allocated, size, j;
	PyObject *object;

	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);
	for (j = 0; j < size; j++)
	{
		printf("Element %d: ", j);
		object = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}

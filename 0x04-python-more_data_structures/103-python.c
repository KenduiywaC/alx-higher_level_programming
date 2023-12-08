#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; ++i) {
        printf("Element %zd: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    const char *bytes_data = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", bytes_data ? bytes_data : "(nope)");

    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < size && i < 10; ++i) {
        printf("%02hhx", bytes_data[i]);
        if (i < 9) {
            printf(" ");
        }
    }
    printf("\n");
}

int main(void) {
    Py_Initialize();

    // Example usage with Python lists
    PyObject *py_list = PyList_New(4);
    PyList_SetItem(py_list, 0, PyLong_FromLong(10));
    PyList_SetItem(py_list, 1, PyLong_FromLong(20));
    PyList_SetItem(py_list, 2, PyUnicode_FromString("Hello"));
    PyList_SetItem(py_list, 3, PyFloat_FromDouble(3.14));

    print_python_list(py_list);

    // Example usage with Python bytes object
    char data[] = {0x48, 0x65, 0x6C, 0x6C, 0x6F};  // ASCII values for "Hello"
    PyObject *py_bytes = PyBytes_FromStringAndSize(data, sizeof(data));

    print_python_bytes(py_bytes);

    Py_XDECREF(py_list);
    Py_XDECREF(py_bytes);
    Py_Finalize();

    return 0;
}


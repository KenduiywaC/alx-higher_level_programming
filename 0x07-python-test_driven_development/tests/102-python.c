#include <Python.h>

void print_python_string(PyObject *p) {
    if (PyUnicode_Check(p)) {
        // Extract the string from the Python object
        const char *str = PyUnicode_AsUTF8(p);

        // Check if the conversion was successful
        if (str == NULL) {
            PyErr_Print();
            return;
        }

        // Print the Python string
        printf("'%s'\n", str);
    } else {
        // Print an error message if p is not a valid string
        fprintf(stderr, "Invalid Python string\n");
    }
}

int main() {
    // Example usage
    Py_Initialize();

    // Create a Python string object
    PyObject *py_str = PyUnicode_FromString("Hello, Python!");

    // Call the print_python_string function
    print_python_string(py_str);

    // Release the Python object
    Py_DECREF(py_str);

    // Finalize the Python interpreter
    Py_Finalize();

    return 0;
}

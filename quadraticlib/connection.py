import ctypes

path_to_dll = "C:\\Users\\osentemova\\estonian\\quadraticlib\\quadratic.dll"

dll = ctypes.cdll.LoadLibrary(path_to_dll)

def solve_equation(a, b, c):
    x1 = ctypes.c_double()
    x2 = ctypes.c_double()
    dll.setA((ctypes.c_double)(a))
    dll.setB((ctypes.c_double)(b))
    dll.setC((ctypes.c_double)(c))
    dll.getSolution.argtypes  = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
    result = dll.getSolution(ctypes.pointer(x1), ctypes.pointer(x2))
    roots = (x1.value, x2.value)
    return result, roots

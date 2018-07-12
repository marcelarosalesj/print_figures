def print_square(n):
    """ Prints a square """
    for i in range(0, n):
        for i in range(0, n):
            print("*", end='', flush=True)
        print()

def print_triangle(n):
    """ Prints a triangle """
    if n == 0:
        return
    for i in range(0, n):
        print("*", end='', flush=True)
    print()
    print_triangle(n-1)

print_square(5)

print_triangle(5)

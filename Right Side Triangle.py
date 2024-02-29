



"""#n = int(input()) #if user want to take input
n = 5 #if input preset
for i in range(n):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
"""
def right_upward_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)

# Example usage:
right_upward_triangle(5)





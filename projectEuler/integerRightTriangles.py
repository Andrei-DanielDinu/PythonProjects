from collections import defaultdict

def find_max_solutions(max_p):
    solutions = defaultdict(int)

    for a in range(1, max_p):
        for b in range(a, max_p - a):
            c = (a**2 + b**2)**0.5
            perimeter = a + b + c
            if c == int(c) and perimeter <= max_p:
                solutions[int(perimeter)] += 1

    max_solutions = max(solutions.values())
    max_perimeter = max(solutions, key=solutions.get)
    return max_perimeter

max_p = 1000
result = find_max_solutions(max_p)
print("The value of p that maximizes the number of solutions is:", result)

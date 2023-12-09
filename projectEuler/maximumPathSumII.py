def maximum_path_sum(triangle):
    # Start from the second-bottom row of the triangle
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # Calculate the maximum sum by choosing the larger adjacent value from the next row
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    # The maximum total will be at the top of the triangle
    return triangle[0][0]

# Read the triangle from triangle.txt
with open('C:/Users/User/PycharmProjects/projectEuler/triangle.txt', 'r') as file:
    triangle = [[int(num) for num in line.split()] for line in file]

# Find the maximum total from top to bottom in the triangle
result = maximum_path_sum(triangle)
print(f"The maximum total from top to bottom in the triangle is: {result}")

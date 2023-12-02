import random
import matplotlib.pyplot as plt


def plot_path(player_path, target_path, target):
    plt.figure(figsize=(8, 8))
    plt.title('2D Number Guessing Game')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Plot the player's path
    for i in range(len(player_path) - 1):
        plt.plot([player_path[i][0], player_path[i + 1][0]], [player_path[i][1], player_path[i + 1][1]], marker='o',
                 linestyle='-', color='b')

    # Plot the target's path
    for i in range(len(target_path) - 1):
        plt.plot([target_path[i][0], target_path[i + 1][0]], [target_path[i][1], target_path[i + 1][1]], marker='x',
                 linestyle='-', color='r')

    # Plot the target
    plt.scatter(target[0], target[1], color='red', label='Target')
    plt.legend()
    plt.grid(True)
    plt.show()


def generate_target():
    return [random.randint(-100, 100), random.randint(-100, 100)]


def move_target(current_position, x, y):
    if(current_position[0]<=x):
        new_x = random.randint(-100,x)
        if (current_position[1] <= y):
            new_y = random.randint(-100,y)
        if (current_position[1] > y):
            new_y = random.randint(y,100)
    if (current_position[0] > x):
        new_x = random.randint(x,100)
        if (current_position[1] <= y):
            new_y = random.randint(-100, y)
        if (current_position[1] > y):
            new_y = random.randint(y, 100)

    return [new_x, new_y]


player_path = []
target_path = []
target = generate_target()

print("Welcome to the 2D Number Guessing Game!")
print("The target is within the range (-100, 100) on both X and Y axes.")
print("Enter '0 0' to exit the game.")

while True:
    print(f"Target is at coordinates ({target[0]}, {target[1]})")
    coordinates = input("Enter your coordinates (x y): ")
    if coordinates == '0 0':
        print("Game stopped. Here is your path:")
        plot_path(player_path, target_path, target)
        break

    try:
        x, y = map(int, coordinates.split())
    except ValueError:
        print("Invalid input! Please enter two integers separated by a space.")
        continue

    player_path.append([x, y])
    target_path.append(target.copy())

    if x > target[0]:
        if y > target[1]:
            print("Go South-West")
        elif y < target[1]:
            print("Go North-West")
        else:
            print("Go West")
    elif x < target[0]:
        print("Go East")
        if y > target[1]:
            print("Go South-East")
        elif y < target[1]:
            print("Go North-East")
        else:
            print("Go East")
    else:
        print("You found it!")

    target = move_target(target, x, y)

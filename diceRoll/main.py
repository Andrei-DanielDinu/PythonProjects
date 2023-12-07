import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def graham_bell_experiment():
    num_trials = int(input("Enter the number of trials: "))
    num_dice = int(input("Enter the number of dice: "))

    results = []
    for _ in range(num_trials):
        total = sum(random.randint(1, 6) for _ in range(num_dice))
        results.append(total)

    # Calculate statistics
    mean = np.mean(results)
    variance = np.var(results)
    std_dev = np.sqrt(variance)

    print(f"Mean: {mean}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_dev}")

    # Plotting the results as a histogram
    plt.hist(results, bins=range(num_dice, 6*num_dice+2), density=True, alpha=0.7, label='Experimental Distribution')

    # Calculate the theoretical normal distribution
    mu = num_dice * 3.5  # Mean of the distribution for n dice (expected value of the sum)
    sigma = np.sqrt(num_dice * (35 / 12))  # Standard deviation for n dice (variance of the sum)
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    plt.plot(x, norm.pdf(x, mu, sigma), label='Theoretical Normal Distribution')

    plt.xlabel('Sum of Dice Rolls')
    plt.ylabel('Probability')
    plt.title(f"Graham's Bell with {num_dice} dice over {num_trials} trials")
    plt.legend()
    plt.show()

# Run the experiment
graham_bell_experiment()

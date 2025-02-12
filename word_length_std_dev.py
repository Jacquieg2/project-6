# Author: Jacqueline Garcia
# GitHub username: Jgarcia2
# Date: 02/11/2025
# Description: sample standard deviation

def word_length_std_dev(text):
    """
    Calculates the sample standard deviation of word lengths in a given string.
    
    Parameters:
    text (str): A string containing words separated by spaces.

    Returns:
    float: The sample standard deviation of the lengths of words in the string.
    """
    words = text.split()  # Split the text into words
    lengths = [len(word) for word in words]  # Get the length of each word
    n = len(lengths)  # Number of words

    if n < 2:
        return 0.0  # Standard deviation is undefined for a single word

    mean_length = sum(lengths) / n  # Calculate mean
    variance = sum((length - mean_length) ** 2 for length in lengths) / (n - 1)  # Sample variance
    return variance ** 0.5  # Return the square root of variance (standard deviation)


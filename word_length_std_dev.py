# Author: Jacqueline Garcia
# GitHub username: Jgarcia2
# Date: 02/04/2025
# Description: sample standard deviation

import math

def calculate_word_length_std_dev(text):
    """
    Calculates the sample standard deviation of word lengths in a given string.
    
    Parameters:
    text (str): A string containing words separated by spaces.
    
    Returns:
    float: The sample standard deviation of word lengths.
    """
    
    # Ensure text is not empty
    words = text.split()
    num_words = len(words)
    
    if num_words < 2:
        return 0.0  # Standard deviation is undefined for 1 or 0 words
    
    # Calculate word lengths
    lengths = [len(word) for word in words]
    
    # Compute mean (average) word length
    mean_length = sum(lengths) / num_words
    
    # Compute variance (sum of squared differences from the mean)
    variance = sum((length - mean_length) ** 2 for length in lengths) / (num_words - 1)
    
    # Compute standard deviation (square root of variance)
    std_dev = math.sqrt(variance)
    
    return std_dev

# Example usage:
text = "There is wisdom in turning as often as possible from the familiar to the unfamiliar"
result = calculate_word_length_std_dev(text)
print(f"Word Length Standard Deviation: {result:.2f}")

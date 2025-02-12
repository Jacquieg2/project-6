# Author: Jacqueline Garcia
# GitHub username: Jgarcia2
# Date: 02/04/2025
# Description: sample standard deviation

def calculate_word_length_std_dev(text):
    """
    Calculates the sample standard deviation of word lengths in a given string.
    
    Parameters:
    text (str): A string containing words separated by spaces.
    
    Returns:
    float: The sample standard deviation of word lengths.
    """
    
    words = text.split()
    num_words = len(words)
    
    if num_words < 2:
        return 0.0  
    
    lengths = [len(word) for word in words]
    mean_length = sum(lengths) / num_words
    variance = sum((length - mean_length) ** 2 for length in lengths) / (num_words - 1)
    
    return math.sqrt(variance)


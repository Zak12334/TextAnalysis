#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on a rainy day
Done on a rainy day

-----------------------------------------
This Python project automates text processing and analysis for .txt files. It cleans and counts words, 
identifies unique terms from filenames, and calculates statistics like empty lines and word sizes. 
The script also visualizes key data points, providing a concise overview of text content dynamics.

"""
import os
import numpy as np


def clean_word(word):
    # Remove non-alphabetic characters from the beginning or end
    while word and not word[0].isalpha():
        word = word[1:]
    while word and not word[-1].isalpha():
        word = word[:-1]

    # Handle non-alphabetic characters in the middle
    return word.split('-')  # Splitting the word by '-'

files = []

# Add our text files to 'files' list
for file in os.listdir():
    if file.endswith(".txt"):
        files.append(file)

for file in files:
    split = file.split("-")
    animal = split[1]
    vegetable = split[2]
    country = split[3].replace(".txt", "")

    print("Animal: ", animal)
    print("Vegetable: ", vegetable)
    print("Country: ", country)

    num_animal = 0
    num_vegetable = 0
    num_country = 0

    num_empty_lines = 0

    with open(file, "r") as f:  # Using 'with' is a better practice for opening files
        lines = f.readlines()

        for line in lines:
            if not line.strip():
                num_empty_lines += 1

            words = line.split()

            for word in words:
                cleaned_words = clean_word(word)

                for cleaned in cleaned_words:
                    cleaned = cleaned.lower()
                    if cleaned == animal.lower():
                        num_animal += 1
                    if cleaned == vegetable.lower():
                        num_vegetable += 1
                    if cleaned == country.lower():
                        num_country += 1

    print(f"In {file}:")
    print(f"{animal} appears {num_animal} times.")
    print(f"{vegetable} appears {num_vegetable} times.")
    print(f"{country} appears {num_country} times.")
    print("-" * 40)


# Function to count empty lines
def count_empty_lines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    empty_count = 0
    for line in lines:
        if line.strip() == "":
            empty_count += 1
            
    return empty_count

# Getting all the .txt files
txt_files = [file for file in os.listdir() if file.endswith('.txt')]

# Counting empty lines in each file
for file in txt_files:
    empty_lines = count_empty_lines(file)
    print(f"In {file}, there are {empty_lines} empty lines.")
    print("---------------")
    
def find_largest_word(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    max_length = 0
    for line in lines:
        words = line.split()
        for word in words:
            word = ''.join(filter(str.isalpha, word))  # Cleaning the word
            if len(word) > max_length:
                max_length = len(word)

    return max_length

# Getting all the .txt files
txt_files = [file for file in os.listdir() if file.endswith('.txt')]

# Finding the size of the largest word in each file
for file in txt_files:
    largest_size = find_largest_word(file)
    print(f"In {file}, the size of the largest word is {largest_size}.")
    print("--------------------")
    
def find_smallest_sentence_size(filename):
    with open(filename, "r") as f:
        content = f.read()

    sentences = content.split(".")
    
    # Removing the first sentence, as per requirement
    if sentences:
        sentences = sentences[1:]
        
    # If there are no sentences left after removing the first, return 0
    if not sentences:
        return 0

    # Find the size of the smallest sentence
    smallest_size = len(content)  # Initialize with a big number
    for sentence in sentences:
        size = len(''.join(sentence.split()))  # Counting characters without spaces
        if 0 < size < smallest_size:  # 0 < size is used to avoid empty sentences
            smallest_size = size

    return smallest_size

# Getting all the .txt files
txt_files = [file for file in os.listdir() if file.endswith('.txt')]

# Finding the size of the smallest sentence in each file
for file in txt_files:
    smallest_size = find_smallest_sentence_size(file)
    print(f"In {file}, the size of the smallest sentence (excluding spaces) is: {smallest_size}.")
    print("--------------------")


def count_file_size_without_invisibles(file_path):
    """Count the size of the file in bytes excluding spaces and invisible characters."""
    size_file = 0
    with open(file_path, 'r') as f:
        content = f.read()
        for char in content:
            if char.isalnum():  # Counting only if the character is alphanumeric
                size_file += 1
    return size_file

# Getting all the .txt files in the directory
txt_files = [file for file in os.listdir() if file.endswith('.txt')]

# Displaying the size of each file without counting invisible characters
for file in txt_files:
    file_size = count_file_size_without_invisibles(file)
    print(f"The size of {file} (excluding spaces and invisible characters) is: {file_size} bytes.")
    print("--------------------")
    

# Get all text files in the directory
txt_files = [file for file in os.listdir() if file.endswith('.txt')]

# Initialize an empty list to store our data
data = []

# Iterate through each file to extract the name values
for file in txt_files:
    parts = file.replace('.txt', '').split('-')  # Split the filename into parts
    row = parts[:5]  # Take only the first 5 parts
    data.append(row)

# Convert our list of data into a numpy array
array = np.array(data, dtype=object)  # Using dtype=object to accommodate different types of data

# Display the numpy array
print(array)

# ----------------------------------

# Function to count the number of empty lines in a file
def count_empty_lines(filename):
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            if not line.strip():  # An empty line has no characters other than whitespace
                count += 1
    return count

rows_with_empty_lines = []

# Loop to count empty lines and identify files with more than 10
for idx, file in enumerate(txt_files):
    if count_empty_lines(file) > 10:
        rows_with_empty_lines.append(array[idx])

# Displaying rows corresponding to files with more than 10 empty lines
print("Rows with more than 10 empty lines:")
for row in rows_with_empty_lines:
    print(row)


# Function to find the length of the largest word in a file
def largest_word_size(filename):
    max_size = 0
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                if len(word) > max_size:
                    max_size = len(word)
    return max_size

# Loop to find the size of the largest word across all files
max_word_sizes = [largest_word_size(file) for file in txt_files]
print("Size of the largest word across all files:", max(max_word_sizes))

# Sorry sir, I ran out of time and i could not get the last 2 questions in time the exam was a lot harder than i imagined!. 





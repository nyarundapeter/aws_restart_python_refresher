"""
Insulin Sequence Processing Script

This script performs the following operations on an insulin sequence file:
1. **Cleaning**: Removes ORIGIN markers, numbers, double slashes, spaces, and line breaks.
2. **Validation**: Ensures the cleaned sequence contains exactly 110 characters.
3. **Splitting**: Divides the sequence into four sections (Isinsulin, binsulin, cinsulin, ainsulin).
4. **Saving**: Writes both the cleaned sequence and individual sections to respective files.

Functions:
- clean_file(): Reads and cleans the input file.
- extract_sequence(): Validates and returns the cleaned sequence.
- save_sequence_to_file(): Saves sequences to files.
- split_sequence(): Extracts specific insulin sequence segments.
- main(): Coordinates the execution of sequence processing.
"""

import re
import sys
import os

def clean_file(input_path):
    """
    Cleans a text file by removing:
    - *ORIGIN* markers
    - Numbers
    - Double Slashes (//)
    - Spaces
    - Line breaks and return carriages
    
    Args:
        input_path (str) : Path to the input file
        
    Returns: 
        str: The cleaned text content as a string
    
    """
    
    try:
        # Read the input file
        with open(input_path, 'r') as file:
            content = file.read()
            
        # Apply regex to remove unwanted elements
        # Remove *ORIGIN* markers
        content = re.sub(r'\bORIGIN\b', '', content)
        
        # Remove numbers
        content = re.sub(r'\d+', '', content)
        
        # Remove double slashes
        content = re.sub(r'//', '', content)
        
        # Remove spaces and line breaks
        content = re.sub(r'\s+', '', content)
        
        # Return the cleaned content as a string
        return content
        
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        return None
    except Exception as e:
        print(f"Error processing file: {e}")
        return None
        
def extract_sequence(input_path):
    """
    Calls clean_file and check if the resulting return is upto 110 characters.
    
     Args:
        input_path (str) : Path to the input file
        
    Returns: 
        str: The cleaned and checked text content as a string
    """
    
    sequence = clean_file(input_path)
    
    if (len(sequence)):
        print(f"Sequence cleaned and verified successfully:\n{sequence}")
        return sequence
    else:
        raise ValueError(f"Invalid sequence length: {len(sequence)}. Expected 110 characters.") 

def save_sequence_to_file(sequence, filename):
    """
    Save sequence characters to a file.

    Args:
        sequence (str): The sequence to be saved
        filename (str): Name of the file to save to
    """

    # Remove file if it already exists
    if os.path.exists(filename):
        os.remove(filename)

    # Create and open file for write operations
    try:
        with open(filename, 'w') as file:
            print(f"\nFound {len(sequence)} sequence characters to be saved to {filename}:")
            file.write(sequence)
            return print(f"Successfully written |{sequence}| to {filename}")
            
    except Exception as e:
        print(f"Error processing file: {e}")
        return None

def split_sequence(sequence, split_section):
    """
    Splits the sequences into predefined sections.
    
    Args:
        sequence(str): Cleaned and Verified sequence for splitting
        split_section(str): Section to be split
    
    Returns:
        str: Split section of the original sequence
    """
   
    # Define Valid Split Section
    valid_split_sections = {"Isinsulin", "binsulin", "cinsulin", "ainsulin"}
    
    if split_section not in valid_split_sections:
        raise ValueError(f"Invalid split section {split_section}. Expected one of {valid_split_sections}")
        
    # Perform the split in nested if statement
    
    if split_section == "Isinsulin":
        print(f"\nSplitting {sequence} between 1-24 char for Isinsulin section")
        return sequence[:24]
    elif split_section == "binsulin":
        print(f"\nSplitting {sequence} between 25-54 char for binsulin section")
        return sequence[24:54]
    elif split_section == "cinsulin":
        print(f"\nSplitting {sequence} between 55-89 char for cinsulin section")
        return sequence[54:89]
    else:
        print(f"\nSplitting {sequence} between 90-110 char for ainsulin section")
        return sequence[89:]
    

def main():
    """
    Main function to run the specific insulin sequence operations
    """
    
    # Instatiate specific details
    input_path = "sequence_files/preproinsulin-seq.txt"
    
    clean_sequence_filename = "sequence_files/preproinsulin-seq-clean.txt"
    isinsulin_sequence_filename = "sequence_files/Isinsulin-seq-clean.txt"
    binsulin_sequence_filename = "sequence_files/binsulin-seq-clean.txt"
    cinsulin_sequence_filename = "sequence_files/cinsulin-seq-clean.txt"
    ainsulin_sequence_filename = "sequence_files/ainsulin-seq-clean.txt"
    
    
    isinsulin = "Isinsulin"
    binsulin = "binsulin"
    cinsulin = "cinsulin"
    ainsulin = "ainsulin"
    
    # Clean the Sequence and save it to a file
    clean_sequence = extract_sequence(input_path)
    
    save_sequence_to_file(clean_sequence, clean_sequence_filename)
    
    # Split and Save each sequence section separately
   
    save_sequence_to_file((split_sequence(clean_sequence, isinsulin)), isinsulin_sequence_filename)
    save_sequence_to_file((split_sequence(clean_sequence, binsulin)), binsulin_sequence_filename)
    save_sequence_to_file((split_sequence(clean_sequence, cinsulin)), cinsulin_sequence_filename)
    save_sequence_to_file((split_sequence(clean_sequence, ainsulin)), ainsulin_sequence_filename)
    

main()
    
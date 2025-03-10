"""
This script reads:
    - human insulin sequence data from text files, 
    - merges specific segments, prints sequence information, -
    - calculates the rough molecular weight of insulin based on amino acid counts.
"""

def read_file(input_path):
    """
    Reads a text file
    
    Args:
        input_path (str) : Path to the text file
        
    Returns: 
        str: The text file content as a string
    
    """
    
    try:
        # Read the input file
        with open(input_path, 'r') as file:
            content = file.read()
        
        # Return the cleaned content as a string
        return content
        
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        return None
    except Exception as e:
        print(f"Error processing file: {e}")
        return None
  
def calculate_molecular_weight(insulin):
    """
    Calculates the molecular weight of an insulin amino acid sequence.
    
    Args:
        (str): A string representing the insulin amino acid sequence using standard single-letter codes.
        
    prints the computed molecular weight 
    
    """
    # Calculating the molecular weight of insulin  
    # Creating a list of the amino acid (AA) weights  
    aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
    'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
    'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
    'V': 117.15, 'W': 204.23, 'Y': 181.19}  
    # Count the number of each amino acids  
    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
    'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
    'V', 'W', 'Y']})  
    # Multiply the count by the weights  
    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
    ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
    'S', 'T', 'V', 'W', 'Y']}.values())  
    print("\nThe rough molecular weight of insulin: " +
    str(molecularWeightInsulin))
        
def main():
    """
    Main function to run the specific insulin sequence operations
    """
  
    # Store the human preproinsulin sequence in a variable called preproinsulin:
    preproInsulin = read_file("sequence_files/preproinsulin-seq-clean.txt")
    print(f"Stored preproInsulin as {preproInsulin}\n")
    
    # Store the remaining split sequences from sequence-analyze.py 
    IsInsulin = read_file("sequence_files/Isinsulin-seq-clean.txt")
    print(f"Stored IsInsulin as {IsInsulin}\n")
    
    bInsulin = read_file("sequence_files/binsulin-seq-clean.txt")
    print(f"Stored bInsulin as {bInsulin}\n")
    
    aInsulin = read_file("sequence_files/ainsulin-seq-clean.txt")
    print(f"Stored aInsulin as {aInsulin}\n")
    
    cInsulin = read_file("sequence_files/cinsulin-seq-clean.txt")
    print(f"Stored cInsulin as {cInsulin}\n")
    
    #Merge smaller insulin grouping into insulin:
    insulin = bInsulin + aInsulin
    
    # Printing " the sequence of human insulin" to console using successive print() commands:
    print(f"The sequence of human preproinsulin:\n{preproInsulin}\n")
    print("The sequence of human insulin, chain a: " + aInsulin)
    
    calculate_molecular_weight(insulin)
    

main()
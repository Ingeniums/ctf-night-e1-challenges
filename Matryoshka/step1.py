import zipfile
import os

def extract_nested_zips(zip_filename):
    """Extracts all nested zip files starting from the given zip file."""
    extracted_parts = []
    current_zip = zip_filename

    while current_zip:
        with zipfile.ZipFile(current_zip, 'r') as zipf:
            # Extract the zip contents
            zipf.extractall()

            # Extract the part.txt file (it should be the last part of the current zip)
            part_filename = None
            for file_name in zipf.namelist():
                if file_name.endswith('.txt'):
                    part_filename = file_name
                    break
            
            # Append the extracted part to the list
            if part_filename:
                extracted_parts.append(part_filename)
            
            # Find the next nested zip file (if any)
            next_zip = None
            for file_name in zipf.namelist():
                if file_name.endswith('.zip'):
                    next_zip = file_name
                    break

            # Update current_zip to the next nested zip file
            current_zip = next_zip
    
    return extracted_parts

def reconstruct_text_file(extracted_parts, output_file):
    """Reconstructs the original text file from the extracted parts."""
    with open(output_file, 'w', encoding='utf-8') as f:
        for part in extracted_parts:
            with open(part, 'r', encoding='utf-8') as part_file:
                f.writelines(part_file.readlines())

            # Optionally remove the part after processing to save space
            os.remove(part)

def main():
    zip_filename = 'part1.zip'  # The starting nested zip file
    output_file = 'input.txt'   # The reconstructed input file

    # Step 1: Extract all the parts from the nested zip files
    extracted_parts = extract_nested_zips(zip_filename)

    # Step 2: Reconstruct the original text file from the extracted parts
    reconstruct_text_file(extracted_parts, output_file)

    print(f"Reconstruction complete! The original text file is saved as {output_file}")

if __name__ == "__main__":
    main()

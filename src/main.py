import pandas as pd
import os
import sys
from excel_converter import convert_to_excel  # Add missing import
from pdf_generator import generate_pdf_from_csv  # Add missing import

def ensure_directories(base_dir):
    """Create directories relative to base_dir"""
    os.makedirs(os.path.join(base_dir, 'output'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'data', 'input'), exist_ok=True)

def read_csv_file(file_path):
    """Read CSV file with semicolon delimiter"""
    return pd.read_csv(file_path, 
                      encoding='utf-8',
                      delimiter=';',
                      engine='python')

def main():
    try:
        # Get correct base directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.dirname(script_dir)
        
        # Debug prints
        print(f"Script directory: {script_dir}")
        print(f"Base directory: {base_dir}")
        
        # Create directories
        ensure_directories(base_dir)
        
        # Set file paths
        input_file = os.path.join(base_dir, "data", "input", "FundraisingBox_donations.csv")
        print(f"Looking for input file at: {input_file}")
        
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"CSV file not found at {input_file}")
            
        df = read_csv_file(input_file)
        
        # Output files
        excel_output = os.path.join(base_dir, "output", "donations_report.xlsx")
        pdf_output = os.path.join(base_dir, "output", "donor_list.pdf")
        
        # Process files
        total = convert_to_excel(df, excel_output)
        generate_pdf_from_csv(input_file, pdf_output)
        
        print(f"Excel file created: {excel_output}")
        print(f"PDF file created: {pdf_output}")
        print(f"Total donations: {total:.2f} €")

    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise  # Add raise to see full traceback

if __name__ == "__main__":
    main()
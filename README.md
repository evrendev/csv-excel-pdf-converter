# fundraising-converter/fundraising-converter/README.md

# Fundraising Converter

This project is a Python application that converts a CSV file containing donation data into an Excel file with German headings and generates a PDF file formatted in three columns.

## Project Structure

```
fundraising-converter
├── src
│   ├── main.py
│   ├── excel_converter.py
│   ├── pdf_generator.py
│   └── utils
│       └── helpers.py
├── data
│   └── input
│       └── FundraisingBox_donations.csv
├── output
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fundraising-converter
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

This will read the `FundraisingBox_donations.csv` file, convert it to an Excel file, and generate a PDF file with the specified formatting.

## Requirements

- Python 3.x
- pandas
- openpyxl
- reportlab

## License

This project is licensed under the MIT License.
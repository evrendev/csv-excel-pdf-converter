# File: /fundraising-converter/fundraising-converter/src/utils/helpers.py

def read_csv(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def format_data_for_pdf(data):
    formatted_data = []
    for item in data:
        formatted_data.append(item)
    return formatted_data

def write_to_excel(data, output_path):
    import pandas as pd
    df = pd.DataFrame(data)
    df.to_excel(output_path, index=False)

def append_total_to_excel(excel_path, total):
    import openpyxl
    wb = openpyxl.load_workbook(excel_path)
    ws = wb.active
    ws.append(['Total', total])
    wb.save(excel_path)
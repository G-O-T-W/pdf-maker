# PDF Generator from CSV

This script generates a multi-page PDF document from a CSV file containing topics and their corresponding number of pages. Using the `FPDF` library, the script creates a title page for each topic, followed by extra blank pages based on the number of pages specified for each topic. Headers and footers are also automatically added to each page for consistency.

## Features

- **Generate PDFs**: Dynamically creates a PDF document with multiple pages for each topic based on CSV data.
- **Custom Headers and Footers**: Each page includes a header with the topic title and a footer that repeats the topic name for easy identification.
- **CSV Integration**: The script reads from a CSV file (`topics.csv`) that contains the topics and the number of pages to be generated.
- **Flexible Layout**: No auto page breaks, allowing full control over layout design.
  
## File Structure

- `topics.csv`: The CSV file containing the topics and page counts.
  - **Columns**:
    - `Topic`: The title of the topic.
    - `Pages`: The number of pages to generate for that topic.
- `pdf_generator.py`: The Python script that reads the CSV and generates the PDF using `FPDF` and `pandas`.

## Technologies Used

- **Python**: The core language used for scripting.
- **FPDF**: A lightweight Python library to generate PDF files.
- **Pandas**: Used to read the CSV file containing the topics and page numbers.

## Usage

1. Make sure you have `FPDF` and `pandas` installed:
   ```bash
   pip install fpdf pandas
   ```
2. Prepare the topics.csv file with the appropriate format.
3. Run the script:
   ```bash
   python pdf_generator.py
   ```
4. The output PDF (output.pdf) will be generated in the same directory.
   

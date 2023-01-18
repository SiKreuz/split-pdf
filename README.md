# Split PDF

Small script that uses a CSV file to automatically split a PDF file into multiple separate PDF files with given file names.

## Usage

```
Usage: main.py [OPTIONS] FILE

Options:
  -s, --separator FILENAME  CSV file with separator page numbers  [required]
  -o, --output_dir PATH     Output directory
  -h, --help                Show this message and exit.
```

### CSV format

The CSV file needs contain the following columns. It's mandatory to include the header in the file, the order is not important.

-   `start`: First page number
-   `end`: Last page number
-   `name`: File name as string (best in in quotation marks)

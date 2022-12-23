import csv
from pathlib import Path

import click
from PyPDF2 import PdfReader, PdfWriter

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def write(filename, pdf):
    with open(filename, 'wb') as f:
        pdf.write(f)
        f.close()


def add_pages(pdf, pages):
    for page in pages:
        pdf.add_page(page)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--separator', '-s',
              type=click.File('r'),
              help='CSV file with separator page numbers',
              required=True)
@click.option('--output_dir', '-o',
              type=click.Path(),
              default=Path(__file__).parent.resolve().joinpath('output'),
              help='Output directory')
@click.argument('file',
                type=click.File('rb'),
                required=True)
def cli(separator, output_dir, file):
    # Init
    separator_pages = csv.DictReader(separator, delimiter=',')
    input_pdf = PdfReader(file)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create with PDFs with starting pages from CSV
    for s in separator_pages:
        output = PdfWriter()
        add_pages(output, input_pdf.pages[int(s['start']) - 1:int(s['end'])])
        write(output_dir.joinpath('{}.pdf'.format(s['name'])), output)

    # Clean up
    file.close()
    separator.close()


if __name__ == '__main__':
    cli()

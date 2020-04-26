import copy, sys, argparse, factory
from PyPDF2 import PdfFileReader, PdfFileWriter
from factory import SortOrderFactory

def reorder_pages(sort_order):
    input = PdfFileReader(open('/dev/stdin', 'rb'))

    numPages = input.getNumPages()
    spreadPages = [0] * (numPages * 2)

    j = 0
    for p in [input.getPage(i) for i in range(0, numPages)]:
        q = copy.copy(p)
        (w, h) = p.mediaBox.upperRight
        p.mediaBox.lowerRight = (w, h/2)
        q.mediaBox.upperRight = (w, h/2)
        spreadPages[j*2] = p
        spreadPages[j*2 + 1] = q
        j = j + 1

    return sort_order.sort(spreadPages)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--first_page")
    return parser.parse_args()

def output_pages(pages: list):
    output = PdfFileWriter()
    for i in range(0, len(pages)):
        output.addPage(pages[i])
    output.write(open('/dev/stdout', 'wb'))

sort_order = SortOrderFactory.create(get_args().first_page)
reordered_pages = reorder_pages(sort_order)
output_pages(reordered_pages)

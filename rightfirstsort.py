from pagesort import PageSort

class RightFirstSort(PageSort):

    def sort(self, lhs):
        numPages = len(lhs)//2
        sortedPages = [0] * numPages*2
        for i in range(0, numPages//2):
            sortedPages[                 i*2] = lhs[i*4 + 1]
            sortedPages[numPages*2 - 1 - i*2] = lhs[i*4]
            sortedPages[numPages*2 - 2 - i*2] = lhs[i*4 + 3]
            sortedPages[             1 + i*2] = lhs[i*4 + 2]
        return sortedPages


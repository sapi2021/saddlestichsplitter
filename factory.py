from rightfirstsort import RightFirstSort
from leftfirstsort import LeftFirstSort

class SortOrderFactory():
    @staticmethod
    def create(opt):
        if opt == "right":
            return RightFirstSort()
        else:
            return LeftFirstSort()
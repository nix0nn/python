class Cell:
    def __init__(self, number_of_cells):
        self.cells = int(number_of_cells)

    def __add__(self, other):
        self.cells += other
        return Cell(self.cells)


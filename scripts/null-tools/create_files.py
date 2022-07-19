"""
Module doc
"""

class Files:
    """
    doc string
    """
    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_file(self, filename):
        """
        doc string
        """
        with open(filename, 'w+', encoding='utf8') as file:
            print("Created file:", file)

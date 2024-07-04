
# Docstring is a string that is written at the beginning of a module, class, or function definition. It provides a description of the module, class, or function. It is used to document the code and make it easier to understand. Docstrings are written inside triple quotes (""" """).
""" One line description. """

""" One line description

    More detailed description.
"""

# Example

"""This module provides functions to convert PDF to text."""


class Converter:
    """ A simple converter for converting PDFs to text."""

    def convert(self, path):
        """Convert PDF to text.

        Parameters: 
        path(str): Path to the PDF file.

        Returns:
        str: Text content of the PDF file.
        """
        print("pdf2text")

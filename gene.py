import random

'''
import importlib, importlib.util
import sys

from gene_string import GeneString
from gene_array import GeneArray
from gene_boolean import GeneBoolean

python gene.py -file gene.txt
'''


class Gene:

    def __init__(self):
        self.readSequence()

    def readSequence(self):
        gene = open("D:/PythonProjects/PycharmProjects/HW1-2/gene.txt", "r")
        print(gene.read())

        # gene_String.py
        self.geneString(gene)

        # gene_Array.py
        self.geneArray(gene)

        # gene_Boolean.py
        self.geneBoolean(gene)

    def geneString(self, gene):
        i = random.randint(1, 1000)

        # Test AddMarker
        self.gene_String.addMarker(gene)

        # Test BaseAt
        self.gene_String.baseAt(i)

        # Test Potential Gene
        self.gene_String.isPotentialGene(gene)

        # Test DisplayResults
        self.gene_String.displayResults(gene)

    def geneArray(self, gene):
        i = random.randint(1, 1000)

        # Test AddMarker
        self.gene_Array.addMarker(gene)

        # Test BaseAt
        self.gene_Array.baseAt(i)

        # Test Potential Gene
        self.gene_Array.isPotentialGene(gene)

        # Test DisplayResults
        self.gene_Array.displayResults(gene)

    def geneBoolean(self, gene):
        i = random.randint(1, 1000)

        # encode gene first
        self.gene_Boolean.encode()

        # Test AddMarker
        self.gene_Boolean.addMarker(gene)

        # Test BaseAt
        self.gene_Boolean.BaseAt(i)

        # Test Potential Gene
        self.gene_Boolean.isPotentialGene(gene)

        # Test DisplayResults
        self.geneBoolean.displayResults(gene)

import random


class GeneString:
    def addMarker(self, gene):
        marker_choices = "ACGT"
        r1 = random.choice(marker_choices)
        r2 = random.choice(marker_choices)
        r3 = random.choice(marker_choices)

        if r1 == "T":
            if r2 == "A":
                if r3 == "G" or r3 == "A":
                    self.addMarker(gene)
                else:
                    print("Marker added: ", r1, r2, r3)
                    self.Marker(gene, r1, r2, r3)
            elif r2 == "G":
                if r3 == "A":
                    self.addMarker(gene)
                else:
                    print("Marker added: ", r1, r2, r3)
                    self.Marker(gene, r1, r2, r3)
        else:
            print("Marker added: ", r1, r2, r3)
            self.Marker(gene, r1, r2, r3)

    def baseAt(self, i, gene):
        if gene.find("A", i, i) != -1:
            print("A")
        elif gene.find("C", i, i) != -1:
            print("C")
        elif gene.find("G", i, i) != -1:
            print("G")
        else:
            print("T")

    def isPotentialGene(self, gene):
        if gene.find("ATG") == 0:
            if gene.find("TAG", gene.len - 3, gene.len):
                return True
            elif gene.find("TAA", gene.len - 3, gene.len):
                return True
            elif gene.find("TGA", gene.len - 3, gene.len):
                return True
            else:
                return False
        else:
            return False

    def displayStatistics(self, gene):
        i = 0
        aChar = 0.0
        cChar = 0.0
        gChar = 0.0
        tChar = 0.0
        while i < gene.len:
            if gene[i] == "A":
                aChar += 1.0
            elif gene[i] == "C":
                cChar += 1.0
            elif gene[i] == "G":
                gChar += 1.0
            else:
                tChar += 1.0

        print("Number of A bases: ", aChar)
        print("Number of C bases: ", cChar)
        print("Number of G bases: ", gChar)
        print("Number of T bases: ", tChar)

        '''
        while i < gene.len:
            gene_str = gene[i] + gene[i+1] + gene[i+2]
            if gene_str == "AAA":
                print()
            elif gene_str == "AAC":
                print()
            elif gene_str == "AAG":

            elif gene_str == "AAT":

            elif gene_str == "ACA":

            elif gene_str == "AGA":

            elif gene_str == "AAT":

            elif gene_str == "":

            elif gene_str == "":

            elif gene_str == "":
        '''

    def Marker(self, gene, r1, r2, r3):
        gene = gene + r1 + r2 + r3

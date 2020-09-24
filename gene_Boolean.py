import random


class GeneBoolean:
    def addMarker(self, gene):
        marker_choices = "ACGT"
        r1 = random.choice(marker_choices)
        r2 = random.choice(marker_choices)
        r3 = random.choice(marker_choices)

        if (r1 == "T"):
            if (r2 == "A"):
                if (r3 == "G" or r3 == "A"):
                    self.addMarker(gene)
                else:
                    print("Marker added: ", r1, r2, r3)
                    gene.append(r1, r2, r3)
            elif (r2 == "G"):
                if (r3 == "A"):
                    self.addMarker(gene)
                else:
                    print("Marker added: ", r1, r2, r3)
                    gene.append(r1, r2, r3)
        else:
            print("Marker added: ", r1, r2, r3)
            gene.append(r1, r2, r3)

    def baseAt(i, gene):
        print()

    def isPotentialGene(self, gene):
        print()

    def displayStatistics(self, gene):
        i = 0
        aChar = 0.0
        cChar = 0.0
        gChar = 0.0
        tChar = 0.0
        while i < gene.len:
            if gene[i] == 0b00:
                aChar += 1.0
            elif gene[i] == 0b01:
                cChar += 1.0
            elif gene[i] == 0b10:
                gChar += 1.0
            else:
                tChar += 1.0

        print("Number of A bases: ", aChar)
        print("Number of C bases: ", cChar)
        print("Number of G bases: ", gChar)
        print("Number of T bases: ", tChar)

    # A = 00, C = 01, G = 10, T = 11
    def encode(self, gene):
        i = 0
        while i < gene.len:
            if gene[i] == "A":
                gene[i] == 0b00
            elif gene[i] == "C":
                gene[i] == 0b01
            elif gene[i] == "G":
                gene[i] = 0b10
            else:
                gene[i] = 0b11

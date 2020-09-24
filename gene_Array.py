import random


class GeneArray:
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
                    gene.append(r1, r2, r3)
            elif r2 == "G":
                if r3 == "A":
                    self.addMarker(gene)
                else:
                    print("Marker added: ", r1, r2, r3)
                    gene.append(r1, r2, r3)
        else:
            print("Marker added: ", r1, r2, r3)
            gene.append(r1, r2, r3)

    def baseAt(self, i, gene):
        print(gene[i])

    def isPotentialGene(self, gene):
        if gene.len % 3 == 0:
            if gene[0] == "A" and gene[1] == "T" and gene[2] == "G":
                if gene[gene.len - 3] == "T":
                    if gene[gene.len - 2] == "A":
                        if gene[gene.len - 1] == "G" or gene[gene.len - 1] == "A":
                            return True
                        else:
                            return False
                    elif gene[gene.length - 2] == "G":
                        if gene[gene.len - 1] == "A":
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
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

    def addCodon(gene):
        i = 0
        gene_str = ""
        while i < gene.len:
            gene_str = gene_str + gene[i]

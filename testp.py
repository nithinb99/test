 with open("//home//nithin//Downloads//master_catalog_csv.txt//") as f:
        for line in f:
            newline = line
            data = newline.split(',')
            books.append(data)
            #print(books[-1])
        return books
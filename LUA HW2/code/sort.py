import csv

# open the file for reading and writing
with open('example.csv', mode='r+', newline='') as f:

   # create a reader and writer opbject
    reader, writer = csv.reader(f), csv.writer(f)
    
    data = list()
    
    # sort all of the rows, based on date, with a lambda expression
    data = sorted(data, key=lambda row: row[0])

    # change the stream position to the given byte offset
    f.seek(0)

    # add a header to data
    header_names = "Clndrs,Volume,Hp:,Lbs-,Acc+,Model,origin,Mpg+",
    data.insert(0, header_names)

    # write data to the file
    writer.writerows(data)

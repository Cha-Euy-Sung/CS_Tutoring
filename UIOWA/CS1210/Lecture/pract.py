import csv

def unpackFile(filename, colnum):
    
    filename = 'test.csv'
    open_file = open(filename)
    read_file = csv.reader(row for row in open_file if not row.startswith('#'))

    column_list=[]
    for row in read_file:
        column_list.append(row[colnum])
    return colmun_list
        
        
        
        
        
        
        
        
    open_flie.close()
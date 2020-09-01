def readFile(stock_file):
    f  = open(stock_file, 'r')
    first_line = f.readline()
    return first_line

def updateFile( stock_file, str):
    f = open(stock_file, 'w')
    f.write(str)

if __name__=="__main__":
    updateFile('../ACB.txt', '1')
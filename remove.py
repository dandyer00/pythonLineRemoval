import sys
import re 

def run(inputFileName, outputFileName):
    print 'input: %s, output: %s' % (inputFileName, outputFileName) 
    try:
        with open(inputFileName, 'r') as f1:
            with open(outputFileName, 'w') as f2:
                for line in f1:
                    print repr(line)
#                    if line != '\n':
                    if re.search('^([0-9A-Fa-f]*)[\s]*\n', line) == None:
                        f2.write(line)
                f2.close()
            f1.close()
    except IOError:
        print IOError
        
if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2])
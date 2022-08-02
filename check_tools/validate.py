import mmap
import re
import os
from optparse import OptionParser

words = {}

def validate_file(inputfilename):
    global words
    print "Validating file:%s"%inputfilename
    input_file = open(inputfilename)
    alllines = input_file.readlines()
    
    line=1
    for eachline in alllines:
        result = re.findall(words,eachline,flags=re.IGNORECASE)
        for eachresult in result:
            if eachresult!=None and len(eachresult)!=0:
                print "\tLine %d:found \"%s\""%(line,str(eachresult))
        line=line+1            

def main():
    global words
    parser = OptionParser()
    parser.add_option("-f", "--inputfile",  dest="inputfile",  action="store", type="string", default="" , help="File to be validated", metavar="FILE")
    parser.add_option("-i", "--wordsfile", dest="wordsfile", action="store", type="string", default="prohibited.txt", help="File containing the words to be checked", metavar="FILE")
    (options, args) = parser.parse_args()

    if len(options.inputfile) <= 0 or len(options.wordsfile) is None:
        parser.error("Invalid arguments")

    words_file = open(options.wordsfile)
    alllines = words_file.read()
    words = alllines[:-1].replace("\n","|")

    if os.path.isfile(options.inputfile):
        validate_file(options.inputfile)

    if(os.path.isdir(options.inputfile)):
        for root, dirs, files in os.walk(options.inputfile, topdown=False):
            for name in files:
                file_to_validate=os.path.join(root, name)
                if(file_to_validate.endswith(".md")):
                    validate_file(os.path.join(root, name))  
            #   print(os.path.join(root, name))
            #for name in dirs:
            #   print(os.path.join(root, name)) 
      
if __name__ == "__main__":
    main() 
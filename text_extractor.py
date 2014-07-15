"""
  Author       : Alexander B. Falgui (alexbfalgui.github.io)
  Program Name : Text Extractor
  Description  : Takes an integer or string as an input and generates a
  text file with the extracted data. 
      
  Note: This program can be used, shared, modified by anyone.
"""
def __init__():    
    # MAIN MENU SCREEN
    with open('menu') as mf: print mf.read()
        
    while (True):
        try:
            menu_input = input("CHOOSE AN OPTION> ")
            if (menu_input == 1):
                try:
                    program_name = raw_input("\nNAME OF THE PROGRAM: ")
                    program_name = open(program_name)

                    print "\nCONTENTS OF FILE:\n"
                    line_number = 1
                    contents = []       
                    for line in program_name:
                        print "  %d: %s" % (line_number, line),
                        contents.append(line)
                        line_number += 1
                   
                    start_line = raw_input("\nSTART LINE: ")
                    end_line = raw_input("END LINE: ")
                    
                    start_line = int(start_line)
                    end_line = int(end_line)
                    
                    open("results", "w") # RESET RESULTS
                    with open("results", "a") as results:
                        if (start_line <= end_line):
                            while (start_line <= end_line):
                                text = contents[start_line-1]
                                results.write(text)
                                start_line += 1
                        else:
                            while (start_line >= end_line):
                                text = contents[start_line-1]
                                results.write(text)
                                start_line -= 1
                        
                    print "\nRESULTS HAVE BEEN GENERATED." + ("\n"*10)
                    
                    __init__()
                    
                except IOError:
                    if (len(program_name) == 0):
                        print "THE LENGTH OF THE NAME SHOULD NOT BE LESS THAN 1",
                        print "! [LEN_ERROR]\n"
                    else: print "%s does not exist" % program_name
                  
                except ValueError:
                    if (type(start_line) != int and type(end_line) == int):
                        print "START LINE MUST BE AN INTEGER! [INT_ERROR]"
                    elif (type(start_line) == int and type(end_line) != int):
                        print "END LINE MUST BE AN INTEGER! [INT_ERROR]"
                    else:
                        print "START LINE AND END LINE MUST BE AN INTEGER!",
                        print " [INT_ERROR]"
            elif (menu_input == 0): break
    
        except NameError as e:
            print e
            print "SOMETHING'S WRONG WITH YOUR INPUT. [INP_ERROR]\n"
        
if __name__ == "__main__": __init__()

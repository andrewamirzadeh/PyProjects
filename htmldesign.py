#Author Name: Bijan Amirzadehasl
#Date: 10/1/2021
#Program Name: Week6_Bijan_Amirzadehasl.py
#Purpose: Prompt user to enter their name and then a description then append it to an Html document

def main():
        #prompt user for information
        name = input('Enter your name: ')
        sentence = input('Describe yourself: ')

        #open file name and set to write
        #w+ checks to see if file has been created yet and creates a new one if not
        file_name = open('crash.html.html', 'w+')

        #series of write statements to form an html body
        file_name.write('<html>\n')
        file_name.write('<head>\n')
        file_name.write('</head>\n')
        file_name.write('<body>\n')
        file_name.write('<center>\n')
        file_name.write('<h1>' + name + '</h1>\n')
        file_name.write('</center>\n')
        file_name.write('<hr />' + sentence + '<hr />\n')
        file_name.write('</body>\n')
        file_name.write('</html>\n')


        #close the file
        file_name.close()

#call main
main()









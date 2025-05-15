#Importing the necessary module and function
from PyPDF2 import PdfMerger

# Create an instance of PdfMerger
joiner = PdfMerger()

#Asking for no. of files so that the system can work accordingly, while handling error
while True:
    try:
        no_of_files = int(input("Enter no. of files you want to merge : "))
        break
    except:
        print("Kindly enter a number")

#Compiling the files 
# Also handling the error in such a way that if one is entered properly then it shouldn't be written again and only wrong file name should be etered again
for x in range(no_of_files):
    while True:
        try:
            file_to_be_merged = input('Enter the file name : ')
            joiner.append(file_to_be_merged)
            break

        except:
            #Giving instructions to user for any error
            print("Kindly enter either the correct name or correct path of the file and kindly attach .pdf at the end")
            print("If you're writing the name then check wether the file in same folder of the merger or not")
    
name_of_the_merged_pdf = input("What should be the name of merged pdf : ")
# Write the merged PDF to a new file
joiner.write(name_of_the_merged_pdf)

# Close the merger
joiner.close()
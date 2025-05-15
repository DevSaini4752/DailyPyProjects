#Morse code rules
#Use single space ( ) between letters
#Use triple space (   ) betweem letters

#importing sys for stopping program when asked
import sys
 
#Creating dictioniory for every letter (for encoding)

morse_code_dict = {
    'A': '.-',  
    'B': '-...',  
    'C': '-.-.',  
    'D': '-..',  
    'E': '.',  
    'F': '..-.',  
    'G': '--.',  
    'H': '....',  
    'I': '..',  
    'J': '.---',  
    'K': '-.-',  
    'L': '.-..',  
    'M': '--',  
    'N': '-.',  
    'O': '---',  
    'P': '.--.',  
    'Q': '--.-',  
    'R': '.-.',  
    'S': '...',  
    'T': '-',  
    'U': '..-',  
    'V': '...-',  
    'W': '.--',  
    'X': '-..-',  
    'Y': '-.--',  
    'Z': '--..',  
    '0': '-----',  
    '1': '.----',  
    '2': '..---',  
    '3': '...--',  
    '4': '....-',  
    '5': '.....',  
    '6': '-....',  
    '7': '--...',  
    '8': '---..',  
    '9': '----.',  
    '.': '.-.-.-',  
    ',': '--..--',  
    '?': '..--..',  
    "'": '.----.',  
    '!': '-.-.--',  
    '/': '-..-.',  
    '(': '-.--.',  
    ')': '-.--.-',  
    '&': '.-...',  
    ':': '---...',  
    ';': '-.-.-.',  
    '=': '-...-',  
    '+': '.-.-.',  
    '-': '-....-',  
    '_': '..--.-',  
    '"': '.-..-.',  
    '$': '...-..-',  
    '@': '.--.-.',  
    ' ': '   '  # Three spaces for word separation
}    

#Dictionary for decoding

reverse_morse_dict = {
    '.-': 'A',  
    '-...': 'B',  
    '-.-.': 'C',  
    '-..': 'D',  
    '.': 'E',  
    '..-.': 'F',  
    '--.': 'G',  
    '....': 'H',  
    '..': 'I',  
    '.---': 'J',  
    '-.-': 'K',  
    '.-..': 'L',  
    '--': 'M',  
    '-.': 'N',  
    '---': 'O',  
    '.--.': 'P',  
    '--.-': 'Q',  
    '.-.': 'R',  
    '...': 'S',  
    '-': 'T',  
    '..-': 'U',  
    '...-': 'V',  
    '.--': 'W',  
    '-..-': 'X',  
    '-.--': 'Y',  
    '--..': 'Z',  
    '-----': '0',  
    '.----': '1',  
    '..---': '2',  
    '...--': '3',  
    '....-': '4',  
    '.....': '5',  
    '-....': '6',  
    '--...': '7',  
    '---..': '8',  
    '----.': '9',  
    '.-.-.-': '.',  
    '--..--': ',',  
    '..--..': '?',  
    '.----.': "'",  
    '-.-.--': '!',  
    '-..-.': '/',  
    '-.--.': '(',  
    '-.--.-': ')',  
    '.-...': '&',  
    '---...': ':',  
    '-.-.-.': ';',  
    '-...-': '=',  
    '.-.-.': '+',  
    '-....-': '-',  
    '..--.-': '_',  
    '.-..-.': '"',  
    '...-..-': '$',  
    '.--.-.': '@',  
    '   ': ' '  # Three spaces mapped to space
}



#Function for encoding

def encoder(message):
    updated_message = list(message)
    for x in range(len(updated_message)):
        if updated_message[x] == ' ':
            updated_message[x] = '   '
            
        else:
            updated_message[x] = morse_code_dict[updated_message[x]]
    finalm =  ' '.join(updated_message)
    print(finalm)

#Function for decoding 
def decoder(message):
    words = message.split("   ")  # Split words by triple spaces
    decoded_message = []
    
    for word in words:
        letters = word.split(" ")  # Split Morse letters by single space
        decoded_word = ''.join(reverse_morse_dict.get(letter, '?') for letter in letters)
        decoded_message.append(decoded_word)

    final_message = ' '.join(decoded_message)  # Join words with a single space
    print(final_message)
        
#Asking for input of code, and other work


while True:
    request = (input("Kindly enter the message that you want to encode/decode : ")).upper()
    
    en_or_de = input('''So what do you want to do with this code ?
    a. Encode
    b. Decode 
    c. End program
    Choose the option (a/b/c) : ''')
    
    while True:
        try:    
            if en_or_de == 'a' :
                encoder(request) 
                break
            elif en_or_de == 'b' :
                decoder(request)
                break
            elif en_or_de == 'c':
                print("Thank you for using me :~)")
                sys.exit()
            else:
                raise ValueError("An error occurred")
        except Exception as x:
            print(f"The error is : {x}")
            print("Kindly enter the valid input \n")
            break
                        
    
    
    
    
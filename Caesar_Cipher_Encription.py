
# Define a function to input your code

def Encrypt_Decrypt():
    
    #Execute the try and except statement to catch expected errors
    try:
        #Request for a user input
        Input=input("Enter 'e' to encrypt or 'd' to decrypt")
        
        # this if block is executed if the encryption condition is met
        if Input=='e':
            key=''
            result=''
            message=input("Enter a message to encrypt")
            key=int(input("Enter a key (0 to 25)"))
            
            # raise an exception if key isn't within the requested range
            if key>25 or key<0:
                raise Exception

            # Iterate over the message to encrypt, get their indexes, shift with the key and add the output to the result variable
            for i in range(len(message)):
                if message[i]==' ':
                    result+=message[i]
                letter=message[i]
                if letter.isupper():
                    result += chr((ord(letter) + key-65) % 26 + 65)
                else:
                    result += chr((ord(letter) + key - 97) % 26 + 97)
            print("Plain message:",message)
            print("Enrypted message:",result)

        #this block is executed if the decryption condition is met
        #Two main methods used (specify key or use brute force technique)
        elif Input=='d':
            Input=input("Enter 'k' to specify key or 'b' to use brute force")
            
            #block executed if user knows the specific key to decrypt the message
            if Input=='k':
                
                translated=''
                message=input('Enter a message to decrypt')
                Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                message=message.upper()
                key=int(input("Enter key (0 to 25)"))
                
                #raise an exception if key isn't within the requested range
                if key>25 or key<0:
                    raise Exception

                #iterate over the message and verify the presence of each letter in the alphabet
                #get the index of each letter in the 'Letters' variable, shift each letter with the key and add the output to the translated variable
                for i in message:
                    if i == ' ':
                        translated+=i
                    elif i in Letters:
                        ch=Letters.find(i)
                        new_num=ch-key
                        if new_num<0:
                            new_num+=len(Letters)
                            translated+=Letters[new_num]
                        else:
                            translated+=Letters[new_num]
                print("Plain message:",message)
                print("Decrypted message:",translated)
            
            #this code block is executed if user doesn't know the specific key to decrypt the message
            elif Input=='b':

                message = input('Enter message to decrypt')
                Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                message=message.upper()

                #Every key from 0-26 is used to iterate over the message for the presence of each letter in the 'Letters' variable
                for key in range(len(Letters)):
                    translated = ''
                    for ch in message:
                        if ch in Letters:
                            num = Letters.find(ch)
                            num = num - key
                            if num < 0:
                                num = num + len(Letters)
                            translated = translated + Letters[num]
                        else:
                            translated = translated + ch
                    print(f'Hacking key is {key}',translated)

            else:
                raise Exception
        else:
            raise Exception
    except:
        print('An error occured')
        print('Execute the program again and follow the instructions carefully')
    

Encrypt_Decrypt()
    

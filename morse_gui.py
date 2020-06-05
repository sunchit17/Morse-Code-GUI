from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Morse Code Translator')
root.geometry("420x420")
root.resizable(False,False)

# dictionary to look up for appropriate morse code for each letter
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

background_image = ImageTk.PhotoImage(Image.open("bg.jpg"))
background_label = Label(image=background_image,height=400,width=400)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

credits_label = Label(text="Python Project Final(17CS661) by Batch-14 Sixth Semester", font=("Helvetica",12))
credits_label.place(relx=1.0, rely=1.0, anchor='se')

def encrypt():
    message = english_entry.get().upper()
    english_entry.delete(0,END)
    morse_entry.delete(0,END)

    cipher = ''
    for letter in message:
        if letter != ' ':
            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    morse_entry.insert(0,cipher)

def decrypt():
    coded_message = morse_entry.get()
    coded_message += ' '
    morse_entry.delete(0,END)
    english_entry.delete(0,END)

    decipher = ''
    citext = ''
    for letter in coded_message:
        # checks for space
        if (letter != ' '):
            # counter to keep track of space
            i = 0
            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
            # if i = 2 that indicates a new word
            if i == 2 :
                 # adding space to separate words
                decipher += ' '
            else:
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''

    english_entry.insert(0,decipher[0:len(decipher)-1])


english_entry = Entry(root,width=30,font=("Helvetica",14))
english_entry.grid(row=0,column=1,padx=20,pady=(20,0))

english_label = Label(root,text="Enter Text in English:")
english_label.grid(row=0,column=0,padx=5,pady=(20,0))

encrypt_btn = Button(root,text="Convert to Morse Code",bg="white",fg="black",command=encrypt)
encrypt_btn.grid(row=1,column=1,pady=(8,0))

morse_entry = Entry(root,width=30,font=("Helvetica",14))
morse_entry.grid(row=5,column=1,padx=20,pady=(20,0))

morse_label = Label(root,text="Enter Text in Morse:")
morse_label.grid(row=5,column=0,padx=5,pady=(20,0))

decrypt_btn = Button(root,text="Convert back to English",bg="white",fg="black",command=decrypt)
decrypt_btn.grid(row=6,column=1,pady=(8,0))

root.mainloop()

import pyperclip
import time

list = []  # we create a list which will store the clipboard content

while True: # infifnite loop to continously check the  clipboard
    
    if pyperclip.paste() != 'None':    # if the clipboard content is not empty ...
        value = pyperclip.paste()      # then we will take its value and put it into variable called value
        print(value) # to see whats present on the clipboard
        #print pyperclip.paste()


        if value not in list:    #now to make sure that we don't get replicated items in our list before appending the value varaible into our list
                                 #we gonna check if the value is stored eariler in the first place, if not then this menas this is a new item
                                 #and we will append it to our list
            
            list.append(value)
        print (list)
        
        time.sleep(3)

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open('./input/Letters/starting_letter.txt', mode='r') as starting_letter:
    letter = starting_letter.read()

with open('./input/Names/invited_names.txt',mode='r') as invited_names:
    # You can also use readlines() function as well.
    for file in invited_names: # This will create a line blank line and hence strip() function is used
        data = letter.replace('[name]',file.strip())
        with open(f'./Output/ReadyToSend/letter_for_{file.strip()}.txt',mode='w') as starting_letter:
            starting_letter.write(data)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
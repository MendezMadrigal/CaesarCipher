

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
newAlphabet = []
holder = []
counter = 27
key = 0
correctKey = False
weAsk = True
encryptMessage = ""
decryptMessage = ""
optionSelected = ""


#Select your option
while weAsk == True:
    print("-------------------------------")
    print("[1] Encrypt")
    print("[2] Decrypt")
    optionSelected = input("Choose an option: ")
    if optionSelected == "1" or optionSelected == "2":
        weAsk = False


#We ask for the message and put all in upper letter.
message = input("Enter the message you want to encrypt: " )
message = message.upper()


#We ask for a key and verify that it can be use it.
while correctKey == False:
    key = input("Enter your key (1-26): ")
    try:
        key = int(key)
    except:
        print("Please enter a number between 1 and 26.")

    if key > 0 and key < 27:
        correctKey = True


def encryption():
    # In the next two fors, we create the new alphabet in base of the key the user gived to us.
    global encryptMessage
    for i in range(counter - key):
        newAlphabet.append(alphabet[i + key])

    for i in range(key):
        newAlphabet.append(alphabet[i])

    # In this section, we encrypt the message
    for i in range(len(message)):
        if message[i] == " ":
            encryptMessage = encryptMessage + " "
        else:
            for j in range(counter):
                if message[i] == alphabet[j]:
                    encryptMessage = encryptMessage + newAlphabet[j]

    print(encryptMessage)

def decryption():
    # In the next two fors, we create the new alphabet in base of the key the user gived to us.
    global decryptMessage
    for i in range(counter - key):
        newAlphabet.append(alphabet[i + key])

    for i in range(key):
        newAlphabet.append(alphabet[i])

    # In this section, we encrypt the message
    for i in range(len(message)):
        if message[i] == " ":
            decryptMessage = decryptMessage + " "
        else:
            for j in range(counter):
                if message[i] == newAlphabet[j]:
                    decryptMessage = decryptMessage + alphabet[j]

    print(decryptMessage)


if optionSelected == "1":
    encryption()
else:
    decryption()
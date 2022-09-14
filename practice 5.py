#Task_1
print('Task 1')
string = "Сегодня прекрасный день: cолнце светит, птички поют. Ля-ля-ля."
counter1 = 0
for i in range(0, len(string)):
    if string[i] == "е":
        counter1+=1
print(string, '\nThe frequency of the russian letter "e": ', str(counter1))

#Task_2
print('\nTask 2')
counter2 = 0
print("Create a program, that will replace all : with % and count the replacements.\nThe text is: \n", string)
for c in string:
    if c!=":": continue
    if c==":":
        string2 = string.replace(c, "%")
        counter2+=1
print('Replaced ":" with "%":', "\n", string2)
print('The number of replacings: ', counter2)

#Task_3
print("\nTask 3")
counter3 = 0
for c in string:
    if c!=".":
        continue
    if c==".":
        string3 = string.replace(".", "")
        counter3+=1
print("Result: \n", string3, "\nThe number of deleted characters: ", counter3)
        
#Task_4
print("\nTask 4")
counter4 = 0
for c in string:
    if c!="а":
        continue
    if c=="а":
        string4 = string.replace("а", "о")
        counter4+=1
print("The number of replacements: ", counter4)
print("Result: ", string4)
        
#Task_5
print("\nTask 5")
lc = string.lower()
print("Changed uppercase to lowercase:\n", lc)

#Task_6
print("\nTask 6")
counter6 = 0
for c in string:
    if c!="а":
        continue
    if c=="а":
        string6 = string.replace("а", "")
        counter6+=1
print("The number of characters removed: ", counter6)
print("Result: ", string6)

#Task_7
print("\nTask 7")
string7 = "Nancy wants to live a long time. She wants to live for one hundred years. She is five years old now. She wants to live 95 more years. Then she will be 100. Her father is 30 years old. He wants to live a long time, too. He wants to live for one hundred years. He wants to live for 70 more years."
l = len(string7)
string7_1 = string7[:l//2].replace("n", "*")+string7[l//2:]
print(string7_1)

#Task_8
print("\nTask 8")
counter8 = 1
string8 = "Nancy wants to live a long time."
for chr in string8:
    if chr==" ":
        counter8+=1
print("The number of words is: ", counter8)
        

#Task_9
print("\nTask 9")
string9 = "Mendy is doing practice work. Mendy is good student."
count = string9.count('Mendy')
print("The string is: ", string9)
print("How namy times word 'Mendy' appears: ", count)

#Task_10
print("\nTask 10")
string10 = "There are four seasons: winter, spring, summer and autumn. John's favourite is winter."
print(string10.title())

#Task_11
print("\nTask 11")
counter11=0
string11 = "There was a big announcement made on this event!"
string11_1 = string11.replace("!", ".")
for chr in string11:        
    if chr=="n" or chr=="N":
        counter11+=1
    else: continue
letter = "n"
res = len([el for el in string11.split() if letter in el])
print("String:\n", string11)
print("Changed ! to . :\n", string11_1)
print("The sequence with the biggest amount of n letters in it: ", str(res))

#Task_12
print("\nTask 12")
string12 = "There was a big announcement made on this event!"
print("Given string: \n", string12)
print("Output all words ending with i: ")
string12_1 = string12.split()
for c in range(0, len(string12_1)):
    if string12_1[c].endswith("i" or "I"):
        print(string12_1[c], end=" ")
    else: pass

#Task_13
print("\nTask 13")
symbols = "`~!@#$%^&*()_-+={[}}|\:;'<>.?/"
symbols = symbols.replace("(", "")
symbols = symbols.replace(")", "")
print("The string: ", symbols)
print("The result: ", "(", symbols, ")")

#Task_14
print("\nTask 14")
text = "1.There are many wild animals in Africa.\n2.My sister is the alumni of a popular uni."
text = text.replace(".", "")
for c in text.split():
    if c.startswith("a") or c.startswith("A"):
        print(c)
    if c.endswith("i"):
        print(c)

#Task_15
print("\nTask 15")
counter15=0
print("Number of occurences of 't': ", text.count("t"))






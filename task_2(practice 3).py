def season_events(m):
    print("You were born in: ")
    if m == 1:
        print("January. ")
    if m == 2:
        print("February. ")
    if m == 3:
        print("March")
    if m == 4:
        print("April")
    if m == 5:
        print("May")
    if m == 6:
        print("June")
    if m == 7:
        print("July")
    if m == 8:
        print("August")
    if m == 9:
        print("September")
    if m == 10:
        print("October")
    if m == 11:
        print("November")
    if m == 12:
        print("December")
    if (m > 12 or m < 1): print("Error! No such month!")

def season_description(m):
        if (m == 1 or m == 2 or m == 12):
            print("White snow fell outside the window.")
        if (m == 3 or m == 4 or m == 5):
            print("Birds sang beautiful songs.")
        if (m == 6 or m == 7 or m == 8):
            print("The sun shone brighter than ever!")
        if (m == 9 or m == 10 or m == 11):
            print("The harvest was incredible!")


month_num = int(input("Enter the number of the month you were born in: "))
season_events(month_num)
season_description(month_num)

        
        
    
    

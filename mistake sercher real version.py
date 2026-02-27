'''
START.
FIRST TAKE THE INPUT FROM THE USER OF 
WHAT MISTAKES DID YO DO??
WHATS THE DATE??---ASK MONTH,YEAR,DATE
TYPE IN THE NOTE
DISPLAY THE FINAL MESSAGE
I WANT TO SAVE EVERYHING PERMENNANTY AND ASK THE USER IF THEY WANT TO SEE IT?

'''
def mistake_searcher():
    # try:
    while True:
            mistakes = input("enter your mistakes for today: ")
            dash = ("--------")
            standing = ("||")
            slash = ("/")
            slash2 = ("//")
            dash1 = ("------------->>")
            mistake_answer = input(f"did you solve {mistakes}??(y/n): ")
            if mistake_answer == 'y':
                    mistake_solver = input("how did you solve it: ")
            else:
                print("TRY SOLVING IT TOMMAROW!!   ")
                break
            #print("TRY SOLVING IT TOMMAROW!!")
        
            date = input(f"enter the date: ")
        #     date = str()

            month = input("enter the month: ")
            year = input(f"enter the year: ")
        #     year = str()
            note = input("enter the notes or wisdom from today: ")

            print(f"today's mistake is {mistakes} its solution is {mistake_solver}")
            print(f"{date}/{month}/{year}-- {note}")

            with open("text.txt", "a") as v:
                    mistakes_save = v.write(mistakes)
                    dash11 = v.write(dash)
                    mistake_solver_save = v.write(mistake_solver)
                    standing1 = v.write(standing)
                    date_save = v.write(date)
                    slash1 = v.write(slash)
                    month_save = v.write(month)
                    slash_save = v.write(slash2)
                    year_save = v.write(year)
                    dash_save = v.write(dash1)
                    note_save = v.write(note)
                    ask = input("do you want to view everyting?(y/n): ").lower()
                    if ask == 'y':
                          print(mistakes,dash,mistake_solver,standing,date,slash,month,slash2,year,dash1,note)
                          break

mistake_searcher()







class Movie_Booking:
    def __init__(self):
        print("Welcome To Killer's Movie".center(100,"*"))
        print("Please Enter Size Of the Movie")
        self.rows = input("Enter Number of rows:  ")
        self.columns = input("Enter number of columns:  ")
        while self.rows.isdigit() == False or self.columns.isdigit() == False:
            print("Please Enter numbers only")
            self.rows = input(" Please Enter no_of rows:  ")
            self.columns = input("Please Enter no_of columns:  ")
        self.rows = int(self.rows)
        self.columns = int(self.columns)
        self.row = []
        for i in range(self.rows):
            self.seats = []
            for j in range(self.columns):
                self.seats.append("S")
            self.row.append(self.seats)
        self.details = {}
        self.total_tickets = 0
        for i in self.row:
            for j in i:
                self.total_tickets += 1
        self.current_income = 0
    def Show_seats(self):
        print(" screen is on this side ".center(100,"*"))
        print("SEATS:  ")
        for i in self.row:
            for j in i:
                print(j,end = " ")
            print()
            
    def Buy_ticket(self):
        print('Please select the Seat,  of enter the rows and columns of movie size')
        print(" BOOKING COUNTER ".center(100,"*"))
        print("Please choose/Select seats between {} Rows and {} Columns  !! only !!".format(self.rows,self.columns))
        self.r = input('select the row: ')
        self.c = input('select the column: ')
        while self.r == '0' or self.c == '0':
            print('Please select the row & seat from 1')
            self.r = input('Please select the row: ')
            self.c = input('Please select the column: ')
            while self.r.isdigit() == False or self.c.isdigit() == False:
                print('Please select the rows & seats in numbers!')
                self.r = input('Please select the row: ')
                self.c = input('Please select the column:')
                continue
            continue
        while self.r.isdigit() == False or self.c.isdigit()==False:
            print('Please select the row & seat in numbers!')
            self.r = input('Please select the row: ')
            self.c = input('Please select the column:')

            while self.r =='0' or self.c == '0':
                print('Please enter the row & seat from 1')
                self.r = input('Please select the row: ')
                self.c = input('Please select the column:')
                continue
            continue

        self.r = int(self.r)
        self.c =  int(self.c)
        while int(self.r)>self.rows or int(self.c)>self.columns:
            print("Please choose the seats whitin the range of",self.rows,self.columns)
            self.r = input('Please select the row: ')
            self.c = input('Please select the column:')
            continue
        if (self.r,self.c) in self.details:
            print('Seat has been booked already! Kindly choose another seat!')
        else:
            print('Please select the name in alphabets!')
            self.name = input('Please enter your name: ')
            while self.name.isalpha()==False:
                print('Please select the name in alphabets!')
                self.name = input('Please enter your name: ')
                continue

            self.age = input('Please enter your age: ')
            while self.age.isdigit() == False:
                print('Please select the age in numbers!')
                self.age = input('Please enter your age: ')
                continue
            self.age = int(self.age)
            self.gender = input("Please select your gender Female/Male/Other: ")
            while self.gender.casefold() not in ['male','female','other']:
                print('choose correct gender!')
                self.gender = input("Please select your gender Female/Male/Other: ")
                continue
            self.phone = input('Please enter your phone number') #cc
            while self.phone.isdigit()==False:
                print('Please choose the phone number in numbers only!')
                self.phone = input('Please enter your number: ')
                continue
            self.phone=int(self.phone)
            self.last = input('Confirm to book seats(Yes/No): ')
            while self.last.isalpha()==False:
                print('Please choose your options in alphabets only!')
                self.last = input('Confirm to book seat Yes/No: ')
                continue
            self.last = self.last.casefold()
            if self.last == 'yes':
                if self.total_tickets<=60:
                    self.opinion = input('Your ticket price is 10$, if you want to confirm type Yes/No: ')
                    while self.opinion.isalpha()==False:
                        print('Please choose your options in alphabets only!')
                        self.opinion = input('Your ticket price is 10$, if you want to confirm type Yes/No: ')
                        continue
                    self.opinion=self.opinion.casefold()
                    if self.opinion=='yes':
                        self.current_income=self.current_income+10
                        self.row[self.r-1][self.c-1]='B'
                        self.details[(self.r,self.c)]=[self.name.capitalize(),self.age,self.gender.capitalize(),self.phone]
                    else:
                        pass
                else:
                    if self.rows%2==0:
                        if self.r<(self.rows/2):
                            self.opinion = input('Your ticket price is 10$, if you want to confirm type Yes/No: ')
                            while self.opinion.isalpha()==False:
                                print('Please choose your options in alphabets only!')
                                self.opinion = input('Your ticket price is 10$, if you want to confirm type Yes/No: ')
                                continue
                            self.opinion = self.opinion.casefold()
                            if self.opinion == 'yes':
                                self.current_income = self.current_income+10
                                self.row[self.r-1][self.c-1]='B'
                                self.details[(self.r,self.c)]=[self.name.capitalize(),self.age,self.gender.capitalize(),self.phone]
                            else:
                                pass
                        else:
                            self.opinion = input('Your ticket price is 8$, if you want to confirm type Yes/No: ')
                            while self.opinion.isalpha()==False:
                                print('Please choose your options in alphabets only!')
                                self.opinion = input('Your ticket price is 8 $, if you want to confirm type Yes/No: ')
                                continue
                            self.opinion = self.opinion.casefold()
                            if self.opinion == 'yes':
                                self.current_income = self.current_income+8
                                self.row[self.r-1][self.c-1]='B'
                                self.details[(self.r,self.c)]=[self.name.capitalize(),self.age,self.gender.capitalize(),self.phone]
                            else:
                                pass
                    else:
                        if self.r<=((self.rows//2)):
                            self.opinion = input('Your ticket price is 10$, if you want to confirm type Yes/No: ')
                            while self.opinion.isalpha()==False:
                                print('Please choose your options in alphabets only!')
                                self.opinion = input('Your ticket price is 10$, if you want to confirm type Yes/No: ')
                                continue
                            self.opinion = self.opinion.casefold()
                            if self.opinion == 'yes':
                                self.current_income = self.current_income+10
                                self.row[self.r-1][self.c-1]='B'
                                self.details[(self.r,self.c)]=[self.name.capitalize(),self.age,self.gender.capitalize(),self.phone]
                            else:
                                pass
                        else:
                            self.opinion = input('Your ticket price is 8$, if you want to confirm type Yes/No: ')
                            while self.opinion.isalpha()==False:
                                print('Please choose your options in alphabets only!')
                                self.opinion = input('Your ticket price is 8 $, if you want to confirm type Yes/No: ')
                                continue
                            self.opinion = self.opinion.casefold()
                            if self.opinion == 'yes':
                                self.current_income = self.current_income+8
                                self.row[self.r-1][self.c-1]='B'
                                self.details[(self.r,self.c)]=[self.name.capitalize(),self.age,self.gender.capitalize(),self.phone]
                            else:
                                pass
                print("SCREEN IS THIS SIDE".center(100,"*"))
                for m in self.row:
                    for n in m:
                        print(n,end=' ')
                    print()
            elif self.last == 'no':
                pass

    def Statistics(self):
        print("It shows Income of the Booked tickets of Movie!!!!")
        self.total = 0
        for i in range(len(self.row)):
            j = self.row[i].count('B')
            self.total+=j
        print('Total number of seats booked are : ',self.total)
        self.percentage = (self.total/self.total_tickets)*100
        print('Booking percentage is : ',self.percentage)
        print('current income is :',self.current_income,'$')
        self.total_income=10
        if self.total_tickets<=60:
            self.total_income=self.total_tickets*10
        else:
            self.z = self.total_tickets//2
            self.y = self.total_tickets-self.z
            self.total_income=(self.z*10+self.y*8)
        print('Total income is:',self.total_income,'$')
    def Get_details(self):
        print("DETAILS OF CUSTOMER".center(100,"*"))
        try:
            self.rr=int(input('Please enter row number you want: '))
            self.ss=int(input('Please enter column number you want: '))
            self.u=(self.rr,self.ss)
            self.a=self.details[self.u]
            print('name:',self.a[0])
            print('age:',self.a[1])
            print('Gender:',self.a[2])
            print('Phone Number:',self.a[3])
            if self.total_tickets<=60:
                print('Ticket Price: 10$')
            else:
                if self.rr<=self.rows//2:
                    print('Ticket Price: 10$')
                elif self.rr<= self.rows/2:
                    print('Ticket price: 10 $')
                    
                else:
                    print('Ticket Price: 8$')
        except:
            print('We dont have that seat')
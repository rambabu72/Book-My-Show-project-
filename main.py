import movie
Book_movie = movie.Movie_Booking()
while True:
    print("SELECT WHAT DO YOU WANT IN NUMBERS ONLY".center(100,"*"))
    print("1. Show_seats")
    print("2. Buy_ticket")
    print("3. Statistics")
    print("4. Show the details of the user")
    print("0. Exit")
    
    choice = input("please select your choice from above!!")
    while  choice.isdigit() == False:
        print("please select your choice from above: ")
        choice = input("please select your choice from above!!")
        continue
        
    choice = int(choice)
    
    if choice == 0:
        print(" THANKYOU , VISIT AGAIN".center(100,"*"))
        break
    if choice == 1:
        Book_movie.Show_seats()
    elif choice == 2:
        Book_movie.Buy_ticket()
    elif choice == 3:
        Book_movie.Statistics()
    elif choice == 4:
        Book_movie.Get_details()
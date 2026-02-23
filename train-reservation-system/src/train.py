# Train Resevation.

class Train:

    @staticmethod
    def greet():
        print("************* Welcome To Eastern Railway **************")
        print("Two trains are available.\n1.Rajdhani Express.\n2.Duronto Express.")
        print("*******************************************************")

    def __init__(self, name, number, Total_Seats, fare):
        self.name = name
        self.number = number
        self.seats = Total_Seats
        self.fare = fare

    def seatCount(self,file_name):
        with open(f'data/{file_name}.txt', 'a+') as f:
            f.seek(0)
            SeatList = [int(line) for line in f.read().split()]
            emtSeat = self.seats - len(SeatList)
            print(f"Seat Available: {emtSeat}")
            print("************************************")
        
    def getInfo(self):
        print(f"Train is {self.name} (No.{self.number}).\nTotal Seats: {self.seats}.\nSeat Fare: Rs.{self. fare}")
        print("************************************")
    

    def bookSeats(self,file_name):
        reservation = input("Do you want to book seat / seats? (Y/N): ")

        if reservation.lower() == "y":
            quantity = int(input("How many seats do you want to book? "))
            
            with open(f'data/{file_name}.txt', 'a+') as f:
                f.seek(0)
                SeatList = [int(line) for line in f.read().split()]
                emtSeat = self.seats - len(SeatList)
                
                if self.seats < quantity or quantity <= 0:
                    print("Invalid seat quantity!")
                    print("************************************")
                    return
                
                elif emtSeat < quantity:
                    print("Sorry, the train is full! Kindly try in Tatkal.")
                    print("************************************")
                    return
                
                else:
                    booked_seats = []
                    for seat in range(1,self.seats+1):

                        if seat not in SeatList and seat not in booked_seats:
                            
                            booked_seats.append(seat)
                            f.write(f"\n{seat}")
                            
                            if len(booked_seats) == quantity:
                                break
                        
                print(f"Your {len(booked_seats)} seat(s) is/are booked\nYour total fare: Rs.{self.fare * len(booked_seats)}")
                print("Your seat numbers are:", " ".join(map(str, booked_seats)))
                print("************************************")
        
        elif reservation.lower() == "n":
            pass
        
        else:
            print("You have entered a wrong input.")
            print("************************************")
            return

    def cancelSeats(self,file_name):

        cancelled_count = 0
        cancellation = input("Do you want to cancel seat / seats? (Y/N): ")

        if cancellation.lower() == "y":
            quantity = int(input("How many seats do you want to cancel? ")) 
            
            if self.seats < quantity or quantity <= 0:
                print("Invalid seat quantity!")
                print("************************************")
                return
            else:
                with open(f'data/{file_name}.txt', 'a+') as f:
                    f.seek(0)
                    SeatList = [int(line) for line in f.read().split()]
                    for _ in range(quantity):
                        seat_to_cancel = int(input("Write seat number: "))
                        if seat_to_cancel in SeatList:
                            SeatList.remove(seat_to_cancel)
                            print(f"Your seat No.{seat_to_cancel} is successfully cancelled.")
                            cancelled_count += 1
                        else:
                            print(f"Your seat No.{seat_to_cancel} wasn't booked or doesn't exist.")

                    f.seek(0)
                    f.truncate()
                    f.write("\n".join(map(str, SeatList)))
                    
                    print(f"Your {quantity} seat(s) is/are canceled.\nYour total refund: Rs.{self.fare * cancelled_count}.")
                    print("************************************")
        
        elif cancellation.lower() == "n":
            pass
        
        else:
            print("You have entered a wrong input.")

        return
    
    @staticmethod
    def farewell():
        print("*******************************************************")
        print("***** Thank You For your visit To Eastern Railway *****")
        print("*******************************************************")


Rajdhani =  Train("Rajdhani Express", 10472, 10, 1000)
Duronto =  Train("Duronto Express" , 10437 , 20, 850)

Train.greet()
Train.getInfo(Rajdhani)
Train.getInfo(Duronto)

print("Which train do you want to book or cancel?" 
        "\n1. Press '1' for 'Rajdhani Express'."
        "\n2. Press '2' for 'Duronto Express'."
        "\n3. Press '0' to 'Exit'.")
option = input("Press: ")
print("************************************")

if option == "1":

    Total_Seats = 10    
    Rajdhani.seatCount("Rajdhani")
    Rajdhani.bookSeats("Rajdhani")
    Rajdhani.cancelSeats("Rajdhani")
    Rajdhani.getInfo()

elif option == "2":

    Total_Seats = 20
    Duronto.seatCount("Duronto")
    Duronto.bookSeats("Duronto")
    Duronto.cancelSeats("Duronto")
    Duronto.getInfo()

elif option == "0":
    pass

else:
    print("You have entered a wrong input")

Train.farewell()

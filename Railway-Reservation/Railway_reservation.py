class RailwayReservation:
    def __init__(self, train_number, train_name, total_seats):
        self.train_number = train_number
        self.train_name = train_name
        self.total_seats = total_seats

        # Initially, all seats are available
        self.seats = {
            seat_number: None
            for seat_number in range(1, total_seats + 1)
        }

        self.reservation_counter = 1000

    # -------------------------------
    # 1. Check Seat Availability
    # -------------------------------
    def check_availability(self):
        available_seats = sum(
            1 for passenger in self.seats.values()
            if passenger is None
        )

        print("\n--- Seat Availability ---")
        print(f"Train Number : {self.train_number}")
        print(f"Train Name   : {self.train_name}")
        print(f"Total Seats  : {self.total_seats}")
        print(f"Available    : {available_seats}")

        return available_seats

    # -------------------------------
    # 2. Reserve a Seat
    # -------------------------------
    def reserve_seat(self, passenger_name):

        # Check availability first
        available_seats = self.check_availability()

        if available_seats == 0:
            print("\nSorry! No seats are available.")
            return None

        # Find the first available seat
        for seat_number, passenger in self.seats.items():

            if passenger is None:

                # Reserve the seat
                self.seats[seat_number] = passenger_name

                # Generate reservation ID
                self.reservation_counter += 1
                reservation_id = f"R{self.reservation_counter}"

                print("\n--- Reservation Successful ---")
                print(f"Reservation ID : {reservation_id}")
                print(f"Passenger      : {passenger_name}")
                print(f"Train Number   : {self.train_number}")
                print(f"Seat Number    : {seat_number}")

                # Immediately show updated availability
                updated_available = self.check_availability()

                print(f"Updated Available Seats: {updated_available}")

                return reservation_id

    # -------------------------------
    # 3. Display All Seats
    # -------------------------------
    def display_seats(self):
        print("\n--- Seat Status ---")

        for seat_number, passenger in self.seats.items():

            if passenger is None:
                print(f"Seat {seat_number}: Available")
            else:
                print(
                    f"Seat {seat_number}: Reserved by {passenger}"
                )


# -------------------------------------
# Create Railway Reservation System
# -------------------------------------

railway = RailwayReservation(
    train_number="12701",
    train_name="Godavari Express",
    total_seats=100
)


# -------------------------------------
# Main Program
# -------------------------------------

while True:

    print("\n==============================")
    print("   RAILWAY RESERVATION SYSTEM")
    print("==============================")

    print("1. Check Seat Availability")
    print("2. Reserve Seat")
    print("3. Display Seat Status")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        railway.check_availability()

    elif choice == "2":

        passenger_name = input("Enter passenger name: ")

        if passenger_name.strip() == "":
            print("Passenger name cannot be empty.")
        else:
            railway.reserve_seat(passenger_name)

    elif choice == "3":

        railway.display_seats()

    elif choice == "4":

        print("\nThank you for using the Railway Reservation System!")
        break

    else:

        print("\nInvalid choice. Please try again.")
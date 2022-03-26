user_input = ""
car_started = False

while True:

    user_input = input("> ").lower()

    if user_input == "help":
        print(
            """
start - to start the car
stop - to stop the cart
quit - to exit
        """
        )

    elif user_input == "start":
        if car_started:
            print("Car already started!")

        else:
            print("Car started ready to go!")
            car_started = True

    elif user_input == "stop":
        if not car_started:
            print("Car already stopped!")

        else:
            print("Car stopped!")
            car_started = False

    elif user_input == "quit":
        break

    else:
        print("I don't understand!")

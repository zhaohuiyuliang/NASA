import time
import motortest

motor = Motor()

if name == "main":
    try:
        while true:
            #Get command from user
            os.system ("clear")
            print ("W = forward")
            print ("Z = background")
            print ("A = left")
            print ("D = right")
            print ("S = stop")

            command = raw_input("Enter command(Q to quit)")

            if (command == "w"):
                moveForward()
                time.sleep(0.5)
                continue
            elif (command == "x"):
                
                continue
            elif (command == "a"):
                
                continue
            elif (command == "d"):
                
                continue
            elif (command == "s"):
                
                continue
            else:
                print("Enter Error")
                continue
            
            

    except (KeyboardInterrupt, SystemExit):
        GPIO.clearup()
                

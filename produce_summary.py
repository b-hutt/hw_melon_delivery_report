
#defining the function
def melon_delivery_report():
    """Will summarize daily delivery of total amount and quantity of each melon type delivered."""


    #these variables will increment each day/time the loop is ran
    day = 1
    date = 20140519
    file = ("um-deliveries-{}.txt".format(date))
  

    while True:

        if day < 4:

            #printing the day
            print("Day {}".format(day))

            #opening the file
            the_file = open(file)

            #sparcing out the variables line by line using |
            for line in the_file:
                line = line.rstrip()
                words = line.split('|')

                # assigning each index to a variable
                melon = words[0]
                count = words[1]
                amount = words[2]


                #printing each melon's delivery summary
                print("Delivered {} {}s for total of ${}".format(
                    count, melon, amount))

            #closing file    
            the_file.close()

    #incrementing the day and date so a new day and the corresponding file will pull    
    day += 1
    date += 1

#calling the function
melon_delivery_report()


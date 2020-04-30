

def melon_delivery_report():


    day = 1
    date = 20140519
    file = ("um-deliveries-{}.txt".format(date))
  
    while True:
        if day < 4:

            print("Day {}".format(day))
            the_file = open(file)
            for line in the_file:
                line = line.rstrip()
                words = line.split('|')

                melon = words[0]
                count = words[1]
                amount = words[2]

                print("Delivered {} {}s for total of ${}".format(
                    count, melon, amount))
            the_file.close()

        day += 1
        date += 1

melon_delivery_report()


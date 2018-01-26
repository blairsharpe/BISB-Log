from request import Request

if __name__ == "__main__":

    dict_seconds = {}

    # Create my bins with a dictionary
    for second in range(0, 3600):

        dict_seconds[second] = 0

    # Open the file
    with open('bisb.log', 'r') as log_file:

            for line in log_file:

                request_obj = Request(line)

                if request_obj.valid():

                    dict_seconds[request_obj.time()] += request_obj.bytes()

            for second, num_bytes in dict_seconds.items():

                print(second, num_bytes)







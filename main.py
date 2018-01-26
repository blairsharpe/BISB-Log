from request import Request

if __name__ == "__main__":

    dict_info = {}

    for second in range(0, 3600):

        dict_info.setdefault(second, [0, 0])

    with open('bisb.log', 'r') as log_file:

        first_line = log_file.readline()
        request_obj = Request(first_line)
        start_time = request_obj.time()
        expire_time = start_time + 120
        pin = request_obj.pin()

        for line in log_file:

            request_obj = Request(line)

            if request_obj.valid():

                # Add the bytes for that second
                dict_info[request_obj.time()][0] += request_obj.bytes()

                current_time = int(request_obj.time())

                if current_time > expire_time or pin != request_obj.pin():

                    if expire_time > 3599:
                        expire_time = 3600

                    for second in range(start_time, expire_time):
                        dict_info[second][1] += 1

                    # Update everything
                    pin = request_obj.pin()
                    start_time = current_time
                    expire_time = current_time + 120

                else:

                    expire_time = current_time + 120

        for second in dict_info:

            print("{}: {}, {}".format(second, dict_info[second][1], dict_info[
                second][0]))









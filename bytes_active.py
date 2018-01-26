from request import Request

if __name__ == "__main__":

    dict_seconds_active = {}

    dict_seconds_bytes = {}

    # Create my bins with a dictionary
    for second in range(0, 3600):

        dict_seconds_active[second] = 0

    # Create my bins with a dictionary
    for second in range(0, 3600):

        dict_seconds_bytes[second] = 0

    with open('bisb.log', 'r') as log_file:

        first_line = log_file.readline()
        request_obj = Request(first_line)
        start_time = request_obj.time()
        expire_time = start_time + 120
        pin = request_obj.pin()

        for line in log_file:

            request_obj = Request(line)

            if request_obj.valid():

                dict_seconds_bytes[request_obj.time()] += request_obj.bytes()

                current_time = int(request_obj.time())

                if current_time > expire_time or pin != request_obj.pin():

                    if expire_time > 3599:
                        expire_time = 3600

                    for second in range(start_time, expire_time):
                        dict_seconds_active[second] += 1

                    # Update everything
                    pin = request_obj.pin()
                    start_time = current_time
                    expire_time = current_time + 120

                else:

                    expire_time = current_time + 120

        for second in dict_seconds_active:
            print(second, dict_seconds_active[second], dict_seconds_bytes[
                second])
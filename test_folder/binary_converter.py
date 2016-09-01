

def binary_converter(number):
    collector = []
    done = False
    if number >= 0:
        if number <= 255:
            while number >= 0 and not done:
                rem = number % 2
                collector.insert(0, str(rem))
                number //= 2
                result = "".join(collector)
                if number == 0:
                    done = True
            return result
        else:
            return "Invalid input"
    else:
        return "Invalid input"


print(binary_converter(62))

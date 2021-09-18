import argparse

def GetPrimeNumbers(limiter=2):
    """
    This Function will return all prime numbers by range of limiter.
    the limiter must be between 2 - 100.
    :param limiter: integer between 2 - 100
    :return: list of prime numbers
    """
    primeNumList = []

    if limiter >=2 and limiter <= 100:
        for x in range(limiter):
            primeNumList.append(x)

    return primeNumList

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Get prime numbers for you limiter")
    parser.add_argument("-n", "--number",
                        default=2,
                        type=int,
                        dest="number",
                        help="Please insert number between 2 - 100")

    args = parser.parse_args()

    if args.number >= 2 and args.number <= 100:
        arrNum = GetPrimeNumbers(args.number)
        print(arrNum)
    else:
        parser.print_help()

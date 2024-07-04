import sys

if len(sys.argv) == 1:
    print("USAGE: python app.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)


# For the code above, run on the terminal the command bellow
# python app.py -1234


# Terminal test:
# with the code being just print(sys.argv)
# execute on the terminal: python app.py -a -b -c

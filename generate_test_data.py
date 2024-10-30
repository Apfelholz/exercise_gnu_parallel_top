import random
import argparse

# Command Line Argument Parser
parser = argparse.ArgumentParser(
<<<<<<< HEAD
    prog="generate_test_data",
    description="Generates n lines of sleep() statements within the specified rang"
)

parser.add_argument('-n', default= 100, type=int, help='Number of lines to generate')
parser.add_argument('-t', default= "0.5-5", help='Range for sleep times, formatted as lower-upper')
=======
    prog='generate_test_data',
    description='Generates a .txt file that contains n lines of sleep() statements within the specified range'
)

parser.add_argument('-n', type=int, default=100, help='Number of lines to generate')
parser.add_argument('-t', default='0.5-5', help='Range for sleep times, formatted as lower-upper')
>>>>>>> 0464d1bf823b3ca106cbc6251ffb43b155f61388

# Initialisieren der Grenzen und Argumente
args = parser.parse_args()

<<<<<<< HEAD
lower_bound, upper_bound = map(float, args.t.split('-'))
lines = args.n 

# Test erstellen
for i in range(lines):
    print("sleep " + str(round(random.uniform(lower_bound, upper_bound), 2)))
=======
if args.t is None:
    lower_bound = 0.2
    upper_bound = 0.5
else:
    lower_bound, upper_bound = map(float, args.t.split('-'))

lines = args.n if args.n is not None else 100

# Datei erstellen oder überschreiben
with open("test_sleep.txt", "w") as datei:
    for i in range(lines):
        datei.write("sleep " + str(round(random.uniform(lower_bound, upper_bound), 2)) + "\n")
>>>>>>> 0464d1bf823b3ca106cbc6251ffb43b155f61388

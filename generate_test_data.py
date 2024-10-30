import random
import argparse

# Command Line Argument Parser
parser = argparse.ArgumentParser(
    prog='generate_test_data',
    description='Generates a .txt file that contains n lines of sleep() statements within the specified range'
)

parser.add_argument('-n', type=int, default=100, help='Number of lines to generate')
parser.add_argument('-t', default='0.5-5', help='Range for sleep times, formatted as lower-upper')

# Initialisieren der Grenzen und Argumente
args = parser.parse_args()

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
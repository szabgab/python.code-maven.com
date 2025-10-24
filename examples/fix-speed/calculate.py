import sys

def run(X, Y):
    total = 0
    for x in range(X):
        for y in range(Y):
            width, height = read_config()
            total += x*width + y*height
    print(total)

def read_config():
    import csv
    with open('config.csv', newline='') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            return int(row['width']), int(row['height'])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        exit("Usage: {sys.argv[0]} X Y")
    X = int(sys.argv[1])
    Y = int(sys.argv[2])
    run(X, Y)

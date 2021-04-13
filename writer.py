def print(n, iterations):
    with open("output.csv", "a") as csv_file:
        line = f"{iterations}"
        csv_file.write(line + "\n")

    


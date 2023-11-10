fname = input("Enter the name of the file: ")
count = 0
lst = []
with open(fname, "r") as f:
    lines = f.read().split('\n\n')
    for i in lines:
        if "pid" in i and "hgt" in i and "cid" in i and "iyr" in i and "byr" in i and "eyr" in i and "hcl" in i:
            count += 1  # tfw no switch cases
            lst += [i]
    # print(lst)
    with open("valid_passports.txt", "w") as n:
        for i in lst:
            n.write(i)
            n.write("\n\n")

print(f'There are {count} valid passports')

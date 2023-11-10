fname = input("Enter the name of the file: ")
count = 0
lst = []
chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
with open(fname, "r") as f:
    lines = f.read().split('\n\n')
    for i in lines:
        check = 0
        origin = i
        i = i.replace("\n", " ")
        # print(i)
        temp = i.split(" ")
        # print(temp)
        temp = [j.split(':', 1) for j in temp]
        # print(temp)
        for j in range(len(temp)):
            if "byr" in temp[j]:
                val = int(temp[j][1])
                if 1920 <= val <= 2007:
                    check += 1
            if "iyr" in temp[j]:
                val = int(temp[j][1])
                if 2013 <= val <= 2023:
                    check += 1
            if "eyr" in temp[j]:
                val = int(temp[j][1])
                if 2023 <= val <= 2033:
                    check += 1
            if "hgt" in temp[j]:
                val = temp[j][1]
                if "cm" in val:
                    if 150 <= int(val[0:3]) <= 193:
                        check += 1
                if "in" in val:
                    if 59 <= int(val[0:2]) <= 76:
                        check += 1
            if "hcl" in temp[j]:
                val = temp[j][1]
                counter = 0
                # print(val)
                if val[0] == "#":
                    # print(val[1:])
                    if len(val[1:]) == 6:
                        for k in val[1:]:
                            if k in chars:
                                counter += 1
                            else:
                                break
                        if counter == 6:
                            counter = 0
                            check += 1
            if "pid" in temp[j]:
                val = temp[j][1]
                if len(val) == 9:
                    check += 1
            if "cid" in temp[j]:
                val = temp[j][1]
                if len(val) == 3:
                    if val[0] != "0":
                        check += 1
            if check == 7:
                count += 1
                check = 0
                lst += [origin]

    # print(lst)
    with open("valid_passports2.txt", "w") as n:
        for i in lst:
            n.write(i)
            n.write("\n\n")

print(f'There are {count} valid passports')

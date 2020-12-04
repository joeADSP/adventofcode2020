import re

with open('data.txt', 'r') as f:
    data = f.read()

data = data.split('\n\n')

targets = ('byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:')

count = 0

correct = []

passports = set()

for item in data:
    allowed = True
    for target in targets:
        if target not in item:
            allowed = False
            break

    if allowed == False:
        continue

    byr = int(re.findall(r"byr:(\d*)", item)[0])
    if not (byr >= 1920 and byr <= 2002):
        continue

    iyr = int(re.findall(r"iyr:(\d*)", item)[0])
    if not (iyr >= 2010 and iyr <= 2020):
        continue

    eyr = int(re.findall(r"eyr:(\d*)", item)[0])
    if not (eyr >= 2020 and eyr <= 2030):
        continue

    try:
        hgt = int(re.findall(r"hgt:(\d*)cm", item)[0])
        unit = 'cm'
    except IndexError:
        try:
            hgt = int(re.findall(r"hgt:(\d*)in", item)[0])
            unit = 'in'     
        except IndexError:
            continue
    
    if unit == 'cm':
        if not (hgt >= 150 and hgt <= 193):
            continue
    if unit == 'in':
         if not (hgt >= 59 and hgt <= 76):
            continue 

    try:
        pid = re.findall(r"pid:([0-9]{9})$", item)[0]
    except IndexError:
        pid = None
    if not pid:
        continue

    try:
        hcl = re.findall(r"hcl:(#[a-f0-9]{6})$", item)[0]
    except IndexError:
        hcl = None
    if not hcl:
        continue 

    try:
        ecl = re.findall(r"ecl:([a-z]{3})$", item)[0]
    except IndexError:
        ecl = None
    if ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        continue
    
    correct.append(item)
    passports.add(pid)
    count += 1

print(count)
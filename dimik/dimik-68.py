from sys import stdin, stdout
bait = 0
fish = 0
fishcomcount = 0
baitcomcount = 0
comcount = 0
for command in stdin:
    command = command.strip()
    if command == "bait":
        comcount += 1
        if bait < 3:
            baitcomcount+= 1
            if baitcomcount == 2:
                bait += 1
                baitcomcount = 0
    elif command == "fish":
        if not fish and bait:
            bait -= 1
            fish += 1
        elif not bait or comcount < 6 or fishcomcount < 2:
            fishcomcount += 1
            comcount += 1
        else:
            bait -= 1
            fish += 1
            comcount = 0
            fishcomcount = 0
    elif command == "lunch":
        comcount += 1
stdout.write(str(fish)+'\n')

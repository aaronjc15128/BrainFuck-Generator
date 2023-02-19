def brainfuck(string, clearmemory):
    import math

    brainfuck_full = ""

    prev_ascii = 0

    for char in string:
        # find decimal
        decimal = ord(char) - prev_ascii

        # check decimal for =0, =1, =-1, <0, >0
        if decimal == 0:
            brainfuck_full += "."
            prev_ascii = ord(char)
            continue
        elif decimal == 1:
            brainfuck_full += "+."
            prev_ascii = ord(char)
            continue
        elif decimal == -1:
            brainfuck_full += "-."
            prev_ascii = ord(char)
            continue
        elif decimal < 0:
            decimal = abs(decimal)
            negativeBool = True
        elif decimal > 0:
            negativeBool = False

        # list factors
        factors = []
        for i in range(1, decimal + 1):
           if decimal % i == 0:
               factors.append(i)

        # check if prime
        if len(factors) == 2:
            if negativeBool:
                brainfuck = ""
                for _ in range(decimal):
                    brainfuck += "-"
                brainfuck += "."
                
                prev_ascii = ord(char)
                brainfuck_full += brainfuck
                continue
            else:
                brainfuck = ""
                for _ in range(decimal):
                    brainfuck += "+"
                brainfuck += "."

                prev_ascii = ord(char)
                brainfuck_full += brainfuck
                continue


        # check if square, find median(s)
        root = math.sqrt(decimal)
        if int(root + 0.5) ** 2 == decimal:
            nums = (factors[int((len(factors)/2)-0.5)], factors[int((len(factors)/2)-0.5)])
        else:
            nums = (factors[int(len(factors)/2)], factors[int((len(factors)/2)-1)])

        # generate brainfuck
        if negativeBool:
            brainfuck = f">"
            for _ in range(nums[0]):
                brainfuck += "-"
            brainfuck += "[<"
            for _ in range(nums[1]):
                brainfuck += "-"
            brainfuck += ">+]<."
        else:
            brainfuck = f">"
            for _ in range(nums[0]):
                brainfuck += "+"
            brainfuck += "[<"
            for _ in range(nums[1]):
                brainfuck += "+"
            brainfuck += ">-]<."
        
        
        prev_ascii = ord(char)
        
        brainfuck_full += brainfuck

    # clear memory
    if clearmemory:    
        # list factors
        factors = []
        for i in range(1, prev_ascii + 1):
           if prev_ascii % i == 0:
               factors.append(i)

        # check if prime
        if len(factors) == 2:
            brainfuck = ""
            for _ in range(decimal):
                brainfuck += "-"
            brainfuck += "."

            brainfuck_full += brainfuck

        # check if square, find median(s)
        root = math.sqrt(prev_ascii)
        if int(root + 0.5) ** 2 == prev_ascii:
            nums = (factors[int((len(factors)/2)-0.5)], factors[int((len(factors)/2)-0.5)])
        else:
            nums = (factors[int(len(factors)/2)], factors[int((len(factors)/2)-1)])
        
        # generate ascii
        brainfuck = f">"
        for _ in range(nums[0]):
            brainfuck += "-"
        brainfuck += "[<"
        for _ in range(nums[1]):
            brainfuck += "-"
        brainfuck += ">+]<."
        
        brainfuck_full += brainfuck

    return f"{brainfuck_full}\n\nCreated by Aaron Chauhan"
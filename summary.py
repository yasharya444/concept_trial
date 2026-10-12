with open('demolog.log','r') as file:
    for line in file:
        print(line.strip())
        if "error" in line:
            with open('error.log','a') as f:
                f.write(line)
        elif "info" in line:
            with open ('info.log','a') as f:
                f.write(line)        
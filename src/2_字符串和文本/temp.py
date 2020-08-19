with open('.\\temp.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        l = line.strip()
        with open(".\\{}.py".format(l), 'w', encoding='utf-8') as f2:
            f2.write('"""{}"""'.format(l))

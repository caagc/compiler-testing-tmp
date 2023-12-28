import os
print("[")
for i in range(1,11):
    configfile = "./config"+str(i)
    assert os.path.exists(configfile)
    config = []
    # open configfile
    with open(configfile, 'r') as f:
        line = f.readline()
        while line:
            line = line.strip().lstrip('[').lstrip('(').rstrip(']').rstrip(')')
            if line != "":
                line = line.split(',')
                tmp_list = {}
                if len(line) > 1:
                    line = line[1:]
                for idx, p in enumerate(line):
                    p = p.split('=')
                    val = float(p[1])
                    if val in tmp_list:
                        tmp_list[val].append(idx)
                    else:
                        tmp_list[val] = [idx]
                if len(tmp_list) == 1:
                    config.append(tmp_list.popitem()[0])
                else:
                    last = 0
                    tmp_config = [0] * len(line)
                    for val in sorted(tmp_list):
                        idxs = tmp_list[val]
                        for idx in idxs:
                            tmp_config[idx] = val - last
                        last = val

                    # concat config with tmp_config
                    config += tmp_config
            line = f.readline()
    print(config, end=",\n")
print("]")
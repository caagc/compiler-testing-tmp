# from sko.GA import RCGA
# import numpy as np
import os
import random
import time
from queue import PriorityQueue
import ast
default_config = [50,50,50,10,10,10,50,80,50,10,50,50,30,20,5,50,50,30,25,0,20,20,50,50,40,0,15,15,5,5,5,5,10,25,25,25,25,5,6,5,6,5,6,5,6,6,5,6,5,6,5,6,5,6,6,0,10,10,10,10,10,10,10,10,10,10,0,25,25,25,25]
extreme_config = [90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,40,0,15,15,5,5,5,5,10,25,25,25,25,5,6,5,6,5,6,5,6,6,5,6,5,6,5,6,5,6,6,0,10,10,10,10,10,10,10,10,10,10,0,25,25,25,25]
hicond_config = [
[50.0, 50.0, 56.0540511, 10.0, 10.0, 10.0, 50.0, 80.0, 50.0, 10.0, 50.0, 49.89045548, 30.0, 20.0, 5.0, 50.07385808, 50.0, 30.0, 25.0, 0.0, 20.0, 20.0, 50.0, 50.0, 40.27443278, 0.0, 14.766312110000001, 14.96132609, 4.987108700000007, 4.987108699999993, 5.06238553, 4.987108699999993, 9.974217390000007, 24.97588926, 25.00688784, 24.975889259999995, 25.041333640000005, 5.55507169, 5.533301509999999, 5.555071690000002, 5.53396562, 5.555071689999998, 5.562444020000001, 5.555071689999998, 5.570393330000002, 5.564065380000002, 5.547121819999994, 5.567128710000006, 5.555071689999998, 5.548086380000001, 5.579445879999994, 5.550438999999997, 5.570867370000002, 5.54231166000001, 5.555070869999994, 0.0, 9.96970384, 9.998133100000002, 9.998133099999997, 9.947796780000001, 10.075520269999998, 10.117705260000001, 9.914876520000007, 10.033452639999993, 9.977043309999999, 9.967635180000002, 0.0, 24.99500907, 25.0149728, 24.995009070000002, 24.99500906],
[68.51039325, 65.38338775, 50.0, 10.0, 8.87780472, 10.0, 50.0, 80.0, 50.0, 10.00655482, 50.0, 49.89045548, 30.0, 27.53185739, 5.00905036, 50.07385808, 50.0, 30.07129124, 25.0, 0.0, 19.96714445, 20.0, 50.0, 50.0, 40.30477293, 0.0, 14.777436100000003, 14.97259699, 4.990865659999997, 4.990865659999997, 4.990865660000011, 4.990865659999997, 9.981731339999996, 24.98363383, 24.98363383, 24.98363383000001, 25.049098509999993, 5.55537201, 5.55537201, 5.555372010000001, 5.53426481, 5.555372009999999, 5.562744739999999, 5.555372009999999, 5.570694490000001, 5.555372009999999, 5.555372009999999, 5.567429680000004, 5.555372009999999, 5.555372009999999, 5.555372009999999, 5.550739070000006, 5.555372009999999, 5.54261129999999, 5.562423800000005, 0.0, 9.96410344, 9.99251673, 9.992516729999998, 9.992516729999998, 9.992516730000006, 10.112021729999995, 9.992516729999998, 10.02781644000001, 9.971438799999987, 9.962035940000007, 0.0, 24.99500907, 25.0149728, 24.995009070000002, 24.99500906],
[50.0, 65.38338775, 56.0540511, 10.0, 10.0, 10.0, 50.0, 80.0, 50.0, 10.00655482, 50.0, 49.89045548, 30.0, 27.53185739, 5.00905036, 50.07385808, 50.0, 30.36445534, 25.0, 0.0, 19.96714445, 20.0, 50.0, 50.0, 40.42753962, 0.0, 14.822447570000001, 15.21598179, 4.503692839999999, 5.006067639999998, 5.006067639999998, 5.006067640000012, 10.012135259999994, 25.01591183, 25.04696009, 24.855666989999996, 25.081461090000005, 5.55607505, 5.53430093, 5.571136749999999, 5.534965170000003, 5.556075049999997, 5.563448699999999, 5.556075050000004, 5.571399460000002, 5.56507036, 5.548123739999994, 5.568134240000006, 5.556075049999997, 5.549088479999995, 5.556075050000004, 5.551441510000004, 5.556075050000004, 5.543312709999995, 5.563127649999998, 0.0, 9.96468798, 9.99310294, 9.99310294, 9.99310294, 10.07045118, 10.11261494, 9.909888249999995, 10.028404710000004, 9.972023759999999, 9.962620360000003, 0.0, 24.96504739, 25.024965339999998, 25.00499363000001, 25.004993639999995],
[68.51039325, 65.38338775, 56.0540511, 12.62096582, 8.87780472, 10.0, 50.0, 80.0, 50.0, 10.00655482, 50.0, 49.89045548, 30.0, 27.53185739, 5.00905036, 50.07385808, 50.0, 30.36445534, 25.0, 0.0, 19.96714445, 20.0, 50.0, 50.0, 40.42753962, 0.0, 14.822447570000001, 15.21598179, 4.503692839999999, 5.006067639999998, 5.006067639999998, 5.006067640000012, 10.012135259999994, 25.01591183, 25.04696009, 24.855666989999996, 25.081461090000005, 5.55607505, 5.53430093, 5.571136749999999, 5.534965170000003, 5.556075049999997, 5.563448699999999, 5.556075050000004, 5.571399460000002, 5.56507036, 5.548123739999994, 5.568134240000006, 5.556075049999997, 5.549088479999995, 5.556075050000004, 5.551441510000004, 5.556075050000004, 5.543312709999995, 5.563127649999998, 0.0, 9.96258795, 9.99099692, 9.99099692, 9.99099692, 10.068328860000001, 10.11048374, 9.907799760000003, 10.02629125, 9.99099692, 9.960520759999994, 0.0, 24.96504739, 25.024965339999998, 25.00499363000001, 25.004993639999995],
[50.0, 65.38338775, 50.0, 12.62096582, 8.87780472, 10.0, 50.0, 80.0, 50.0, 10.00655482, 50.0, 49.89045548, 30.0, 27.53185739, 5.00905036, 50.07385808, 50.0, 30.36445534, 25.0, 0.0, 20.0, 20.0, 50.0, 50.0, 40.27583946, 0.0, 14.76682786, 14.96184865, 4.987282879999995, 5.036951170000009, 4.987282879999995, 5.009401319999995, 9.974565780000006, 25.01591183, 25.04696009, 24.855666989999996, 25.081461090000005, 5.55433592, 5.53256863, 5.569392910000001, 5.533232649999999, 5.55433592, 5.561707269999999, 5.545539509999998, 5.5696555400000065, 5.563328419999998, 5.546387099999997, 5.566391340000003, 5.554335919999993, 5.554335920000014, 5.578706879999999, 5.549703839999992, 5.570129510000001, 5.541577579999995, 5.554335140000006, 0.0, 9.9784754, 10.01048814, 9.98468575, 10.006929680000002, 10.08438494, 10.006929679999999, 9.923599850000002, 10.042280300000002, 9.985821340000001, 9.976404919999993, 0.0, 24.96504739, 25.024965339999998, 25.00499363000001, 25.004993639999995],
[50.0, 50.0, 56.0540511, 12.62096582, 8.87780472, 10.0, 50.0, 80.0, 50.0, 10.00655482, 50.0, 49.89045548, 30.0, 27.53185739, 5.00905036, 50.07385808, 50.0, 30.36445534, 25.0, 0.0, 20.0, 20.0, 50.0, 50.0, 40.42753962, 0.0, 14.822447570000001, 15.21598179, 4.503692839999999, 5.006067639999998, 5.006067639999998, 5.006067640000012, 10.012135259999994, 25.01591183, 25.04696009, 24.855666989999996, 25.081461090000005, 5.55472088, 5.532952080000001, 5.569778909999998, 5.53361615, 5.554720880000001, 5.562092739999997, 5.554720880000005, 5.57004156, 5.563713999999997, 5.546771509999999, 5.566777139999999, 5.554720879999998, 5.547736020000002, 5.579093529999994, 5.550088480000014, 5.554720879999991, 5.541961659999998, 5.561771820000004, 0.0, 9.96258795, 9.99099692, 9.99099692, 9.99099692, 10.068328860000001, 10.11048374, 9.907799760000003, 10.02629125, 9.99099692, 9.960520759999994, 0.0, 24.96504739, 25.024965339999998, 25.00499363000001, 25.004993639999995],
[68.51039325, 50.0, 50.0, 12.62096582, 8.87780472, 10.0, 50.02058602, 79.96408289, 49.99551688, 10.00308283, 50.0, 50.0, 30.0, 27.53185739, 5.0, 50.0, 50.10025291, 30.0, 25.0, 0.0, 19.96714445, 20.0, 50.0, 50.0, 39.97928432, 0.0, 14.7968148, 15.189668480000009, 4.99741053999999, 5.047179690000007, 4.99741053999999, 4.997410540000004, 9.994821090000002, 25.02353343, 24.991007179999997, 24.960028280000003, 25.02543111, 5.54953045, 5.5582573, 5.573324920000001, 5.53713913, 5.515588619999999, 5.558257300000001, 5.558257300000001, 5.558257300000001, 5.558257299999994, 5.558257300000001, 5.558257300000001, 5.558257299999994, 5.551267990000014, 5.558257299999994, 5.558257299999994, 5.574062040000001, 5.558257300000008, 5.558256549999996, 0.0, 9.99962351, 10.003179380000002, 9.99962351, 9.94927968, 9.99962351, 10.1192135, 9.916354519999999, 10.034948319999998, 9.978530579999997, 9.999623490000005, 0.0, 24.96504669, 25.00499293, 25.02887148, 25.0010889],
[50.0, 65.38338775, 56.0540511, 10.0, 8.87780472, 10.0, 50.0, 79.96408289, 49.99551688, 10.00655482, 50.0, 49.89045548, 30.0, 20.0, 5.00905036, 50.07385808, 50.0, 30.36445534, 25.0, 0.0, 19.96714445, 20.0, 50.0, 50.0, 40.42753962, 0.0, 14.822447570000001, 15.21598179, 4.503692839999999, 5.006067639999998, 5.006067639999998, 5.006067640000012, 10.012135259999994, 25.01591183, 25.04696009, 24.855666989999996, 25.081461090000005, 5.55607505, 5.53430093, 5.571136749999999, 5.534965170000003, 5.556075049999997, 5.563448699999999, 5.556075050000004, 5.571399460000002, 5.56507036, 5.548123739999994, 5.568134240000006, 5.556075049999997, 5.549088479999995, 5.556075050000004, 5.551441510000004, 5.556075050000004, 5.543312709999995, 5.563127649999998, 0.0, 9.96258795, 9.99099692, 9.99099692, 9.99099692, 10.068328860000001, 10.11048374, 9.907799760000003, 10.02629125, 9.99099692, 9.960520759999994, 0.0, 24.96504739, 25.024965339999998, 25.00499363000001, 25.004993639999995],
[68.51039325, 65.38338775, 50.0, 10.0, 8.87780472, 10.0, 50.0, 80.0, 50.0, 10.00655482, 50.0, 49.89045548, 30.0, 20.0, 5.00905036, 50.07385808, 50.0, 30.36445534, 25.0, 0.0, 20.0, 20.0, 50.0, 50.0, 40.42753962, 0.0, 14.822447570000001, 15.21598179, 4.503692839999999, 5.006067639999998, 5.006067639999998, 5.006067640000012, 10.012135259999994, 25.01591183, 25.04696009, 24.855666989999996, 25.081461090000005, 5.55607505, 5.53430093, 5.571136749999999, 5.534965170000003, 5.556075049999997, 5.563448699999999, 5.556075050000004, 5.571399460000002, 5.56507036, 5.548123739999994, 5.568134240000006, 5.556075049999997, 5.549088479999995, 5.556075050000004, 5.551441510000004, 5.556075050000004, 5.543312709999995, 5.563127649999998, 0.0, 9.96468798, 9.99310294, 9.99310294, 9.99310294, 10.07045118, 10.11261494, 9.909888249999995, 10.028404710000004, 9.972023759999999, 9.962620360000003, 0.0, 24.96504739, 25.024965339999998, 25.00499363000001, 25.004993639999995],
[50.0, 65.38338775, 56.0540511, 10.0, 10.0, 10.0, 50.0, 80.0, 50.0, 10.0, 50.0, 49.89045548, 30.0, 20.0, 5.00905036, 50.07385808, 50.0, 30.36445534, 25.0, 0.0, 19.96714445, 20.0, 50.0, 50.0, 40.30477293, 0.0, 14.777436100000003, 14.97259699, 4.990865659999997, 4.990865659999997, 4.990865660000011, 4.990865659999997, 9.981731339999996, 25.06360684, 25.03102851, 24.83985708000001, 25.065507569999994, 5.55656398, 5.53478795, 5.571627000000001, 5.535452239999998, 5.55656398, 5.563938280000002, 5.547764039999997, 5.571889740000003, 5.565560079999997, 5.548611970000003, 5.5686242299999975, 5.556563980000007, 5.549576789999989, 5.556563980000007, 5.551930040000002, 5.556563979999993, 5.543800520000005, 5.563617219999998, 0.0, 9.96141031, 9.98981592, 9.989815920000002, 9.939521469999995, 10.067138720000003, 10.10928861, 9.989815919999998, 10.02510608, 9.968743680000003, 9.95934337, 0.0, 24.96504739, 25.024965339999998, 25.00499363000001, 25.004993639999995],
]
mxCloseSize = 10000
config_range = {
    "single" : [0, 23],
    "statement": [24, 32],
    "unary": [33, 36],
    "binary": [37, 54],
    "types": [55, 66],
    "safe": [67, 70],
}
config_format = []

VOID_ID = 55
Counter = 0

config_saving_path = "./config.txt"
default_config_path = "./default.txt"
csmith_feature_file = "./csmith_cnt.csv"
coverage_path = "./coverage.txt"
coverageLog_path = "./coverage_log.txt"
state_path = "./state.txt"
list_path = "./list.txt"

c_file_cnt_per_iter = 100
fromfile = False
def ConfigToRange(config):
    res = []
    for c in config:
        res.append(int(c / 10))
    return res

def RangeToConfig(ranges):
    res = []
    for r in ranges:
        res.append(int(r * 10) + random.randint(0, 9))
    res[VOID_ID] = 0
    for key in config_range:
        if key == "single":
            continue
        r = config_range[key]
        # calculate the sum of the range
        sum = 0
        for i in range(r[0], r[1] + 1):
            sum += res[i]
        # normalize the res[i] from r[0] to r[1]
        for i in range(r[0], r[1] + 1):
            res[i] = int(res[i] * 100 / sum)
    return res

class ConfigItem():
    def __init__(self, config, coverageScore=0):
        global Counter
        self.config = config
        self.crashes = 0
        self.wrongcodes = 0
        self.coverageScore = coverageScore
        self.timeScore = 0
        self.id = Counter
        self.range = ConfigToRange(config)
        self.lastmutation = {}
        self.father = None
        self.removetimes = 0
        Counter += 1
    def __repr__(self):
        return "{'config':%s,'coverageScore':%s}" % (self.config, self.coverageScore)
    def __lt__(self, other):
        if self.coverageScore == other.coverageScore and self.wrongcodes == other.wrongcodes:
            return self.crashes > other.crashes
        elif self.coverageScore == other.coverageScore:
            return self.wrongcodes > other.wrongcodes
        return self.coverageScore > other.coverageScore
    def updateBugScore(self, crashes, wrongcodes):
        if crashes == -1 and wrongcodes == -1:
            self.crashes = -1
            self.wrongcodes = -1
        self.crashes += crashes
        self.wrongcodes += wrongcodes
        print("updateBugScore: ", self.crashes, self.wrongcodes)
    def updateCoverageScore(self, score):
        self.coverageScore = score
    def updateTimeScore(self, score):
        self.timeScore = max(self.timeScore, score)
    def canBeRemoved(self):
        self.removetimes += 1
        if self.isTimeout():
            return True
        if self.wrongcodes == 0:
            return True
        if self.crashes >= 10:
            print("crash >= 5")
            return True
        if self.removetimes >= 3:
            print("remove times >= 3")
            return True
        self.wrongcodes -= 1
        return False
    def getScore(self):
        return self.coverageScore
    def selfMutate(self):
        self.config = RangeToConfig(self.range)
    def isTimeout(self):
        return self.crashes == -1 and self.wrongcodes == -1
    
class ConfigList():
    def __init__(self, default_config=None, fromfile=False):
        self.closeList = set()
        self.openList = PriorityQueue()
        self.crashcount = 0
        self.wrongcodecount = 0
        self.mutationpool = {}
        if fromfile:
            self.recoverList()
            return
        if default_config != None:
            self.openList.put(ConfigItem(default_config))
        self.showList()
    def openlen(self):
        return len(self.openList.queue)
    def closelen(self):
        return len(self.closeList)
    def push(self, configItem):
        self.openList.put(configItem)
    def pop(self):
        if self.openlen() == 0:
            print("open list is empty, push default config")
            self.openList.put(ConfigItem(default_config))
        return self.openList.get()
    def fade(self, configItem):
        assert configItem not in self.openList.queue
        if configItem.canBeRemoved():
            self.closeList.add(tuple(configItem.range))
            self.mutate(configItem)
        else:
            configItem.selfMutate()
            self.push(configItem)
        if len(self.closeList) > mxCloseSize:
            self.closeList.clear()
    def strongMutate(self, configItem):
        res = None
        def change():
            tmp = random.randint(0, 2)
            if(tmp == 0):
                return 0
            elif(tmp == 1):
                return -1
            else:
                return 1
        def isGroup(idx):
            return config_range["single"][1] < idx
        while True:
            _range = configItem.range.copy()
            for idx in range(len(_range)):
                if idx == VOID_ID:
                    continue
                if isGroup(idx):
                    break
                # find idx's config _range using config__range
                c = change()
                if c == 0:
                    continue
                _range[idx] = (_range[idx] + c) % 10
            for grp in config_range:
                if grp == "single":
                    continue
                idx = random.randint(config_range[grp][0], config_range[grp][1])
                if idx == VOID_ID:
                    continue
                c = change()
                if c == 0:
                    continue
                _range[idx] = (_range[idx] + c) % 10
                new_config = RangeToConfig(_range)
                _range = ConfigToRange(new_config)
            if tuple(_range) not in self.closeList:
                res = ConfigItem(RangeToConfig(_range))
                # just use old configItem's Coverage Score
                if configItem.coverageScore != 0:
                    res.updateCoverageScore(configItem.coverageScore - 1)
                res.father = configItem.config
                self.openList.put(res)
                break
        return res
    def mutate(self, configItem):
        res = None
        def change():
            if(random.randint(0, 1) == 0):
                return 1
            else:
                return -1
        def isGroup(idx):
            return config_range["single"][1] < idx
        dup_cnt = 0
        while True:
            range = configItem.range.copy()
            idx = random.randint(0, len(range) - 1)
            if idx == VOID_ID:
                continue
            # find idx's config range using config_range
            range[idx] = (range[idx] + change()) % 10
            if isGroup(idx):
                new_config = RangeToConfig(range)
                range = ConfigToRange(new_config)
            if tuple(range) not in self.closeList:
                res = ConfigItem(RangeToConfig(range))
                # just use old configItem's Coverage Score
                if configItem.coverageScore != 0:
                    res.updateCoverageScore(configItem.coverageScore - 1)
                res.father = configItem.config
                self.openList.put(res)
                break
            else:
                dup_cnt += 1
                if(dup_cnt >= 5):
                    return self.strongMutate(configItem)
        return res
    def showList(self):
        print("open list:")
        for configitem in self.openList.queue:
            print(configitem.config)
        print("close list:")
        for config in self.closeList:
            print(config)

    def saveList(self):
        with open(list_path, 'w') as f:
            f.write("open_list len: "+str(self.openlen())+"\n")
            f.write("close_list len: "+str(self.closelen())+"\n")
            f.write("\ncurrent open_list:\n")
            for configitem in self.openList.queue:
                f.write(str(configitem) + '\n')
            f.write("\ncurrent close_list:\n")
            for config in self.closeList:
                f.write(str(config) + '\n')
    def recoverList(self):
        with open(list_path, 'r') as f:
            for line in f.readlines():
                line = line.strip('\n')
                if line == '':
                    continue
                if line[0] == '{':
                    item = ast.literal_eval(line)
                    configItem = ConfigItem(item['config'], coverageScore=item['coverageScore'])
                    self.openList.put(configItem)
                elif line[0] == '(':
                    item = ast.literal_eval(line)
                    self.closeList.add(tuple(item))
    # detect dead point which can not be mutated to another neighborhood
    def deadPointdetect(self):
        pass
    # detect invalid mutation which can't produce program
    def recInvalidMutation(self, configItem):
        for pos, val in configItem.lastmutation.items():
            if pos not in self.mutationpool:
                self.mutationpool[pos] = []
            if val in self.mutationpool[pos]:
                continue
            self.mutationpool[pos].append(val)
    def isInvalidMutation(self, pos, val):
        if val in self.mutationpool[pos]:
            return True
        return False
    def incCrashCnt(self):
        self.crashcount += 1
    def incWrongcodeCnt(self):
        self.wrongcodecount += 1
    # def bugScore(self):
    #     if self.crashcount < 3:
    #         return self.crashcount + self.wrongcodecount
    #     return self.wrongcodecount

def get_config_format():
    config_cnt = 0
    # check if default config path exists
    if not os.path.exists(default_config_path):
        os.system("$CSMITH_HOME/build/bin/csmith --dump-default-probabilities " + default_config_path)
    with open(default_config_path, 'r') as f:
        line = f.readline()
        while line:
            line = line.strip().lstrip('[').lstrip('(').rstrip(']').rstrip(')')
            if line != "":
                line = line.split(',')
                tmp_list = []
                if len(line) > 1:
                    tmp_list.append(line[0])
                    line = line[1:]
                for p in line:
                    p = p.split('=')
                    config_cnt += 1
                    config_name = p[0]
                    if len(tmp_list) >= 1:
                        tmp_list.append(config_name)
                    else:
                        config_format.append(config_name)
                if len(tmp_list) >= 1:
                    config_format.append(tmp_list)
            line = f.readline()
    return config_cnt

def save_config(configuration):
    with open(config_saving_path, 'w') as f:
        j = 0
        for c in config_format:
            if isinstance(c, list):
                f.write('[' + str(c[0]) + ',')
                sum = 0
                sums = []
                default_sums = default_config[j:j+len(c)-1]
                for k in range(len(c) - 1):
                    inc = int(configuration[j])
                    if inc == 0 or sum == 100:
                        sums.append(0)
                    else:
                        sum += inc
                        if sum > 100:
                            sum = 100
                        sums.append(sum)
                    j += 1
                # turn the last non-zero value to 100
                flag = False
                for k in range(len(sums) - 1, -1, -1):
                    if sums[k] != 0:
                        flag = True
                        sums[k] = 100
                        break
                if not flag:
                    assert len(sums) == len(default_sums)
                    sums = default_sums
                for k in range(len(c) - 1):
                    f.write(str(c[k + 1]) + '=' + str(sums[k]))
                    if k != len(c) - 2:
                        f.write(',')
                    
                f.write(']\n')
            elif isinstance(c, tuple):
                assert False
            else:
                reduced_config = int(configuration[j])
                if reduced_config == 100:
                    reduced_config = 90
                f.write(str(c) + '=' + str(reduced_config) + '\n')
                j += 1

def ReadCoverage():
    with open(coverage_path, 'r') as f:
        f.readline()
        line = f.readline()
        assert line != ""
        line = line.strip()
        line = line.split('=')
        return float(line[1])

def ReadBug(configItem):
    crashes, wrongcodes = 0, 0
    if not os.path.exists(state_path):
        configItem.updateBugScore(-1, -1)
        return
    with open(state_path, 'r') as f:
        line = f.readline()
        while line:
            line = line.strip()
            if line != "":
                line = line.split(':')
                if line[0] == "Wrongcode":
                    wrongcodes += 1
                elif line[0] == "Crash":
                    crashes += 1
            line = f.readline()
    configItem.updateBugScore(crashes, wrongcodes)
    

def GetCoverage(configItem):
    # TODO: run the compiler with the given config and get the coverage
    save_config(configItem.config)
    os.system("perl ./generate.pl " + " " + config_saving_path + " " + csmith_feature_file + " " + str(c_file_cnt_per_iter))
    return ReadCoverage()

def SavePost():
    with open("./coverage_log.txt", 'a') as f:
        f.write(time.asctime()+"\n")
        f.write("bugs: ")
    os.system("ls ./data/bugs/ | wc -l >> ./coverage_log.txt")
    os.system("bash " + GCC_PATH + "/build/gcc/cal.sh >> ./coverage_log.txt")
    

def UpdateCoverage(configItem, coverage):
    with open("./coverage_log.txt", 'a') as f:
        if coverage == 0:
            f.write("\nzerocoverage:\n")
        else:
            f.write("\ncoverage:\n")
        f.write(str(configItem.id) + ": " + str(configItem.config) + '\n')
        f.write(str(coverage) + '\n')
    SavePost()

def Fuzzingenhanced():
    get_config_format()
    list = ConfigList(default_config=default_config, fromfile=fromfile)
    while True:
        # select config
        configItem = list.pop()
        # get coverage
        coverage = GetCoverage(configItem)
        ReadBug(configItem)
        configItem.updateCoverageScore(coverage)
        UpdateCoverage(configItem, coverage)
        
        if configItem.isTimeout():
            print("Error: "+str(configItem.config)+" can't generate programs")
            print("Father is "+str(configItem.father))
            list.saveList()
            continue
        if coverage == 0:
            list.fade(configItem)
        else:
            r = random.randint(0, list.openlen())
            if r == 0:
                list.mutate(configItem)
            # try to decrease the pri of continuous configuration to increase diversity
            # configItem.updateCoverageScore(0)
            configItem.selfMutate()
            list.push(configItem)
        list.saveList()

def Fuzzingdefault():
    get_config_format()
    list = ConfigList(default_config=default_config)
    while True:
        # select config
        configItem = list.pop()
        # get coverage
        coverage = GetCoverage(configItem)
        configItem.updateCoverageScore(coverage)
        UpdateCoverage(configItem, coverage)
        list.push(configItem)
        list.saveList()
    
def Fuzzinghicond():
    get_config_format()
    while True:
        # select config
        idx = random.randint(0, len(hicond_config) - 1)
        configItem = ConfigItem(hicond_config[idx])
        # get coverage
        coverage = GetCoverage(configItem)
        UpdateCoverage(configItem, coverage)

def Fuzzingextreme():
    get_config_format()
    list = ConfigList(default_config=extreme_config)
    while True:
        # select config
        configItem = list.pop()
        # get coverage
        coverage = GetCoverage(configItem)
        configItem.updateCoverageScore(coverage)
        UpdateCoverage(configItem, coverage)
        list.push(configItem)
        list.saveList()

def Fuzzingguided():
    get_config_format()
    open_list, close_list = [], set()
    open_list.append(ConfigItem(default_config))
    def Savelist():
        with open(list_path, 'w') as f:
            f.write("open_list len: " + str(len(open_list)) + '\n')
            f.write("close_list len: " + str(len(close_list)) + '\n')
            f.write("\ncurrent open_list:\n")
            for configitem in open_list:
                f.write(str(configitem) + '\n')
            f.write("\ncurrent close_list:\n")
            for config in close_list:
                f.write(str(config) + '\n')
    def Mutate(configItem):
        res = []
        def change():
            if(random.randint(0, 1) == 0):
                return 1
            else:
                return -1
        def isGroup(idx):
            return config_range["single"][1] < idx
        while True:
            range = configItem.range.copy()
            idx = random.randint(0, len(range) - 1)
            if idx == VOID_ID:
                continue
            # find idx's config range using config_range
            range[idx] = (range[idx] + change()) % 10
            if isGroup(idx):
                new_config = RangeToConfig(range)
                range = ConfigToRange(new_config)
            if tuple(range) not in close_list:
                res = RangeToConfig(range)
                break
        open_list.append(ConfigItem(res))
        return res
    while True:
        idx = random.randint(0, len(open_list) - 1)
        configItem = open_list[idx]
        # get coverage
        coverage = GetCoverage(configItem)
        UpdateCoverage(configItem, coverage)
        if coverage == 0:
            open_list.remove(configItem)
            close_list.add(tuple(configItem.range))
            Mutate(configItem)
            if len(close_list) > mxCloseSize:
                close_list.clear()
        else:
            r = random.randint(0, len(open_list))
            if r == 0:
                Mutate(configItem)
        Savelist()

def Fuzzingcombined():
    get_config_format()
    list = ConfigList(fromfile=fromfile)
    # push hicond_config into ConfigList
    if not fromfile:
        for config in hicond_config:
            list.push(ConfigItem(config))
    while True:
        # select config
        configItem = list.pop()
        # get coverage
        coverage = GetCoverage(configItem)
        ReadBug(configItem)
        configItem.updateCoverageScore(coverage)
        UpdateCoverage(configItem, coverage)
        
        if configItem.isTimeout():
            print("Error: "+str(configItem.config)+" can't generate programs")
            print("Father is "+str(configItem.father))
            list.saveList()
            continue
        if coverage == 0:
            list.fade(configItem)
        else:
            r = random.randint(0, list.openlen())
            if r == 0:
                list.mutate(configItem)
            # try to decrease the pri of continuous configuration to increase diversity
            # configItem.updateCoverageScore(0)
            configItem.selfMutate()
            list.push(configItem)
        list.saveList()
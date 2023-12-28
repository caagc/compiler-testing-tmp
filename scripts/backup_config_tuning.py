# Input: A set of configuration files, a set of features
# Output: A set of configuration files tuned according to the features
# Description: This script is used to tune the configuration files according to the features.
import os
import numpy as np
# import warnings
# np.warnings = warnings
from sklearn.cluster import KMeans
# from pyclustering.cluster import cluster_visualizer_multidim
# from pyclustering.cluster.xmeans import xmeans
# from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer

default_config_path = "./default.txt"
config_saving_path = "./config.txt"
config_format = []
iteration_cnt = 10 #10
csmith_cnt_output_file = "./csmith_cnt.csv"
c_file_cnt_per_iter = 2000 #2000
config_cnt_per_iter = 8 #100
default_config = [50,50,50,10,10,10,50,80,50,10,50,50,30,20,5,50,50,30,25,0,20,20,50,50,40,0,15,15,5,5,5,5,10,25,25,25,25,5,6,5,6,5,6,5,6,6,5,6,5,6,5,6,5,6,6,0,10,10,10,10,10,10,10,10,10,10,0,25,25,25,25]
state_path = "./state.txt"
res_path = "./res.txt"
all_configurations_explored = []
all_explored_marks = []

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
                    config_value = p[1]
                    # default_config.append(config_value)
                    if len(tmp_list) >= 1:
                        tmp_list.append(config_name)
                    else:
                        config_format.append(config_name)
                if len(tmp_list) >= 1:
                    # if tmp_list[0] != "statement_prob":
                    if False:
                        tmp_list = tuple(tmp_list)
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
                # if not isdefault:
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
                    # if isdefault:
                    #     f.write(str(c[k + 1]) + '=' + str(configuration[j]))
                    #     j += 1
                    # else:
                    f.write(str(c[k + 1]) + '=' + str(sums[k]))
                    if k != len(c) - 2:
                        f.write(',')
                    
                f.write(']\n')
            elif isinstance(c, tuple):
                assert False
                f.write('(' + str(c[0]) + ',')
                for k in range(len(c) - 1):
                    f.write(str(c[k + 1]) + '=' + str(configuration[j]))
                    if k != len(c) - 2:
                        f.write(',')
                    j += 1
                f.write(')\n')
            else:
                reduced_config = int(configuration[j])
                if reduced_config == 100:
                    reduced_config = 90
                f.write(str(c) + '=' + str(reduced_config) + '\n')
                j += 1

def fill_blank_feature(features, cnt_per_config):
    # compute the average value of each feature column, not line
    # if a feature is -1, fill it with the column average value

    feature_avg, feature_cnt = [], []
    st = len(features) - cnt_per_config
    for i in range(len(features[0])):
        feature_avg.append(0)
        feature_cnt.append(0)
    for feature in features[st:]:
        for i in range(len(feature)):
            if feature[i] == '-1':
                continue
            feature_avg[i] += float(feature[i])
            feature_cnt[i] += 1
    for i in range(len(feature_avg)):
        if feature_cnt[i] == 0:
            assert feature_avg[i] == 0
        if feature_cnt[i] != 0:
            feature_avg[i] /= feature_cnt[i]
    for feature in features[st:]:
        for i in range(len(feature)):
            if feature[i] == '-1':
                feature[i] = feature_avg[i]
            else:
                feature[i] = float(feature[i])


def cluster(features, states, n_clusters):
    X = np.array(features)
    # X = features
    # initial_centers = kmeans_plusplus_initializer(X, 3).initialize()
    # xmeans_instance = xmeans(X, initial_centers, 20)
    # xmeans_instance.process()
    # clusters = xmeans_instance.get_clusters()
    # labels = xmeans_instance.predict(X)
    # centers = xmeans_instance.get_centers()
    kmeans = KMeans(n_clusters=n_clusters, random_state=0, n_init='auto').fit(X)
    centroids = kmeans.cluster_centers_  
    labels = kmeans.labels_
    new_configurations = []
    # initialize the mark to list of 0 of length len(centroids)
    mark = [0 for i in range(len(centroids))]
    for i in range(len(states)):
        if states[i] == 1 or states[i] == 2:
            mark[labels[i]] += 1
    # sort the centroids according to the mark
    for i in range(len(mark)):
        for j in range(i+1, len(mark)):
            if mark[i] < mark[j]:
                mark[i], mark[j] = mark[j], mark[i]
                centroids[i], centroids[j] = centroids[j], centroids[i]
    
    for centroid in centroids:
        for i in range(len(centroid)):
            centroid[i] = int(centroid[i])
            if centroid[i] < 0:
                centroid[i] = 0
    # choose the first n_clusters centroids as new configurations
    for i in range(n_clusters):
        new_configurations.append(centroids[i])
    for i in range(len(mark)):
        all_configurations_explored.append(centroids[i])
        all_explored_marks.append(mark[i])
    with open(res_path, 'a') as f:
        # only write newly explored configurations
        for i in range(len(all_configurations_explored) - len(mark), len(all_configurations_explored)):
            f.write(str(all_explored_marks[i]) + " " + str(list(all_configurations_explored[i])) + "\n")
    return new_configurations, mark

    


def config_tuning(config, cnt_per_config, states, features):
    save_config(config)
    os.system("perl ./generate.pl " + " " + config_saving_path + " " + csmith_cnt_output_file + " " + str(cnt_per_config))
    # we won't get total 20000 programs using only the default center, but we can tune our center in each iteration
    # open csmith_cnt_output_file and read the file by line
    if not os.path.exists(state_path) or not os.path.exists(csmith_cnt_output_file):
        return

    with open(state_path, 'r') as f:
        line = f.readline()
        while line:
            line = line.strip()
            if line != "":
                line = line.split(':')
                if line[0] == "Correct":
                    states.append(0)
                elif line[0] == "Wrongcode":
                    states.append(1)
                elif line[0]== "Crash":
                    states.append(2)
            line = f.readline()

    with open(csmith_cnt_output_file, 'r') as f:
        line = f.readline()
        while line:
            line = line.strip()
            if line != "":
                line = line.split(',')
                features.append(line)
            line = f.readline()

    fill_blank_feature(features, cnt_per_config)


def auto_config_tuning():
    i = 0
    # inital configurations {<config, bug_cnt, (coverage)>}
    assert len(default_config) == 71
    get_config_format()
    configurations = [default_config for i in range(config_cnt_per_iter)]
    marks = [0 for i in range(config_cnt_per_iter)]
    marks[0] = 1
    while i < iteration_cnt:
        cnt_per_config = c_file_cnt_per_iter // len(configurations)
        states = []
        features = []
        for config in configurations:
            config_tuning(config, cnt_per_config, states, features)
        configuration_tmp, marks_tmp = cluster(features, states, config_cnt_per_iter)
        j, k = 0, 0
        new_configurations, new_marks = [], []
        while j < len(configurations) and k < len(configuration_tmp) and len(new_configurations) < config_cnt_per_iter:
            if marks[j] < marks_tmp[k]:
                new_configurations.append(configuration_tmp[k])
                new_marks.append(marks_tmp[k])
                k += 1
            else:
                new_configurations.append(configurations[j])
                new_marks.append(marks[j])
                j += 1
        while j < len(configurations) and len(new_configurations) < config_cnt_per_iter:
            new_configurations.append(configurations[j])
            new_marks.append(marks[j])
            j+=1
        marks = new_marks
        configurations = new_configurations
        print(configurations)
        print(new_marks)
        i += 1
    # with open(res_path, 'w') as f:
    #     for i in range(len(all_configurations_explored)):
    #         f.write(str(all_explored_marks[i]) + " " + str(list(all_configurations_explored[i])) + "\n")

auto_config_tuning()
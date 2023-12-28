import matplotlib.pyplot as plt
from matplotlib_venn import venn2
from matplotlib_venn import venn3

version = "gcc-4.6.0"
def make_eff_venn():
      bugs_path = "../dedup_bak/" + version
      hicond, mcs, my = set(), set(), set()
      with open(bugs_path + "/HiCOND.txt", "r") as f:
            for line in f:
                  line = line.strip()
                  line = line.split(':')
                  line = line[1]
                  if line == "" or line == "-1":
                        continue
                  hicond.add(line)
      with open(bugs_path + "/MCS.txt", "r") as f:
            for line in f:
                  line = line.strip()
                  line = line.split(':')
                  line = line[1]
                  if line == "" or line == "-1":
                        continue
                  mcs.add(line)
      with open(bugs_path + "/combined.txt", "r") as f:
            for line in f:
                  line = line.strip()
                  line = line.split(':')
                  line = line[1]
                  if line == "" or line == "-1":
                        continue
                  my.add(line)
      print(hicond)
      print(mcs)
      print(my)
      # make venn diagram using set1, set2, set3
      venn3([hicond, mcs, my], ('HiCOND', 'MCS', 'Our Approach'))
      plt.savefig(version+'_eff_venn.png')

def make_abl_venn():
      bugs_path = "../dedup_bak/" + version
      nohicond, my = set(), set()
      with open(bugs_path + "/enhanced.txt", "r") as f:
            for line in f:
                  line = line.strip()
                  line = line.split(':')
                  line = line[1]
                  if line == "" or line == "-1":
                        continue
                  nohicond.add(line)
      with open(bugs_path + "/combined.txt", "r") as f:
            for line in f:
                  line = line.strip()
                  line = line.split(':')
                  line = line[1]
                  if line == "" or line == "-1":
                        continue
                  my.add(line)
      print(nohicond)
      print(my)
      # make venn diagram using set1, set2, set3
      plt.clf()
      venn2([nohicond, my], ('Without HiCOND', 'Our Approach'))
      plt.savefig(version+'_abl_venn.png')
      

make_eff_venn()
make_abl_venn()

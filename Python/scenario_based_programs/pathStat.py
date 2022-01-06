import os
import sys
from itertools import groupby

inp_path=sys.argv[1]


#recursive listing of files and directories
l=list(os.walk(inp_path))

#recursive count of directories
rec_dir_cnt= len([x[0] for x in l])-1

l_final=[]
l_file_stat_all=[]

for i in range(len(l)):
    #list of tuple of file names and its extensions sorted by extensions
    l_new=sorted([os.path.splitext(x) for x in l[i][2]],key=lambda x :x[1])

    #list of tuple of file extension and  count of files under the extension
    file_stat=[(x,len(list(y))) for x,y in groupby(l_new,lambda x : x[1].replace(".",""))]

    #preparing a cumulative list of all extension count pairs under each directory
    l_file_stat_all=l_file_stat_all + file_stat

    #building dictionary for summary2
    d_stat = {"path": l[i][0], "dir_count": len(l[i][1]), "file_count":file_stat}

    #sppending each dictionary to final list of summary2
    l_final.append(d_stat)

#preparing Summary1
l_file_stat_all.sort(key=lambda x :x[0])
l_file_count_all=[(x,sum(list(zip(*list(y)))[1])) for x,y in groupby(l_file_stat_all,key=lambda x : x[0].strip())]
rec_f_cnt_tot=sum(list(zip(*l_file_count_all))[1])

#SUMMARY1
d_summary={"parent_directory":l[0][0],"recursive_dir_count":rec_dir_cnt,"recursive_file_count_tot":rec_f_cnt_tot,"recursive_file_count":l_file_count_all}

dir_to_be_created="_".join(inp_path.split("\\")).replace(":","")
full_file_path1="A:\\Summary\\{0}\\{0}.summary1.json".format(dir_to_be_created)
full_file_path2="A:\\Summary\\{0}\\{0}.summary2.json".format(dir_to_be_created)
os.makedirs(os.path.dirname(full_file_path1), exist_ok=True)
with open(full_file_path1,"w") as f:
    f.write(str(d_summary))

with open(full_file_path2,"w") as f:
    for i in l_final: \
            f.write(str(i))
import csv
import re

path=r"A:\lab\data\other\destination.csv"
out_type={'orig':2,'cmn':2,'fav':1}
user=[1]
with open(path) as f:
    r = csv.reader(f)
    start = len(' '.join(next(r)))+2

    while True:
        for i in user:
            for j in out_type:
                s=next(r)
                #pattern = re.compile(f"{i}\s{j}\s[a-zA-Z]+")
                #found=pattern.match(s)
                if j in :






# with open(path) as f:
#     r=csv.reader(f)
#     next(r)
#     user_dest={}
#     user_remove=[]
#     dest_typ = {}
#     dest_typ_remove = []
#     for i in r:
#         if i[0] in user_remove:
#
#             if i[1] in dest_typ_remove:
#                 user_dest[i[0]][i[1]].append(i[2])
#             else:
#                 user_dest[i[0]][i[1]]  = [i[2]]
#                 dest_typ_remove.append(i[1])
#         else:
#             dest_typ_remove = []
#             dest_typ = {}
#             dest_typ[i[1]]=[i[2]]
#             user_dest[i[0]]=dest_typ
#             user_remove.append(i[0])
#             dest_typ_remove.append(i[1])
#
#
# print(user_dest)
#
#
# out_type={'orig':2,'cmn':2,'fav':1}
# out={}
# out_dest_typ={}
# for i in user_dest:
#     for j in out_type:
#         if j in user_dest[i] and len(user_dest[i][j][:out_type[j]])>=out_type[j]:
#             out_dest_typ[j]=user_dest[i][j][:out_type[j]]


#l= list(map(lambda x : x.strip("\n").split(","),l))[1:]
#dest_typ_list=['orig','orig','cmn','cmn','fav']







#for i in groupby(l,lambda x : x[0]):





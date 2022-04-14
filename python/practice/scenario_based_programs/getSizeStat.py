import os



def recursiveTotalSize(inp_path):
    total_size = 0
    for path, dirs, files in os.walk(inp_path):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)
    return fileSizeFormatter(total_size)
def main():
    inputPath=r'A:\mygit'
    print(recursiveTotalSize(inputPath))


    rec_path_list=[path for path, dirs, files in os.walk(inputPath)]
    size_stat={}
    for path in rec_path_list:
        size_stat[path]=recursiveTotalSize(path)
    out_file="{}_sizestat.json".format(inputPath.replace(":\\","_"))
    fp=os.path.join("A:\Summary\Size_stat",out_file)
    with open(fp,"w+") as f:
        f.write(str(size_stat))

if __name__=="__main__":
    main()
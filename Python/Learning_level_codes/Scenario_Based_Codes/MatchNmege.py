import re
def matchOut(long_str,short_str):
    pattern2= re.compile(r'[a-zA-Z]*{}[a-zA-Z]*'.format(short_str.upper()))

    if pattern2.search(long_str.upper()):
        return True
def cleanAndMerge(*args):
    pattern = re.compile("^[A-Za-z ]*$")
    out_list=[]
    for i in args:
        out_list=out_list+list(set([x for x in i if pattern.search(str(x))]))
    return out_list

def driver(final_list):
    output_list =[]
    del_list=[]
    for i in final_list:
        if i not in del_list:
            del_list.append(i)
            matched = False
            for j in final_list:
                if  j not in del_list:
                    if len(i)>len(j):
                        long_str=i
                        short_str=j
                    else:
                        long_str = j
                        short_str =i
                    out=matchOut(long_str, short_str)
                    if out:
                        matched=True
                        del_list.append(short_str)
                        output_list.append(long_str)


            if not matched:
                    output_list.append(i)

    return set(output_list)
def main():
    input1 = ["Karnataka", "Kerala", "Delhi", "Bihar", "Andaman", "Tamil N", "Ponicherry"]
    input2 = ["Rajasthan", "Kesala", "Tamil N", 11, "Ponicherry"]
    input3 = ["Karnatak", "Kerala", "New Delhi", "Bihar", "Andaman Islands", "Tamil Nadu", "Orissa", ":-)"]
    final_list=cleanAndMerge(input1,input2,input3)
    out=driver(final_list)
    print(sorted(list(out)))

if __name__=="__main__":
    main()







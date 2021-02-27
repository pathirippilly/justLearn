import re
from difflib import SequenceMatcher

def relevantIrrelevant(long_str,short_str):
    ind_st=['Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
     'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya',
     'Mizoram', 'Nagaland', 'Orissa', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttarakhand',
     'Uttar Pradesh', 'West Bengal', 'Tamil Nadu', 'Tripura', 'Andaman and Nicobar Islands', 'Chandigarh',
     'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Lakshadweep', 'Pondicherry']
    long_str_ratio=max(SequenceMatcher(None, long_str.upper(), x.upper()).ratio() for x in ind_st)
    short_str_ratio = max(SequenceMatcher(None, short_str.upper(), x.upper()).ratio() for x in ind_st)
    if long_str_ratio>short_str_ratio:
        return long_str,short_str
    else:
        return short_str,long_str

def similar(a,b):
    if SequenceMatcher(None, a, b).ratio() >= 0.50:
        return True
    else:
        return False
def matchOut(long_str,short_str):
    long_str_list=long_str.split(" ")
    if len(long_str_list)>1:
        #print(long_str,short_str)
        return max(True if similar(x,short_str) else False for x in long_str_list)
    elif similar(long_str,short_str):
        return True
    else:
        return False
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
                        relevantIrrelevant_tuple=relevantIrrelevant(long_str, short_str)
                        del_list.append(relevantIrrelevant_tuple[1])
                        output_list.append(relevantIrrelevant_tuple[0])


            if not matched:
                    output_list.append(i)

    return set(output_list)
def main():
    input1 = ["Karnataka", "Kerala", "Delhi", "Bihar", "Andaman", "Tamil N", "Ponicherry"]
    input2 = ["Rajasthan", "Kesala", "Tamil N", 11, "Pondicherry"]
    input3 = ["Karnatak", "Kerala", "New Delhi", "Bihar", "Andaman Islands", "Tamil Nadu", "Orissa", ":-)"]
    final_list=cleanAndMerge(input1,input2,input3)
    out=driver(final_list)
    print(sorted(list(out)))

if __name__=="__main__":
    main()







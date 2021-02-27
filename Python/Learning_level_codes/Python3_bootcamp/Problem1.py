import re


sub_list=[] #list for accepting intermediate inputs for each of the test case
final_list=[] #list for accepting final set of inputs from user. Also this will hold the final sorted output
l=list(map(lambda x : str(x),range(1,201))) #list for checking the testcase number limit


main_count=1 # counter which controlls the number of test cases possible for any test execution.Max possible value is 500.


#Below while loop will prepare the input list which includes both correct and incorect inputs
while(main_count<=500):
    val=input()
    sub_list.append(val)
    if val=='0':
        break
    elif val in l:
        #print("its a number")
        sub_count=1
        while(sub_count<=int(val)):
            name=input()
            sub_list.append(name)
            sub_count=sub_count+1     
    final_list.append(sub_list.copy())
    sub_list.clear()
    main_count=main_count+1

#Below for loop will validate the input data and prpepare the sorted final list
for i in final_list:
    
    eval1=i[0] in l #checkig the testcase input number for its limit(or if its a number or not)
    eval2=''.join(re.findall('[a-zA-Z]+',''.join(i[1:])))==''.join(i[1:]) #checking if names contains only alphabet or not
    eval3=min(list(map(lambda x : len(x) in range(2,21),i[1:]))) #checking for length of the name
    
    if (eval1 and eval2 and eval3):
        name_list=i[1:]
        ordered=sorted(name_list,key=lambda x:x[:2:])
        final_list[final_list.index(i)]=ordered
    elif (eval1==False):
        final_list[final_list.index(i)]=["TesCase(n={}):\n ValueError:improper Test Case Number Value.\n Test case number should be positive integer of value between 1 and 200".format(i[0])]
    elif (eval2==False):
        final_list[final_list.index(i)]=["TesCase(n={}):\n ValueError:non-aplha entry found  for one (or all) of the names\nNote:Name should have only alphabets".format(i[0])]
    else:
        final_list[final_list.index(i)]=["TesCase(n={}):\n ValueError:improper length for one (or all) the names\nNote:Name should be of length between 2 and 20".format(i[0])]
#Below for loop will print the sorted output(if any test case have improper inputs , that also will be printed)
for i in final_list:
    print("\n")
    for j in i:
        print(j)
       
        
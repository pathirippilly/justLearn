try:
    open_flag = 1
    f= open(r"A:\lab\test_outs\test1.csv","r")
    r= f.read()
    print(r)

except FileNotFoundError as e:
    open_flag=0
    print(e)
except PermissionError as e:
    open_flag=0
    print(e)
except Exception as e:
    print(e)
finally:
    if open_flag==1:
        f.close()

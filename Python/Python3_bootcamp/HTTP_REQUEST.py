import requests as r
from pyfiglet import figlet_format
from termcolor import colored

print((colored(figlet_format(text="Lets listen to your favourite joke!!"),'cyan'))+"\n")

while True:
    t=input("Enter your search text(like dog,cat,phone..etc.The jokes will be appeared based on your text: " )
    n=input("How many jokes you demand :(put a number) ")
    try:
        
        url="https://icanhazdadjoke.com/search"
        res_api=r.get(url,headers={"Accept":"application/json"},
        params={"term":f"{t}","limit":f"{n}"}
        )   
        if res_api.ok:
            data=res_api.json()
            jokes={"joke"+y:x["joke"] for x,y in 
                   zip(data["results"],[str(x+1) for x in range(int(n))])}
            if jokes.items():
                
                for joke in jokes.items():
                    print(colored(joke[0],color="red")+":"+colored(joke[1][:joke[1].find("?"):],color="blue")+colored(joke[1][joke[1].find("?")::],color="yellow")+"\n")
                break;
            else:
                print("\nSorry no jokes found for your text!!\n")
                while True:
            
                    flag=input("wanna try again Y/N: ")
                    
                    if(flag.upper() in 'YN' ):
                        break
                    else:
                        print("\ninvalid input,you want to give Y or N!!")
        else:
            print("you have recieved a response code of "+res_api.status_code)
            break;
    except TypeError as e:
        print("\nnumber of jokes you have demanded should be a number")
        while True:
            
            flag=input("wanna try again Y/N: ")
            
            if(flag.upper() in 'YN' ):
                break
            else:
                print("invalid input,you want to give Y or N!!")
        if flag.upper()=='N':
            break
        
                
        
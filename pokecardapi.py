import requests


notfound = True

while notfound :
    #While notfound is TRUE 
    
    poke=input("Print Pokemon here: ")

    try:
        myrequest = requests.get("https://api.pokemontcg.io/v1/cards?name="+poke)
        datajson = myrequest.json()
        datajson['cards'][4]
        
    except:
        print("Invalid Pokémon name. Make sure spelling is correct")

    else:
        hipng0=[]

        for i in range(30):
            hipng0.append(datajson['cards'][i]['imageUrl'])


        for i in range(len(hipng0)):
            print(hipng0[i])

        ofile = open("testing.html","w")
        ofile.write("<img src=" +hipng0[0]+">")

        notfound = False






        














         

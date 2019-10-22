import requests
from tkinter import *
from tkinter import messagebox



def Getit():
    notfound = True

    print("getit")

    while notfound == True:
        
        try:
            myrequest = requests.get("https://api.pokemontcg.io/v1/cards?name="+poke.get())
            datajson = myrequest.json()
            cards = datajson['cards'][4]
                
        except:
            messagebox.showinfo("Uh oh!", "Check your internet connection. If you're connected, check the Pokémons spelling")
               
        else:
            hipng0=[]
            imageUrlHiRes0=[]

            for i in range(len(datajson['cards'])):
               
                v=datajson['cards'][i]['imageUrl']
                
                if v[-9:-7]!="SM":
                    hipng0.append(datajson['cards'][i]['imageUrl'])
                    imageUrlHiRes0.append(datajson['cards'][i]['imageUrlHiRes'])



            ofile = open("testing.html","w")

            counter=0
            ofile.write("<table><tr>")
                
            for i in range(len(hipng0)):
                ofile.write("<td>" + "<img src=" +hipng0[i]+"><p><a href=' " +imageUrlHiRes0[i]+"'>To high resolution photo</a></p> " + "</td>")
                counter=counter+1
                if counter==5:
                    ofile.write("</tr>" + "<tr>")
                    counter=0

            ofile.write("</tr>" + "</table>")
                    
                    
              
            ofile.close()
            messagebox.showinfo("Success!", "Check out testing.html")


            notfound = False

win=Tk()
poke=Entry(win)
b1=Button(win,text="Find Pokémon", command=Getit)
poke.grid(row=0,column=0)
b1.grid(row=1,column=0)
mainloop()


        














         

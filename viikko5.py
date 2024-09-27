import tkinter as tk
import winsound
import time
import threading
import random
from tkinter import PhotoImage

ikkuna=tk.Tk()

ikkuna.geometry("800x500+200+200")

#globaali dictionary
tiedot={}
tiedot['apinamaara']=0
tiedot['apinamaaraErne']=0
tiedot['apinamaaraKerne']=0
tiedot['apina']={}

haitila = 0
lopputila = 0

pohterinkirja =set()
eteterinkirja =set()




def eapina(): #tämä on ykköskohdan apina ernestille
    global tiedot
    tiedot['apinamaara']+=1
    tiedot['apinamaaraKerne']+=1  
    apina_id=tiedot['apinamaara']

    print("Apina kiitää")
    tiedot['apina'][apina_id]={'nimi':'ernestin apina','x':100,'y':random.randint(60,90),'elossa':1,'ID':apina_id,
        'tarkistettu': False}
    print("Tällä hetkellä yhteensä ",tiedot['apinamaara'], " apinaa")
    

    #havainnollistus
    apinaleima=tk.Label(text=''.join(['E',str(tiedot['apina'][apina_id]['ID'])]),bg='green')
    apinaleima.place(x=tiedot['apina'][apina_id]['x'],y=[tiedot['apina'][apina_id]['y']])

    tiedot['apina'][apina_id]['leima']=apinaleima

    
    for i in range(100):
        tiedot['apina'][apina_id]['x']+=5
        apinaleima.place(x=tiedot['apina'][apina_id]['x'],y=[tiedot['apina'][apina_id]['y']])
        soundthread(tiedot['apina'][apina_id])
        time.sleep(0.1)

     


def kapina(): #tämä on ykköskohdan apina kernestille
    global tiedot
    tiedot['apinamaara']+=1
    tiedot['apinamaaraErne']+=1  
    apina_id=tiedot['apinamaara']

    print("Apina kiitää")
    tiedot['apina'][apina_id]={'nimi':'kernestin apina','x':100,'y':random.randint(190,220),'elossa':1,'ID':apina_id,
        'tarkistettu': False}
    print("Tällä hetkellä yhteensä ",tiedot['apinamaara'], " apinaa")
    

    #havainnollistus
    apinaleima=tk.Label(text=''.join(['K',str(tiedot['apina'][apina_id]['ID'])]),bg='lightgreen')
    apinaleima.place(x=tiedot['apina'][apina_id]['x'],y=[tiedot['apina'][apina_id]['y']])

    tiedot['apina'][apina_id]['leima']=apinaleima

    

    for i in range(100):
        tiedot['apina'][apina_id]['x']+=5
        apinaleima.place(x=tiedot['apina'][apina_id]['x'],y=[tiedot['apina'][apina_id]['y']])
        soundthread(tiedot['apina'][apina_id])
        time.sleep(0.1)

def eapina2(): #tämä on lopputehtävän apina ernestille
    global tiedot
    tiedot['apinamaara']+=1
    apina_id=tiedot['apinamaara']

    print("Apina kiitää")
    tiedot['apina'][apina_id]={'nimi':'ernestin apina','x':100,'y':random.randint(60,90),'elossa':1,'Sana':randomsana(),'ID':apina_id,'tarkistettu': False}
    print("Tällä hetkellä yhteensä ",tiedot['apinamaara'], " apinaa")
    print(tiedot['apina'][apina_id])
    

    #havainnollistus
    apinaleima=tk.Label(text=''.join(['E',str(tiedot['apina'][apina_id]['ID'])]),bg='green')
    apinaleima.place(x=tiedot['apina'][apina_id]['x'],y=[tiedot['apina'][apina_id]['y']])

    tiedot['apina'][apina_id]['leima']=apinaleima

    
    for i in range(100):
        tiedot['apina'][apina_id]['x']+=5
        apinaleima.place(x=tiedot['apina'][apina_id]['x'],y=[tiedot['apina'][apina_id]['y']])
        
        time.sleep(0.05)
        sound(tiedot['apina'][apina_id])
        time.sleep(0.05)  
        #soundthread(tiedot['apina'][apina_id])
        
        if haitila == 1:
            arpa = random.randint(1, 10000)
            if arpa <= 70:
                tapaapinathread(tiedot['apina'][apina_id])
                time.sleep(1)
                break
        if i == 99:  
            time.sleep(2)
            winsound.Beep(880, 3000)  
            time.sleep(3)
            break
                 

def kapina2(): #tämä on ykköskohdan apina kernestille
    global tiedot
    tiedot['apinamaara']+=1
    apina_id=tiedot['apinamaara']

    print("Apina kiitää")
    tiedot['apina'][apina_id]={'nimi':'kernestin apina','x':100,'y':random.randint(190,220),'elossa':1,'Sana':randomsana(),'ID':apina_id,'tarkistettu': False}
    print("Tällä hetkellä yhteensä ",tiedot['apinamaara'], " apinaa")
    print(tiedot['apina'][apina_id])
    

    #havainnollistus
    apinaleima=tk.Label(text=''.join(['K',str(tiedot['apina'][apina_id]['ID'])]),bg='lightgreen')
    apinaleima.place(x=tiedot['apina'][apina_id]['x'],y=[tiedot['apina'][apina_id]['y']])

    tiedot['apina'][apina_id]['leima']=apinaleima

    

    for i in range(100):
        tiedot['apina'][apina_id]['x']+=5
        apinaleima.place(x=tiedot['apina'][apina_id]['x'],y=[tiedot['apina'][apina_id]['y']])
        time.sleep(0.05)
        sound(tiedot['apina'][apina_id])
        time.sleep(0.05) 
        #soundthread(tiedot['apina'][apina_id])
        
        if haitila == 1:
            arpa = random.randint(1, 10000)
            if arpa <= 70:
                tapaapinathread(tiedot['apina'][apina_id])
                time.sleep(1)
                break
        if i == 99:  
            time.sleep(2)
            winsound.Beep(880, 3000)  
            time.sleep(3)
            break
    
       

def randomsana():
    sana = random.choice([
        'Ernesti',
        'ja',
        'Kernesti',
        'tässä',
        'terve',
        'olemme',
        'autiolla',
        'saarella',
        'voisiko',
        'joku',
        'tulla',
        'sieltä',
        'sivistyneestä',
        'maailmasta',
        'hakemaan',
        'meidät',
        'pois',
        'kiitos'
        ])
    return sana

def haitilavipu():
    global haitila
    if haitila == 0:
       haitila += 1
    else:
        haitila = 0
    print(haitila)   

def tapaApina(apinanid): #tämän funktion  koodi on osaltaan chatGPT koodia
    global tiedot
    apinaid = apinanid['ID']
    if tiedot['apina'][apinaid]['elossa'] == 1:  
        tiedot['apina'][apinaid]['elossa'] = 0   
        apinaleima = tiedot['apina'][apinaid]['leima']
        apinaleima.config(bg='red')               #tämä kohta
        print(f"Apina {apinaid} syötiin.")
        time.sleep(1)
        winsound.Beep(400,3000)
        time.sleep(1)
        
        apinaleima.after(3000, apinaleima.destroy)

def tapaapinathread(apinanid):
    kahvaapinatappo=threading.Thread(target=tapaApina, args=(apinanid,))
    kahvaapinatappo.start()

def tarkista_ja_tallenna(apina, omistaja): #Tämä funktio sisältää ChatGPT koodia
    sana = apina.get('Sana')  
    if not sana or sana == 'None':  #tässä
        return  
    
    if omistaja == 'ernesti':  
        sanakirja = pohterinkirja
    elif omistaja == 'kernesti':
        sanakirja = eteterinkirja
    else:
        print("Tuntematon omistaja")
        return
    
    if sana not in sanakirja: #tässä
        sanakirja.add(sana)  #tässä
        print(f"Sana '{sana}' tallennettu sanakirjaan '{omistaja}'")

        if len(sanakirja) == 10: #tässä
            print(f"Sanakirjassa '{omistaja}' on nyt 10 uniikkia sanaa!")
            lopetus(omistaja)
           
    else:
        print(f"Sana '{sana}' on jo sanakirjassa '{omistaja}'")



def sound(apinatieto):
    apinanid = apinatieto['ID']
    winsound.Beep(440+apinanid,350)
    #time.sleep(0.35)

def soundthread(apinatieto):
    kahvaAani=threading.Thread(target=sound, args=(apinatieto,))
    kahvaAani.start()


def eapinathread(): #ykkös kohdan ernestin apina
    kahvaEapina=threading.Thread(target=eapina)
    kahvaEapina.start()

def eapina2thread(): #kakkos kohdan ernestin apina
    kahvaEapina2=threading.Thread(target=eapina2)
    kahvaEapina2.start()    

def kapinathread(): #ykkös kohdan kernestin apina
    kahvaKapina=threading.Thread(target=kapina)
    kahvaKapina.start()

def kapina2thread(): #kakkos kohdan kernestin apina
    kahvaKapina2=threading.Thread(target=kapina2)
    kahvaKapina2.start()

def e10apinaathread():
    for i in range(10):
        time.sleep(0.05)
        eapina2thread()

def k10apinaathread():
    for i in range(10):
        time.sleep(0.05)
        kapina2thread()

def tarkistaranta():
    global tiedot
    while True:
        for apina_id, apina in tiedot['apina'].items():
            if apina['x'] >= 600 and not apina['tarkistettu']:  # Tarkistetaan, onko x-koordinaatti 600 tai enemmän
                tiedot['apina'][apina_id]['tarkistettu'] = True
                print(f"Apina {apina_id} on saapunut rannalle! tarkailiata")
                if apina['y'] < 150:  #Pohteri
                    omistaja = 'ernesti'
                    tiedot['apinamaaraErne']+=1  
                else:                #Eteteri
                    omistaja = 'kernesti'
                    tiedot['apinamaaraKerne']+=1   
                
                # Kutsutaan tarkista_ja_tallenna-funktiota, jos apinalla on sana
                tarkista_ja_tallenna(apina, omistaja)

        time.sleep(1)  # Odotetaan 1 sekunti ennen seuraavaa tarkistusta        

tarkistaja_thread = threading.Thread(target=tarkistaranta)
tarkistaja_thread.daemon = True 


def tarkkaile_saikeistin():
    pohterileima.place(x=620,y=50)
    eteterileima.place(x=620,y=75)

    tarkistaja_thread.start()

def loppuhuipennus(laukaisija):
    print('LOPPU ALKAA')
    pelastaja=laukaisija
    laivax=600

    if pelastaja == 'ernesti':
        
        laivaleima.place(x=laivax,y=75)
        for i in range(10):
            laivax-= 50
            laivaleima.place(x=laivax,y=75)
            winsound.Beep(200,600)
        tekstileima.config(text='Ernesti: UI JUNA! Minä pelastin meidät!')
        tekstileima.place(x=50, y=50)
        time.sleep(5)
        tekstileima.place_forget()
        for i in range(10):
            laivax+= 50
            laivaleima.place(x=laivax,y=75)
            winsound.Beep(200,600)
            
    else:
        laivaleima.place(x=laivax,y=225)
        for i in range(10):
            laivax-= 50
            laivaleima.place(x=laivax,y=225)
            winsound.Beep(200,600)
        tekstileima.config(text='Kernesti: Hurraa! Minä pelastin meidät!')
        tekstileima.place(x=50, y=200)
        time.sleep(5)
        tekstileima.place_forget()
        for i in range(10):
            laivax+= 50
            laivaleima.place(x=laivax,y=225)
            winsound.Beep(200,600)
    tilastot(pelastaja)        

def lopetus(laukaisija):
    print('LOPPU ALKAA KOHTA')
    global lopputila
    if lopputila == 0:
       ('NYT SE TULEE')
       loppukahva=threading.Thread(target=loppuhuipennus,args=(laukaisija,))
       loppukahva.start()
       lopputila += 1
    else:
        return   

def tilastot(pelastaja):
    global tiedot

    teksti1 = tk.Label(text='Lopullinen pelastaja oli ' + pelastaja)
    teksti2 = tk.Label(text='Apinoita yhteensä oli : ' + str(tiedot['apinamaara']))
    teksti3 = tk.Label(text='Ernestillä eläviä apinoita yhteensä oli : ' + str(tiedot['apinamaaraErne']))
    teksti4 = tk.Label(text='Kernestillä eläviä apinoita yhteensä oli : ' + str(tiedot['apinamaaraKerne']))
    ernepippuri = tiedot['apinamaaraErne'] * 2
    kernepippuri = tiedot['apinamaaraKerne'] * 2
    teksti5 = tk.Label(text='Ernestin juhlissa pippuria tarvitaan : ' + str(ernepippuri) + 'tl')
    teksti6 = tk.Label(text='Kernestin juhlissa pippuria tarvitaan : ' + str(kernepippuri) + 'tl')
    teksti7= tk.Label(text='')
    if ernepippuri > kernepippuri:
        teksti7.config(text='Ernestin juhlat ovat isommat')
    else:
        teksti7.config(text='Kernestin juhlat ovat isommat')  
    teksti1.place(x=560,y=300)
    teksti2.place(x=560,y=325)  
    teksti3.place(x=560,y=350)  
    teksti4.place(x=560,y=375)  
    teksti5.place(x=560,y=400)  
    teksti6.place(x=560,y=425)  
    teksti7.place(x=560,y=450)  
           
    

ernesti_lahettaa=tk.Button(text='Ernestin perus apina',command=eapinathread, bg='blue')
ernesti_lahettaa.place(x=10,y=400)

kernesti_lahettaa=tk.Button(text='Kernestin perus apina',command=kapinathread, bg='blue')
kernesti_lahettaa.place(x=10,y=425)

ernesti_lahettaa2=tk.Button(text='Ernestin edistynyt apina',command=eapina2thread, bg='yellow')
ernesti_lahettaa2.place(x=160,y=400)

kernesti_lahettaa2=tk.Button(text='Kernestin edistynyt apina',command=kapina2thread, bg='yellow')
kernesti_lahettaa2.place(x=160,y=425)

ernesti_lahettaa10=tk.Button(text='Ernestin 10 apinaa',command=e10apinaathread, bg='orange')
ernesti_lahettaa10.place(x=310,y=400)

kernesti_lahettaa10=tk.Button(text='Kernestin 10 apinaa',command=k10apinaathread, bg='orange')
kernesti_lahettaa10.place(x=310,y=425)

tarkkailijanappi=tk.Button(text='Tarkkaile!',command=tarkkaile_saikeistin, bg='cyan')
tarkkailijanappi.place(x=460,y=400)

aktivoiHaitnappi=tk.Button(text="Toggle hait",command=haitilavipu ,bg='orange')
aktivoiHaitnappi.place(x=310,y=450)



meri = PhotoImage(file="images/meri.png")
saari = PhotoImage(file="images/saari.png")
manner = PhotoImage(file="images/manner.png")

merileima = tk.Label(ikkuna ,image=meri)
saarileima = tk.Label(ikkuna ,image=saari)
mannerleima = tk.Label(ikkuna ,image=manner)

merileima.place(x=100, y=50)
saarileima.place(x=0, y=50)
mannerleima.place(x=600, y=50)

pohterileima=tk.Label(text='Pohteri',bg='cyan')
eteterileima=tk.Label(text='Eteteri',bg='cyan')
laivaleima=tk.Label(text='LAIVA',bg='grey')
tekstileima=tk.Label(text='',bg='cyan')



ikkuna.mainloop()
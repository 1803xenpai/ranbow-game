import random
#player naming no duplication to avoid confusion-----------------------------
players=[]
main1= ['[ ]','[ ]','[ ]','[ ]']
layer1=['[ ]','[ ]','[ ]','[ ]']
layer2=['[ ]','[ ]','[ ]','[ ]']
layer3=['[ ]','[ ]','[ ]','[ ]']
layer4=['[ ]','[ ]','[ ]','[ ]']
langlaman=['[ ]','[ ]','[ ]','[ ]']

main11= ['[ ]','[ ]','[ ]']
layer11=['[ ]','[ ]','[ ]']
layer22=['[ ]','[ ]','[ ]']
layer33=['[ ]','[ ]','[ ]']
layer44=['[ ]','[ ]','[ ]']

main111= ['[ ]','[ ]']
layer111=['[ ]','[ ]']
layer222=['[ ]','[ ]']
layer333=['[ ]','[ ]']
layer444=['[ ]','[ ]']
colselect=0
colselect2=0
colselect3=0
top=['[ ]']
score1=0
score2=0
score3=0
score4=0
def jackpot():
    print("welcome to jackpot round",top[0])
    hello=input("Hello to jackpot round")
#player naming------------------------------------------------------------
def player_naming():
    dagdag=1
    while dagdag!=5:
        players1=input(f"Enter player {dagdag} name: ")
        if players1 in players:
            print(f"The name is already in use.")
        else:
            players.append(players1)
            dagdag+=1
          
          
          



#ex 1

#list daw tawag d2
mgatanong = [["Anong kulay ang kalabaw?", ["Itim", "Black","Brown"]],
             ["ano kulay ng laman ng avocado?", ["Green","Berde"]],
             ["Ilan ang pulo sa Pilipinas?", ["7641"]],
             ["Miss mo?", ["Oo","Hindi","Minsan"]],
             ["Sa kantang Bahay Kubo, ano ang unang gulay na binanggit?", ["Singkamas"]],
             ["Pang ilan ang letrang R sa alphabet?", ["18"]],
             ["Sa E-Vehicles, ano ang ibig sabihin ngh E?", ["Electric","Electronic"]],
             ["Ano sininisimbolo ng kulay asul sa watawat ng Pilipinas?", ["Kapayapaan","Peace","Freedom","Intergrity"]],
             ["Origin ng pandemic na sakit na Covid 19?", ["Wuhan, China","China"]],
             ["Anong blood type ang kino-consider na 'rare'?", ["AB","AB negative","AB-"]],
             ["Doctor na specialist ang pag aaral sa balat ng tao?", ["Dermatologist"]],
             ["Pinaka common na bitamina na nakukuha natin sa prutas na orange?", ["Vitamin C","C"]],
             ["Unang Presidente ng Pilipias? ", ["Emilio Aguinaldo"]],
             ["Pambansang puno ng Pilipinas? ", ["Narra"]],
             ["Anong sport ang may salitang 'Homerun'? ", ["Baseball"]],
             ["Kung ang 7 days ay 'week', ang 12 months naman ay 'taon', ano naman ang 1000 years? ", ["Millennia","Millenium"]],
             ["Anong buan ang may 28 na araw lang? ", ["Lahat"]],
             ["Ano ang tawag sa mga taong nag aaral tungkol sa mga halaman? ", ["Botanist"]],
             ["Kung ang meteorite ay naglalakbay sa ating atmosphere, ano naman ang tawag dito pag ito'y nasa loob na ng atmospera ng Mundo? ",
              ["Meteor"]],
             ["Anong hayop ang binabansagan na 'man's bestfriend? ", ["Aso","Dog"]],
             ["Saan binaril ang ating pambansang bayani na si Jose Rizal? ", ["Sa likod","Bagumbayan","Luneta Park","Rizal Park"]],
             ["sa Periodic Table ano ang sinisimbolo ng letrang 'Na'? ", ["Sodium"]],
             ["Anong kulay  ng apoy ang pinaka mainit? ", ["Blue"]],
             ["Anong petsa ang araw ng kalayaan sa Pilipinas? ", ["Hunyo 12","July 12"]],
             ["Anong sport ang may player na tinatawag na Libero? ", ["Volleyball"]],
             ["Sino ang pumatay sa banyagang nagngangalang na Ferdinand Magellan? ", ["Lapu lapu"]],
             ["Ano ang probability mo na lalabas ang 6 na sagot sa die? ", ["6", "Anim"]],
             ["Sa Science, ano ang tawag sa proseso ng gas to liquid? ", ["Condensation"]],
             ["Kung ang aso ay Canine, ano naman ang mga pusa? ", ["Feline"]],
             ["Ano ang kapital ng pilipinas? ", ["Manila"]],
             ["Sino ang singers ng bandang ben&ben? ", ["Paolo and Miguel Benjamin Guico"]],
             ["Ano ang pambansang dahon ng pilipinas? ", ["Anahaw"]],
             ["Ibigay ang ingles ng hagdan-handang palayan? ", ["Banaue Rice Terraces"]],
             ["Kung life ay buhay ano naman ang lovelife? ", ["buhay pag-ibig"]],
             ["Anong tawag sa malaking virus ang kumalat noong 2019? ", ["COVID-19"]],
             ["Isang Prinsesa, nakaupo sa tasa? ", ["Kasoy"]],
             ["Ayon sa mga kwentong-bayan ano ang hawak hawak ng kapre? ", ["Tobacco","Tabako"]],
             ["Si Olaf ng Frozen ay isang? ", ["Snowman"]],
             ["Kilala ang Marikina sa? ", ["Shoe Capital of the Philippines"]],
             ["Ano ang tawag sa pera ng pilipinas? ", ["Peso","Pesos"]],
             ["Kung ang ina ay ilaw ng tahanan ano naman ang sa ama? ", ["Haligi ng tahanan]"]],
             ["Ano naman ang pambansang isda ng pilinas? ", ["Bangus"]],
             ["Sino ang kasalukuyang kurakot na presidente ng pilipinas? ", ["Bongbong Marcos"]],
             ["Ano ang kahulugan ng PBB? ", ["Pinoy Big Brother"]],
             ["Ano ang pinaka mataas na bundok sa Pilipinas? ", ["Mt. Apo"]],
             ["Ano ang pinakamatandang lungsod sa Pilipinas? ", ["Cebu"]],
             ["Saan matatagpuan ang Chocolate Hills? ", ["Bohol"]],
             ["Ano ang pambansang ulam ng mga Pilipino? ", ["Adobo"]],
             ["Ilang ang rehiyon sa Pilipinas? ", ["17"]],
             ["Ano ang pinakamahabang ilog sa Pilipinas? ", ["Cagayan River"]],
             ["Ilang beses nabanggit ang salitang 'twinkle' sa kantang 'Twinkle, Twinkle, Litle Star'? ", ["6"]],
             ["Ano ang English ng bangus? ", ["Milkfish"]],
             ["Bugtong: Kung Kailan mo pinatay, saka pa humaba ang buhay? ", ["kandila"]],
             ["Bugtong: Hindi hari, hindi pari,nagsusuot ng sari-sari? ", ["Sampayan"]],
             ["Ano ang kinagat ni Snow White? ", ["Apple","Mansanas"]],
             ["Sino ang Disney Princess na nagmamay-ari ng glass na heels? ", ["Cinderella"]],
             ["Sino ang Presidenteng palamura? ", ["Duterte","Rodrigo Duterte","Digong"]],
             ["Ano ang unang araw sa isang linggo? ", ["Sunday"]],
             ["Anong larong kalye ang ginagamitan ng lata at tsinelas? ", ["Tumbang preso"]],
             ["Anong larong kalye ang ginagamitan ng garter o kaya naman rubber band? ", ["Chinese garter"]],
             ["Ilan ang kulay ng watawat ng Pilipinas? ", ["4","Apat"]],
             ["Ilan ang standard players ng basketball? ", ["5","Lima"]],
             ["Ilan ang bola sa bilyar? ", ["15"]],
             ["Anong laro ang may player na tinatawag na libero? ", ["Volleyball"]],
             ["Ano ang English ng butanding? ", ["Whale Shark"]],
             ["Anong kulay ni Majin buu? ", ["Pink"]],
             ["Kung ang bulak ay cotton, ano naman ang bulaklak? ", ["Flowers","Flower"]],
             ["Ano ang tawag sa batang kangaroo? ", ["Joey"]],
             ["Kung English ng ulo ay head, ano naman ang noo? ", ["Forehead"]],
             ["Kung 5 ang daliri mo sa isang kamay, ilan naman ang daliri mo sa paa? ", ["10","Sampo"]],
             ["Bugtong: Buhok ni Adan hindi mabilang-bilang? ", ["Ulan"]],
             ["Bugtong: Nung bata apat ang paa, nung nagbinata dalawa ang paa, nung tumanda naging 3 naman ang paa? ",
              ["Tao"]],
             ["Kung ang tricycle ay may tatlong gulong at na-flat ang isa, ilan nalang ang natira? ", ["3","Tatlo"]],
             ["kung ang buko ay coconut ano naman ang English ng kubo? ", ["nipa hut","hut","cottage"]]]
bilang=72
#question shuffleeeeeeee--------------------------------------------------------------------------------------------------
def print_pyramid():
    print("Main Pyramid:")
    print("        ", top)
    print("     ", main111)
    print("   ", main11)
    print(main1)
    print("\nLayers:")
    print(layer1)
    print(layer2)
    print(layer3)
    print(layer4)
    print("\n")
def randquest():
    global bilang
    global randoms
    
    
    while bilang>=0:
        if score1==4 or score2==4 or score3==4 or score4==4:
            print('Main pyramid')
            top[0]=players[sasagot]
            print("        ",top)
            print("    ",main111)
            print("  ",main11)
            print(main1)
            print('\n\n\n')
            print(layer1)
            print(layer2)
            print(layer3)
            print(layer4)
            jackpot()
        print("Main Pyramid:")
        print("        ", top)
        print("     ", main111)
        print("   ", main11)
        print(main1)
        randoms = random.randint(0, bilang)
        
        print(mgatanong[randoms][0])
        if layer11[colselect2]==players[0] and layer22[colselect2]==players[1] or layer11[colselect2]==players[0] and layer33[colselect2]==players[2] or layer11[colselect2]==players[0] and layer44[colselect2]==players[3] or layer1[colselect]==players[0] and layer2[colselect]==players[1] or layer1[colselect]==players[0] and layer3[colselect]==players[2] or layer1[colselect]==players[0] and layer4[colselect]==players[3]:
            laban1()
        elif layer111[colselect3]==players[0] and layer222[colselect3]==players[1] or layer111[colselect3]==players[0] and layer333[colselect3]==players[2] or layer111[colselect3]==players[0] and layer444[colselect3]==players[3] or layer222[colselect3]==players[1] and layer333[colselect3]==players[2] or layer444[colselect3]==players[3] and layer333[colselect3]==players[2] or layer444[colselect3]==players[3] and layer333[colselect3]==players[2]:
            laban1()
        else:
            paunahan()
        
        
        bilang-=1
    

#check ans---------------------------------------------------------------------------------------------------------
def print_pyramid2():
            
            print("laban2")
            print('Main pyramid')
            print("        ",top)
            print("    ",main111)
            print("  ",main11)
            print(main1)
            print('\n\n\n')
            print(layer11)
            print(layer22)
            print(layer33)
            print(layer44)     
    
def print_pyramid3():
            
            print("laban2")
            print('Main pyramid')
            print("        ",top)
            print("    ",main111)
            print("  ",main11)
            print(main1)
            print('\n\n\n')
            print(layer111)
            print(layer222)
            print(layer333)
            print(layer444)             
#player selection------------------------------------------------------------------------------------------------
def paunahan():
    global sasagot
    global score1
    global score2
    global score3
    global score4
    
    sasagot=int(input("Sino ang mauuna:  "))
    match sasagot:
        case 1:
            print("SASAGOT: ",players[0])
            sasagot-=1
            sagot = input("SAGOT: ").lower()
            if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                print('edi wow')
                score1+=1
                if score1==1:
                    ascension1()
                elif score1==2:
                    ascension2()
                elif score1==3:
                    ascension3()
            else:
                print('luh')
            mgatanong.pop(randoms)
        case 2:
            print("SASAGOT: ",players[1])
            sasagot-=1
            sagot = input("SAGOT: ").lower()
            if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                print('edi wow')
                score2+=1
                if score2==1:
                    ascension1()
                elif score2==2:
                    ascension2()
                elif score1==3:
                    ascension3()
                
                    
            else:
                print('luh')
            mgatanong.pop(randoms)
        case 3:
            print("SASAGOT: ",players[2])
            sasagot-=1
            sagot = input("SAGOT: ").lower()
            if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                print('edi wow')
                score3+=1
                if score3==1:
                    ascension1()
                elif score3==2:
                    ascension2()
                elif score1==3:
                    ascension3()
            else:
                print('luh')
                mgatanong.pop(randoms)
        case 4:
            print("SASAGOT: ",players[3])
            sasagot-=1
            sagot = input("SAGOT: ").lower()
            if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                print('edi wow')
                score4+=1
                if score4==1:
                    ascension1()
                elif score4==2:
                    ascension2()
            else:
                print('luh')
            mgatanong.pop(randoms)
        
def laban1():
        global score1
        global score2
        global score3
        global score4
        global layer1
        global layer2
        global layer4
        global randoms
        # global score2
        global layer3
        global layer11
        global layer22
        global layer44
        global randoms
        global layer33
        global layer111
        global layer222
        global layer444
        global randoms
        global layer333
    
        
        # 11111111111111111111111111111111 11111111111111                               22222222222222222222222222222222222222222222222222222222222222
        if layer1[colselect]==players[0] and layer2[colselect]==players[1]:
            print("Tile Breaker")
            
            print_pyramid()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 1 vs player 2")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 1:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main1[colselect]==players[1]:
                        main1[colselect]=players[0]
                    
                    score2-=1
                    layer2=langlaman    
                else:
                    print('luh')
                print(score1)
                print (score2)
                mgatanong.pop(randoms)
            if sasagot== 2:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main1[colselect]==players[0]:
                        main1[colselect]=players[1]
                        
                    score1-=1
                    layer1=langlaman    
                
                else:
                    print('luh')
                print(score1)
                print (score2)
                mgatanong.pop(randoms)      
                
               
         #111111111111111111111111111111111111111111111111111111111111111111111111111                                      3333333333333333333333333333333333333333333333333333333 
        if layer1[colselect]==players[0] and layer3[colselect]==players[2]:
            print("Tile Breaker")
            
            print_pyramid()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 1 vs player 3")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 1:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main1[colselect]==players[2]:
                        main1[colselect]=players[0]
                    
                    score3-=1
                    layer3=langlaman    
                else:
                    print('luh')
                print(score1)
                print (score3)
                mgatanong.pop(randoms)
            if sasagot== 3:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main1[colselect]==players[0]:
                        main1[colselect]=players[2]
                        
                    score1-=1
                    layer1=langlaman    
                
                else:
                    print('luh')
                print(score1)
                print (score3)
                mgatanong.pop(randoms)      
                    
        
        #1111111111111111111111111111111111111111111111111111111111                                  4444444444444444444444444444444444444444444444444444444444
        if layer1[colselect]==players[0] and layer4[colselect]==players[3]:
            print("Tile Breaker")
            
            print_pyramid()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 1 vs player 4")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 1:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main1[colselect]==players[3]:
                        main1[colselect]=players[0]
                    
                    score4-=1
                    layer4=langlaman    
                else:
                    print('luh')
                print(score1)
                print (score4)
                mgatanong.pop(randoms)
            if sasagot== 4:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main1[colselect]==players[0]:
                        main1[colselect]=players[3]
                        
                    score1-=1
                    layer4=langlaman    
                
                else:
                    print('luh')
                print(score1)
                print (score4)
                mgatanong.pop(randoms)     
                
        #2222222222222222222222222222222222222222222--------------------------------------------------------------33333333333333333333333333333333333333333333333
        
        
        if layer2[colselect]==players[1] and layer3[colselect]==players[2]:
            print("Tile Breaker")
            
            print_pyramid()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 2 vs player 4")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 2:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main1[colselect]==players[2]:
                        main1[colselect]=players[1]
                    
                    score3-=1
                    layer3=langlaman    
                else:
                    print('luh')
                print(score2)
                print (score3)
                mgatanong.pop(randoms)
            if sasagot== 3:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main1[colselect]==players[1]:
                        main1[colselect]=players[2]
                        
                    score1-=1
                    layer1=langlaman    
                
                else:
                    print('luh')
                print(score2)
                print (score3)
                mgatanong.pop(randoms)       
             
    
        #333333333333333333333333333333333333333333333333333333333----------------------------------------------------------4444444444444444444444444444444444444444444
        
        if layer4[colselect]==players[3] and layer3[colselect]==players[2]:
            print("Tile Breaker")
            
            print_pyramid()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 3 vs player 4")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 3:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main1[colselect]==players[3]:
                        main1[colselect]=players[2]
                    
                    score4-=1
                    layer4=langlaman    
                else:
                    print('luh')
                print(score4)
                print (score3)
                mgatanong.pop(randoms)
            if sasagot== 4:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main1[colselect]==players[2]:
                        main1[colselect]=players[3]
                        
                    score3-=1
                    layer3=langlaman    
                
                else:
                    print('luh')
                print(score4)
                print (score3)
                mgatanong.pop(randoms)   
        
        
        #222222222222222222222222222222222222222222222222222222222222222222222---------------------------------------------4444444444444444444444444444444444
        
        
        if layer4[colselect]==players[3] and layer2[colselect]==players[1]:
            print("Tile Breaker")
            
            print_pyramid()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 2 vs player 4")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 2:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main1[colselect]==players[3]:
                        main1[colselect]=players[1]
                    
                    score4-=1
                    layer4=langlaman    
                else:
                    print('luh')
                print(score4)
                print (score2)
                mgatanong.pop(randoms)
            if sasagot== 4:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main1[colselect]==players[1]:
                     main1[colselect]=players[3]
                        
                    score2-=1
                    layer2=langlaman    
                
                else:
                    print('luh')
                print(score2)
                print (score4)
                mgatanong.pop(randoms)           
                
           
        # 11111111111111111111111111111111 11111111111111                               22222222222222222222222222222222222222222222222222222222222222
        if layer11[colselect2]==players[0] and layer22[colselect2]==players[1]:
            print("Tile Breaker")
            print_pyramid2()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 1 vs player 2")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 1:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main11[colselect2]==players[1]:
                        main11[colselect2]=players[0]
                    
                    score2-=1
                    layer22=langlaman    
                else:
                    print('luh')
                print(score1)
                print (score2)
                mgatanong.pop(randoms)
            if sasagot== 2:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main11[colselect2]==players[0]:
                        main11[colselect2]=players[1]
                        
                    score1-=1
                    layer11=langlaman    
                
                else:
                    print('luh')
                print(score1)
                print (score2)
                mgatanong.pop(randoms)      
                
               
         #111111111111111111111111111111111111111111111111111111111111111111111111111                                      3333333333333333333333333333333333333333333333333333333 
        if layer11[colselect2]==players[0] and layer33[colselect2]==players[2]:
            print("Tile Breaker")
            
            print_pyramid2()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 1 vs player 3")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 1:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main11[colselect2]==players[2]:
                        main11[colselect2]=players[0]
                    
                    score3-=1
                    layer33=langlaman    
                else:
                    print('luh')
                print(score1)
                print (score3)
                mgatanong.pop(randoms)
            if sasagot== 3:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main11[colselect2]==players[0]:
                        main11[colselect2]=players[2]
                        
                    score1-=1
                    layer11=langlaman    
                
                else:
                    print('luh')
                print(score1)
                print (score3)
                mgatanong.pop(randoms)      
                    
        
        #1111111111111111111111111111111111111111111111111111111111                                  4444444444444444444444444444444444444444444444444444444444
        if layer11[colselect2]==players[0] and layer44[colselect2]==players[3]:
            print("Tile Breaker")
            
            print_pyramid2()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 1 vs player 4")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 1:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main11[colselect2]==players[3]:
                        main11[colselect2]=players[0]
                    
                    score4-=1
                    layer44=langlaman    
                else:
                    print('luh')
                print(score1)
                print (score4)
                mgatanong.pop(randoms)
            if sasagot== 4:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main11[colselect2]==players[0]:
                        main11[colselect2]=players[3]
                        
                    score1-=1
                    layer44=langlaman    
                
                else:
                    print('luh')
                print(score1)
                print (score4)
                mgatanong.pop(randoms)     
                
        #2222222222222222222222222222222222222222222--------------------------------------------------------------33333333333333333333333333333333333333333333333
        
        
        if layer22[colselect2]==players[1] and layer33[colselect2]==players[2]:
            print("Tile Breaker")
            
            print_pyramid2()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 2 vs player 3")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 2:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main11[colselect2]==players[2]:
                        main11[colselect2]=players[1]
                    
                    score3-=1
                    layer33=langlaman    
                else:
                    print('luh')
                print(score2)
                print (score3)
                mgatanong.pop(randoms)
            if sasagot== 3:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main11[colselect2]==players[1]:
                        main11[colselect2]=players[2]
                        
                    score1-=1
                    layer11=langlaman    
                
                else:
                    print('luh')
                print(score2)
                print (score3)
                mgatanong.pop(randoms)       
             
    
        #333333333333333333333333333333333333333333333333333333333----------------------------------------------------------4444444444444444444444444444444444444444444
        
        if layer44[colselect2]==players[3] and layer33[colselect2]==players[2]:
            print("Tile Breaker")
            
            print_pyramid2()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 3 vs player 4")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 3:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main11[colselect2]==players[3]:
                        main11[colselect2]=players[2]
                    
                    score4-=1
                    layer44=langlaman    
                else:
                    print('luh')
                print(score4)
                print (score3)
                mgatanong.pop(randoms)
            if sasagot== 4:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main11[colselect2]==players[2]:
                        main11[colselect2]=players[3]
                        
                    score3-=1
                    layer33=langlaman    
                
                else:
                    print('luh')
                print(score4)
                print (score3)
                mgatanong.pop(randoms)   
        
        
        #222222222222222222222222222222222222222222222222222222222222222222222---------------------------------------------4444444444444444444444444444444444
        
        
        if layer44[colselect2]==players[3] and layer22[colselect2]==players[1]:
            print("Tile Breaker")
            
            print_pyramid2()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 2 vs player 4")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 2:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main11[colselect2]==players[3]:
                        main11[colselect2]=players[1]
                    
                    score4-=1
                    layer44=langlaman    
                else:
                    print('luh')
                print(score4)
                print (score2)
                mgatanong.pop(randoms)
            if sasagot== 4:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main11[colselect2]==players[1]:
                        main11[colselect2]=players[3]
                        
                    score2-=1
                    layer22=langlaman    
                
                else:
                    print('luh')
                print(score2)
                print (score4)
                mgatanong.pop(randoms)  
        
        # 11111111111111111111111111111111 11111111111111                               22222222222222222222222222222222222222222222222222222222222222
        if layer111[colselect3]==players[0] and layer222[colselect3]==players[1]:
            print("Tile Breaker")
            print_pyramid3()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 1 vs player 2")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 1:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main111[colselect3]==players[1]:
                        main111[colselect3]=players[0]
                    
                    score2-=1
                    layer222=langlaman    
                else:
                    print('luh')
                print(score1)
                print (score2)
                mgatanong.pop(randoms)
            if sasagot== 2:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main111[colselect3]==players[0]:
                        main111[colselect3]=players[1]
                        
                    score1-=1
                    layer111=langlaman    
                
                else:
                    print('luh')
                print(score1)
                print (score2)
                mgatanong.pop(randoms)      
                
               
         #111111111111111111111111111111111111111111111111111111111111111111111111111                                      3333333333333333333333333333333333333333333333333333333 
        if layer111[colselect3]==players[0] and layer333[colselect3]==players[2]:
            print("Tile Breaker")
            print_pyramid3()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 1 vs player 3")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 1:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main111[colselect3]==players[2]:
                        main111[colselect3]=players[0]
                    
                    score3-=1
                    layer333=langlaman    
                else:
                    print('luh')
                print(score1)
                print (score3)
                mgatanong.pop(randoms)
            if sasagot== 3:
                
                print("SASAGOT: ",players[sasagot-1])
                print("ikaw number 3")
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main111[colselect3]==players[0]:
                        main111[colselect3]=players[2]
                    print("Updated main111[colselect3]:", main111[colselect3])
                    score1-=1
                    layer111=langlaman    
                
                else:
                    print('luh')
                print(score1)
                print (score3)
                mgatanong.pop(randoms)      
                    
        
        #1111111111111111111111111111111111111111111111111111111111                                  4444444444444444444444444444444444444444444444444444444444
        if layer111[colselect3]==players[0] and layer444[colselect3]==players[3]:
            print("Tile Breaker")
            
            print_pyramid3()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 1 vs player 4")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 1:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main111[colselect3]==players[3]:
                        main111[colselect3]=players[0]
                    
                    score4-=1
                    layer444=langlaman    
                else:
                    print('luh')
                print(score1)
                print (score4)
                mgatanong.pop(randoms)
            if sasagot== 4:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main111[colselect3]==players[0]:
                        main111[colselect3]=players[3]
                        
                    score1-=1
                    layer444=langlaman    
                
                else:
                    print('luh')
                print(score1)
                print (score4)
                mgatanong.pop(randoms)     
                
        #2222222222222222222222222222222222222222222--------------------------------------------------------------33333333333333333333333333333333333333333333333
        
        
        if layer222[colselect3]==players[1] and layer333[colselect3]==players[2]:
            print("Tile Breaker")
            
            print_pyramid3()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 2 vs player 3")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 2:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main111[colselect3]==players[2]:
                        main111[colselect3]=players[1]
                    
                    score3-=1
                    layer333=langlaman    
                else:
                    print('luh')
                print(score2)
                print (score3)
                mgatanong.pop(randoms)
            if sasagot== 3:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main111[colselect3]==players[1]:
                        main111[colselect3]=players[2]
                        
                    score1-=1
                    layer111=langlaman    
                
                else:
                    print('luh')
                print(score2)
                print (score3)
                mgatanong.pop(randoms)       
             
    
        #333333333333333333333333333333333333333333333333333333333----------------------------------------------------------4444444444444444444444444444444444444444444
        
        if layer444[colselect3]==players[3] and layer333[colselect3]==players[2]:
            print("Tile Breaker")
            
            print_pyramid3()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 3 vs player 4")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 3:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main111[colselect3]==players[3]:
                        main111[colselect3]=players[2]
                    
                    score4-=1
                    layer444=langlaman    
                else:
                    print('luh')
                print(score4)
                print (score3)
                mgatanong.pop(randoms)
            if sasagot== 4:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main111[colselect3]==players[2]:
                        main111[colselect3]=players[3]
                        
                    score3-=1
                    layer333=langlaman    
                
                else:
                    print('luh')
                print(score4)
                print (score3)
                mgatanong.pop(randoms)   
        
        
        #222222222222222222222222222222222222222222222222222222222222222222222---------------------------------------------4444444444444444444444444444444444
        
        
        if layer444[colselect2]==players[3] and layer222[colselect2]==players[1]:
            print("Tile Breaker")
            
            print_pyramid3()
            randoms = random.randint(0, bilang)
            print(mgatanong[randoms][0])
            print("player 2 vs player 4")
            sasagot=int(input("Sino ang mauuna:  "))
            
            
            if sasagot== 2:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('edi wow')
                            
                    if main111[colselect3]==players[3]:
                        main111[colselect3]=players[1]
                    
                    score4-=1
                    layer444=langlaman    
                else:
                    print('luh')
                print(score4)
                print (score2)
                mgatanong.pop(randoms)
            if sasagot== 4:
                
                print("SASAGOT: ",players[sasagot-1])
                
                sagot = input("SAGOT: ").lower()
                if sagot in [answer.lower() for answer in mgatanong[randoms][1]]:
                    print('tama ka',sasagot)
                        
                    if main111[colselect3]==players[1]:
                        main111[colselect3]=players[3]
                        
                    score2-=1
                    layer222=langlaman    
                
                else:
                    print('luh')
                print(score2)
                print (score4)
                mgatanong.pop(randoms)  
                                  
#ascension----------------------------------------------------------------------------------------------------
def ascension1():
    global colselect
    colselect=random.randint(0,3)
    # colselect=0
    print(players[sasagot])
    main1[colselect]=players[sasagot]
    if sasagot==0:
        layer1[colselect]=players[sasagot]
    if sasagot==1:
        layer2[colselect]=players[sasagot]
    if sasagot==2:
        layer3[colselect]=players[sasagot]
    if sasagot==3:
        layer4[colselect]=players[sasagot]
    laban1()
    print('Main pyramid')
    print("        ",top)
    print("    ",main111)
    print("  ",main11)
    print(main1)
    print('\n\n\n')
    print(layer1)
    print(layer2)
    print(layer3)
    print(layer4)
    

def ascension2():
    colselect2=random.randint(0,2)
    
    print(players[sasagot])
    main11[colselect2]=players[sasagot]
    if sasagot==0:
        layer11[colselect2]=players[sasagot]
       
    if sasagot==1:
        layer22[colselect2]=players[sasagot]
    if sasagot==2:
        layer33[colselect2]=players[sasagot]
    if sasagot==3:
        layer44[colselect2]=players[sasagot]
    print('Main pyramid')
    print("        ",top)
    print("    ",main111)
    print("  ",main11)
    print(main1)
    print('\n\n\n')
    print(layer11)
    print(layer22)
    print(layer33)
    print(layer44)

def ascension3():
    colselect3=random.randint(0,1)
    # colselect3=0
    print(players[sasagot])
    main111[colselect3]=players[sasagot]
    if sasagot==0:
        layer111[colselect3]=players[sasagot]
       
    if sasagot==1:
        layer222[colselect3]=players[sasagot]
    if sasagot==2:
        layer333[colselect3]=players[sasagot]
    if sasagot==3:
        layer444[colselect3]=players[sasagot]
    print('Main pyramid')
    print("        ",top)
    print("    ",main111)
    print("  ",main11)
    print(main1)
    print('\n\n\n')
    print(layer111)
    print(layer222)
    print(layer333)
    print(layer444)




name=True       
while name==True:
    player_naming()
    randquest()

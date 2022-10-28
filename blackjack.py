import random
import time
#定数
BLACK_JACK = 21
Card_Number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
Card_Mark =  ["♠","♣","♥","♦"]
Start_Tip = 10000
PLAYER = 0
DEALER = 1
END = 1
NOT_END = 0
#--------------------------------------------------
class Me:
    tip = 0
    cards = []
    sum = 0
    def __init__(self,tip):
        self.tip = tip

class dealer:
    cards = []
    sum = 0

def Bet(m):
    print("How much to bet？")
    while(True):
        print("→",end="")
        try:
            t = int(input())
            print()
        except:
            t = -1
            pass
        if t >= 0 and m.tip - t >= 0:
            while(True):
                print("Really?")
                print("0:yes,1:no")
                print("→",end="")
                try:
                   really = int(input())
                except:
                   really = -1
                if really == 0:
                    break
                elif really == 1:
                    print("How much to bet？")
                    t = -1
                    break
            if t >= 0:
                m.tip -= t
                break
        else:
            print("How much to bet？")
    print()
    return t

def Start_Call():
    already_cards = []
    print("Place your bet...")

def Distribute_Card():
    while(1):
        num = random.randint(0,51)
        if num in already_cards:
            continue
        already_cards.append(num)
        break
    return num


def Cul_Sum(Card):
    sum = 0
    ace_num = 0
    for i in Card:
        num = (i % 13) + 1
        if num > 10:
            num = 10

        if num == 1:
            ace_num += 1
            continue
        sum += num
    for i in range(ace_num):
        rest = ace_num - (i+1)
        if sum + 11 + rest <= BLACK_JACK:
            sum += 11
        else:
            sum += 1

    return sum

def Find_Mark_And_Number(N):
    mark = int(N/13)
    array_num = N%13
    print(str(Card_Mark[mark]) + str(Card_Number[array_num]),end = "")

def Player_Or_Dealer(PoD,Card):
    if PoD == PLAYER:
        print("Player: ",end = "")
    else:
        print("Dealer: ",end = "")
    for i,c in enumerate(Card):
        Find_Mark_And_Number(c)
        if i != len(Card) - 1:
            print(",",end = "")
    print()

def Game(me,de):
    end = 0
    me.cards = []
    de.cards = []
    #最初の手順
    print()
    me.cards.append(Distribute_Card())
    me.cards.append(Distribute_Card())
    me.sum = Cul_Sum(me.cards)

    de.cards.append(Distribute_Card())
    de.cards.append(Distribute_Card())
    de.sum = Cul_Sum(de.cards)

    #player
    print("---------------------------------------------------------------------------------------------------")
    Player_Or_Dealer(PLAYER,me.cards)
    print("Dealer: ",end = "")
    Find_Mark_And_Number(de.cards[0])
    print()
    print("---------------------------------------------------------------------------------------------------")
    while(True):
        print("hit(0) or end(1)?")
        print("→",end="")
        try:
            hit_or_end = int(input())
        except:
            hit_or_end = -1
            pass
        if hit_or_end in [0,1]:
            #end
            if hit_or_end == 1:
                break
            #hit
            elif hit_or_end == 0:
                print("---------------------------------------------------------------------------------------------------")
                me.cards.append(Distribute_Card())
                me.sum = Cul_Sum(me.cards)
                Player_Or_Dealer(PLAYER,me.cards)
                print("Dealer: ",end = "")
                Find_Mark_And_Number(de.cards[0])
                print()
                print("---------------------------------------------------------------------------------------------------")
                if me.sum > BLACK_JACK:
                    end = END
                    print("Result:You Lose")
                    return 0
        else:
            print("enter the key 0 or 1")

    if end != END:
        #dealer
        while(True):
            print("---------------------------------------------------------------------------------------------------")
            Player_Or_Dealer(PLAYER,me.cards)
            Player_Or_Dealer(DEALER,de.cards)
            print("---------------------------------------------------------------------------------------------------")
            if de.sum < 17:
                de.cards.append(Distribute_Card())
                de.sum = Cul_Sum(de.cards)
                print()
            else:
                print()
                break

        print("Player Point: "+str(me.sum))
        print("Dealer Point: "+str(de.sum))
        time.sleep(1)
        print()

        #judge
        if me.sum > de.sum or de.sum > BLACK_JACK:
            if me.sum == BLACK_JACK:
                print("★BLACK_JACK★")
            print("Result:You Win!")
            return int(BLACK_JACK - abs(BLACK_JACK - me.sum))
        elif me.sum < de.sum:
            if de.sum == BLACK_JACK:
                print("★BLACK_JACK★")
            print("Result:You Lose")
            return 0
        else:
            print("Result:DRAW")
            return -1


me = Me(Start_Tip)
de = dealer()
play_num = 0
while(True):
    bet = 0
    start = -1
    already_cards = []
    print("Your tip: ",end="")
    print("{0}".format(me.tip))
    print()
    print("Are you ready to start the game?")
    print("0:yes,1:no")
    print("→",end="")
    while(True):
        try:
            start = int(input())
        except:
            start = -1
        if start == 0 or start == 1:
            break
    if start == 1:
        print("Thanks for Playing!!({0} play)".format(play_num))
        break
    play_num += 1
    print() 
    Start_Call()
    bet = Bet(me)
    print("Let the games begin!")
    result = Game(me,de)
    print()
    if result ==  - 1:
        print("Return your tip...")
        print()
        continue
    me.tip += (result * bet)
    print("You got {0}".format(result * bet))
    print("---------------------------------------------------------------------------------------------------")

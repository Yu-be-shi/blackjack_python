import random
import time
#定数
BLACK_JACK = 21
Card_Number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
Card_Mark =  ["♠","♣","♥","♦"]
Start_bet = 10000
PLAYER = 0
DEALER = 1
#--------------------------------------------------
class Me:
    bet = 0
    cards = []
    sum = 0
    def __init__(self,bet):
        self.bet = bet

class dealer:
    cards = []
    sum = 0

#---------------------------------------------------

def Placing_Bet(m):
    while(True):
        print("How much to bet？")
        print("→",end="")
        try:
            t = int(input())
            print()
        except:
            t = -1
            pass
        if t >= 0 and m.bet - t >= 0:
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
                    t = -1
                    break
            if t >= 0:
                m.bet -= t
                break
        print()
    print()
    return t

def Print_Divide(n):
    if n == 0:
        print()
        print("♠"*100)
        print()
    if n == 1:
        print()
        print("♣"*100)
        print()
    if n == 2:
        print()
        print("♥"*100)
        print()
    if n == 3:
        print()
        print("♦"*100)
        print()

def Start_Call():
    print("Place your bet...")

def Distribute_Card():
    while(True):
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
    me.cards = []
    de.cards = []
    me.cards.append(Distribute_Card())
    me.cards.append(Distribute_Card())
    me.sum = Cul_Sum(me.cards)

    de.cards.append(Distribute_Card())
    de.cards.append(Distribute_Card())
    de.sum = Cul_Sum(de.cards)

    #player
    print("-" * 100)
    Player_Or_Dealer(PLAYER,me.cards)
    Player_Or_Dealer(DEALER,[de.cards[0]])
    print("-" * 100)
    print()
    while(True):
        print("0:Hit or 1:End?")
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
                print("-" * 100)
                me.cards.append(Distribute_Card())
                me.sum = Cul_Sum(me.cards)
                Player_Or_Dealer(PLAYER,me.cards)
                Player_Or_Dealer(DEALER,[de.cards[0]])
                print("-" * 100)
                print()
                if me.sum > BLACK_JACK:
                    time.sleep(3)
                    Print_Divide(1)
                    print("Bust!Your point:{0}".format(me.sum))
                    print("Result: You lose")
                    return 0
        else:
            print("Press the key 0 or 1")
    print()
    #dealer
    print("Next: Dealer's Turn",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print()
    turn = 1
    while(True):
        print("Turn over the card... ({0})".format(turn))
        time.sleep(1)
        print("-" * 100)
        Player_Or_Dealer(PLAYER,me.cards)
        Player_Or_Dealer(DEALER,de.cards)
        print("-" * 100)
        print()
        if de.sum < me.sum:
            turn += 1
            de.cards.append(Distribute_Card())
            de.sum = Cul_Sum(de.cards)
        else:
            break

    time.sleep(3)
    Print_Divide(1)
    print("Player point: "+str(me.sum))
    print("Dealer point: "+str(de.sum))
    print()
    #judge
    if me.sum > de.sum or de.sum > BLACK_JACK:
        if me.sum == BLACK_JACK:
            print("★BLACK_JACK★")
            print()
        if de.sum > BLACK_JACK:
            print("Dealer busts!")
            print()
        print("Result: You win!")
        return int(BLACK_JACK - abs(BLACK_JACK - me.sum))
    elif me.sum <= de.sum:
        if de.sum == BLACK_JACK:
            print("★BLACK_JACK★")
            print()
        print("Result: You lose")
        return 0
    else:
        print("Result: Draw")
        return -1

#---------------------------------------------------

me = Me(Start_bet)
de = dealer()
play_num = 0
while(True):
    if me.bet <= 0:
        print("Game over!({0} play)".format(play_num))
        print()
        break
    place_bet = 0
    start = -1
    already_cards = []
    print("Your bet: ",end="")
    print("{0}".format(me.bet))
    print()
    print("Are you ready to start the game?")
    print("0:yes,1:no")
    print("→",end="")
    while(True):
        try:
            start = int(input())
            print() 
        except:
            start = -1
        if start == 0 or start == 1:
            break
    if start == 1:
        Print_Divide(2)
        print("Thanks for playing!!({0} play,point:{1})".format(play_num,me.bet))
        print()
        break

    Start_Call()
    play_num += 1
    place_bet = Placing_Bet(me)
    Print_Divide(0)
    print("Let the games begin!")
    print()
    result = Game(me,de)
    print()
    if result ==  - 1:
        me.bet += place_bet
        print("Return your bet...")
        print("-" * 100)
        continue
    _bet = int((result * place_bet)/10)
    me.bet += _bet
    print("You got {0}".format(_bet))
    Print_Divide(3)

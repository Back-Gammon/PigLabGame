import random

def Hold_at_20(int):
    sum = 0
    while sum < 20 and sum+int < 100:
        roll = random.randrange(1, 7)
        print("Roll: ", roll)
        sum += roll
        if roll == 1:
            sum = 0
            break
    print("Turn total: ", sum)
    return sum

def Hold_at_Whatever(hold):
    sum = 0
    while sum < hold:
        roll = random.randrange(1, 7)
        #print("Roll: ", roll)
        sum += roll
        if roll == 1:
            sum = 0
            break
    #print("Turn total: ", sum)
    return sum

def Holding_to_100():
    hold = int(input("When should the simulation hold?"))
    print("Hold-at-",hold,"turn simulation?")
    num = int(input())
    i = 0
    hundred = 0
    while i < num:
        value = Hold_at_Whatever(hold)
        if value == 100:
            hundred+= 1
        i += 1
    print("Score     Estimated Probability")
    print("100        ",       hundred/num)
    
def Hold_at_20_Outcome():
    num = int(input("Hold-at-20 turn simulation?"))
    i = 0
    zeroes = 0
    twenty = 0
    twentyone = 0
    twentytwo= 0
    twentythree = 0
    twentyfour = 0
    twentyfive = 0
    while i < num:
        value = Hold_at_20()
        if value == 0:
            zeroes+= 1
        elif value == 20:
            twenty+= 1
        elif value == 21:
            twentyone+= 1
        elif value == 22:
            twentytwo+= 1
        elif value == 23:
            twentythree+= 1
        elif value == 24:
            twentyfour+= 1
        elif value == 25:
            twentyfive+= 1
        i += 1
        
    print("Score     Estimated Probability")
    print("0        ",       zeroes/num)
    print("20       ",      twenty/num)
    print("21       ",      twentyone/num)
    print("22       ",      twentytwo/num)
    print("23       ",      twentythree/num)
    print("24       ",      twentyfour/num)
    print("25       ",      twentyfive/num)

def Hold_at_20_or_Goal_Turn():
    og_score = int(input("What is the beginning score?"))
    turn = int(Hold_at_20())
    print("New Score:",     og_score+turn)

def Hold_at_20_or_Goal_Game():
    score = 0
    while score < 100:
        turn_score = Hold_at_20()
        score = score+turn_score
        print("New Score:   ", score)

def holdat20orGoalGame():
    score = 0
    while score < 100:
        turnTotal, newScore = holdat20orGoal(score)
        print("Turn total:", turnTotal)
        print("Score: ", newScore)
        score = newScore

def averagePigTurns():
    totalTurns = 0
    TRIALS = 10000
    for _ in range(TRIALS):
        turns = holdat20orGoalGame()
        totalTurns += turns
    print(totalTurns/TRIALS)
        
def Average_Pig_Turns():
    games = int(input("Games?"))
    total_turns = 0
    i = 0
    while i < games:
        score = 0
        turn = 0
        while score < 100:
            turn_score = Hold_at_20()
            score = score+turn_score
            turn += 1
        total_turns += turn
        i += 1
    print("Average turns:", total_turns/games)

def Two_Player_Pig():
    p2score = 0
    p1score = 0
    while p1score < 100 and p2score < 100:
        print("Player 1 score:", p1score)
        print("Player 2 score:", p2score)
        print("It is player 1's turn")
        turn_score = Hold_at_20()
        p1score = p1score+turn_score
        print("New Score:   ", p1score)
        if p1score < 100:
            print("Player 1 score:", p1score)
            print("Player 2 score:", p2score)
            print("It is player 2's turn")
            turn_score = Hold_at_20()
            p2score = p2score+turn_score
            print("New Score:   ", p2score)
        else:
            break

def Pig_Game():
    p1score = 0
    p2score = 0
    
    choice = random.choice([1, 2])
    if choice == 1:
        print("You will be player 1")
        
    elif choice == 2:
        print("You will be player 2")

    print("Enter nothing to roll; enter anything to hold.")
    
    if choice == 2:
        while p1score < 100 and p2score < 100:
            print("Player 1 score:", p1score)
            print("Player 2 score:", p2score)
            print("It is player 1's turn")
            turn_score = Hold_at_20(p1score)
            p1score = p1score+turn_score
            print("New Score:   ", p1score)
            print("Player 1 score:", p1score)
            print("Player 2 score:", p2score)
            if p1score < 100:
                print("It is player 2's turn")
                answer = ""
                currturntot = 0
                while answer == "" and p2score+currturntot < 100:
                    roll = random.randrange(1, 7)
                    print("Roll: ", roll)
                    currturntot += roll
                    if roll == 1:
                        currturntot = 0
                        print("Turn total: ", currturntot)
                        break
                    print("Turn total: ", currturntot)
                    answer = input("Roll/Hold?")
                print("Turn total: ", currturntot)
                p2score += currturntot
                print("New score: ", p2score)
                
    if choice == 1:
        while p1score < 100 and p2score < 100:
            print("Player 1 score:", p1score)
            print("Player 2 score:", p2score)
            print("It is player 1's turn")
            answer = ""
            currturntot = 0
            while answer == "" and p1score+currturntot < 100:
                roll = random.randrange(1, 7)
                print("Roll: ", roll)
                currturntot += roll
                if roll == 1:
                    currturntot = 0
                    break
                print("Turn total: ", currturntot)
                answer = input("Roll/Hold?")
            print("Turn total: ", currturntot)
            p1score += currturntot
            print("New score: ", p1score)
            print("Player 1 score:", p1score)
            print("Player 2 score:", p2score)
            if p1score <= 100:
                print("It is player 2's turn")
                turn_score = Hold_at_20(p2score)
                p2score = p2score+turn_score
                print("New Score:   ", p2score)
                
                    
Pig_Game()

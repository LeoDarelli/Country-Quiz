#Quiz

input("Welcome to the Country Quiz! Press ENTER to start! ")

print("""
      
180 150W  120W  90W   60W   30W  000   30E   60E   90E   120E  150E 180
|    |     |     |     |     |    |     |     |     |     |     |     |
+90N-+-----+-----+-----+-----+----+-----+-----+-----+-----+-----+-----+
|          . _..::__:  ,-"-"._       |7       ,     _,.__             |
|  _.___ _ _<_>`!(._`.`-.    /        _._     `_ ,_/  '  '-._.---.-.__|
|.{     " " `-==,',._\{  \  / {)     / _ ">_,-' `                mt-2_|
+ \_.:--.       `._ )`^-. "'      , [_/(                       __,/-' +
|'"'     \         "    _L       oD_,--'                )     /. (|   |
|         |           ,'         _)_.\\._<> 6              _,' /  '   |
|         `.         /          [_/_'` `"(                <'}  )      |
+30N       \\    .-. )          /   `-'"..' `:._          _)  '       +
|   `        \  (  `(          /         `:\  > \  ,-^.  /' '         |
|             `._,   ""        |           \`'   \|   ?_)  {\         |
|                `=.---.       `._._       ,'     "`  |' ,- '.        |
+000               |    `-._        |     /          `:`<_|h--._      +
|                  (        >       .     | ,          `=.__.`-'\     |
|                   `.     /        |     |{|              ,-.,\     .|
|                    |   ,'          \   / `'            ,"     \     |
+30S                 |  /             |_'                |  __  /     +
|                    | |                                 '-'  `-'   \.|
|                    |/                                        "    / |
|                    \.                                            '  |
+60S                                                                  +
|                     ,/           ______._.--._ _..---.---------._   |
|    ,-----"-..?----_/ )      _,-'"             "                  (  |
|.._(                  `-----'                                      `-|
+90S-+-----+-----+-----+-----+----+-----+-----+-----+-----+-----+-----+
      
""")

q1 = input("""1. What is the largest country in the world by land area?
      
    a) Brazil
    b) India
    c) USA
    d) Russia
    e) China

Type the letter of the correct option: """).lower()

if q1 == "d":
    print("\nGreat! Let's move on to the next one!")

    q2 = input("""\n2. Which country has the largest population?
     
    a) India
    b) Australia
    c) Japan
    d) China
    e) USA
 
Type the letter of the correct option: """).lower()
    
    if q2 == "a":
        print("\nExcellent! You're doing well!")
        
        q3 = input("""\n3. Which country had the highest GDP in 2023?
         
    a) South Korea
    b) USA
    c) Russia
    d) China
    e) India
                   
Type the letter of the correct option: """).lower()
        
        if q3 == "b":
            print("\nKeep it up, don't stop!")

            q4 = input("""\n4. Which country has the highest Human Development Index (HDI) currently?
    
    a) France
    b) Norway
    c) Germany
    d) Mexico
    e) Switzerland         

Type the letter of the correct option: """).lower()
            
            if q4 == "e":
                print("\nGreat job! Let's move on!")

                q5 = input("""\n5. Which of the following countries are NOT members of the European Union?
    
    a) Poland, England, and Portugal
    b) Turkey, Switzerland, and England
    c) Switzerland, Sweden, and England
    d) Turkey, England, and Belgium
    e) Turkey, Denmark, and England
                           
Type the letter of the correct option: """).lower()
                
                if q5 == "b":
                    print("\nCongratulations! You've completed the quiz!")
                else:
                    print("\nIncorrect answer!\n\nGame Over")
            else:
                print("\nIncorrect answer!\n\nGame Over")
        else:
            print("\nIncorrect answer!\n\nGame Over")
    else:
        print("\nIncorrect answer!\n\nGame Over")
else:
    print("\nIncorrect answer!\n\nGame Over")

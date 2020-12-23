dictionary_question={}
while True:
    gender = input("1.Enter your gender M-male , F- female:")
    if gender in "mMfF":
        break
    print("Error-enter M or F! ")
while True:
    try:
        print("""
     2.Enter your age: 
    
        1.Less then 18
        2.18-30
        3.30-45
        4.45-55
        5.55-65
        6.65+
""")
        age = int(input("2.Enter your answer:"))

        if age==1:
            print("Sorry, we don't do survey with minors! ")
            exit(1)
        if age in [2, 3, 4, 5, 6]:

            break
        else:
            raise ValueError
    except ValueError:
        print("Please enter a number")
while True:
    try:
        print("""
    3.Enter your level of education:
        
        1.Elementary school
        2.High school
        3.College
        4.Master
        5.PHD
        """)
        level=int(input("3.Enter your answer:"))
        if level in [1, 2, 3, 4, 5]:
            break
        else:
            raise Exception()
    except ValueError:
        print("Please enter a number! ")
    except:
        print("Please enter a number between 1 and 5")
while True:
    try:

        print("""
    4.Please enter your employment status:
         
        1-Employed
        2-Unemployed
        3-Student
        """)
        status = int(input("5.Enter your answer: "))
        if status in [1, 2, 3]:
            break
        else:
            raise Exception()
    except ValueError:
        print("Please enter a number! ")
    except:
        print("Please enter a number between 1 and 4")
while True:
    try:
        print("""
    5.Enter your income: 
        
        1.Less then 1000$
        2.Between 1000$ and 2000$
        3.Between 2000$ and 3000$
        4.Over 3000$
        """)

        income=int(input("5.Enter your answer: "))
        if income in [1, 2, 3, 4]:
            break
        else:
            raise Exception()
    except ValueError:
        print("Please enter a number! ")
    except:
        print("Please enter a number between 1 and 4")
while True:
    try:
        print("""
    6.Your favourite destination:
        
        1. Spain
        2. France
        3. Switzerland
        4. Germany
        5. Other
        
        """)
        destination=int(input("Enter your answer:"))
        if destination in [1,2,3,4,5]:
            break
        else:
            raise Exception
    except ValueError:
        print("Enter your answer:")
    except:
        print("Please enter a number between 1 and 5! ")

while True:
    try:
        print("""
    7.Your favourite sport:
        
        1. Football
        2. Basketball
        3. Volleyball
        4. Handball
        5. Tennis
        6. Other
        
        """)
        sport=int(input("Enter your answer:"))
        if sport in [1, 2, 3, 4, 5, 6]:
            break
        else:
            raise Exception
    except ValueError:
        print("Please enter a number! ")
    except:
        print("Please enter a number between 1 and 6! ")
while True:
    try:
        print("""
    8.Your favourite food: 
        
        1. Domestic cuisine
        2. Hamburger
        3. Burger
        4. Pancakes
        5. McDonalds
        6. OTHER
        
        """)
        food=int(input("Enter your answer:"))
        if food in [1,2,3,4,5,6]:
            break
        else:
            raise Exception
    except ValueError:
        print("Please enter a number! ")
    except:
        print("Please enter a number between 1 and 6!")

while True:
    try:
        print("""
    9.Your favourite dog breed: 
        
        1.German Shepherd
        2.French Bulldog
        3.Beagle
        4.Doberman
        5.Poodle
        6.Other
        """)
        dog=int(input("Enter your answer:"))
        if dog in [1, 2, 3, 4, 5, 6]:
            break
        else:
            raise Exception
    except ValueError:
        print("Please enter a number! ")
    except:
        print("Please enter a number between 1 and 6!")
while True:
    try:
        print("""
    10.Your favourite season?
        
        1.Spring
        2.Summer
        3.Autumn
        4.Winter
        """)
        season=int(input("Enter your answer: "))
        if season in [1, 2, 3, 4]:
            break
        else:
            raise Exception
    except ValueError:
        print("Please enter a number!")
    except:
        print("Please enter a number between 1 and 4! ")
while True:
    try:
        print("""
    11.What would you give to a dear person:
         
        1.A perfume
        2.A weekend break
        3.A flowers
        4.A jewelry
        5.Other
        """)
        gift=int(input("Enter your answer: "))
        if gift in [1, 2, 3, 4, 5]:
            break
        else:
            raise Exception
    except ValueError:
        print("Please enter a number! ")
    except:
        print("Please enter a number between 1 and 5! ")
while True:
    try:
        print("""
    13.Your favourite colour: 
        
        1.Black 
        2.White
        3.Blue
        4.Grey
        5.Brown
        6.Green
        """)
        colour=int(input("Enter your answer: "))
        if colour in [1, 2, 3, 4, 5, 6]:
            break
        else:
            raise Exception
    except ValueError:
        print("Please enter a number! ")
    except:
        print("Please enter a number between 1 and 6! ")



if gender.upper() == "M":
    gender = "Male"
else:
    gender = "Famale"
age_list = ["","less then 18","18-30","30-45",'45-65',"65+" ]
age_dictionary = {1: "less then 18", 2: "18-30", 3: "30-45", 4:"45-65", 5:"65+" }
dictionary_question["1.Enter your gender M-male , F- female: "] = gender
dictionary_question["2.Enter your age: "] = age_list[age]
dictionary_question["3.Enter your level of education: "] = level
dictionary_question["4.Please enter your employment status: "] = status
dictionary_question["5.Enter your income: "] = income
dictionary_question["6.Your favourite destination: "] = destination
dictionary_question["7.Your favourite sport: "] = sport
dictionary_question["8.Your favourite food:  "] = food
dictionary_question["9.Your favourite dog breed: "] = dog
dictionary_question["10.Your favourite season? "] = season
dictionary_question["11.What would you give to a dear person: "] = gift
dictionary_question["12.Your favourite colour: "] = colour

for dictionary,question in dictionary_question.items():
    print(f"{dictionary}:{question}")





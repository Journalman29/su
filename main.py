# Asks questions about the user to determine which Steven Universe character they are.

print("Answer the following questions using Y or N:\n")

first_question = input("Are you overprotective?: ")

if first_question == "Y":
    print("You match Pearl!")
    print("Description:\n")
    print("""
Pearl from Steven Universe is a multi-faceted character known for her diligent and methodical nature,
as well as her passionate loyalty and deep emotions. Her intelligence and thirst for knowledge make
her an invaluable source of information, while her refined and elegant demeanor adds a touch of
sophistication to her personality. Through her journey, Pearl learns to confront her insecurities
and embrace change, showcasing her growth and inspiring viewers with her complexity and relatability.
          """)
    exit()

second_question = input("Are you stoic and/or collected?: ")

if second_question == "Y":
    print("You match Garnet!")
    exit()

third_question = input("Are you careless and/or a slob?: ")

if third_question == "Y":
    print("You match Amethyst!")
    exit()

fourth_question = input("Are you academic or technical?: ")

if fourth_question == "Y":
    print("You match Peridot!")
    exit()

fifth_question = input("Do you ever feel lost and alone?: ")

if fifth_question == "Y":
    print("You match Lapis!")
    exit()

else:
    print("\nWhy are you here then!?")
    exit()
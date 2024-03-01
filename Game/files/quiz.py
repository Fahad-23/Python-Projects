def quest(q):
    print(q.get("X"))

def choice():
    c = input("Enter the option(A,B,C or D): ").upper()
    return c
def loop(op):
    for i in op:
        print(i)
def correct(q,s):
    if choice() == q.get("ans"):
        print("\nCorrect!\n")
        return s + 1

    else:
        print("\nIncorrect!\n")
        return s

def options(q,op):
    quest(q)
    loop(op)

def quiz():
        s = 0

        q1 = {"X": "The Mona Lisa is displayed in which museum?\n", "ans": "A"}
        op1 = ["A -> The Louvre", "B -> The British Museum", "c -> The Met",
               "D -> The Vatican Museums"]
        options(q1,op1)
        s = correct(q1, s)

        q2 = {"X": "Which planet in our solar system has the most moons?\n", "ans": "B"}
        op2 = ["A -> Jupiter", "B -> Saturn", "C -> Uranus", "D -> Neptune"]
        options(q2, op2)
        s = correct(q2, s)

        q3 = {"X": "Which war is often referred to as the War to End All Wars?\n", "ans": "B"}
        op3 = ["A -> World War I", "B -> World War II", "C -> Korean War", "D -> Vietnam War"]
        options(q3,op3)
        s = correct(q3, s)

        q4 = {"X": "The Renaissance period originated in which country?\n", "ans": "A"}
        op4 = ["A -> France", "B -> Italy", "C -> Spain", "D -> England"]
        options(q4, op4)
        s = correct(q4, s)

        q5 = {"X": "What is the largest ocean on Earth?\n", "ans": "C"}
        op5 = ["A -> Atlantic Ocean", "B -> Indian Ocean", "C -> Pacific Ocean",
               "D -> Arctic Ocean"]
        options(q5, op5)
        s = correct(q5, s)

        q6 = {"X": "What is the largest Animal on Earth?\n", "ans": "B"}
        op6 = ["A -> African Elephant", "B -> Blue Whale", "C -> Giraffe",
               "D -> Hippopotamus"]
        options(q6, op6)
        s = correct(q6, s)

        q7 = {"X": "What is the largest organ in the human body?\n", "ans": "D"}
        op7 = ["A -> Liver", "B -> Brain", "C -> Heart ", "D -> Skin"]
        options(q7, op7)
        s = correct(q7, s)

        q8 = {"X": "Which world-renowned building features a glass pyramid at its entrance?\n",
              "ans": "D"}
        op8 = ["A -> The Eiffel Tower", "B -> The Sydney Opera House", "C -> The Colosseum",
               "D -> The Louvre Museum"]
        options(q8, op8)
        s = correct(q8, s)

        q9 = {"X": "The Hagia Sophia is located in which city?\n", "ans": "C"}
        op9 = ["A -> Athens", "B -> Cairo", "C -> Istanbul", "D -> Rome"]
        options(q9, op9)
        s = correct(q9, s)

        q10 = {"X": "The Atomium, a building shaped like an iron crystal, "
                    "is a major landmark in which European city?\n", "ans": "A"}
        op10 = ["A -> Brussels", "B -> Amsterdam", "C -> Stockholm", "D -> Vienna"]
        options(q10, op10)
        s = correct(q10, s)

        print(f"Your total score is: {s}")
#quiz()



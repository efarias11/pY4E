# prompt user to enter a score from 0.0-1.0

# program makes user follow the prompt and repeats if user makes an error.
while True:
    try:
        u_score = float(input("Please enter a score between (0.0-1.0): "))
        if 0.0 <= u_score <= 1.0:
            break
        else:
            print("Please reread the prompt. Slower, next time.")
    except ValueError:
        print("Dawg! You making me mad! Follow the prompt!")

# assigns a letter grade and message to user's score.
if u_score == 1.0:
    print("Woah! I feel like you are not being honest with your score, but you made a 100!")
elif u_score >= 0.9:
    print("Congratulations you brainiac! You got an A!")
elif u_score >= 0.8:
    print("Very good you earned a modest score! You got a B!")
elif u_score >= 0.7:
    print("Uhhh! No shame in just passing. You finished with a C.")
elif u_score >= 0.6:
    print("I hope this D doesn\'t foreshadow a trend with you.")
elif u_score == 0.0:
    print("I am very impressed! That you managed to not get a single answer correct...")
elif u_score < 0.6:
    print("*places test face down on your desk. See me after class...")

print("\nEnd.")   
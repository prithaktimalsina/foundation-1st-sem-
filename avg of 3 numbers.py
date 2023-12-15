
scores = []
exit_choice = "1"

try:
    score = float(input("Input a score: "))
    scores.append(score)
except ValueError:
    print("Invalid input. Enter a valid number.")

while exit_choice == "1":
    try:
        score = float(input("To exit program choose 0, to keep adding scores choose 1, then hit enter: "))
        if score == 0:
            break
        elif score == 1:
            score = float(input("Input a score: "))
            scores.append(score)
        else:
            print("Invalid choice. Exiting program.")
            break
    except ValueError:
        print("Invalid input. Enter a valid number.")

print("\nScores:")
for score in scores:
    print(score)
    
if len(scores) > 0:
    average_score = sum(scores) / len(scores)
    print(f"Average: {average_score}")
else:
    print("No scores entered.")
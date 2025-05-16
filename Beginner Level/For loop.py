print("\nFor Loop Section")
import random
rolls = [random.randint(1, 6) for _ in range(20)]
six_count = rolls.count(6)
one_count = rolls.count(1)
double_sixes = sum(1 for i in range(len(rolls)-1) if rolls[i] == 6 and rolls[i+1] == 6)
print("Dice rolls:", rolls)
print("6s rolled:", six_count)
print("1s rolled:", one_count)
print("Double 6s in a row:", double_sixes)
completed = 0
while completed < 100:
    completed += 10
    response = input(f"You completed {completed} jumping jacks. Are you tired? (yes/no): ").strip().lower()
    if response in ['yes', 'y']:
        skip = input("Do you want to skip the remaining? (yes/no): ").strip().lower()
        if skip in ['yes', 'y']:
            print(f"You completed a total of {completed} jumping jacks.")
            break
    if completed == 100:
        print("Congratulations! You completed the workout.")

import morse

decoded = input("Enter your sentence")

#print(f"Are you sure you want to transfer this sentence into morse, {decoded}")

confirmation = input(f"Are you sure you want to transfer this sentence into morse?, {decoded} (Y / N)")

if confirmation.upper() == "Y":
    print("Here is your sentence converted into morse:")
else:
    print("Script is cancelled by user")
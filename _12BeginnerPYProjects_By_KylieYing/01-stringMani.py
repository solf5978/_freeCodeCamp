youtuber = "Say Something" # Gonna have some string input

# Basic Concatenation
print("thanks to " + youtuber)

# W/ {} Placeholder
print("Subscribe to {} ".format(youtuber))

# f-Direct Format String
print(f"donate to {youtuber}")

noun = input("Somewhere you'd liek to be: ")
verb = input("Gonna do some verb to the somewhere: ")
verb_end = input("What's gonna end: ")


stringManipulate = f"""You start to wonder where the {noun} goes, 
                    the promising land seems nowhere to be {verb},
                    wanna hold onto something that won't get away.                    
                    """

print(stringManipulate)


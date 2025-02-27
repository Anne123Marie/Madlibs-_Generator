def mad_libs():
    # Prompting the user to choose a story
    print("Choose a story to create:")
    print("1. Adventure in the land of {place}")
    print("2. The mysterious {noun1} and the {noun2}")
    print("3. A day in the life of a {animal}")
    print("4. The {adjective1} journey of the {noun1}")
    
    choice = int(input("Enter the number of the story you want to create: "))
    
    # Asking the user for various words (20 user inputs)
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter one more noun: ")
    verb1 = input("Enter a verb (past tense): ")
    verb2 = input("Enter another verb: ")
    verb3 = input("Enter one more verb: ")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    adjective3 = input("Enter one more adjective: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    emotion = input("Enter an emotion (e.g., happiness, excitement, fear): ")
    color = input("Enter a color: ")
    food = input("Enter a food: ")
    number = input("Enter a number: ")
    body_part = input("Enter a body part: ")
    time_of_day = input("Enter a time of day (e.g., morning, evening): ")
    object1 = input("Enter an object: ")
    weather = input("Enter a type of weather (e.g., sunny, rainy): ")
    
    # Defining different story templates with a shorter narrative
    if choice == 1:
        story = f"""
        In the {place}, there was a {adjective1} {noun1} who loved to {verb1}. One {time_of_day}, it met a {noun2} 
        and decided to {verb2}. Together, they journeyed through a {adjective2} forest. The air was {weather}, 
        and they found a hidden {noun3} filled with {food} and {number} shiny {object1}s. The {animal} who lived nearby 
        gave them a {color} gem, and they left feeling {emotion}.
        """
    elif choice == 2:
        story = f"""
        A {noun1} and a {noun2} were best friends, but they had a problem. They both wanted to {verb1} the {adjective1} 
        treasure hidden deep in the {place}. After many adventures and a few {verb2}s, they stumbled upon a {noun3} and 
        found the treasure! It was full of {food} and {number} magical {object1}s, and they celebrated with the wise {animal}. 
        It was the happiest {time_of_day}.
        """
    elif choice == 3:
        story = f"""
        A curious {animal} woke up one {time_of_day} and decided to explore the {place}. The {adjective1} {animal} 
        found a {noun1} and a {noun2} along the way. They decided to {verb1} together through the {adjective2} forest. 
        They ate {food} and found {number} {object1}s in a hidden cave. By the end of the day, the {animal} felt {emotion} 
        and was ready for a {color} nap.
        """
    elif choice == 4:
        story = f"""
        There was a {adjective1} {noun1} who set off on a {adjective2} journey. Along the way, it met a {animal} who taught it 
        how to {verb1}. After crossing a {place}, they found a {noun2} with {food} and {number} {object1}s. The {noun1} 
        felt {emotion} and decided to {verb2} with the {animal}, knowing they would always share this adventure. The journey 
        was full of {adjective3} surprises!
        """

    # Displaying the final story
    print("\nHere's your story:\n")
    print(story)

# Run the Mad Libs function
mad_libs()
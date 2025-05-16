import random

DICE_VISUALS = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

# Constants
DICE_HEIGHT = 5
DICE_SEPARATOR = "  "

def validate_user_input(user_input):
    """Validate user input for number of dice."""
    if user_input.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(user_input)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)

def throw_dice(dice_count):
    """Throw the dice and return a list of random values."""
    dice_values = []
    for _ in range(dice_count):
        value = random.randint(1, 6)
        dice_values.append(value)
    return dice_values

def create_dice_diagram(dice_values):
    """Create ASCII art diagram of dice faces."""
    dice_faces = get_dice_graphics(dice_values)
    dice_diagram_rows = create_diagram_rows(dice_faces)

    # Generate header with the word "RESULTS" centered
    width = len(dice_diagram_rows[0])
    header = " RESULTS ".center(width, "~")

    complete_diagram = "\n".join([header] + dice_diagram_rows)
    return complete_diagram

def get_dice_graphics(dice_values):
    """Get the ASCII art for each dice value."""
    dice_graphics = []
    for value in dice_values:
        dice_graphics.append(DICE_VISUALS[value])
    return dice_graphics

def create_diagram_rows(dice_faces):
    """Create rows of the dice diagram."""
    diagram_rows = []
    for row_idx in range(DICE_HEIGHT):
        row_parts = []
        for dice in dice_faces:
            row_parts.append(dice[row_idx])
        row_text = DICE_SEPARATOR.join(row_parts)
        diagram_rows.append(row_text)
    return diagram_rows

def calculate_results(dice_values):
    """Calculate and return dice roll results."""
    results = {
        "values": dice_values,
        "sum": sum(dice_values)
    }
    return results

def display_results(results):
    """Display the results of the dice roll."""
    print("\n----- DICE ROLL RESULTS -----")
    print(f"Dice values: {results['values']}")
    print(f"Sum: {results['sum']}")
    print("----------------------------")

def main():
    playing = True
    
    while playing:
        # Get user input for the number of dice to roll
        num_dice_input = input("\nHow many dice do you want to roll? [1-6] ")
        num_dice = validate_user_input(num_dice_input)
        
        # Roll the dice and get the results
        dice_values = throw_dice(num_dice)
        
        # Generate and display the ASCII diagram of dice faces
        dice_diagram = create_dice_diagram(dice_values)
        print(f"\n{dice_diagram}")
        
        # Calculate and display results
        roll_results = calculate_results(dice_values)
        display_results(roll_results)
        
        # Ask if the user wants to roll again
        play_again = input("\nWould you like to roll again? (y/n): ").lower()
        playing = play_again.startswith('y')
    
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()  
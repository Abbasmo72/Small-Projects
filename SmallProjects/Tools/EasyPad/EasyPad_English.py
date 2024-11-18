import os

# Path for storing the notes file
NOTES_FILE = "notes.txt"  # File name to store notes

# Function to read notes from the file
def read_notes():
    if not os.path.exists(NOTES_FILE):  # If the file doesn't exist, return an empty list
        return []
    
    with open(NOTES_FILE, "r") as file:  # Open the file in read mode
        notes = file.readlines()  # Read all lines from the file
    return [note.strip() for note in notes]  # Remove extra spaces and return the notes

# Function to add a new note
def add_note(note):
    with open(NOTES_FILE, "a") as file:  # Open the file in append mode
        file.write(note + "\n")  # Write the note to the file
    print("Note added successfully.")  # Success message after adding the note

# Function to display all notes
def display_notes():
    notes = read_notes()  # Read the notes from the file
    if not notes:  # If no notes are available
        print("No notes available.")  # Message if no notes are found
    else:
        print("\nYour Notes:")  # Display the title for the notes
        for i, note in enumerate(notes, 1):  # Iterate and display each note
            print(f"{i}. {note}")

# Function to delete a note
def delete_note(index):
    notes = read_notes()  # Read the notes from the file
    if index < 1 or index > len(notes):  # Check if the note number is valid
        print("Invalid note number.")  # Error message for invalid number
        return

    del notes[index - 1]  # Delete the specified note
    with open(NOTES_FILE, "w") as file:  # Open the file in write mode
        for note in notes:  # Write the remaining notes to the file
            file.write(note + "\n")
    print("Note deleted successfully.")  # Success message after deleting the note

# Main menu loop for the program
def main():
    while True:
        print("\nSimple Note Taking App")  # Displaying the app title
        print("1. Add Note")  # Option to add a note
        print("2. View Notes")  # Option to view notes
        print("3. Delete Note")  # Option to delete a note
        print("4. Exit")  # Option to exit the program

        choice = input("Choose an option: ")  # Getting the user's choice for an option

        if choice == '1':  # If the user chooses option 1
            note = input("Enter your note: ")  # Get the new note from the user
            add_note(note)  # Add the note to the file
        elif choice == '2':  # If the user chooses option 2
            display_notes()  # Display all the notes
        elif choice == '3':  # If the user chooses option 3
            display_notes()  # Display all the notes
            try:
                index = int(input("Enter the note number to delete: "))  # Get the note number to delete
                delete_note(index)  # Delete the specified note
            except ValueError:  # If the input is not a valid number
                print("Please enter a valid number.")  # Error message for invalid input
        elif choice == '4':  # If the user chooses option 4
            print("Exiting the program.")  # Message for exiting the program
            break
        else:  # If the user enters an invalid option
            print("Invalid option. Please try again.")  # Error message for invalid option

if __name__ == "__main__":  # Ensures the script runs only when executed directly
    main()

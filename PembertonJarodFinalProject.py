import tkinter as tk
from tkinter import messagebox, simpledialog


def main_window():
    """
    Sets up the main window for user inputs.
    This window allows the user to enter the total weight, dolly weight,
    and whether the load is a bulk load.
    """
    global main_win  # Main window reference
    main_win = tk.Tk()  # Create the main window
    main_win.title("FedEx Weight Calculator")  # Set the window title

    # Labels for user input
    tk.Label(main_win, text="Enter Total Weight (1100 - 9999 lbs):").grid(row=0, column=0)
    tk.Label(main_win, text="Enter Dolly Weight (1000 - 3000 lbs):").grid(row=1, column=0)
    tk.Label(main_win, text="Is this a bulk load? (yes/no):").grid(row=2, column=0)

    # Entry fields for user input
    global total_weight_entry  # Entry for total weight
    global dolly_weight_entry  # Entry for dolly weight
    global bulk_load_entry  # Entry for bulk load status

    total_weight_entry = tk.Entry(main_win)  # Create entry for total weight
    dolly_weight_entry = tk.Entry(main_win)  # Create entry for dolly weight
    bulk_load_entry = tk.Entry(main_win)  # Create entry for bulk load status

    # Place entry fields in the grid
    total_weight_entry.grid(row=0, column=1)
    dolly_weight_entry.grid(row=1, column=1)
    bulk_load_entry.grid(row=2, column=1)

    # Buttons for actions
    tk.Button(main_win, text="Calculate Final Weight", command=calculate_final_weight).grid(row=3,
                                                                                            column=0)  # Calculate button
    tk.Button(main_win, text="Exit", command=main_win.quit).grid(row=3, column=1)  # Exit button

    main_win.mainloop()  # Start the main event loop


def calculate_final_weight():
    """
    Calculates the final weight based on user inputs.
    Retrieves input values, validates them, and computes the final weight.
    Displays the result in a message box.
    """
    try:
        # Validate and retrieve weights
        total_weight = validate_weight(total_weight_entry.get(), 1100, 9999, "Total weight")  # Validate total weight
        dolly_weight = validate_weight(dolly_weight_entry.get(), 1000, 3000, "Dolly weight")  # Validate dolly weight
        bulk_load = bulk_load_entry.get().strip().lower()  # Get and normalize bulk load input

        # Check if the bulk load input is valid
        if bulk_load not in ['yes', 'no']:
            raise ValueError("Please enter 'yes' or 'no' for bulk load.")

        # Calculate final weight based on whether it is a bulk load
        if bulk_load == 'yes':
            # Ask for container weight if it is a bulk load
            container_weight = validate_weight(
                simpledialog.askstring("Input", "Enter Container Weight (100 - 300 lbs):"), 100, 300,
                "Container weight")  # Validate container weight
            final_weight = total_weight - dolly_weight - container_weight  # Calculate final weight for bulk load
        else:
            final_weight = total_weight - dolly_weight  # Calculate final weight for non-bulk load

        # Show the final weight in a message box
        messagebox.showinfo("Final Weight", f"The final weight is {final_weight:.2f} lbs.")

    except ValueError as ve:
        # Handle input errors and show a message box with the error
        messagebox.showerror("Input Error", str(ve))
    except Exception as e:
        # Handle unexpected errors
        messagebox.showerror("Error", "An unexpected error occurred.")


def validate_weight(value, min_val, max_val, field_name):
    """
    Validates the weight input.
    Checks if the input is empty, a valid number, and within the specified range.

    Args:
        value: The input value to validate.
        min_val: Minimum acceptable value.
        max_val: Maximum acceptable value.
        field_name: Name of the field for error messages.

    Returns:
        The validated weight as a float.
    """
    if not value:  # Check if input is empty
        raise ValueError(f"{field_name} cannot be empty.")
    try:
        weight = float(value)  # Convert the input to float
    except ValueError:
        raise ValueError(f"{field_name} must be a number.")  # Handle non-numeric input

    # Check if the weight is within the specified range
    if not (min_val <= weight <= max_val):
        raise ValueError(f"{field_name} must be between {min_val} and {max_val}.")

    return weight  # Return the validated weight


if __name__ == "__main__":
    main_window()  # Run the main window function to start the application
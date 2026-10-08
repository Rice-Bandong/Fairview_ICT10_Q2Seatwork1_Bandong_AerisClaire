from pyscript import document

# list of official Glee Club members
members = [
    "Stella of Solaria",
    "Flora of Linphea",
    "Musa of Melody",
    "Tecna of Zenith",
    "Aisha of Andros",
    "Roxy of Earth",
]


def check_candidate(event):
    # retrieve first and last name from input fields
    first = document.getElementById("first_name").value.strip()
    last = document.getElementById("last_name").value.strip()
    # combine inputs cleanly 
    full_name = f"{first} {last}".strip()
    # check membership status without if/else or loops
    is_in_list = full_name in members
    # dictionary lookup mapping boolean results directly to strings
    output_messages = {
        True: f"✨🎶 Congratulations {full_name}! You are now part of the Glee Club! 🎤🌸",
        False: f"Sorry {full_name}, your name is not on the Glee Club roster.",
    }
    # output message to result area
    document.getElementById("result_area").innerText = output_messages[
        is_in_list
    ]
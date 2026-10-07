from pyscript import document

members = ["Jhoana Evangelista", "Stella of Solaria", "Flora of Linphea", "Musa of Melody", "Tecna of Zenith", "Aisha of Andros", "Roxy of Earth"]


def check_candidate(event):
    first = document.getElementById("first_name").value.strip()
    last = document.getElementById("last_name").value.strip()

    full_name = f"{first} {last}".strip().title()

    is_in_list = full_name in members

    output_messages = {
        True: f"Congratulations {full_name}! You are now part of the ICT club.",
        False: f"Sorry {full_name}, your name is not on the list.",
    }

    document.getElementById("result_area").innerText = output_messages[
        is_in_list
    ]
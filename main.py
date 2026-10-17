from pyscript import document

# List of official Glee Club members
members = [
    "Jordin San Juan",
    "Elina Elysse Padre",
    "Savanah Fugueroa",
    "Franshellyahna Pilao",
    "Kyrie Cerise Funtanilla",
    "Antoinette Caleigh Garcia",
    "Julianna Omaking",
    "Aeris Bandong",
    "Vyelle Mikayla Bunag",
    "Gavin Ghonn Taguiga",
    "Hans Arada",
    "Alexi Villanueva",
    "Dannielle Luna Dimasuhid",
    "Ebtisam A. Al Hazmi",
    "Marley Summer Reyes Manese",
    "Queeny Haraj Guilas Ramos",
    "Maia Isabelle Fabro",
    "Erin Mandapat",
    "Maria Elisha Padre",
    "Nica Gabriela Crispino"
]

def check_candidate(event):
    # Grab what user typed in the boxes
    first = document.getElementById("first_name").value.strip()
    last = document.getElementById("last_name").value.strip()
    
    # Put first and last name together
    full_name = f"{first} {last}".strip()
    
    # Check if the name is in the list
    is_in_list = full_name in members
    
    # Pick the right message depending on True or False
    output_messages = {
        True: f"✨🎶 Congratulations {full_name}! You are now part of the Glee Club! 🎤🌸",
        False: f"Sorry {full_name}, your name is not on the Glee Club roster.",
    }
    
    # Show the message on the webpage
    document.getElementById("result_area").innerText = output_messages[is_in_list]
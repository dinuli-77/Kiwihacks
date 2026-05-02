import sys
import time
import tkinter as tk 

# ---------------- STORY DATA ---------------- #

story = {
    "path_1": {
        "story": "You only remember waking up, not how you got there.\nYou look up at a screen that traps you in with whatever monsters lie inside.\nYou're trapped… Inside a computer.",
        "options": {
            "1": {"text": "Sit there", "path": "death_sit_there"},
            "2": {"text": "Follow the light", "path": "path_2"},
            "3": {"text": "Go into the darkness", "path": "path_darkness"}
        }
    },

    "death_sit_there": {
        "story": "The light seems to fade and then claws of pure blackness grab your shoulder.\nPain floods through your body and then the world becomes nothing but black, jagged teeth and agony.",
        "options": "K"
    },

    "path_2": {
        "story": "A tiny pixel lights up and the rest is surrounded by blackness.\nYou start to follow the tiny light in the total darkness until you come across a small circle made up of little elements.",
        "options": {
            "1": {"text": "Stand in the center", "path": "death_stand_center"},
            "2": {"text": "Follow the light", "path": "path_water_light"},
            "3": {"text": "Walk away", "path": "path_walk_away"}
        }
    },

    "death_stand_center": {
        "story": "The pixels start swirling slowly around your body. They tickle you and they start to form something.\nIt glows an eerie white light and it makes you smile.\nBut it becomes more creepy, the soft edges becoming sharp points before they stab you in the stomach.\nYou fall, leaving behind a corpse and a monster.",
        "options": "K"
    },

    "path_water_light": {
        "story": "You find a pool of water with a loose wire inside.",
        "options": {
            "1": {"text": "Drink", "path": "path_drink_safe_water"},
            "2": {"text": "Ignore", "path": "death_leave_water"},
            "3": {"text": "Test it", "path": "death_test_water"}
        }
    },

    "path_drink_safe_water": {
        "story": "You drink. It's safe.\nHope returns.",
        "options": {
            "1": {"text": "Ponder", "path": "death_ponder"},
            "2": {"text": "Seek", "path": "path_seek"},
            "3": {"text": "Discover", "path": "medium_win"}
        }
    },

    "death_ponder": {
        "story": "You overthink until your mind collapses into darkness.",
        "options": "K"
    },

    "path_seek": {
        "story": "You feel eyes watching you in the dark.",
        "options": {
            "1": {"text": "Run", "path": "death_run"},
            "2": {"text": "Stop", "path": "death_stop_eyes"},
            "3": {"text": "Keep going", "path": "path_cliff"}
        }
    },

    "death_run": {
        "story": "You fall into nothingness while running.",
        "options": "K"
    },

    "death_stop_eyes": {
        "story": "The eyes consume you.",
        "options": "K"
    },

    "path_cliff": {
        "story": "You reach a cliff.",
        "options": {
            "1": {"text": "Jump", "path": "weird_win"},
            "2": {"text": "Stay", "path": "death_cliff_stop"},
            "3": {"text": "Step back", "path": "death_cliff_stop"}
        }
    },

    "weird_win": {
        "story": "Time freezes...\nWIN",
        "options": {}
    },

    "death_cliff_stop": {
        "story": "Creatures drag you down.",
        "options": "K"
    },

    "medium_win": {
        "story": "You wake up. You escaped.\nWIN - MEDIUM",
        "options": {}
    },

    "death_leave_water": {
        "story": "You collapse from thirst.",
        "options": "K"
    },

    "death_test_water": {
        "story": "Something grabs you from the water.",
        "options": "K"
    },

    "path_walk_away": {
        "story": "You find another pool.",
        "options": {
            "1": {"text": "Ignore", "path": "death_ignore_water"},
            "2": {"text": "Drink", "path": "death_drink_electrocuted_water"},
            "3": {"text": "Touch", "path": "death_burn_finger"}
        }
    },

    "death_ignore_water": {
        "story": "You collapse before reaching anything.",
        "options": "K"
    },

    "death_drink_electrocuted_water": {
        "story": "Electric shock spreads through your body.",
        "options": "K"
    },

    "death_burn_finger": {
        "story": "Something rises from the water and kills you.",
        "options": "K"
    },

    "path_darkness": {
        "story": "Something is making a sound in the darkness.",
        "options": {
            "1": {"text": "Freeze", "path": "death_freeze"},
            "2": {"text": "Fight", "path": "death_fight"},
            "3": {"text": "Run", "path": "easy_ending"}
        }
    },

    "death_freeze": {
        "story": "Something grabs you from behind.",
        "options": "K"
    },

    "death_fight": {
        "story": "Spider creatures overwhelm you.",
        "options": "K"
    },

    "easy_ending": {
        "story": "You escape and wake up.\nEASY ENDING",
        "options": {}
    }
}

# ---------------- UI ---------------- #

def show_death_screen():
    root = tk.Tk()
    root.title("...")
    root.configure(bg="black")
    root.attributes("-fullscreen", True)

    label = tk.Label(
        root,
        text="YOU DIED",
        fg="#8B0000",
        bg="black",
        font=("Arial", 100, "bold")
    )
    label.pack(expand=True)

    root.bind("<Key>", lambda e: root.destroy())
    root.mainloop()


# ---------------- TEXT EFFECT ---------------- #

def type_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()


# ---------------- GAME LOGIC ---------------- #

def story_run(story, current_path, previous_path):

    node = story[current_path]

    # NORMAL PATH
    if node["options"] not in ("K", {}):
        type_print(node["story"])

        print("\nChoices:")
        for key, option in node["options"].items():
            print(f"{key}. {option['text']}")

        while True:
            choice = input("Choose (1/2/3): ")
            if choice in node["options"]:
                break
            print("Invalid choice.")

        previous_path = current_path
        current_path = node["options"][choice]["path"]
        return current_path, previous_path

    # DEATH
    elif node["options"] == "K":
        type_print(node["story"])
        show_death_screen()

        while True:
            retry = input("Try again? (Y/N): ")
            if retry in ("Y", "N"):
                break

        if retry == "Y":
            return previous_path, previous_path
        else:
            sys.exit()

    # WIN / END
    else:
        type_print(node["story"])
        print("\n🎉 ENDING REACHED 🎉")

        while True:
            again = input("Play again? (Y/N): ")
            if again in ("Y", "N"):
                break

        if again == "Y":
            return "path_1", ""
        else:
            sys.exit()


# ---------------- MAIN LOOP ---------------- #

current_path = "path_1"
previous_path = ""

while True:
    current_path, previous_path = story_run(story, current_path, previous_path)

import sys
import time
import os
import random

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
        "story": "The light fades. Something grabs you.\nEverything turns into pain.",
        "options": "K"
    },

    "path_2": {
        "story": "A tiny pixel lights up in the darkness.\nYou follow it.",
        "options": {
            "1": {"text": "Stand in the center", "path": "death_stand_center"},
            "2": {"text": "Follow the light", "path": "path_water_light"},
            "3": {"text": "Walk away", "path": "path_walk_away"}
        }
    },

    "death_stand_center": {
        "story": "The pixels sharpen and stab into you.",
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
        "story": "The water is safe. You feel hope return.",
        "options": {
            "1": {"text": "Ponder", "path": "death_ponder"},
            "2": {"text": "Seek", "path": "path_seek"},
            "3": {"text": "Discover", "path": "medium_win"}
        }
    },

    "death_ponder": {
        "story": "Your thoughts spiral until everything fades.",
        "options": "K"
    },

    "path_seek": {
        "story": "You feel something watching you.",
        "options": {
            "1": {"text": "Run", "path": "death_run"},
            "2": {"text": "Stop", "path": "death_stop_eyes"},
            "3": {"text": "Keep going", "path": "path_cliff"}
        }
    },

    "death_run": {
        "story": "You run… and fall into nothing.",
        "options": "K"
    },

    "death_stop_eyes": {
        "story": "The eyes consume you.",
        "options": "K"
    },

    "path_cliff": {
        "story": "A cliff blocks your path.",
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
        "story": "Creatures drag you into the void.",
        "options": "K"
    },

    "medium_win": {
        "story": "You wake up safely.\nWIN - MEDIUM",
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
        "story": "Something moves in the darkness.",
        "options": {
            "1": {"text": "Freeze", "path": "death_freeze"},
            "2": {"text": "Fight", "path": "death_fight"},
            "3": {"text": "Run", "path": "easy_ending"}
        }
    },

    "death_freeze": {
        "story": "Something grabs you.",
        "options": "K"
    },

    "death_fight": {
        "story": "Creatures overwhelm you.",
        "options": "K"
    },

    "easy_ending": {
        "story": "You escape.\nEASY ENDING",
        "options": {}
    }
}

# ---------------- EFFECTS ---------------- #

def type_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()

def glitch_text(text, duration=2):
    chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*")
    end_time = time.time() + duration

    while time.time() < end_time:
        glitched = ""
        for c in text:
            if random.random() < 0.3:
                glitched += random.choice(chars)
            else:
                glitched += c
        print("\r" + glitched, end="", flush=True)
        time.sleep(0.05)

    print("\r" + text + " " * 10)

def show_death_screen():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n" * 5)
    glitch_text("YOU DIED", 2)
    print("\n")
    time.sleep(0.5)

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

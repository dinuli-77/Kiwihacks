import sys
import time
import tkinter as tk 

story = {
    "path_1": {
        "story": "You only remember waking up, not how you got there.\nYou look up at a screen that traps you in with whatever monsters lie inside.\nYou're trapped… Inside a computer.",
        "options": {
            "1": {
                "text": "Sit there",
                "path": "death_sit_there"
            },
            "2": {
                "text": "Follow the light",
                "path": "path_2"
            },
            "3": {
                "text": "Go into the darkness",
                "path": "path_darkness"
            }
        }
    },

    "death_sit_there": {
        "story": "The light seems to fade and then claws of pure blackness grab your shoulder.\nPain floods through your body and then the world becomes nothing but black, jagged teeth and agony.",
        "options": "K"
    },

    "path_2": {
        "story": "A tiny pixel lights up and the rest is surrounded by blackness.\nYou start to follow the tiny light in the total darkness until you come across a small circle made up of little elements.",
        "options": {
            "1": {
                "text": "Stand in the center",
                "path": "death_stand_center"
            },
            "2": {
                "text": "Follow the light",
                "path": "path_water_light"
            },
            "3": {
                "text": "Walk away, going deep in the computer",
                "path": "path_walk_away"
            }
        }
    },

    "death_stand_center": {
        "story": "The pixels start swirling slowly around your body. They tickle you and they start to form something.\nIt glows an eerie white light and it makes you smile.\nBut it becomes more creepy, the soft edges becoming sharp points before they stab you in the stomach.\nYou fall, leaving behind a corpse and a monster.",
        "options": "K"
    },

    "path_water_light": {
        "story": "As you keep going towards the light, the ring behind you disappears.\nAren’t you glad that you kept walking towards the light?\nYou keep walking, leaving behind a blank trail of pixels.\nYou finally discover what you’ve been looking for: a small pool of water.\nYou notice there is a loose wire inside.\nThe water could be electrocuted.",
        "options": {
            "1": {
                "text": "Drink the water",
                "path": "path_drink_safe_water"
            },
            "2": {
                "text": "Leave the water behind and keep following the light",
                "path": "death_leave_water"
            },
            "3": {
                "text": "Use your finger to test if the water is electrocuted",
                "path": "death_test_water"
            }
        }
    },

    "path_drink_safe_water": {
        "story": "The water is soothing as it travels down your thirsty throat.\nNot electrocuted.\nYou feel relieved and hope starts to travel back to your body.\nAs the light continues, you follow behind, wondering what comes next.\nThe questions in your head are too deep to get out of.",
        "options": {
            "1": {
                "text": "Ponder",
                "path": "death_ponder"
            },
            "2": {
                "text": "Seek",
                "path": "path_seek"
            },
            "3": {
                "text": "Discover",
                "path": "medium_win"
            }
        }
    },

    "death_ponder": {
        "story": "You think to yourself as you continue to follow the light.\nThen the world starts to turn twisted as you lose the ability to think.\nYour head won't stop spinning and thinking of just two things: blackness and a single light that is leading towards your doom.\nThen you collapse.\nYou wonder why everything is wrong, why you are here.\nThen, you cry.\nSobbing until you are too exhausted.\nThen blackness, the one you have been dreading.\nYour brain stops, and for once, you enjoy peace.",
        "options": "K"
    },

    "path_seek": {
        "story": "You won’t just think. You want to do something.\nBut what?\nThe light is eerie and starting to bore you.\nYou follow, but become more aware.\nThis is a new world that you are excited to discover.\nThen, the light speeds up, and you know why.\nYou can feel eyes on you, and can see them through the dark.",
        "options": {
            "1": {
                "text": "Run",
                "path": "death_run"
            },
            "2": {
                "text": "Stop",
                "path": "death_stop_eyes"
            },
            "3": {
                "text": "Discover",
                "path": "path_cliff"
            }
        }
    },

    "death_run": {
        "story": "You follow the light, almost beating it as you run.\nYou feel the eyes follow, like hungry wolves.\nYou keep running as the light stops, afraid of the fact that they are killing you.\nBut then you don't feel air underneath your feet as you fall.\nThen, the world is only pain and death.",
        "options": "K"
    },

    "death_stop_eyes": {
        "story": "The light races ahead.\nBefore you can change your mind, you are consumed by the millions of eyes that stare into your soul and eat it alive.",
        "options": "K"
    },

    "path_cliff": {
        "story": "You follow the light barely, watching the eyes.\nThey are made of spiderlike creatures with legs sharper than spears.\nThey look like they are made of a special AI, made to kill you.\nYou turn around and the light has stopped, and you notice why.\nA cliff is staring right at you.",
        "options": {
            "1": {
                "text": "Jump",
                "path": "weird_win"
            },
            "2": {
                "text": "Stop",
                "path": "death_cliff_stop"
            }
        }
    },

    "weird_win": {
        "story": "You feel the world close as the air rushes past your face.\nYou land… in heaven.\n???\nTime freezes…\nThe world stops.\nYoU DoNt KnOw WhAt YoUrE DoInG!!!\nWIN",
        "options": {}
    },

    "death_cliff_stop": {
        "story": "The creatures consume the ground from underneath you.\nYou die, knowing that there was no other way.",
        "options": "K"
    },

    "medium_win": {
        "story": "You know there's answers waiting to be discovered, so you leave the light.\nYou follow the voice in your head.\nThe world is slowly fitting in.\nThen the voice says, “Sit.”\nYou do so.\nThen a river of memories floods your brain.\nYou are here because you're sleeping.\nIf you don't get out, you die.\nThat includes real life.\nThen you think about everything, and it makes sense.\nYour fears are the monsters, the debugs, the nightmare spiders who have neurotoxins, killing you instantly.\nThe lights are the pixelflies, like fireflies that help you.\nYou breathe.\nIt makes sense.\nWhen you open your eyes, an interbug, a beetle like a microchip, is sitting on your arm.\nIt seems to smile.\nThen, you wake, feeling refreshed and more in control.\nWIN - MEDIUM",
        "options": {}
    },

    "death_leave_water": {
        "story": "The light seems to travel all the way, but somehow it stops.\nYour throat constantly reminds you how thirsty you are.\nBut you collapse.\nUnable to feel how fresh air smells like.\nThe world becomes black.\nYou never wake up.",
        "options": "K"
    },

    "death_test_water": {
        "story": "The water feels calm and smooth.\nNOT electrocuted.\nYour body relaxes, and then you feel it.\nClaws grabbing your finger.\nThe water becomes cloudy and red before it sucks you in.\nWATER.\nCalming, but screaming means death.\nTOO MUCH WATER.\nYou start to lose consciousness.",
        "options": "K"
    },

    "path_walk_away": {
        "story": "The light continues and you wish you followed it.\nThe world seems dark as you start to lose hope.\nThen, something glints in the path ahead.\nYou notice a pool.\nA small puddle of water that has a wire going through it.\nThe wire is clearly broken and the water could be electrocuted.",
        "options": {
            "1": {
                "text": "Ignore the water pool and keep walking ahead",
                "path": "death_ignore_water"
            },
            "2": {
                "text": "Drink the water",
                "path": "death_drink_electrocuted_water"
            },
            "3": {
                "text": "Test the water and burn your finger",
                "path": "death_burn_finger"
            }
        }
    },

    "death_ignore_water": {
        "story": "Time doesn’t stop for you.\nThe world around you reminds you of water and how desperately you crave it.\nJust one more step.\nBut you lose consciousness before it hits you.\nSorry world, this was another dead end.",
        "options": "K"
    },

    "death_drink_electrocuted_water": {
        "story": "You have been thirsty for so long that you can’t resist drinking the water right in front of you.\nAs you drink the water, nothing seems to feel weird.\nYou feel relieved that you were finally able to drink some water.\nAs soon as you finish drinking, your throat starts to feel tingly.\nAt first, it feels like a little buzz, like static.\nThen before you know it, the feeling spreads all around your body.\nSlowly, your chest starts to tighten.\nYou try to scream for help, but nothing comes out of your mouth.\nYour vision starts to flicker and the whole world turns black.",
        "options": "K"
    },

    "death_burn_finger": {
        "story": "You hesitate before you start to lean in to touch the water.\nSuddenly, a shock.\nYou pull back your hand quickly, your finger feeling like it’s about to fall off.\nThat was close, you think.\nBut suddenly, the water starts to move. Slowly.\nIt can’t possibly be the wire, you think to yourself.\nIt feels like something is inside of it.\nA flowy shape starts to rise out of the water.\nThe shape slowly turns its way toward you.\nIts eyes look blank and it looks at you with a blank smile.\nThe thing starts to make its way towards you.\nBefore you know it, you die.",
        "options": "K"
    },

    "path_darkness": {
        "story": "The curiosity of what lies beyond urges you to go deep into the computer.\nEverything makes a sound, whether it is a quiet hum of the wires or the sudden popping noise of the…\nA computer doesn't make that sound.",
        "options": {
            "1": {
                "text": "Freeze",
                "path": "death_freeze"
            },
            "2": {
                "text": "Fight",
                "path": "death_fight"
            },
            "3": {
                "text": "Flight",
                "path": "easy_ending"
            }
        }
    },

    "death_freeze": {
        "story": "Your body starts to get stiff.\nThen the popping sound slowly starts to fade away.\nYou sigh in relief, knowing that now the popping sound is no longer bothering you.\nBut not long after, you feel a cold, sharp prick on your shoulder.\nIt twists your shoulder.\nBefore you know it, the world goes completely dark.",
        "options": "K"
    },

    "death_fight": {
        "story": "You use your blind rage to push yourself forward, going towards the sound.\nIt gets more powerful and more clear.\nWhen you arrive, you look at the web.\nA giant web, white, that sticks to the sides of the screen and battery.\nYou notice small black spheres stuck to the web.\nThey pop every once in a while, like they are trying to jump out.\nThen it happens.\nThe spheres open up, like eggs hatching.\nSmall spider-like creatures with pure white eyes and jagged edges.\nThey look at you, waiting.\nYou scream and run towards them, ready to do… something.\nThey jump on you and bare their teeth, small, but coated in a thin layer of glowing green venom.\nThey bite your arm.\nIt feels as if your arm snaps off and freezes before being set on fire.\nYou collapse, your body unable to handle the pain.\nBut you don’t wake up.",
        "options": "K"
    },

    "easy_ending": {
        "story": "You run in the opposite direction, unsure if this is the correct path.\nYou feel sudden consciousness, like the world came into place.\nThen you feel like you know something.\nYou let your mind lead you to a small opening, not sure how you got there.\nOne step out, then…\nYou wake up.\nEyes sore.\nHead sore.\nIn a bed, unsure if you were sleeping or sick.\nEither way, you're glad you made it out alive.\nEASY ENDING WON",
        "options": {}
    }
}

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
        font=("Arial", 120, "bold")
    )
    label.pack(expand=True)

    root.update()  # makes sure it shows instantly

    root.bind("<Key>", lambda e: root.destroy())
    root.mainloop()


def type_print(text):
    for i in text:
        print(i, end="")
        time.sleep(0.05)
    print()


def story_run(story, current_path, previous_path):
    type_print(story[current_path]["story"])

    # NORMAL PATH (choices)
    if story[current_path]["options"] != "K":

        print(
            "\n1.", story[current_path]["options"]["1"]["text"], "\n"
            "2.", story[current_path]["options"]["2"]["text"], "\n"
            "3.", story[current_path]["options"]["3"]["text"]
        )

        while True:
            try:
                user_choice = int(input("What path do you choose? 1, 2, or 3: "))
                if user_choice in (1, 2, 3):
                    break
                else:
                    print("Please choose between 1-3")
            except ValueError:
                print("Please type a number")

    # DEATH PATH
    else:
        type_print("\n" + story[current_path]["story"])
        show_death_screen()

        while True:
            user_choice_YN = input("\nTry again? (Y/N): ")
            if user_choice_YN in ("Y", "N"):
                break
            else:
                print("Please type either Y or N")

        if user_choice_YN == "Y":
            return previous_path, previous_path

        sys.exit()

    previous_path = current_path
    current_path = story[current_path]["options"][str(user_choice)]["path"]

    return current_path, previous_path


# ---------------- MAIN GAME LOOP ----------------

current_path = "path_1"
previous_path = ""

while True:
    current_path, previous_path = story_run(story, current_path, previous_path)

over_world = {
    (0, 0): {
        "location": "train1",
        "description": "You are in the train station",
        "options": "Look around[1]\nMove along the train tracks towards the engine[2]\n>",
        1: "look around",
        2: "west",
        "detailed_description": "You see your friend Dave asleep on the platform a couple feet away from where you woke up.",
    },
    (-1, 0): {
        "location": "train2",
        "description": "You move down the tracks towards the trains engine",
        "options": "Look around[1]\nMove back the way you came[2]\n>",
        1: "look around",
        2: "east",
        "detailed_description": "The trains engine on, but as you look through the windows you notice everyone in their seats and asleep.",
    },
}

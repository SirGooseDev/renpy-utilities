# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    call extra_screen

    $ unlockMemory("james_event_1")
    $ unlockMemory("james_event_2")
    $ unlockMemory("james_event_3")
    $ unlockMemory("james_event_4")
    $ unlockMemory("james_event_5")

    $ unlockMemory("kim_event_1")
    $ unlockMemory("kim_event_2")
    $ unlockMemory("kim_event_3")

    $ unlockPhotoFragmentWithMessage(name="kim_event_4", fragment=1, message="The Trial")
    $ unlockPhotoFragmentWithMessage(name="kim_event_4", fragment=2, message="The Trial")
    $ unlockPhotoFragmentWithMessage(name="kim_event_4", fragment=3, message="The Trial")
    $ unlockPhotoFragmentWithMessage(name="kim_event_4", fragment=4, message="The Trial")

    $ unlockPhotoFragmentWithMessage(name="james_event_5", fragment=1, message="James Extra Event")
    
    $ unlockPhotoFragmentWithMessage(name="kim_event_5", fragment=1, message="Kim Extra Event")

    # This ends the game.

    return

image je1 = im.Scale("james_event1.png", 1920, 1080)
label james_event_1:

    scene je1

    "Test Event"

    return

image je2 = im.Scale("james_event2.png", 1920, 1080)
label james_event_2:

    scene je2

    "Test Event"

    return

image je3 = im.Scale("james_event3.png", 1920, 1080)
label james_event_3:

    scene je3

    "Test Event"

    return

image je4 = im.Scale("james_event4.png", 1920, 1080)
label james_event_4:

    scene je4

    "Test Event"

    return

image je5 = im.Scale("james_event5.png", 1920, 1080)
label james_event_5:

    scene je5

    "Test Event"

    return

image ke1 = im.Scale("kim_event1.png", 1920, 1080)
label kim_event_1:

    scene ke1

    "Test Event"

    return

image ke2 = im.Scale("kim_event2.png", 1920, 1080)
label kim_event_2:

    scene ke2

    "Test Event"

    return

image ke3 = im.Scale("kim_event3.png", 1920, 1080)
label kim_event_3:

    scene ke3

    "Test Event"

    return

image ke4 = im.Scale("kim_event4.png", 1920, 1080)
label kim_event_4:

    scene ke4

    "Test Event"

    return

image ke5 = im.Scale("kim_event5.png", 1920, 1080)
label kim_event_5:

    scene ke5

    "Test Event"

    return
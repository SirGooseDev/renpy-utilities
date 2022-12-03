transform gallery_button_scale:
    zoom 0.90

transform gallery_character_slot_scale:
    zoom 0.70

transform gallery_character_thumbnail_scale:
    zoom 0.40

init python:

    if persistent.unlockedMemories is None:
        persistent.unlockedMemories = []
        print(f"Created unlockedMemories: {persistent.unlockedMemories}")
    else: 
        print(f"Loaded unlockedMemories: {persistent.unlockedMemories}")

    def checkUnlockedMemory(name):
        b = False
        for x in persistent.unlockedMemories:
            if x == name:
                b = True
        return b
    
    def unlockMemory(name):
        if checkUnlockedMemory(name) == False:
            persistent.unlockedMemories.append(name)
            print(_(f"Unlocked Memory: {name}"))
            #renpy.notify(_(f"Unlocked Memory: {name}"))

    class SMemory:
        def __init__(self, name, title, thumbnail):
            self.name = name
            self.title = title
            self.thumbnail = thumbnail

    class SGallery:
        def __init__(self):
            self.memories = []

        def addMemory(self, name, title, thumbnail):
            self.memories.append(SMemory(name, title, thumbnail))

        def addMemories(self, data):
            for d in data:
                self.addMemory(d[0], d[1], d[2])

        def unlockMemory(self, name):
            for m in self.memories:
                if m.name == name:
                    unlockMemory(m.name)
                    
        def unlockAllMemories(self):
            for m in self.memories:
                unlockMemory(m.name)

        def countMemories(self):
            return len(self.memories)

        def countUnlockedMemories(self):
            total = 0
            for m in self.memories:
                if checkUnlockedMemory(m.name) == True:
                    total = total + 1
            return total

        def getTotalPages(self, n):
            if len(self.memories) > 0:
                return int((len(self.memories) - 1)/n) + 1
            else:
                return 0

        def getPage(self, n, p):
            page = []
            for x in range((n * p), ((n * p) + n)):
                if x < len(self.memories):
                    page.append((self.memories[x].name, self.memories[x].title, self.memories[x].thumbnail))
                else:
                    page.append((None, None, None))

            return page
    
    # James
    james_gallery_data = (
        # Name, Title, Image
        ("james_event_1", _("Event 1"), "james_event1.png"),
        ("james_event_2", _("Event 2"), "james_event2.png"),
        ("james_event_3", _("Event 3"), "james_event3.png"),
        ("james_event_4", _("Event 4"), "james_event4.png"),
        ("james_event_5", _("Event 5"), "james_event5.png"),
    )

    james_gallery = SGallery()
    james_gallery.addMemories(james_gallery_data)

    # Kim
    kim_gallery_data = (
        # Name, Title, Image
        ("kim_event_1", _("Event 1"), "kim_event1.png"),
        ("kim_event_2", _("Event 2"), "kim_event2.png"),
        ("kim_event_3", _("Event 3"), "kim_event3.png"),
        ("kim_event_4", _("Event 4"), "kim_event4.png"),
        ("kim_event_5", _("Event 5"), "kim_event5.png"),
    )

    kim_gallery = SGallery()
    kim_gallery.addMemories(kim_gallery_data)

# Galeria
screen buttons_gallery(xpos, ypos, characters):
    fixed:
        xpos xpos
        ypos ypos

        hbox at truecenter:
            xalign 1

            spacing 15

            for (name, character_button, character_card, sgallery) in characters:
                vbox:
                    spacing 10

                    if sgallery.countUnlockedMemories() > 0:
                        imagebutton at center, gallery_button_scale:
                            idle character_button
                            hover tint_hover(character_button)
                            focus_mask True
                            action ShowMenu("gallery_character", name, character_button, character_card, sgallery)
                        text str(sgallery.countUnlockedMemories()) + "/" + str(sgallery.countMemories()) at center:
                            size 40
                    else:
                        imagebutton at center, gallery_button_scale:
                            idle "gallery/locked_button.png"
                            #hover tint_hover("gallery/locked_button.png")
                            focus_mask True
                            action NullAction()
                        text "" at center:
                            size 40

screen gallery():

    modal True

    tag menu

    default main_characters = [
        # Name, Button, Card, SGallery
        ("James",       "gallery/james_button.png", "gallery/james_card.png", james_gallery),
        ("Kim",        "gallery/kim_button.png", "gallery/kim_card.png", kim_gallery),
    ]

    add im.Scale("gallery/background.png", 1920, 1080)

    use buttons_gallery(0, 0, main_characters)

    imagebutton:
        xalign 0.05
        yalign 0.95
        idle "buttons/left_button.png"
        hover tint_hover("buttons/left_button.png")
        focus_mask True
        action Return()

# Galeria Personaje

screen buttons_gallery_character(memories):
    for (name, title, thumbnail) in memories:
        if name:
            fixed at gallery_character_slot_scale:
                xmaximum 480
                ymaximum 320

                add im.Scale("gallery/slot.png", 480, 320)

                if checkUnlockedMemory(name) == True:
                    imagebutton at gallery_character_thumbnail_scale:
                        xalign 0.5
                        ypos 25

                        idle thumbnail
                        hover tint_hover(thumbnail)
                        focus_mask True
                        action Replay(name, locked=False)

                    text title:
                        xpos 35
                        ypos 250

                        size 28
                        color "#000"
                else:
                    text __("Locked"):
                        xpos 35
                        ypos 250

                        size 28
                        color "#000"
        else:
            text ""

screen gallery_character(name, character_button, character_card, sgallery):

    modal True

    tag menu

    default page = 1

    default grid_size = 9

    add im.Scale("gallery/background.png", 1920, 1080)

    add character_card:
        zoom 1.25

        yalign 1.00

        xpos 50

    fixed:
        xalign 0.5
        yalign 0.5

        xpos 0.625

        text name:
            xalign 0.5
            yalign 0.075

            size 60

        grid 3 3:
            xalign 0.5
            yalign 0.46

            spacing 10

            use buttons_gallery_character(sgallery.getPage(grid_size, page - 1))

    if sgallery.getTotalPages(grid_size) > 1:
        hbox:
            xalign 0.5
            yalign 0.95

            spacing 50

            if page > 1:
                imagebutton:
                    idle "buttons/left_button.png"
                    hover tint_hover("buttons/left_button.png")
                    focus_mask True
                    action SetScreenVariable("page", page - 1)
            else:
                imagebutton:
                    idle "buttons/left_button.png"
                    # hover tint_hover("buttons/left_button.png")
                    focus_mask True
                    action NullAction()

            if page < sgallery.getTotalPages(grid_size):
                imagebutton:
                    idle "buttons/right_button.png"
                    hover tint_hover("buttons/right_button.png")
                    focus_mask True
                    action SetScreenVariable("page", page + 1)
            else:
                imagebutton:
                    idle "buttons/right_button.png"
                    # hover tint_hover("buttons/right_button.png")
                    focus_mask True
                    action NullAction()

        text __("Page ") + str(page) + "/" + str(sgallery.getTotalPages(grid_size)):
            size 70

            xalign 0.93
            yalign 0.9375

    imagebutton:
        xalign 0.05
        yalign 0.95
        idle "buttons/left_button.png"
        hover tint_hover("buttons/left_button.png")
        focus_mask True
        action ShowMenu("gallery")

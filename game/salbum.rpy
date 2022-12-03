transform album_slot_scale:
    zoom 0.20
    rotate renpy.random.randint(-2, 2)

transform album_thumbnail_scale:
    zoom 1.00

init python:
    if persistent.photos is None:
        persistent.photos = []
        print(f"Created photos: {persistent.photos}")
    else: 
        print(f"Loaded photos: {persistent.photos}")
        
    # Check if a photo has been unlocked, total number of fragments needed
    def checkUnlockedPhoto(name, nfragments):
        fragments = []
        for x in range(nfragments):
            fragments.append(name + "_fragment_" + str(x + 1))

        b =  all(item in persistent.photos for item in fragments)

        return b

    # Check if a fragment has been unlocked
    def checkUnlockedPhotoFragment(name):
        b = False
        for x in persistent.photos:
            if x == name:
                b = True
        return b
    
    def unlockPhotoFragment(name, fragment):
        if checkUnlockedPhotoFragment(name + "_fragment_" + str(fragment)) == False:
            persistent.photos.append(name + "_fragment_" + str(fragment))
            print(_(f"Unlocked Photo Fragment: {name}_fragment_{fragment}"))
            #renpy.notify(_(f"Unlocked Photo Fragment: {name}_fragment_{fragment}"))

    def unlockPhotoFragmentWithMessage(name, fragment, message):
        renpy.notify(_(f"Unlocked Photo Fragment: {message}"))
        unlockPhotoFragment(name, fragment)

    class TPhoto:
        def __init__(self, name, title, thumbnail, nfragments):
            self.name = name
            self.title = title
            self.thumbnail = thumbnail
            self.nfragments = nfragments

    class SAlbum:
        def __init__(self):
            self.photos = []

        def addPhoto(self, name, title, thumbnail, nfragments):
            self.photos.append(TPhoto(name, title, thumbnail, nfragments))

        def addPhotos(self, data):
            for d in data:
                self.addPhoto(d[0], d[1], d[2], d[3])

        def unlockPhoto(self, name):
            for m in self.photos:
                if m.name == name:
                    for x in range(m.nfragments):
                        unlockPhotoFragment(m.name, x + 1)
                    
        def unlockAllPhotos(self):
            for m in self.photos:
                unlockPhoto(m.name)

        def countPhotos(self):
            return len(self.photos)

        def countUnlockedPhotos(self):
            total = 0
            for m in self.photos:
                if checkUnlockedPhoto(m.name, m.nfragments) == True:
                    total = total + 1
            return total

        def countPhotoFragments(self, name):
            fragments = [ x for x in persistent.photos if (name + "_fragment_") in x ]
           
            return len(fragments)

        def getTotalPages(self, n):
            if len(self.photos) > 0:
                return int((len(self.photos) - 1)/n) + 1
            else:
                return 0

        def getPage(self, n, p):
            page = []
            for x in range((n * p), ((n * p) + n)):
                if x < len(self.photos):
                    page.append((self.photos[x].name, self.photos[x].title, self.photos[x].thumbnail, self.photos[x].nfragments))
                else:
                    page.append((None, None, None, None))
            return page

    album_data = (
        # Name, Title, Image, Type, Number of fragments
        ("kim_event_4", _("The Trial"), "kim_event4.png", 4),
        ("james_event_5", _("Extra Event"), "james_event5.png", 1),
        ("kim_event_5", _("Extra Event"), "kim_event5.png", 1),
    )

    photo_album = SAlbum()
    photo_album.addPhotos(album_data)

screen buttons_album(photos):
    for (name, title, thumbnail, nfragments) in photos:
        if name:
            fixed at album_slot_scale:
                xmaximum 920
                ymaximum 1080

                if checkUnlockedPhoto(name, nfragments) == True:

                    add "album/slot.png"
                    
                    imagebutton at album_thumbnail_scale:
                        xpos 82
                        ypos 78
                        idle im.Crop(im.Scale(thumbnail, 1920, 1080), (425, 0, 1070, 1080))
                        hover tint_hover(im.Crop(im.Scale(thumbnail, 1920, 1080), (425, 0, 1070, 1080)))
                        focus_mask True
                        action Replay(name, locked=False)

                    text title:
                        xalign 0.5
                        yalign 1.5

                        size 76
                        color "#000"
                else:
                    text str(photo_album.countPhotoFragments(name)) + "/" + str(nfragments):
                        xalign 0.5
                        yalign 1.5

                        size 160
                        color "#fff"
        else:
            text ""

screen album:
    modal True

    tag menu

    default page = 1

    default grid_size = 8

    add im.Scale("album/background.png", 1920, 1080)

    text __("Album"):
        size 70

        xalign 0.5
        yalign 0.1

    grid 4 2:
        xalign 0.5
        yalign 0.35

        xspacing 10
        yspacing 120

        use buttons_album(photo_album.getPage(grid_size, page - 1))

    text __("Extra Events"):
        size 45

        xalign 0.5
        yalign 0.93

    if photo_album.getTotalPages(grid_size) > 1:
        hbox:
            xalign 0.97
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

            if page < photo_album.getTotalPages(grid_size):
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

        text __("Page ") + str(page) + "/" + str(photo_album.getTotalPages(grid_size)):
            size 70

            xalign 0.92
            yalign 0.83

    imagebutton:
        xalign 0.05
        yalign 0.95
        idle "buttons/left_button.png"
        hover tint_hover("buttons/left_button.png")
        focus_mask True
        action Return()
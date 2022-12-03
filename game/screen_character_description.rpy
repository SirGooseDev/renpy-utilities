screen character_description(xpos, ypos, separation, size, name, lastname, age, hei, hobby, occupation):
    text __("Name: ") + name:
        xpos xpos
        ypos ypos

        size size
    text __("Lastname: ") + lastname:
        xpos xpos
        ypos (ypos + separation)

        size size
    text __("Age: ") + age:
        xpos xpos
        ypos (ypos + (separation * 2))

        size size
    text __("Height: ") + hei:
        xpos xpos
        ypos (ypos + (separation * 3))

        size size
    text __("Hobby: ") + hobby:
        xpos xpos
        ypos (ypos + (separation * 4))

        size size
    text __("Occupation: ") + occupation:
        xpos xpos
        ypos (ypos + (separation * 5))

        size size


label extra_screen:

    show screen character_description(100, 100, 50, 30, "James", "McGill", "34", "1.70", __("Movies"), __("Lawyer"))
    
    pause

    hide screen character_description

    return
def demo_1():

    title = "Demo of textbox: Classic box"

    gnexp = ("This is a demo of the classic textbox call, "
             "you can see it closes when ok is pressed.\n\n")

    challenge = "INSERT A TEXT WITH MORE THAN TWO PARAGRAPHS"

    text = "Insert your text here\n"

    msg = gnexp + challenge

    finished = False
    while True:

        text = textbox(msg, title, text)
        escaped = not text
        if escaped or finished:
            break

        if text.count("\n") >= 2:
            msg = (u"You did it right! Press OK")
            finished = True
        else:
            msg = u"You did it wrong! Try again!\n" + challenge
            
demo_1()

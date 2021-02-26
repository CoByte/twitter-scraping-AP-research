import tkinter as tk
from tkinter import N, E, S, W
import tkinter.font as font
import json
from random import shuffle


# Green + is if text is pro-conspiracy
# Red - is if text is anti-conspiracy
# Gray o is if text is conspiracy neutral


totalTweets = 175504

target = "hydroxychloroquine"

outPro = "../data/training data/{}/pro-conspiracy.txt".format(target)
outAnti = "../data/training data/{}/anti-conspiracy.txt".format(target)
outNeutral = "../data/training data/{}/conspiracy-neutral.txt".format(target)


class Dataer:

    def __init__(self, dataset, display):
        self.dataset = dataset
        self.display = display

        self.started = False
        self.ended = False
        self.currentText = None

        self.keysDown = set()

    def start(self):
        self.started = True

        self.update_data()

    def update_data(self):
        try:
            self.currentText = next(self.dataset)
            self.display.config(text=self.currentText)
        except StopIteration:
            self.display.config(text="Data has been exhausted!", fg="blue")

    def button_pushed(self, sortTo):
        if not self.started:
            return

        if self.ended:
            return

        if sortTo == "+":
            fileToAddTo = outPro
        elif sortTo == "-":
            fileToAddTo = outAnti
        elif sortTo == "o":
            fileToAddTo = outNeutral
        else:
            raise Exception("Button is doing bad things that it shouldn't")

        with open(fileToAddTo, "a") as file:
            file.write(self.currentText + "\n")

        self.update_data()

    def key_pushed(self, sortTo, button):
        def inner(_):
            self.keysDown.add(sortTo)
            button.config(relief=tk.SUNKEN)
        return inner

    def key_released(self, sortTo, button):
        def inner(_):
            self.keysDown.discard(sortTo)
            button.config(relief=tk.RAISED)

            if len(self.keysDown) == 0:
                self.button_pushed(sortTo)

        return inner


def update_dataer(dataer, output):
    return lambda: dataer.button_pushed(output)


def get_data_set(countLbl):
    with open("../data/cleaned data/hydroxychloroquine + 2020-01 - 2020-10-31.json") as file:
        data = json.load(file, strict=False)

    shuffle(data)
    data = data[0:100]

    for c, d in enumerate(data):
        countLbl.config(text="{} / {}".format(c+1, len(data)))
        yield d["tweet"]



root = tk.Tk()
root.resizable(False, False)

labelFont = font.Font(family="Courier New")
buttonFont = font.Font(family="Courier New", size=15, weight="bold")

label = tk.Label(root, justify=tk.CENTER, wraplength=350, font=labelFont, width=40, height=15)
label.grid(row=0, column=0, columnspan=3)

countLbl = tk.Label(root, justify=tk.CENTER, font=labelFont)
countLbl.grid(row=2, column=0, columnspan=3)

inator = Dataer(get_data_set(countLbl), label)

buttons = [
    tk.Button(root, text="+", font=buttonFont, bg="green"),
    tk.Button(root, text="o", font=buttonFont, bg="gray"),
    tk.Button(root, text="-", font=buttonFont, bg="red")
]

for count, b in enumerate(buttons):
    b.grid(row=1, column=count, sticky=N+E+S+W)
    b.config(command=update_dataer(inator, b.cget("text")))

for k, out, b in zip(["Left", "Down", "Right"], ["+", "o", "-"], buttons):
    kPress = "<{}>".format(k)
    kRelease = "<KeyRelease-{}>".format(k)

    root.bind(kPress, inator.key_pushed(out, b))
    root.bind(kRelease, inator.key_released(out, b))

root.bind("<a>", lambda _: print("wack"))

if input("WARNING: running this code will erase your data set. Are you sure you wish to continue? (y/n): ") == "y":
    for path in [outNeutral, outAnti, outPro]:
        with open(path, "w+") as f:
            f.write("")

    inator.start()
    root.mainloop()

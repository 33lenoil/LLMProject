from langchain import PromptTemplate
from langchain.llms import OpenAI
from tkinter import *
from tkinter import ttk

LANGUAGES = ["Pick a language", "English", "French", "Spanish", "Chinese", "German", "Italian",
             "Portuguese", "Russian", "Japanese", "Dutch", "Arabic", "Hindi", "Hebrew"]

# set up the LLM
llm = OpenAI(temperature=0.9)

# the prompt template
country_prompt = PromptTemplate(
    template="Translate \"{text}\" from {source_language} to {destination_language}?",
    input_variables=["text", "source_language", "destination_language"],
)


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        # the exit button
        exit_button = Button(self, text="Exit", fg="Red", width=13, height=8, command=self.click_exit_button)
        exit_button.pack(side=BOTTOM)

        # the language drop-down lists
        source_frame = Frame(self)
        source_label = Label(source_frame, text="Select the source language")
        source_label.pack(side=TOP)
        source_lan = StringVar(source_frame)
        source_lan.set(LANGUAGES[0])
        source_list = OptionMenu(source_frame, source_lan, *LANGUAGES)
        source_list.pack(side=TOP)
        source_frame.pack(side=TOP)

        destination_frame = Frame(self)
        destination_label = Label(destination_frame, text="Select the destination language")
        destination_label.pack(side=TOP)
        destination_lan = StringVar(destination_frame)
        destination_lan.set(LANGUAGES[0])
        destination_list = OptionMenu(destination_frame, destination_lan, *LANGUAGES)
        destination_list.pack(side=TOP)
        destination_frame.pack(side=TOP)

        source_text = Text(self)
        source_text.pack(side=LEFT)

        destination_text = Text(self)
        destination_text.pack(side=RIGHT)

        # the submit button
        submit_button = Button(self, text="Submit", fg="Blue", width=13, height=8,
                               command=lambda: self.click_submit_button(source_lan, destination_lan, source_text,
                                                                        destination_text))
        submit_button.pack(side=BOTTOM)

    def click_exit_button(self):
        exit()

    def click_submit_button(self, source_lan, destination_lan, source_text, destination_text):
        print(source_text.get(1.0, "end-1c"))
        print(source_lan.get())
        print(destination_lan.get())
        result = llm(country_prompt.format(text=source_text.get(1.0, "end-1c"), source_language=source_lan.get(),
                                           destination_language=destination_lan.get()))
        print(result)
        print(len(result))
        destination_text.delete(1.0, "end")
        destination_text.insert(1.0, result[2:])


def main():
    print("Program started!")

    # set up Tkinter window
    root = Tk()
    app = Window(root)
    root.wm_title("Smart Translator")
    root.geometry("1300x800")
    style = ttk.Style(root)
    style.theme_use('aqua')

    # show window
    root.mainloop()


if __name__ == "__main__":
    main()

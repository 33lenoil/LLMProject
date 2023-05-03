from langchain import PromptTemplate
from langchain.llms import OpenAI


def main():
    print("Program started!")
    llm = OpenAI(temperature=0.9)

    while 1:
        country_prompt = PromptTemplate(
            template="how to say \"{text}\" in {language}?",
            input_variables=["text", "language"],
        )
        text_input = input("Please type in a piece of text.\n")
        language_input = input("What language do you want to translate to?\n")
        print(llm(country_prompt.format(text=text_input, language=language_input)))


if __name__ == "__main__":
    main()

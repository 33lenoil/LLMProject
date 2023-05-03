from langchain.llms import OpenAI


def main():
    print("Program started!")
    llm = OpenAI(temperature=0.9)


if __name__ == "__main__":
    main()

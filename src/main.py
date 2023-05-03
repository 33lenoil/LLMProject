from langchain.llms import OpenAI


def main():
    print("Program started!")
    llm = OpenAI(temperature=0.9)

    while 1:
        curr_input = input("Ask me something.\n")
        # curr_input = "What would be a good company name for a company that makes colorful socks?"
        print(llm(curr_input))


if __name__ == "__main__":
    main()

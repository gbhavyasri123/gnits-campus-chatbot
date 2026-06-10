from chatbot.engine import ask_question

while True:

    query = input("Ask GNITS Bot: ")

    if query.lower() == "exit":
        break

    answer = ask_question(query)

    print("\nBot:", answer)
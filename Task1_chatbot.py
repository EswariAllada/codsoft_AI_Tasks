def chatbot():
    print("Hello! I'm a simple chatbot. Type 'exit' to end our conversation.")

    while True:
        user_input = input("You: ").lower()  # Get user input and convert to lowercase for easier matching

        if user_input == "exit":
            print("Goodbye! Have a great day!")
            break
        elif "hi" in user_input or "hello" in user_input:
            print("Chatbot: Hello! How can I help you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I’m a chatbot created for this task. You can call me Chatbot!")
        elif "what is ai" in user_input:
            print("Chatbot: AI, or Artificial Intelligence, refers to the simulation of human intelligence in machines that are programmed to think, learn, "
            "and make decisions like humans. It includes areas like machine learning, deep learning, natural language processing, and robotics. "
            "AI is used in applications like self-driving cars, virtual assistants (like me!), healthcare diagnostics, and much more.")
        elif "thank you" in user_input:
            print("Chatbot: You're welcome! Let me know if you need anything else.")
        else:
            print("Chatbot: Sorry, I don't understand that. Can you try asking something else?")

# Start the chatbot
chatbot()
#output
#Hello! I'm a simple chatbot. Type 'exit' to end our conversation.
#You: hi
#Chatbot: Hello! How can I help you today?
#You: how are you
#Chatbot: I'm just a bot, but I'm doing great! How about you?
#You: your name
#Chatbot: I’m a chatbot created for this task. You can call me Chatbot!
#You: what is ai
#Chatbot: AI, or Artificial Intelligence, refers to the simulation of human intelligence in machines that are programmed to think, learn, and make decisions like humans. It includes areas like machine learning, deep learning, natural language processing, and robotics. AI is used in applications like self-driving cars, virtual assistants (like me!), healthcare diagnostics, and much more.
#You: thank you
#Chatbot: You're welcome! Let me know if you need anything else.
#You: exit
#Goodbye! Have a great day!

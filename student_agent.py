# Simple Rule-Based Student Assistant Agent
# SLE-1: Introduction to Artificial Intelligence

def student_agent(user_input):
    user_input = user_input.lower()

    if "study" in user_input or "exam" in user_input:
        return "Agent: Make a study plan and focus on one topic at a time."

    elif "break" in user_input:
        return "Agent: Take a short break and relax for a few minutes."

    elif "sleep" in user_input:
        return "Agent: Get enough sleep so you can study with better concentration."

    elif "coding" in user_input:
        return "Agent: Practice coding regularly and solve small problems."

    elif "hello" in user_input or "hi" in user_input:
        return "Agent: Hello! How can I help you today?"

    elif "help" in user_input:
        return "Agent: You can ask me about study, coding, break, exam or sleep."

    else:
        return "Agent: I do not have a rule for this input yet."


print("===== Student Assistant Agent =====")
print("Type 'exit' to stop the agent.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
        break

    response = student_agent(user_input)
    print(response)
    
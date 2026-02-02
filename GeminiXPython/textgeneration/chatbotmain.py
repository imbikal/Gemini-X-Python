from google import genai
from google.genai import types

client = genai.Client()
chat = client.chats.create(model="gemini-2.5-flash")

print("Chat begins here... type 'endchat' to close")

userinput = input("User : ")

while userinput != 'endchat':
    response = chat.send_message(userinput)
    print("Jarvis : " + response.text)
    userinput = input("User : ")



"""
Previous code referring to chatbotdemo.py

1. Automatic Memory Management
In your previous code, you were manually carrying a "notebook" (chat = []) and writing down every line yourself using .append().

The New Way: client.chats.create() creates a stateful session.

The Subtlety: The chat object now acts like a dedicated "Chat Room." When you call chat.send_message(), the object automatically remembers what you said previously and what it replied. You no longer have to manage a list of strings manually.

2. Cleaner Data Structure
Your old code sent a list of raw strings to the AI. This new version sends structured Message Objects.

The Difference: Instead of just sending a block of text that says "User : Hello", this version sends data that explicitly tells the AI: "This part is the User's role, and this part is the Model's role." This prevents the AI from getting confused about who said what.

3. "Leaner" Code
Notice how the while loop has shrunk:

Old Loop: 5-6 lines (append user, call model, append AI, print).

New Loop: 3 lines (send message, print, get next input).

Why it's better: It's easier to read and less prone to bugs. You can't accidentally forget to "append" a message to the history because the chat object handles it for you.

"""
    



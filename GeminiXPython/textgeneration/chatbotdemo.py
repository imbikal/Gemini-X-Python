from google import genai
from google.genai import types

client = genai.Client()

print("Chat begins here... type 'endchat' to close")
chat = []
userinput = input("User : ")

while userinput != 'endchat':
    chat.append("User : " + userinput)
    systemoutput = client.models.generate_content(
        contents=chat,
        model = 'gemini-2.5-flash-lite',
        config = types.GenerateContentConfig(
            system_instruction="Answer in 1 line with 50 characters"
        )

    )
    chat.append("Jarvis : " + systemoutput.text)
    print("Jarvis : ",systemoutput.text)
    userinput = input("User : ")




    """

    1. The "Memory Bank" (chat = [])
    You've created an empty list called chat. Think of this as a transcript or a notebook. Every time you say something, and every time the AI (Jarvis) replies, it gets written down in this notebook using chat.append().
    
    2. The Endless Loop (while userinput != 'endchat')
    This tells the program: "Keep the conversation going forever until I specifically type the word 'endchat'." This is what makes it feel like a real chat app rather than a one-off command.
    
    3. Giving the AI the Full Story (contents=chat)
    In your previous scripts, you probably just sent a single prompt. Here, you are sending the entire chat list.Because Gemini receives the whole list every time, it can "remember" that you said "Hi, my name is Bikal" five messages ago.
    
    4. The "Brain Surgery" (GenerateContentConfig)
    This is the most interesting part of your code. You are using System Instructions to rewrite the AI's personality:System Instruction: You told it to "Answer in 1 line with 50 characters." * The Result: No matter how much you talk, Jarvis will be extremely brief and blunt—like a very busy assistant.
    
    5. Managing the Transcriptchat.append
    ("User : " + userinput):
    Saves your message to the notebook.chat.append

    ("Jarvis : " + systemoutput.text):
    Saves the AI's reply to the notebook.Summary TableCode ComponentWhat it does in "Layman" termschat = []The "Long-term memory" of the conversation.whileThe "Engine" that keeps the chat alive.system_instructionThe "Rulebook" the AI must follow (be short/brief).configThe "Settings" menu for the AI's behavior.

    """
     
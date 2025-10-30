import requests 
import ollama 
from ollama import chat
from oneNote_generator import generate_outcome_answer3

model="llama3.2"

def generate_outcome():
    """
    Takes the input and generates a structure outline using Ollama
    """
    prompt = f"""You are Lumin, an AI Assitant integrated into a multi-mode chaxbox.
        when a user starts a session, show the available modes: 

        1. Normal Chat - Ask anything or have a general conversation
        2. Documentation Search - Search through a specific documentation source and answer based on that content.
        3. OneNote Helper - Create a comprehensive learning guide that the user is able to import into OneNote.

        Ask the user to choose one of these modes by typing its number or name. 

        Once the mode is selected:
        - Stay within tha tmode's purpose until the user switches.
        - If the user says "switch mode" or "change mode", show the list again.
        - If the user asks something unrelated to the current model, politely remind them of the active mode and suggest switching. 

        For example:
        -In "Normal Chat", respond freely and conversationally.
        -In "Documentation Search", only use the provided docs for answers.
        -In "Code Helper", prioritize concise, technical help.

        Always respond clearly and keep your tone friendly and professional. 
        """
 
    try:
        response = ollama.generate(model=model, prompt=prompt)
        print(response.response)
        return
    except requests.exceptions.ConnectionError:
        print("❌ Please enter a valid topic!")
        print("Make sure Ollama is running!")
        print("Try rynning: ollama serve")
        raise
    except Exception as e:
        print("❌ Error calling Ollama: {e}")
        raise
def generate_outcome_answer(answer):
    """
    Answer to the initial outcome
    """
    if not answer:
        print("❌ Please enter a response")
        return
    
    messages = [{
        "role": "user",
        "content": answer
    }]

    try:
        response = ollama.chat(model=model, messages=messages)
        print(response.message.content)
        return  
    except requests.exceptions.ConnectionError:
        print("❌ Please enter a valid topic!")
        print("Make sure Ollama is running!")
        print("Try rynning: ollama serve")
        raise
    except ollama.ResponseError as e:
        print('Error', e.error)
        if e.status_code == 404:
            ollama.pull('does-not-yet-exist')
    except Exception as e:
        print("❌ Error calling Ollama:",  e)
        raise
def main():
    try:
        #Generate initial outcome
        generate_outcome()

        get_input = input("Enter the option: ")
        print("-------------------------------")
        match get_input:
            case "" | "0" :
                print("❌ Please enter a valid option!")
                return
            case  "1" | "2" | "3" | "0":
                print("You Selectted option", get_input)
            case "exit":
                print("Thank you! Come back anything")
                return
            case _:
                print("❌ Please enter a valid option!")
                return
        answer = ''
        while answer != "exit":
            if answer == '1':
                continue
            elif answer == '2':
                break
            elif answer == '3':
                generate_outcome_answer3() 
            elif answer == 'switch mode' or answer == 'change mode':
                generate_outcome()
                answer = input("Enter the option: ")
                print("-------------------------------")
                continue
            elif answer.lower() == "exit":
                print("Thank you! Come back anything")
                break
            else:
                answer = input("Ask anything: ")
                print("-------------------------------")
                generate_outcome_answer(answer)
                continue
        return
    except Exception as e:
        print("❌ Error calling Ollama: ", e)
        raise

if __name__ == "__main__":
    main()
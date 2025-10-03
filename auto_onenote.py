import requests
import json

def generate_learning_outline(topic, model="llama3.2"):
    """
    Takes a learning topic and generates a structured outline with content using Ollama
    """
    
    prompt = f"""Create a comprehensive learning guide for: "{topic}"

Structure your response as a detailed outline with:
- Main sections (use ## for section headers)
- Subsections with specific topics (use ### for subsection headers)
- Key points under each subsection (use bullet points)
- Brief explanations for each point

Make it practical and beginner-friendly. Include 4-6 main sections covering the topic from basics to intermediate level.

Format example:
## Section 1: Getting Started
### What is [Topic]?
- Key point 1
- Key point 2

### Why Learn [Topic]?
- Reason 1
- Reason 2
"""

    print(f"🤖 Generating learning guide for: {topic}")
    print(f"🦙 Using Ollama model: {model}")
    print("⏳ This may take a moment...\n")
    
    # Call Ollama API (runs locally)
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        return result['response']
    except requests.exceptions.ConnectionError:
        print("❌ Error: Cannot connect to Ollama.")
        print("Make sure Ollama is running!")
        print("Try running: ollama serve")
        raise
    except Exception as e:
        print(f"❌ Error calling Ollama: {e}")
        raise

def save_to_markdown(topic, content):
    """
    Saves the generated content to a markdown file
    """
    # Create a safe filename
    filename = topic.replace(" ", "_").replace("/", "-") + ".md"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# {topic}\n\n")
        f.write(content)
    
    return filename

def main():
    print("=" * 60)
    print("  AUTO-ONENOTE GENERATOR")
    print("  Create structured learning notes automatically")
    print("  Using Ollama (FREE & LOCAL)")
    print("=" * 60)
    print()
    
    # Get topic from user
    topic = input("📚 Enter a topic you want to learn: ").strip()
    
    if not topic:
        print("❌ Please enter a valid topic!")
        return
    
    # Optional: let user choose model
    print("\n💡 Tip: Using default model 'llama3.2'")
    print("   (You can modify the script to use other models)")
    print()
    
    # Generate the outline
    try:
        content = generate_learning_outline(topic)
        
        # Save to file
        filename = save_to_markdown(topic, content)
        
        print("\n✅ Success!")
        print(f"📄 Saved to: {filename}")
        print()
        print("🎯 Next steps:")
        print("  1. Open the .md file in any text editor")
        print("  2. Copy the content")
        print("  3. Paste into OneNote (or any note app)")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nTroubleshooting:")
        print("  1. Make sure Ollama is running: 'ollama serve'")
        print("  2. Check you have a model: 'ollama list'")
        print("  3. If no model, download one: 'ollama pull llama3.2'")

if __name__ == "__main__":
    main()
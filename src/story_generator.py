from transformers import pipeline

def generate_story(emotion, user_text):
    """
    Generates a short AI-powered story based on detected emotion.
    """
    story_prompt = f"A {emotion} story inspired by: {user_text}"
    generator = pipeline("text-generation", model="gpt2")
    story = generator(story_prompt, max_length=200, num_return_sequences=1)
    
    return story[0]['generated_text']

# Example Usage
if __name__ == "__main__":
    emotion = "Positive"
    user_text = "I'm feeling nostalgic and joyful"
    story_text = generate_story(emotion, user_text)
    print(f"Generated Story:\n{story_text}")

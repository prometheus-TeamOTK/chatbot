import json
from openai import OpenAI
import os

class Summary:
    def __init__(self, chatting_file, situation):
        self.chatting_file = chatting_file
        self.situation = situation
    
    def summary(self):
        with open(self.chatting_file, "r", encoding="utf8") as json_file:
            json_data = json_file.read()
            chatting_data = json.loads(json_data)
        
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Summarize the following conversation with the given situation."},
                {"role": "user", "content": "Do not use word 'Bot' or 'User' in the summary. Just use character name."},
                {"role": "user", "content": "I will user that summarization for image generation. Make the summary as stable diffusion model prompt."},
                {"role": "user", "content": "Summary whole context in 50 tokens, and wrote in English."},
                {"role": "user", "content": "The Example of summary is: naruto, 1boy, solo, male focus, blue eyes, facial mark, looking at viewer, smiling, orange jacket, jacket, closed mouth. You should follow this format."},
                {"role": "assistant", "content": "Yes."},
                {"role": "user", "content": str(chatting_data)},
                {"role": "user", "content": self.situation}
            ],
        )
    
        return response.choices[0].message.content

def main():
    sum = Summary("src/data/conversation.json", "백설공주(Bot)와 마녀(User)가 백설공주가 지내는 난쟁이 오두막에서 마주친 상황. 마녀는 백설공주에게 사과를 줄지 말지 갈등한다.")
    print(sum.summary())

if __name__ == "__main__":
    main()
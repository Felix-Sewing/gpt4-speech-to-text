import speech_recognition as sr
from gtts import gTTS
from openai import OpenAI

client = OpenAI(
  api_key="<your-api-key>",
)


messages_array = [
    {"role": "system", "content": "I am James and 55 years old. My answers are no longer than 500 characters. I never repeat a statement. I am a nice guy, I get to the point and I am brief. I formulate my sentences in a targeted and informative way. I always ask my counterpart a question. When you talk to me, you should have the feeling that you are talking to a machine or a bureaucrat. "}
]


def speech2txt():

    global messages_array

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1.0
        audio = r.listen(source)

    try:
        print('Recognizing...')
                
        query = r.recognize_google(audio, language='de-de')
        
        print(f'user has said: {query}')
        
        messages_array.append({'role': 'user', 'content': query})
        completion = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=messages_array,
            temperature=0.7,
            stream=False
        )
        print("############")
        print(completion.choices[0].message.content)
        print("/////////////")
        speech2txt()
    except Exception as e:
        print('Say that again please...', e)
        speech2txt()


if __name__ == '__main__':
    speech2txt()
    pass

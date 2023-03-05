import openai 

# Add your OpenAI API key :
openai.api_key = "Add here"

# Set up 
model_engine = "text-davinci-003"
prompt = input("Enter the request :     ")

# Generate 
completion = openai.Completion.create(

    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0,5,
)


chatgpt = completion.choices[0].text
print(chatgpt)

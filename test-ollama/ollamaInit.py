from ollama import chat
from ollama import ChatResponse

def getQuery(question):
    with open('prompts/query.txt', 'r', encoding='utf-8') as file:
        queryPrompt = file.read() 
    with open("prompts/question.txt", 'r') as file:
        content = file.read()
    formattedContent = content.replace("{question}",question)
    response: ChatResponse = chat(model='llama3.2',messages=[
        {
            'role': 'system',
            'content': queryPrompt,
        },
        {
            'role': 'user',
            'content': formattedContent,
        },
    ])
    return response.message.content

def getResponse(question,data):
    with open('prompts/query.txt', 'r', encoding='utf-8') as file:
        responsePrompt = file.read() 
    formattedResponsePrompt = responsePrompt.format(data=data, question=question)
    response: ChatResponse = chat(model='custom-llm', messages=[
        {
            'role': 'user',
            'content': formattedResponsePrompt,
        },
    ])
    return response.message.content
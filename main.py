from gpt4all import GPT4All
import json

"""
**********************************************************
Takes two strings one being a requests the other being the
model used for the request sends the request to the LLM
returns the response
Parameters: Search Queue, Model used
Returns: A Response from your Model of choice
*********************************************************
"""
def ask_ai(quere, model):
    model = GPT4All(model)
    with model.chat_session():
        response = model.generate(prompt=quere)
        return response


def all_models(datafile='models2.json'):
    with open (datafile,'r') as model_data:
        model_dict = json.load(model_data)
        for dict_model in model_dict:
            print('Name:',dict_model['name'],'\n'
                  'filename:',dict_model['filename'],'\n'
                   'type:',dict_model['type'],'\n'
                   'description:',dict_model['description'],'\n'
                    'URL:',dict_model['description'],'\n')
        model_data.close()

def model_check(name,datafile='models2.json'):
    with open(datafile,'r') as model_data:
        model_dict = json.load(model_data)
        for dict_model in model_dict:
            if dict_model['name'].upper() in name.upper():
                return dict_model['name']
            else:
                continue



def change_model():
    change_made = False
    while not change_made:
        model = input('Please enter the name of the model or type ls to list all the available models ')
        if 'ls' in model:
            all_models()
        else:
            return model


if __name__ == "__main__":
    model = 'orca-2-7b.Q4_0.gguf'
    while True:
        prompt = input("Hello What You Want ")
        if 'ls' in prompt:
            all_models('models2.json')
        elif 'ch' in prompt:
            model = change_model()
            print(model)
        else:
            print(ask_ai(prompt, model))
print(model_check("Mistral OpenOrca"))

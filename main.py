from gpt4all import GPT4All
import json


def ask_ai(quere, model):
    model = GPT4All(model)
    with model.chat_session():
        response = model.generate(prompt=quere)
        return response


def all_models(datafile):
    with open (datafile,'r') as model_data:
        model_dict = json.load(model_data)
        for dict_model in model_dict:
            print('Name:',dict_model['name'],'\n'
                  'filename:',dict_model['filename'],'\n'
                   'type:',dict_model['type'],'\n'
                   'description:',dict_model['description'],'\n'
                    'URL:',dict_model['description'],'\n')


model = 'orca-2-7b.Q4_0.gguf'
while True:
    prompt = input("Hello What You Want ")
    if 'model' in prompt:
        all_models('models2.json')
    else:
        print(ask_ai(prompt, 'orca-2-7b.Q4_0.gguf'))

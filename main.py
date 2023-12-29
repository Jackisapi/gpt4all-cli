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
def ask_ai(quere, model,debug=False):
    model = GPT4All(model)
    with model.chat_session():
        if debug == True:
            tokens = []
            response = model.generate(prompt=quere)
            for token in response:
                tokens.append(token)
                print(tokens)
                return response
            else:
                response = model.generate(prompt=quere)
                return response

"""
*************************************************************
Opens "models2.json from the GPT4All Project and prints all
The the Data lables Name filename type Desc and url from 
each object 
Parameters File ("Function Can however be called without
Data file being defined")
Returns: All the Models officialy supported by GPT4ALL
*************************************************************
"""
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

"""
*************************************************************
In development (aka no workie) at the moment butin theory
takes a String Checks to see if that string is a available 
model for gpt4all if not found it will throw an error
Parameters: Name, datafile(doesnt need filled)
Returns: Currently just the name of the model if found
*************************************************************
"""
def model_check(name,datafile='models2.json'):
    with open(datafile,'r') as model_data:
        model_dict = json.load(model_data)
        for dict_model in model_dict:
            if dict_model['name'].upper() in name.upper():
                return dict_model['filename']
            else:
                continue


"""
*************************************************************
Asks the user for input and returns that input however
if the input is ls it calls all_models Soon to be exteneded 
with model_check as seen above 
Params: None
Returns: User Input
*************************************************************
"""
def change_model():
    change_made = False
    while not change_made:
        model = input('Please enter the name of the model or type ls to list all the available models ')
        if 'ls' in model:
            all_models()
        else:
            model = model_check(model)
            return model



if __name__ == "__main__":
    model = 'orca-2-7b.Q4_0.gguf'
    while True:
        prompt = input("Hello What You Want ")
        if prompt == 'ls':
            all_models('models2.json')
        elif prompt == 'ch':
            model = change_model()
            print(model)
        else:
            print(ask_ai(prompt, model,debug=True))



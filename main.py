from modular_function_main_function import *
from text_function import txt_reader
from gpt4all import GPT4All

# To See all the functions for this program please look at modular_function_main_function.py and text_function.py


if __name__ == "__main__":
    model = "gpt4all-falcon-q4_0.gguf"
    device = 'amd'
    talk = GPT4All(model_name=model, device=device)
    with talk.chat_session():
        while True:
            prompt = input("Hello What You Want ")
            if prompt == 'ls':
                all_models('models2.json')
            elif prompt == 'ch':
                model = change_model(model)
                print(model)
                talk = GPT4All(model_name=model, device=device)
            elif prompt == 'hw':
                device = hw_change(device)
                print(f"Device Changed To {device}")
                talk = GPT4All(model_name=model, device=device)
            elif prompt == 'exit':
                exit_prompt()
            elif prompt == 'help':
                txt_reader('README.md')
            else:
                response = talk.generate(prompt=prompt)
                print(response)

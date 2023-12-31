from modular_function_main_function import *
from text_function import txt_reader
# To See all the functions for this program please look at modular_function_main_function.py and text_function.py

if __name__ == "__main__":
    model = 'orca-2-7b.Q4_0.gguf'
    device = 'cpu'
    while True:
        prompt = input("Hello What You Want ")
        if prompt == 'ls':
            all_models('models2.json')
        elif prompt == 'ch':
            model = change_model(model)
            print(model)
        elif prompt == 'hw':
            device = hw_change(device)
        elif prompt == 'exit':
            exit_prompt()
        elif prompt == 'help':
            txt_reader('README.md')
        else:
            print(ask_ai(prompt, model, debug=True, device=device))

from transformers import AutoModelForSequenceClassification, AutoTokenizer
from safetensors import safe_open


def download_model(model_tag):
    try:
        tensors = {}
        with safe_open('/home/jack/.cache/gpt4all/tesk/model-00001-of-00002.safetensors', framework='pt',
                       device=0) as f:
            for k in f.keys():
                tensors[k] = f.get_tensor(k)
        # return f'Model Successfully Downloaded at {output_dir}'
        return tensors
    except Exception as hf_error:
        return f'Sorry ; ( Model Download Failed Due To Error: {hf_error}'


print(download_model('SkunkworksAI/tinyfrank-1.4B'))

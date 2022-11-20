import pdb
import bittensor as bt

import argparse

from transformers import AutoModelForCausalLM



def split_models(model, num_gpus: int):
    layers = model.transformer.h
    layers_per_gpu = len(layers) // num_gpus
    
    # a for loop that adds the layers to the gpu with .to(device)
    counter = 0
    gpu_id = 0
    for i in range(len(layers)):
        # add the layer to the gpu
        if i+1 % layers_per_gpu == 0:
            gpu_id += 1
            counter = 0
            
        print(f"Adding layer {i} to gpu {gpu_id}")
        layers[i].to(f"cuda:{gpu_id}")
        counter += 1

    pdb.set_trace()



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_gpus', type=int, default=1)
    args = parser.parse_args()

    model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M")

    tokenizer = bt.tokenizer()
    split_models(model, args.num_gpus)
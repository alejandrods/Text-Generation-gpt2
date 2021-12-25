# -*- coding: utf-8 -*-

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
# Disable gradient calculation - Useful for inference
torch.set_grad_enabled(False)

# Check if gpu or cpu
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")
model = model.to(device)


def generate(user_text, size=20):
    """
    Function to generate text

    :param user_text: User text
    :param size: Number of words to generate
    :return: string with user text + generated text
    """

    # Tokenizer user_text
    tokens = tokenizer.encode(user_text)

    # Send to cpu/gpu
    tokens = torch.tensor([tokens]).to(device)

    # Generate
    # max_length = context_length + output_length
    tokens = model.generate(tokens, max_length=size+tokens.shape[1], do_sample=True, top_k=50)
    tokens = tokens[0].tolist()
    return tokenizer.decode(tokens, skip_special_tokens=True)

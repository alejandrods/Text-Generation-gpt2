# -*- coding: utf-8 -*-

# Downloads model(s)
# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# GPT2LMHeadModel.from_pretrained('distilgpt2').save_pretrained('./src/distilgpt2')
# GPT2Tokenizer.from_pretrained('distilgpt2').save_pretrained('./src/distilgpt2')

from transformers import AutoTokenizer, AutoModelWithLMHead

AutoTokenizer.from_pretrained('gpt2').save_pretrained('./gpt2-xl')
AutoModelWithLMHead.from_pretrained('gpt2').save_pretrained('./gpt2-xl')

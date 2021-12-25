# GPT-3 EleutherAI
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained(
    "EleutherAI/gpt-neo-1.3B").save_pretrained('./src/gpt-neo')
model = AutoModelForCausalLM.from_pretrained(
    "EleutherAI/gpt-neo-1.3B").save_pretrained('./src/gpt-neo')

# GPT-2
# from transformers import AutoTokenizer, AutoModelWithLMHead
#
# AutoTokenizer.from_pretrained('gpt2').save_pretrained('./gpt2-xl')
# AutoModelWithLMHead.from_pretrained('gpt2').save_pretrained('./gpt2-xl')
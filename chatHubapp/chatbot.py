from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Model ve tokenizer'ı yükle
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

def generate_response(user_input, chat_history_ids=None):
    # Tokenizer kısmını güncelle:
    new_input = tokenizer.encode_plus(
        user_input + tokenizer.eos_token,
        return_tensors="pt",
        return_attention_mask=True,
    )

    # Yanıt üretme kısmı:
    chat_history_ids = model.generate(
        input_ids=new_input["input_ids"],
        attention_mask=new_input["attention_mask"],
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        temperature=0.7,
        do_sample=True
    )

    # Yanıtı decode et
    bot_response = tokenizer.decode(
        chat_history_ids[:, new_input["input_ids"].shape[-1]:][0],
        skip_special_tokens=True
    )
    return bot_response

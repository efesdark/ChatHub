from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Model ve tokenizer'ı yükle
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

def generate_response(user_input, chat_history_ids=None):
    # Kullanıcı mesajını tokenize et
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    
    # Modelden yanıt al
    chat_history_ids = model.generate(
        new_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        temperature=0.7,
    )
    
    # Yanıtı decode et
    bot_response = tokenizer.decode(chat_history_ids[:, new_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return bot_response





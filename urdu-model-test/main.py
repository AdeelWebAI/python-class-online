from unsloth import FastLanguageModel
import torch

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "enstazao/Qalb-1.0-8B-Instruct",
    max_seq_length = 2048,
    dtype = None,
    load_in_4bit = True, # <--- Currently set to use 4-bit quantization
)
FastLanguageModel.for_inference(model)


urdu_system_prompt = "آپ ایک مددگار اور بے ضرر مصنوعی ذہانت کے اسسٹنٹ ہیں۔ آپ اردو میں سوالات کے درست جوابات دیتے ہیں۔"

questions = [
    "پاکستان کا قومی کھیل کیا ہے؟",                         
    "لاہور شہر کیوں مشہور ہے؟ مختصر وضاحت کریں۔",
    "سوال: لیاقت علی خان کون تھے؟",
    "کراچی کو روشنیوں کا شہر کیوں کہا جاتا ہے؟",             
    "انگریزی میں ترجمہ کریں: 'محنت کامیابی کی کنجی ہے۔'"
]

print("🚀 Starting Batch Generation...\n")


for user_input in questions:
    print(f"🔹 Question: {user_input}")

    # Manually Format Prompt (Llama-3 Style)
    prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{urdu_system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{user_input}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""

    inputs = tokenizer([prompt], return_tensors = "pt").to("cuda")

    outputs = model.generate(
        **inputs,
        max_new_tokens = 256,
        temperature = 0.1,
        top_p = 0.9,
        repetition_penalty = 1.1,
        do_sample = True,
        eos_token_id = [tokenizer.eos_token_id, tokenizer.convert_tokens_to_ids("<|eot_id|>")]
    )

    response = tokenizer.decode(outputs[0][inputs.input_ids.shape[-1]:], skip_special_tokens=True)
    
    print(f"✅ Answer: {response}")
    print("-" * 50)

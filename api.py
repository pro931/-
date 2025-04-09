# from flask import Flask, request, jsonify
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# # تحميل النموذج المدرب
# model_path = "./fine_tuned_chatbot"
# tokenizer = AutoTokenizer.from_pretrained(model_path)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

# # إعداد Flask
# app = Flask(__name__)

# # دالة الرد
# def generate_response(question):
#     input_text = f"question: {question}"
#     inputs = tokenizer(input_text, return_tensors="pt", max_length=128, truncation=True)
#     outputs = model.generate(
#         inputs.input_ids,
#         attention_mask=inputs.attention_mask,
#         max_length=128,
#         num_beams=5,
#         temperature=0.7,
#         top_k=50,
#         early_stopping=True
#     )
#     return tokenizer.decode(outputs[0], skip_special_tokens=True)

# # نقطة استقبال الرسائل من الواجهة
# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.get_json()
#     question = data.get("message")
#     response = generate_response(question)
#     return jsonify({"response": response})

# if __name__ == "__main__":
#     app.run(debug=True)

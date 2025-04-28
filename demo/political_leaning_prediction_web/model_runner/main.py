import os
from datetime import datetime

from flask import Flask, jsonify, request
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

model_politicalness_pipe = pipeline(
    "zero-shot-classification", model="mlburnham/Political_DEBATE_large_v1.0"
)
tokenizer_leaning = AutoTokenizer.from_pretrained("microsoft/deberta-v3-large")
model_leaning = AutoModelForSequenceClassification.from_pretrained(
    "matous-volf/political-leaning-deberta-large"
)
model_leaning_pipe = pipeline(
    "text-classification",
    tokenizer=tokenizer_leaning,
    model=model_leaning,
    device="cpu",
)


def log_input_text(input_text: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("input_texts.log", "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {input_text}\n")


app = Flask(__name__)


@app.route("/politicalness", methods=["POST"])
def handle_politicalness():
    data = request.json
    input_text = data["text"]

    log_input_text(input_text)

    prediction_politicalness_result = model_politicalness_pipe(
        input_text,
        ["is not", "is"],
        hypothesis_template="This text {} about politics.",
        multi_label=False,
    )
    predicted_class_politicalness = {"is not": "non-political", "is": "political"}[
        prediction_politicalness_result["labels"][0]
    ]

    return jsonify(
        {
            "result": predicted_class_politicalness,
        }
    )


@app.route("/political-leaning", methods=["POST"])
def handle_political_leaning():
    data = request.json
    input_text = data["text"]

    log_input_text(input_text)

    prediction_leaning_result = model_leaning_pipe(input_text)[0]
    match prediction_leaning_result["label"]:
        case "LABEL_0":
            predicted_class_leaning = "left"
        case "LABEL_2":
            predicted_class_leaning = "right"
        case _:
            predicted_class_leaning = "center"

    return jsonify(
        {
            "result": predicted_class_leaning,
            "confidence": round(
                (round(prediction_leaning_result["score"], 2) - 0.33) * 100 / 0.67
            ),
        }
    )


@app.route("/", methods=["GET"])
def root():
    return "", 200


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG"), host="0.0.0.0", port=8001)

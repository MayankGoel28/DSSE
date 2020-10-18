from flask import Flask, request, jsonify
from pprint import pprint
from dialog import DialogFlow
from ml.prediction import get_predictions

app = Flask(__name__)
dflow = DialogFlow()


@app.route("/chat/", methods=["POST"])
def chat():
    req_data = request.get_json()
    input_query = req_data["input"]

    try:
        flow_output = dflow.collect_intent(input_query)
    except Exception as error:
        pprint(error)
        return "Error"
    pprint(flow_output)

    return {
        "message": flow_output.query_result.fulfillment_text,
        "predictions": get_predictions("Hello", "books", "biographies")[1],
    }


if __name__ == "__main__":
    app.run(debug=True)

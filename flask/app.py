from flask import Flask, request, jsonify
from pprint import pprint
from dialog import DialogFlow
from ml.prediction import get_predictions
from ml.cleaned.search_engine import best_file, best_object

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

    scs = []
    for field in flow_output.query_result.parameters.fields:
        if flow_output.query_result.parameters[field] and field != "product":
            scs.append(field)
            scs.append(flow_output.query_result.parameters[field])

    print(scs)

    objs = []
    for s in scs:
        obj = best_object(s, *best_file(s))
        print(obj)
        objs.append(obj)

    return {
        "message": flow_output.query_result.fulfillment_text,
        "predictions": get_predictions(input_query, scs[0], scs[1])[1],
        "objs": objs,
    }


if __name__ == "__main__":
    app.run(debug=True)

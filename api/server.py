from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import json
import random


app = Flask(__name__)
CORS(app, origins="*", supports_credentials=False)


options_data = [
    ['1+1', '2'],
    ['24x2', '48'],
    ['24+2*0', '24']
]

word_data = """1+2={"a": ["1", "2", "3", "4"]}+4=7"""


for i in range(5):
    question_string = str(random.randrange(0, 100)) + random.choice(['+', '-', '*', '/']) + str(random.randrange(0, 100))

    print(question_string)
    print(eval(question_string))

    options_data.append([question_string, str(eval(question_string))])


@app.route('/exam_options', methods=["GET"])
def exam_options():
    # response = jsonify(
    #     left = [
    #         '1+1',
    #         '24x2',
    #         '24+2*0'
    #     ],
    #     right = [
    #         '24',
    #         '2',
    #         '48'
    #     ]
    # )
    left = list(map(lambda row: row[0], options_data))
    right = list(map(lambda row: row[1], options_data))

    random.shuffle(left)
    random.shuffle(right)

    response = jsonify(
        left = left,
        right = right
    )

    response.headers.add("Access-Control-Allow-Origin", '*')

    return response


@app.route('/chk_options', methods=['POST'])
def chk_options():
    answer = request.form.get("answer")

    print("Answer => ")
    print(answer)


    if answer:
        answer_load = json.loads(answer)


        is_all_true = True

        if len(answer_load) == len(options_data):
            for row in answer_load:
                if row not in options_data:
                    is_all_true = False
                    break

        
        if is_all_true:
            return "true"
        
        else:
            return "false"

 


    return "false!"


@app.route('/chk_exam_word', methods=['POST'])
def chk_exam_word():
    answer = request.form.get("a")

    if answer == "3":
        return "true"

    return "false"


@app.route('/update_exam_word', methods=['POST'])
def UpdateExamWord():
    global word_data

    word_data_recv = request.form.get('word_data')


    if word_data_recv:
        word_data = word_data_recv


    return "Success"


@app.route('/exam_word', methods=['POST'])
def ExamWord():
    return word_data





if __name__ == "__main__":
    app.run('0.0.0.0', )
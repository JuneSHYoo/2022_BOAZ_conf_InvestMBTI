from flask import Flask, request, jsonify
import sys
import time
import pickle
from keras.models import load_model

from model import mbti_main

app = Flask(__name__)
answerlist = {}
mbti_results = {}

# load tokenizer and lstm model
with open('models/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
lstm_model = load_model('models/bilstm_model.h5')
        
    
@app.route("/")
def Keyboard():
    dataSend = {
    "Subject":"OSSP",
    "user":"챗봇 떡상이"
    }
    return jsonify(dataSend)


@app.route('/answer1',methods=['POST'])
def ans1():
    req = request.get_json()
    content = req['userRequest']
    content = content['utterance']
    param= req['action']['detailParams']
    answer1 = param['answer1']['value'] 
    answer2 = param['answer2']['value']
    answer3 = param['answer3']['value']
    
    user_id = req['userRequest']['user']['id']
    answerlist[user_id] = []
    
    answerlist[user_id].append(answer1)
    answerlist[user_id].append(answer2)
    answerlist[user_id].append(answer3)
    
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": '{}'.format(answerlist[user_id]) 
                    }
                }
            ]
        }
    }

    return response


@app.route('/answer2',methods=['POST'])
def ans2():
    req = request.get_json()
    content = req['userRequest']
    content = content['utterance']
    param= req['action']['detailParams']
    answer4 = param['answer4']['value'] 
    answer5 = param['answer5']['value']
    
    user_id = req['userRequest']['user']['id']
    
    answerlist[user_id].append(answer4)
    answerlist[user_id].append(answer5)
    
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": '{}'.format(answerlist[user_id]) 
                    }
                }
            ]
        }
    }

    return response


@app.route('/answer3',methods=['POST'])
def ans3():
    req = request.get_json()
    content = req['userRequest']
    content = content['utterance']
    param= req['action']['detailParams']
    answer6 = param['answer6']['value'] 
    answer7 = param['answer7']['value']
    answer8 = param['answer8']['value']
    
    user_id = req['userRequest']['user']['id']
    
    answerlist[user_id].append(answer6)
    answerlist[user_id].append(answer7)
    answerlist[user_id].append(answer8)
    
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": '{}'.format(answerlist[user_id]) 
                    }
                }
            ]
        }
    }

    return response


@app.route('/answer4',methods=['POST'])
def ans4():
    req = request.get_json()
    content = req['userRequest']
    content = content['utterance']
    param= req['action']['detailParams']
    answer9 = param['answer9']['value'] 
    answer10 = param['answer10']['value']
    answer11 = param['answer11']['value']
    answer12 = param['answer12']['value']
    
    user_id = req['userRequest']['user']['id']
    
    answerlist[user_id].append(answer9)
    answerlist[user_id].append(answer10)
    answerlist[user_id].append(answer11)
    answerlist[user_id].append(answer12)
    
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": '{}'.format(answerlist[user_id]) 
                    }
                }
            ]
        }
    }

    return response


@app.route('/answer5',methods=['POST'])
def ans5():
    req = request.get_json()
    content = req['userRequest']
    content = content['utterance']
    param= req['action']['detailParams']
    answer13 = param['answer13']['value'] 
    
    user_id = req['userRequest']['user']['id']
    
    answerlist[user_id].append(answer13)

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": '{}'.format(answerlist[user_id]) 
                    }
                }
            ]
        }
    }

    return response


@app.route('/answer6',methods=['POST'])
def ans6():
    req = request.get_json()
    content = req['userRequest']
    content = content['utterance']
    param= req['action']['detailParams']
    answer14 = param['answer14']['value'] 
    answer15 = param['answer15']['value'] 
    
    user_id = req['userRequest']['user']['id']
    
    answerlist[user_id].append(answer14)
    answerlist[user_id].append(answer15)

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": '{}'.format(answerlist[user_id]) 
                    }
                }
            ]
        }
    }

    return response


@app.route('/answer7',methods=['POST'])
def ans7():
    req = request.get_json()
    content = req['userRequest']
    content = content['utterance']
    param= req['action']['detailParams']
    answer16 = param['answer16']['value'] 
    
    user_id = req['userRequest']['user']['id']
    
    answerlist[user_id].append(answer16)

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": '{}'.format(answerlist[user_id]) 
                    }
                }
            ]
        }
    }

    return response


@app.route('/answer8',methods=['POST'])
def ans8():
    req = request.get_json()
    content = req['userRequest']
    content = content['utterance']
    param= req['action']['detailParams']
    answer17 = param['answer17']['value'] 
    answer18 = param['answer18']['value'] 
    
    user_id = req['userRequest']['user']['id']
    
    answerlist[user_id].append(answer17)
    answerlist[user_id].append(answer18)

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": '{}'.format(answerlist[user_id]) 
                    }
                }
            ]
        }
    }

    return response


@app.route('/answer9',methods=['POST'])
def ans9():
    req = request.get_json()
    content = req['userRequest']
    content = content['utterance']
    param= req['action']['detailParams']
    answer19 = param['answer19']['value'] 
    
    user_id = req['userRequest']['user']['id']
    
    answerlist[user_id].append(answer19)

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": '{}'.format(answerlist[user_id]) 
                    }
                }
            ]
        }
    }

    return response


@app.route('/answer10',methods=['POST'])
def ans10():
    req = request.get_json()
    content = req['userRequest']
    content = content['utterance']
    param= req['action']['detailParams']
    answer20 = param['answer20']['value'] 
    
    user_id = req['userRequest']['user']['id']
    
    answerlist[user_id].append(answer20)

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": '{}'.format(answerlist[user_id]) 
                    }
                }
            ]
        }
    }

    return response


# 마지막 스킬
@app.route('/investmbti',methods=['POST'])
def investmbti():
    req = request.get_json()
    content = req['userRequest']
    content = content['utterance']
    param= req['action']['detailParams']
    answer21 = param['answer21']['value'] 
    
    user_id = req['userRequest']['user']['id']
    
    answerlist[user_id].append(answer21)
    
    
    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": '{}'.format(answerlist[user_id]) 
                    }
                }
            ]
        }
    }
    
    return responseBody


@app.route('/modeling',methods=['POST'])
def modeling():
    req = request.get_json()
    user_id = req['userRequest']['user']['id']
    
    #model.py에 mbti함수 return값을 user_mbti로 받음
    mbti_result = mbti_main(answerlist[user_id], lstm_model, tokenizer)
    mbti_results[user_id] = mbti_result
    
    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {	
                    "simpleText": {
                        "text": '{}'.format(mbti_results[user_id]) 
                    }
                }
            ]
        }
    }
    
    return responseBody

@app.route('/result',methods=['POST'])
def result():
    req = request.get_json()
    user_id = req['userRequest']['user']['id']
    
    user_mbti = mbti_results[user_id]
    
    print(f'[ mbti in result func : {user_mbti} ]')

    if user_mbti == 'ENF':
        response = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleImage": {
                        #"imageUrl": "/workspace/Stalker/ENF.jpg"
                        "imageUrl": "https://proxy.goorm.io/service/62ca6b4904027a2b1ddcb489_dNgHW1lKXPIoslna9pN.run.goorm.io/9080/file/load/ENF.jpg?path=d29ya3NwYWNlJTJGU3RhbGtlciUyRkVORi5qcGc=&docker_id=dNgHW1lKXPIoslna9pN&secure_session_id=VtT1n4zimncyL46cpNrTPgkZEA1yHU3B"
                        }
                    }
                ]
            }
        }
    elif user_mbti == 'ENT':
        response = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleImage": {
                        "imageUrl": "https://proxy.goorm.io/service/62ca6b4904027a2b1ddcb489_dNgHW1lKXPIoslna9pN.run.goorm.io/9080/file/load/ENT.jpg?path=d29ya3NwYWNlJTJGU3RhbGtlciUyRkVOVC5qcGc=&docker_id=dNgHW1lKXPIoslna9pN&secure_session_id=VtT1n4zimncyL46cpNrTPgkZEA1yHU3B"
                        }
                    }
                ]
            }
        }
    elif user_mbti == 'ESF':
        response = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleImage": {
                        "imageUrl": "https://proxy.goorm.io/service/62ca6b4904027a2b1ddcb489_dNgHW1lKXPIoslna9pN.run.goorm.io/9080/file/load/ESF.jpg?path=d29ya3NwYWNlJTJGU3RhbGtlciUyRkVTRi5qcGc=&docker_id=dNgHW1lKXPIoslna9pN&secure_session_id=VtT1n4zimncyL46cpNrTPgkZEA1yHU3B"
                        }
                    }
                ]
            }
        }
    elif user_mbti == 'EST':
        response = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleImage": {
                        "imageUrl": "https://proxy.goorm.io/service/62ca6b4904027a2b1ddcb489_dNgHW1lKXPIoslna9pN.run.goorm.io/9080/file/load/EST.jpg?path=d29ya3NwYWNlJTJGU3RhbGtlciUyRkVTVC5qcGc=&docker_id=dNgHW1lKXPIoslna9pN&secure_session_id=VtT1n4zimncyL46cpNrTPgkZEA1yHU3B"
                        }
                    }
                ]
            }
        }
    elif user_mbti == 'INF':
        response = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleImage": {
                        "imageUrl": "https://proxy.goorm.io/service/62ca6b4904027a2b1ddcb489_dNgHW1lKXPIoslna9pN.run.goorm.io/9080/file/load/INF.jpg?path=d29ya3NwYWNlJTJGU3RhbGtlciUyRklORi5qcGc=&docker_id=dNgHW1lKXPIoslna9pN&secure_session_id=VtT1n4zimncyL46cpNrTPgkZEA1yHU3B"
                        }
                    }
                ]
            }
        }
    elif user_mbti == 'INT':
        response = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleImage": {
                        "imageUrl": "https://proxy.goorm.io/service/62ca6b4904027a2b1ddcb489_dNgHW1lKXPIoslna9pN.run.goorm.io/9080/file/load/INT.jpg?path=d29ya3NwYWNlJTJGU3RhbGtlciUyRklOVC5qcGc=&docker_id=dNgHW1lKXPIoslna9pN&secure_session_id=VtT1n4zimncyL46cpNrTPgkZEA1yHU3B"
                        }
                    }
                ]
            }
        }
    elif user_mbti == 'ISF':
        response = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleImage": {
                        "imageUrl": "https://proxy.goorm.io/service/62ca6b4904027a2b1ddcb489_dNgHW1lKXPIoslna9pN.run.goorm.io/9080/file/load/ISF.jpg?path=d29ya3NwYWNlJTJGU3RhbGtlciUyRklTRi5qcGc=&docker_id=dNgHW1lKXPIoslna9pN&secure_session_id=VtT1n4zimncyL46cpNrTPgkZEA1yHU3B"
                        }
                    }
                ]
            }
        }
    elif user_mbti == 'IST':
        response = {
            "version": "2.0",
            "template": {
            "outputs": [
                  {
                    "simpleImage": {
                        "imageUrl": "https://proxy.goorm.io/service/62ca6b4904027a2b1ddcb489_dNgHW1lKXPIoslna9pN.run.goorm.io/9080/file/load/IST.jpg?path=d29ya3NwYWNlJTJGU3RhbGtlciUyRklTVC5qcGc=&docker_id=dNgHW1lKXPIoslna9pN&secure_session_id=VtT1n4zimncyL46cpNrTPgkZEA1yHU3B"
                        }
                    }
                ]
            }
        }
    
    answerlist.pop(user_id)
    mbti_results.pop(user_id)
        
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded= True)

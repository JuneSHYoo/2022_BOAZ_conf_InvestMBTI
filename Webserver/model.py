import time
import pickle
import numpy as np
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

location_info = {'e' : [0, 1, 2, 3], 
                 'n' : [4, 6, 18, 19],
                 'f' : [7, 8, 11, 17], 
                 'profit' : [10, 12, 16],
                 'focus' : [5, 13, 14], 
                 'period' : [9, 15]}

question_type = {'multiple' : [0, 3, 5, 8, 12, 13, 15, 16, 18, 19],
                 'essay' : [1, 2, 4, 6, 7, 9, 10, 11, 14, 17]}

multiple_dict = {
    1 : ['회식 많은 모임', '상대에게 먼저 말을 건다', '대표주인 테슬라를 산다', '어피치',
         '50프로 확률 5억', '한 종목 몰빵 투자', '가사',
         '여러가지상상한다',
         '6개월 이내', '40프로이상'],
    0 : ['회식 전혀 없는 모임', '말을 걸 때까지 기다린다', '전기차 테마주를 산다', '라이언',
         '100프로 확률 1억', '여러군데 분산 투자', '멜로디', '아무생각안한다',
         '3년이상', '원금10프로이내'],
    0.3 : ['6개월이상~1년이내', '30프로~40프로'],
    0.5 : ['1년이상~2년이내', '20프로~30프로'],
    0.7 : ['10프로~20프로', '2년이상~3년이내']
}


def split(key, ans):
    #key = e, n, f, profit, focus, period
    new = []
    for i in location_info.get(key):
        for idx, label in ans:
            if i == idx:
                new.append(label)
                break     
    return sum(new) / len(new)


def result(ans):
    mbti = ""
    score = 0
    for idx, val in enumerate(ans):
        if idx == 0:
            if val > 0.5: mbti += 'e'
            elif val <= 0.5: mbti += 'i'
            continue
        if idx == 1:
            if val > 0.5: mbti += 'n'
            elif val <=0.5: mbti += 's'
            continue
        if idx == 2:
            if val > 0.5: mbti += 'f'
            elif val <=0.5: mbti += 't'
            continue
        if idx in [3, 4, 5]:
            if val > 0.5: score += 1
            elif val < 0.5: score -= 1
    
    return mbti, score


def mbti_main(answerlist, model, tokenizer):
    
    print(f'input answer : {answerlist} (length : {len(answerlist)})')
    
    using_answer = answerlist[:20]
    start_time = time.time()
    # 주관식, 객관식 분리
    multiple = [(i, using_answer[i]) for i in question_type['multiple']]
    essay = [(i, using_answer[i]) for i in question_type['essay']]

    # 객관식 스코어
    multiple_pred = []
    for tpl in multiple:
        if tpl[1] in multiple_dict.get(1):
            multiple_pred.append((tpl[0], 1))
        elif tpl[1] in multiple_dict.get(0):
            multiple_pred.append((tpl[0], 0))
        elif tpl[1] in multiple_dict.get(0.3):
            multiple_pred.append((tpl[0], 0.3))
        elif tpl[1] in multiple_dict.get(0.5):
            multiple_pred.append((tpl[0], 0.5))
        elif tpl[1] in multiple_dict.get(0.7):
            multiple_pred.append((tpl[0], 0.7))
    
    print('[ multiple problme scroing done. ]')
    
    # 주관식 스코어
    okt = Okt()
    essay_text = [tpl[1] for tpl in essay]
    essay_test = [okt.morphs(ans) for ans in essay_text]

    # text to idx
    essay_ans = tokenizer.texts_to_sequences(essay_test)
    
    print('[ tokenizing done. ]')
    
    # lstm
    trunc_type = 'post'
    padding_type = 'post'
    max_length = 75
    essay_ans_p = pad_sequences(essay_ans, truncating=trunc_type, padding = padding_type, maxlen = max_length)

    pred = model.predict(essay_ans_p)
    pred_label = np.argmax(pred, axis = 1)
    essay_pred = [(essay[idx][0], label) for idx, label in enumerate(pred_label)]
    
    print('[ essay problem scoring done. ]')
    print(f'[ takes {time.time()-start_time:.2f} sec ]')

    final = essay_pred + multiple_pred
    
    ans_mean = []
    for key in list(location_info.keys()):
        ans_mean.append(split(key, final))
            
    mbti_dict = {
        'inf':0, 'int':1, 'isf':2, 'enf':3,
        'ist':4, 'ent':5, 'esf':6, 'est':7
    }    
    
    mbti, score = result(ans_mean)
    final_score = mbti_dict.get(mbti) + score
    if final_score < 0:
        final_mbti = 'inf'
    elif final_score > 7:
        final_mbti = 'est'
    else:
        for idx, mbti in enumerate(mbti_dict):
            if final_score == idx:
                final_mbti = mbti
                break
    
    mbti_result = final_mbti.upper()

    print(f'[ result : {mbti_result} ]')
    
    return mbti_result

# if __name__ == "__main__":
    # answerlist = ['회식 많은 모임', 'not good', 'not good', '상대에게 먼저 말을 건다', 'no', '대표주인 테슬라를 산다', 'are you n?', 'what color?', '어피치', 'ignore', 'are u crazy?', 'fuck off', '50프로 확률 5억', '여러군데 분산 투자', 'd', '1년이상~2년이내', '20프로~30프로', 'd', '멜로디', '여러가지상상한다', '~6개월']
    # start_time = time.time()
    # result = mbti_main(answerlist)
    # print(result, time.time()-start_time)
   
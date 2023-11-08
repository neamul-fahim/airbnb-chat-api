

import json
import re
from transformers import pipeline
import pickle

# RUN JUST ONCE  SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
# nlp = pipeline("question-answering",
#                model="distilbert-base-cased-distilled-squad", revision="626af31")
# # Pickle the model
# with open("qa_model.pkl", "wb") as file:
#     pickle.dump(nlp, file)
# RUN JUST ONCE  EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE


# Unpickle the model
with open("qa_model.pkl", "rb") as file:
    nlp = pickle.load(file)

# Loading the answer corpus SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
ans_corpus = ""
file_path = "ans_corpus.txt"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        ans_corpus = file.read()

except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


def reload_ans_corpus_file():
    global ans_corpus
    file_path = "ans_corpus.txt"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            ans_corpus = file.read()

    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

# ans_corpus = """
# IPSITA COMPUTERS PTE LTD was founded in the year of 1994.
# IPSITA provides services in Software and Web application development for the clients in local and international market and also active in ICT based training, conducted a good number of government training projects.
# IPSITA has More than 25 years of experience in business.
# Address of ipsita is Level 7 25/A Green Road Dhaka-1205 Bangladesh.

# """
# Loading the answer corpus EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE


def get_meaning(question, context):
    # model_checkpoint = "huggingface-course/bert-finetuned-squad"
    # nlp = pipeline("question-answering", model=model_checkpoint)

    result = nlp(question=question, context=context)
    answer = result["answer"]
    score = result["score"]
    print(result)
    return answer, score


def find_ans(question):

    context = ans_corpus

    answer, score = get_meaning(question, context)

    if score >= 0.5:
        j = {"answer": answer,
             "question": question,
             "score": score,
             "found": 1
             }
    else:
        j = {"answer": "I don't have the answer.",
             "question": question,
             "score": score,
             "found": 0
             }
    return j


# while True:
#     ans = find_ans(input("input: "))
#     print(f"score--- {ans['score']}  answer----  {ans['answer']}")

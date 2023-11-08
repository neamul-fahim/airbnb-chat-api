from flask import jsonify, Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)
# app.config["MONGO_URI"] = "mongodb+srv://ipsita:Ipsita%402023@uk-bd0.u3pngqk.mongodb.net/airbnb"
app.config["MONGO_URI"] = "mongodb://localhost:27017/airbnb"
try:
    mongo = PyMongo(app)
    print("____________________connection successfull____________________________")

except Exception as e:
    print(f"error________________{e}")

# gets all the question answer from the database


def get_data():
    try:
        collection = mongo.db.ans_corpus
        # Assuming you have a single document with the "text" key
        document = collection.find_one()
        if document:
            text_data = document.get("text")

            # Save the data to a text file named "ans_corpus.txt" in the current directory
            file_path = "ans_corpus.txt"

            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text_data)

            return {"text": text_data}
        else:
            return None  # No data found
    except Exception as e:
        print(f"Error: {e}")
        return None


# this fuction posts all the ques ans after user sets or alters them
def overwrite_data(new_data):

    try:
        collection = mongo.db.ans_corpus
    except Exception as e:
        print(f"error_______________________{e}")

    # Delete all existing documents in the collection

    try:
        collection.delete_many({})
        collection.insert_one({"text": new_data})

    # Insert the new data into the collection
    except Exception as e:
        print(f"error________________{e}")

    return {'message': 'Collection overwritten with new data'}

import requests

if __name__ == '__main__':
    while True:

        # bangladesh = """The capital city of Bangladesh is Dhaka.The official language of Bangladesh is Bengali (Bangla).The currency used in Bangladesh is the Bangladeshi Taka (BDT).The main industries in Bangladesh include textiles, garments, agriculture, and pharmaceuticals.The population of Bangladesh is approximately 165 million.Some famous tourist attractions in Bangladesh are the Sundarbans, Cox's Bazar, and Srimangal.The traditional dress of Bangladesh is the saree for women and the panjabi with pajama or lungi for men.The national flower of Bangladesh is the Shapla (water lily).A popular dish in Bangladesh is biryani or Kacchi biryani, especially in Dhaka.Bangladesh has a tropical monsoon climate with distinct rainy and dry seasons.The largest river in Bangladesh is the Padma (Ganges).The national anthem of Bangladesh is 'Amar Shonar Bangla'."""

        # data = {"text": bangladesh}

        # api_url = "http://127.0.0.1:5000/ans_corpus_post"
        # response = requests.post(api_url, json=data)

        # api_url = "http://127.0.0.1:5000/ans_corpus_get"  # Replace with the correct URL
        # response = requests.get(api_url)

        text = input("user:")
        if text == '':
            break

        text = {"text": text}
        api_url = "http://127.0.0.1:5000/chat_bot"
        response = requests.post(api_url, json=text)

        print(response.json())

        if response.status_code == 200:
            data = response.json()
            text = data.get("response", "No response")
            print(text)

        else:
            print(f"response-----------{response.status_code}")

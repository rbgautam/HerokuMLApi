#Refrence from the following link
#https://towardsdatascience.com/create-an-api-to-deploy-machine-learning-models-using-flask-and-heroku-67a011800c50
import json
import requests

def test_predict():
    # local url
    # url = 'http://127.0.0.1:5000/predict' # change to your url
    url = 'https://rbgautammlapi.herokuapp.com/predict' # change to your url
    # sample data
    data = {'Pclass': 3
        , 'Age': 2
        , 'SibSp': 1
        , 'Fare': 50}
    data = json.dumps(data)
    send_request = requests.post(url,data)
    print(send_request.json())

if __name__== "__main__":
  test_predict()
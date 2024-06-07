from flask import Flask , render_template , request
import pickle
app = Flask(__name__)
model = pickle.load(open('saved_model.pkl', 'rb'))

@app.route('/')
def home ():
    result = ''
    return render_template('index.html',**locals())
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
        
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        return render_template('index.html', result=result)
    else:
        return render_template('index.html')
if __name__ =='__main__':
    app.run(debug=True)
import numpy as np 
from flask import Flask,render_template,request
import pickle

app=Flask(__name__,template_folder='template')

model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['post'])
def predicted():
    input=[float(x) for x in request.form.values()]
    c_array=[np.array(input)]
    pred=model.predict(c_array)
    
    if pred==1:
        result='You are eligible to get loan'
    else:
        result='You are not eligible to get loan'
        
    output=result
    
    return render_template('index.html',prediction='{}'.format(output))
if __name__ == "__main__":
    app.run(debug=True)
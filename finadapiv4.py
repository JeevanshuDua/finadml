from flask import Flask, request, jsonify
import json
from sklearn.externals import joblib
import pandas as pd
df = pd.read_csv('agents_test.csv')
app = Flask(__name__)

# Load the model
MODEL = joblib.load('finad.pkl')


from flask_restful import Resource , Api

import datetime 

app =Flask(__name__)
api = Api(app)


class operate(Resource):

	def post(self):
		#if request == POST:
	    		a_code = 0
	    		s_code = 0
	    	# Retrieve query parameters related to this request.
	    		area = request.form.get('area')
	    		services = request.form.get('services') 
	    	#to_predict_list = list(to_predict_list) 
	    	#area =to_predict_list[0]
	    		if area == 'West Delhi':
	        		a_code = 3
	    		elif area == 'East Delhi':
	        		a_code = 0
	    		elif area == 'North Delhi':
	       			a_code =  2
	    		elif area == 'South Delhi':
	        		a_code = 4
	    		elif area == 'Central Delhi':
	        		a_code = 1
	    	#services = to_predict_list[1]
	    		if services == 'Insurance':
	        		s_code = 0
	    		elif services == 'Investment':
	       			s_code = 3
	   	
	# Our model expects a list of records
	    		features = [[a_code,s_code]]
	    
	    	# Use the model to predict the class
	    		pred = MODEL.predict(features)
	    		pred = int(pred)
	    		temp = df[df['Agent Number']== pred]
	    		value = temp
	    	#value = value.to_dict('list')
	    	#value = json.dumps(value)
	    	#value = json.loads(value)
	    	#value = value.to_json()
	    		value = value.to_json()
	   
	    	# Create and send a response to the API caller
	    		return jsonify(status='complete', label=value)


api.add_resource(operate , '/')
# api.add_resource(data , '/user_id')


if __name__ == '__main__':
    app.run()

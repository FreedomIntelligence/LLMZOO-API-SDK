#encoding=utf-8
import configparser
import json
import requests
import os

class Model:
	def __init__(self,model_name = "phoenix", ip= "localhost" ):
		config = configparser.ConfigParser()

		current_path,_ = os.path.split(os.path.abspath(__file__))
		# print(os.path.join(current_path,'ip.config'))
		config.read(os.path.join(current_path,'ip.config'))
		
		config.sections()
		if model_name in config["MODELS"]:
			port = config["MODELS"][model_name]
		else:
			raise NameError("we do not have the model {}, model name should be one of : {}. ".format(model_name, ", ".join(config["MODELS"]) ))

		self.url = "{}:{}/api/{}/question".format(ip,port,model_name)
		# print(self.url)


	def response(self, prompt, history = [] ):
		payload = json.dumps({
		  "text": prompt,
		  "history": history
		})

		headers = {
		  'Content-Type': 'application/json'
		}

		response = requests.request("POST", self.url, headers=headers, data=payload)

		result = json.loads(response.text)

		return result["results"]["answer"]


if __name__ == "__main__":
	model = Model("chimera",ip= "http://61.241.103.32")
	# model = Model("phoenix",ip= "http://61.241.103.32")
	prompt = "那该吃什么药?"
	history = [ "肚子疼怎么办",  "保持休息。如果您的腹痛是由于消化问题引起的，那么您需要多休息以减轻症状并促进康复。如果情况严重的话，建议您立即就医。此外，保持良好的睡眠也有助于缓解胃肠不适的症状。"]
	response = model.response(prompt, history= history) 
	
	print(response)

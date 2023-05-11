import configparser
import json
import requests
import os

class Model:
	def __init__(self,model_name = "phoenix" ):
		config = configparser.ConfigParser()

		current_path,_ = os.path.split(os.path.abspath(__file__))
		print(os.path.join(current_path,'../config/ip.config'))
		config.read(os.path.join(current_path,'../config/ip.config'))
		
		config.sections()
		if model_name in config["MODELS"]:
			ip_address = config["MODELS"]["phoenix"]
		else:
			raise NameError("we do not have the model {}, model name should be one of : {}. ".format(model_name, ", ".join(config["MODELS"]) ))

		self.url = "{}api/{}/question".format(ip_address,model_name)
		print(self.url)


	def response(self, prompt, history = [] ):
		payload = json.dumps({
		  "text": prompt,
		  "history": [
		    # [
		    #   "肚子疼怎么办",
		    #   "保持休息。如果您的腹痛是由于消化问题引起的，那么您需要多休息以减轻症状并促进康复。如果情况严重的话，建议您立即就医。此外，保持良好的睡眠也有助于缓解胃肠不适的症状。"
		    # ]
		  ]
		})
		headers = {
		  'Content-Type': 'application/json'
		}

		response = requests.request("POST", self.url, headers=headers, data=payload)

		result = json.loads(response.text)

		return result["results"]["answer"]


if __name__ == "__main__":
	model = Model("phoenix")
	prompt = "那该吃什么药?"
	response = model.response(prompt) 
	print(response)
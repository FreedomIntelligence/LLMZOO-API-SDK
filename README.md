# LLMZOO-API-SDK


### how to install 
```
pip install git+https://github.com/FreedomIntelligence/LLMZOO-API-SDK.git
```
### how to use
```
from llmzoo import Model
model = Model("phoenix", ip ="0.0.0.0")
print(model.response("肚子饿了怎么办？"))
```

you can acess the IP via [here](https://eegb6fzscd.feishu.cn/wiki/QSEqwhsEMiQnZakL88cc8SaCnNd), or ask `wangbenyou@cuhk.edu.cn` for the IP

### if you would like to chat with a given history, you could try 
```
history = [ "肚子疼怎么办",  "保持休息。如果您的腹痛是由于消化问题引起的，那么您需要多休息以减轻症状并促进康复。如果情况严重的话，建议您立即就医。此外，保持良好的睡眠也有助于缓解胃肠不适的症状。"]
print(model.response("肚子饿了怎么办？", history= history))
```

### Other than `phoenix` you could also use the following models
- `huatuo-RAG` 
- `flamingo`
- `Huatuo_bloom`
- `chimera` 
- `phoenix` 


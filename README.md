# AI endpoints with FAST-API exmaple 
- /predict
  - predict the sentiment using the text input argument 
- /translate
  - predice the text from en to fr 
## Example
![image](https://github.com/seonwoo960000/fastapi-ai-example/assets/69591622/880c3748-9bb7-4c79-89cf-d740ea5fb758)

## Considerations 
- Model is loaded entirely to memory
  - Should be careful about memory
- Are models thread safe? Can models handle multiple requests?

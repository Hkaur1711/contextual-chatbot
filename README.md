# contextual-chatbot
A chatbot that intelligently understands the context of the input and makes decisions accordingly. This chatbot can be used to perform various tasks like sending emails, scheduling meetings, creating todos, etc. 

### Intro
![image](https://user-images.githubusercontent.com/63356527/109415583-83277080-79df-11eb-94ed-2e922045d748.png)

### Workflow
We will be working through 3 steps:
1. We’ll transform conversational intent definitions to a Tensorflow model.
2. Next, We’ll build a chatbot framework to process responses.
3. Lastly, We’ll incorporate basic context into our response processor.
We’ll be using tflearn, Tensorflow and Python.

Each conversational intent contains:
* a tag (a unique name)
* patterns (sentence patterns for our neural network text classifier)
* responses (one will be used as a response)

![image](https://user-images.githubusercontent.com/63356527/109415661-fcbf5e80-79df-11eb-86c2-cb2a3fcfcaf7.png)

### Flowchart
![image](https://user-images.githubusercontent.com/63356527/109415535-478ca680-79df-11eb-9b4e-ef49c809c749.png)

from dotenv import dotenv_values

from langchain.chat_models import init_chat_model

userdata = dotenv_values()

llm = init_chat_model(
    model=userdata["MODEL"]
    , base_url = userdata["BASE_URL"]
    , api_key = userdata["CEREBRAS"]
    , temperature = userdata["TEMPERATURE"]
)

risposta = llm.invoke("chi e anders heijsberg e perche è importante? Rispondi brevemente")
print(risposta.content)



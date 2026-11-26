import os
from dotenv import load_dotenv
from gigachat import GigaChat

load_dotenv('../.env')

with GigaChat(
    base_url="https://api.giga.chat/v1",
    credentials=os.getenv('GIGACHAT_CREDENTIALS'),
    scope="GIGACHAT_API_PERS",
    verify_ssl_certs=False,
) as client:
    models = client.get_models()
    for m in models.data:
        print(m.id_)
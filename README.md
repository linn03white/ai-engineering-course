# ai-engineering-course
## Troubleshooting

### 'ascii' codec can't encode characters

**Что видел:** ошибка при запуске со сломанным ключом.
**Почему:** в `GIGACHAT_CREDENTIALS` попали русские буквы, а ключ уходит в HTTP-заголовок, где допустима только латиница.
**Что сделал:** вернул настоящий ключ. Убедился, что благодаря fallback скрипт не упал, а ответил через `[HuggingFace]`.

### ModuleNotFoundError: No module named 'gigachat'

**Что видел:** при запуске `python llm_client.py` — ошибка, что модуль не найден.
**Почему:** виртуальное окружение не было активировано, пакеты стояли в системном Python.
**Что сделал:** активировал `.venv` командой `.venv\Scripts\activate` и установил зависимости заново.
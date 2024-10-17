# Blog API

Это простое REST API для ведения блога, разработанное с использованием Flask.

## Установка и запуск

1. **Клонируйте репозиторий**
2. ```bash
   git clone <ссылка на репозиторий>
   cd blogapi
   ```

3. **Создайте виртуальное окружение и активируйте его**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows используйте venv\Scripts\activate
   ```

4. **Установите зависимости**
   ```bash
   pip install -r requirements.txt
   ```

5. **Запустите приложение**
   ```bash
   python app.py
   ```

   После запуска вы должны увидеть сообщение, что сервер работает на `http://127.0.0.1:5000/`.

   
## Тестирование API

### 1. Использование Postman
- Установите [Postman](https://www.postman.com/downloads/).
- Создайте новый запрос.
- Выберите метод (POST, GET, PUT или DELETE) и введите соответствующий URL (например, `http://127.0.0.1:5000/posts`).
- Для создания и обновления постов добавьте тело запроса в формате JSON в разделе `Body`.
- Нажмите "Send" и посмотрите на ответ.


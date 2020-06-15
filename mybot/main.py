from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime

token = "1329a396bd8cf4751a5a20daa0127182688e78b69efa01273bfa12a3df3e8de1c607a8c07e1b2ffbe706c"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
#While True здесь оказался не нужен. Его функцию выполняет for event in longpoll.listen(): Спасибо подписчику за это уточнение.

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))

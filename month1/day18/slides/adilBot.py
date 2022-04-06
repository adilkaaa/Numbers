"""
Создать телеграм бот который читает данные из файла 'kloop.json'
И отправляет их к пользователю

Скинуть мне ссылку на телеграм бота для теста
"""

from aiogram import Bot, executor, types,Dispatcher
from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint


TOKEN = '5262459262:AAEkjlprM1owmen6tNeH9_HNrhAeJZOHYSM'

JSON = 'kloop.json'
URL = 'https://kloop.kg/news/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0'  #Замените на свой Юзер агент
}

def get_content():
    r = requests.get(URL, headers=HEADERS, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    items = soup.find_all('article', class_='elementor-post')

    new_posts = []

    for item in items:
        #image link
        image = str(item.find('img'))
        images = image.split()
        image_src = images[6]
        need_image = image_src[5:len(image_src)-1]
        #title link
        a_href = str(item.find('a'))
        links = a_href.split()[2]
        need_link = links[6:len(links)-2]

        new_posts.append({
            "title" : item.find('h3',class_='elementor-post__title').get_text(strip=True), # спарсите заголовок
            "data" : item.find('span',class_='elementor-post-date').get_text(strip=True), # спарсите дату публикации
            'photo' : need_image, # спарсите ссылку на фото
            'link' : need_link # спарсите ссылку на новость
        })
    with open('kloop.json', 'w') as file:
        json.dump(new_posts, file ,indent=4, ensure_ascii=False)
get_content()
bot = Bot(token= TOKEN)
dp = Dispatcher(bot)
count = 0
@dp.message_handler(commands = 'start')
async def start(message: types.Message):
    await message.reply("""Hi, I am newsBot.\n
    you could get information about KG news.\n
    type /help for more information""")

@dp.message_handler(commands = 'help')
async def help(message: types.Message):
    await message.reply("""
    /help - shows all commands\n
    /getnews - shows you news""")

@dp.message_handler(commands = ['getnews'])
async def echo(message: types.Message):
    await getnews(message)

async def getnews(message: types.Message):
    global count
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    next_button = types.InlineKeyboardButton(text = 'next',callback_data='next')
    previous_button = types.InlineKeyboardButton(text = 'previous',callback_data='previous')
    with open('kloop.json','r') as f:
        news = json.load(f)
    if count>0 and count<len(news):
        keyboard.add(previous_button,next_button)
    elif count<len(news):
        keyboard.add(next_button)
    else:
        keyboard.add(previous_button)    

    all_news = [f"""{news[i]['photo']}\n
    {news[i]['data']}\n
    {news[i]['title']}\n
    {news[i]['link']}""" for i in range(len(news))]


    await bot.send_message(message.from_user.id,all_news[count], reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data)
async def answer_query(callback_query: types.CallbackQuery):
    global count
    code = callback_query.data
    if code == 'previous':
        count-=1
        await getnews(callback_query)
    if code == 'next':
        count+=1
        await getnews(callback_query)



if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)

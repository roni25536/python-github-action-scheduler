import telegram
import requests

def job():
    TELEGRAM_BOT_TOKEN = '775005668:AAFLsiwi4ul8aBO3swzMkDmpkJmjjlT_3EA'
    TELEGRAM_CHAT_ID = '@virtual_shipping'
    webUrl = 'https://www.zipy.co.il/p/%D7%90%D7%9C%D7%99%D7%90%D7%A7%D7%A1%D7%A4%D7%A8%D7%A1/'
    userName = "/#roni25536"
    limit = 1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
    res = requests.get('https://www.zipy.co.il/api/product/getPromoProducts',headers=headers ,
                       params={'shopIds': ["aliexpress"], 'limit': limit})
    print(res.text)  
    res = res.json().get('result')
    products = list(map(lambda p: {**p, 'url': webUrl + ('-'.join(p.get('name').lower().split(' '))) + '/' + p.get(
        'id') + userName}, res))
    messages = list(map(lambda p: {'image': p.get('image'),
                                   'msg': "\n\n\nשם:    " +
                                          p.get('name') +
                                          "\n\nמחיר:    " +
                                          str(p.get('price').get('value')) + p.get('price').get('icon') +
                                          "\n\nבמקום:   " +
                                          str(p.get('notDiscountedPrice').get('value')) + p.get(
                                       'notDiscountedPrice').get('icon') +
                                          "\n\nהנחה:   " +
                                          str(p.get('discount')) + "%" +
                                          "\n\nדירוג:    " +
                                          str(p.get('reviewsAverage')) +
                                          "\n\nתגובות:    " +
                                          str(p.get('reviewsTotal')) +
                                          "\n\nקישור:    " +
                                          p.get('url')}, products))
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    for p in messages:
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=p.get('image'), caption=p.get('msg'))
    print('done')

job()

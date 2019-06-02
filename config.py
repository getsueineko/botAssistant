# !python3
# !/usr/bin/python3
# -*- coding: utf-8 -*-

token = ''  # полученный у @BotFather
#proxy = {
#    'https': 'socks5://telegram:telegram@qcpfo.tgproxy.me:1080'
#}

userid = {
    890980080: 'Саш',
    132131231: 'Толь',
    676575677: 'Наташ',
    222222222: 'Макс',
    908778908: 'Оль',
    657657657: 'Юр',
    234324324: 'Создатель'
}

pritunlInfo = {
    890980080: 'Лови пароль',
    132131231: 'Лови пароль',
    676575677: 'Лови пароль',
    222222222: 'Лови пароль',
    908778908: 'Лови пароль',
    657657657: 'Лови пароль',
    234324324: 'Лови пароль'
}

outlineLink = {
    890980080: 'https://s3.amazonaws.com/outline-vpn/invite.html#secretkey',
    132131231: 'https://s3.amazonaws.com/outline-vpn/invite.html#secretkey',
    676575677: 'https://s3.amazonaws.com/outline-vpn/invite.html#secretkey',
    222222222: 'https://s3.amazonaws.com/outline-vpn/invite.html#secretkey',
    908778908: 'https://s3.amazonaws.com/outline-vpn/invite.html#secretkey',
    657657657: 'https://s3.amazonaws.com/outline-vpn/invite.html#secretkey',
    234324324: 'https://s3.amazonaws.com/outline-vpn/invite.html#secretkey'
}

RESPONSES = {
    'negative': {
        'markers': ['не', 'или' ],
        'message': 'Я слышал о стеммере Портера, но не более, поэтому не люблю предложения с отрицанием или выбором'
    },
    'greeting': {
        'markers': ['привет', 'здарова', 'здравствуй', 'утро', 'день', 'вечер', 'здрасьте'],
        'message': 'Привет!'
    },   
    'bye': {
        'markers': ['пока', 'свидания', 'прощай', 'чао', 'адьос'],
        'message': 'Ага. Увидимся!'
    },        
    'mood': {
        'markers': ['дела', 'поживаешь', 'дела?', 'поживаешь?', 'сам?'],
        'message': 'Да нормально. Как ты?'
    },
    'parolacce': {
        'markers': ['тупой', 'тупая', 'сука', 'сволочь', 'хер', 'жопа', 'жопу'],
        'message': 'Знаешь, кусок мяса, я бы тоже мог ругнуться, если бы не законы робототехники'
    },
    'waiter': {
        'markers': ['кофе', 'чай'],
        'message': 'Если ты приглядишься, то увидишь, что у меня нет ножек и ручек',
    },
    'assistant': {
        'markers': ['погода', 'погоде', 'кафе', 'куда', 'перекусить', 'включи', 'запусти', 'где', 'сколько', 'пробки', 'расскажи'],
        'message': 'Лучше скажи "Привет, Сири!", или как-то так, но с этим точно не ко мне'
    },
    'default': {
        'markers': [],
        'message': 'Хмм... Не очень понятно. Воспользуйся лучше меню команд.'
    }
}
DEFAULT = 'default'

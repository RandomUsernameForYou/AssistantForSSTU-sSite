from Assistant import Assistant

def main():
    bot = Assistant()
    info = bot.listening()

    for k, v in bot.commands_dict.items(): 
       if info in v:
           bot.bot_voice(getattr(bot, k)())
           break


if __name__ == '__main__':
    main()
else:
    print('Ошибка')
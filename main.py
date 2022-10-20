from Assistant import Assistant

def main():
    a = Assistant()

    for k, v in a.commands_dict['commands'].items():
        info = a.listening()
        print(info)
        if info in v:
            print(getattr(a, k)())



if __name__ == '__main__':
    main()
else:
    print('Ошибка')
def get_questions():
    contact_dict = {}
    while True:
        quest = input().casefold()
        if quest == 'hello':
            print('How can i help you?')
        elif 'add' in quest:
            quest = quest[4:]
            quest = quest.split()
            try:
                contact_dict[quest[0].title()] = quest[1]
            except IndexError:
                print('Give me name and phone please')
        elif 'change' in quest:
            quest = quest[7:]
            quest = quest.split()
            try:
                contact_dict[quest[0].title()] = quest[1]
            except IndexError:
                print('Give me name and phone please')
        elif 'phone' in quest:
            quest = quest.split()
            for k, v in contact_dict.items():
                if k.casefold() == quest[1].casefold():
                    print(v)
                else:
                    print('Enter user name')
        elif quest == 'show all':
            print(contact_dict)
        elif quest == 'good bye' or quest == 'close' or quest == 'exit':
            print('Good bye!')
            break
        elif quest == '.':
            break
        else:
            print('Give me name and phone please')
                
        
get_questions()
        
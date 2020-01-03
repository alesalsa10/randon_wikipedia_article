import wikipedia,sys



while True:
    print('Type exit to stop the program')
    random = wikipedia.random(pages=1)
    page_content = wikipedia.page(random).content

    print(f'Title: {random}')
    answer = input('Are you interested in reading this article ').title()
    if answer == 'Yes':
        print(page_content)
        answer2 = input('Do you want to to read another one? ').title()
        if answer2 == 'Yes':
            continue
        else:
            sys.exit()
    elif answer == 'No':
        continue
    elif answer == 'Exit':
        sys.exit()
    else:
        print('Check your spelling')
        continue






translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

def translate(d, word):
    for x, y in d.items():
        if word in x:
            print(d[f'{x}'])
            return
        elif word in y:
            print(x)
            return
    print('Content not in dictionary')

translate(translations, 'computer')
translate(translations, 'klawiatura')
translate(translations, 'apple')
    
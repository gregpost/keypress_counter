import keyboard

keys: str = ' qwertyuiop[]asdfghjkl;\'\zxcvbnm,./{}:"|<>?|\\1234567890-=!@#$%^&*()_+\s\t\n\e\r\b\a\R\B\f\v\cA\cZ\ca\cz\0йцукенгшщзхъфывапролджэячсмитьбюQWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
pressed_keys: str = ''
print('Press "~" to stop counting pressed keys')
while True:
    for key in keys:
        try:
            if keyboard.is_pressed(key):
                pressed_keys += key
                break
        except:
            break
    if keyboard.is_pressed('~'):
        pressed_keys_without_duplicates = ''
        prev_key: str = ''
        for key in pressed_keys:
            if key != prev_key:
                pressed_keys_without_duplicates += key
            prev_key = key
        pressed_keys_count: int = len(pressed_keys_without_duplicates)
        print('\nPressed keys count: ' + str(pressed_keys_count))
        print('Pressed keys:\n' + pressed_keys_without_duplicates)
        break


import math
import re

def getInput(inputType, colour=None):
    class Error(Exception):
        pass

    class ValueTooLongError(Error):
        pass

    class ValueTooShortError(Error):
        pass

    class ValueOutOfRangeAlphaError(Error):
        pass

    class ValueTooLargeError(Error):
        pass

    class ValueNegativeError(Error):
        pass

    if inputType == "hex":
        while True:
            try:
                hex_input = input('Enter the Hex value: #')
                if len(hex_input) > 6:
                    raise ValueTooLongError
                elif len(hex_input) < 6:
                    raise ValueTooShortError
                elif not re.match("^[a-f0-9]*$", hex_input):
                    raise ValueOutOfRangeAlphaError
                break

            except ValueTooLongError:
                print('Input must not be longer than 6 characters, try again.\n')
            except ValueTooShortError:
                print('Input must not be shorter than 6 characters, try again.\n')
            except ValueOutOfRangeAlphaError:
                print('Input must only contain letters from "a" to "f", try again.\n')
        return hex_input

    elif inputType == "rgb":
        while True:
            try:
                i = int(input(f"Enter the {colour} value: "))
                if i < 0:
                    raise ValueNegativeError
                elif i > 255:
                    raise ValueTooLargeError
                break
            except ValueNegativeError:
                print('Input must be not be a negative number, try again.\n')
            except ValueTooLargeError:
                print('Input must not be greater than 255, try again.\n')
            except ValueError:
                print('Input must be a valid integer, try again.\n')
        return i

    elif inputType == "cmyk":
        while True:
            try:
                i = int(input(f'{colour} colour ({colour[0]}): '))
                if i < 0:
                    raise ValueNegativeError
                elif i > 100:
                    raise ValueTooLargeError
                break

            except ValueNegativeError:
                print('Input cannot be negative, try again.')
            except ValueTooLargeError:
                print('Input cannot exceed 100%, try again.')
            except ValueError:
                print('Input must be a valid integer, try again.')
        return i

    elif inputType == "xyz":
        while True:
            try:
                i = float(input(f"Enter the {colour} value: "))
                if i < 0:
                    raise ValueNegativeError
                elif i > 1:
                    raise ValueTooLargeError 
                break
            except ValueNegativeError:
                print('Input must be not be a negative number, try again.\n')
            except ValueTooLargeError:
                print('Input must not be greater than 1, try again.\n')
            except ValueError:
                print('Input must be a float value, try again.\n')
        return i


def hex_to_rgb_function():
    print('\nYou have selected Hex to RGB.')
    hex_to_rgb = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 12, 'b': 11,
                  'c': 12, 'd': 13, 'e': 14, 'f': 15}

    hex_input = getInput("hex")
    hex_list = list(hex_input)

    raw_hex1, raw_hex2, raw_hex3, raw_hex4, raw_hex5, raw_hex6 = hex_list

    hex1 = hex_to_rgb[raw_hex1]
    hex2 = hex_to_rgb[raw_hex2]
    hex3 = hex_to_rgb[raw_hex3]
    hex4 = hex_to_rgb[raw_hex4]
    hex5 = hex_to_rgb[raw_hex5]
    hex6 = hex_to_rgb[raw_hex6]

    r = (hex1 * 16) + hex2
    g = (hex3 * 16) + hex4
    b = (hex5 * 16) + hex6

    print(f'#{hex_input} converted to RGB is ({r}, {g}, {b}).\n\n')


def rgb_to_hex_function():
    print('\nYou have selected RGB to Hex.')
    rgb_to_hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b',
                  12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    
    r = getInput("rgb", "red")
    g = getInput("rgb", "green")
    b = getInput("rgb", "blue")

    hex1 = int(math.floor(r / 16))
    hex2 = int(((r / 16) - hex1) * 16)
    hex3 = int(math.floor(g / 16))
    hex4 = int(((g / 16) - hex3) * 16)
    hex5 = int(math.floor(b / 16))
    hex6 = int(((b / 16) - hex5) * 16)

    print(f'\n({r}, {g}, {b}) converted to Hex Colour Code is #{rgb_to_hex[hex1]}{rgb_to_hex[hex2]}'
          f'{rgb_to_hex[hex3]}{rgb_to_hex[hex4]}{rgb_to_hex[hex5]}{rgb_to_hex[hex6]}\n\n')


def cmyk_to_rgb_function():
    print('You have selected CMYK to RGB.\nPlease enter the CMYK values as a percentage.\n')

    c = getInput("cmyk", "Cyan")
    m = getInput("cmyk", "Magenta")
    y = getInput("cmyk", "Yellow")
    b = getInput("cmyk", "Black")

    r = round(255 * (1 - (c / 100)) * (1 - (b / 100)))
    g = round(255 * (1 - (m / 100)) * (1 - (b / 100)))
    b = round(255 * (1 - (y / 100)) * (1 - (b / 100)))

    print(f'({c},{m},{y},{b}) converted to RGB is ({r}, {g}, {b}).\n\n')


def rgb_to_cmyk_function():
    print('You have selected RGB to CMYK.\nPlease enter the RGB values.\n')

    r = getInput("rgb", "red")
    g = getInput("rgb", "green")
    b = getInput("rgb", "blue")

    c = 1 - (r / 255)
    m = 1 - (g / 255)
    y = 1 - (b / 255)
    k = 1

    if c < k:
        k = c
    if m < k:
        k = m
    if y < k:
        k = y
    if k == 1:
        c = 0
        m = 0
        y = 0

    else:
        c = round((c - k) / (1 - k) * 100)
        m = round((m - k) / (1 - k) * 100)
        y = round((y - k) / (1 - k) * 100)
        k = round(k * 100)

    print(f'({r}, {g}, {b}) converted to CMYK is {c}%, {m}%, {y}%, {k}%.\n\n')


def xyz_to_rgb_function():
    print('You have selected XYZ to RGB.\nPlease enter the XYZ values.\n')

    x = getInput("xyz", "X")
    y = getInput("xyz", "Y")
    z = getInput("xyz", "Z")

    r = x * 3.2406 + y * -1.5372 + z * - 0.4986
    g = x * -0.9689 + y * 1.8758 + z * 0.0415
    b = x * 0.0557 + y * -0.2040 + z * 1.0570

    if r > 0.0031308:
        r = 1.055 * (r ** (1 / 2.4)) - 0.055
    else:
        r = 12.92 * r
    if g > 0.0031308:
        g = 1.055 * (g ** (1 / 2.4)) - 0.055
    else:
        g = 12.92 * g
    if b > 0.0031308:
        b = 1.055 * (b ** (1 / 2.4)) - 0.055
    else:
        b = 12.92 * b

    red = round(r * 255)
    green = round(g * 255)
    blue = round(b * 255)

    print(f'{x}, {y}, {z} converted to RGB is ({red}, {green}, {blue})\n\n')


def main():
    while True:
        print('(1) RGB to Hex\n(2) Hex to RGB\n(3) CMYK to RGB\n(4) RGB to CMYK\n(5) XYZ to RGB')

        while True:
            try:
                choice = input('Enter your choice: ')
                break
            except:
                print('Please enter a valid input.\n')

        if choice == '1':
            rgb_to_hex_function()
        elif choice == '2':
            hex_to_rgb_function()
        elif choice == '3':
            cmyk_to_rgb_function()
        elif choice == '4':
            rgb_to_cmyk_function()
        elif choice == '5':
            xyz_to_rgb_function()
        else:
            print('Please enter a valid input.\n')


if __name__ == '__main__':
    main()

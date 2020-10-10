def field_string_to_field_array(field_string):
    field_array = [[field_string[0], field_string[1], field_string[2]],
                   [field_string[3], field_string[4], field_string[5]],
                   [field_string[6], field_string[7], field_string[8]]]
    return field_array


def print_field(field_string):
    print('---------')
    print('|', field_string[0], field_string[1], field_string[2], '|')
    print('|', field_string[3], field_string[4], field_string[5], '|')
    print('|', field_string[6], field_string[7], field_string[8], '|')
    print('---------')


def check_win(field_string, symbol):
    if (field_string[0] == field_string[1] == field_string[2] == symbol or
            field_string[0] == field_string[3] == field_string[6] == symbol or
            field_string[0] == field_string[4] == field_string[8] == symbol):
        return True
    elif field_string[1] == field_string[4] == field_string[7] == symbol:
        return True
    elif (field_string[2] == field_string[5] == field_string[8] == symbol or
          field_string[2] == field_string[4] == field_string[6] == symbol):
        return True
    elif field_string[3] == field_string[4] == field_string[5] == symbol:
        return True
    elif field_string[6] == field_string[7] == field_string[8] == symbol:
        return True


def check_field_state(field_string):
    if abs(field_string.count('X') - field_string.count('O')) >= 2:
        print('Impossible')
    elif check_win(field_string, 'O') and check_win(field_string, 'X'):
        print('Impossible')
    elif check_win(field_string, 'X'):
        print_field(user_list)
        print('X wins')
    elif check_win(field_string, 'O'):
        print_field(user_list)
        print('O wins')
    elif field_string.count('_') == 0:
        print_field(user_list)
        print('Draw')
        return 'Draw'
    else:
        return 'Game not finished'


def player_move(symbol):
    while True:
        print('Enter the coordinates:')
        coordinates = ''.join(input().split())
        if coordinates.isdigit():
            coordinates = int(coordinates)
            if coordinates in COORD_LIST:
                if user_list[COORD_LIST.index(coordinates)] == '_':
                    user_list[COORD_LIST.index(coordinates)] = symbol
                    break
                else:
                    print('This cell is occupied! Choose another one!')
            else:
                print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')


COORD_LIST = [13, 23, 33, 12, 22, 32, 11, 21, 31]
user_string = '_________'
user_list = [x for x in user_string]

while check_field_state(user_list) in ['Game not finished', 'Draw']:
    print_field(user_list)
    player_move('X')
    if check_field_state(user_list) != 'Game not finished':
        break
    print_field(user_list)
    player_move('O')

# check_field_state(user_string)

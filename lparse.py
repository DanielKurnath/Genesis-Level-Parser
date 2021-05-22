import json


map_file = input('Enter Map File Name: ')
output_file = input('Enter Output File: ')
# TODO: check for .c file extension and add one if not specified
level_number = input('Level Number: ')
output_header = output_file + '.h'
# TODO: strip the .c extension and then add the .h extension

with open(map_file, "r") as map_file:
    map_data = json.load(map_file)

    print(map_data)

    map_height = map_data['layers'][0]['height']
    map_width = map_data['layers'][0]['width']

    try:
        test_output_exists = open(output_file)
    except FileNotFoundError:
        test_output_exists = open(output_file, 'a')
    test_output_exists.close()

    with open(output_file, mode='w') as output_file:
        output_file.write('#include <genesis.h>\n\n')

        headers = 'u8 level' + level_number + '[' + str(map_height) + '][' + str(map_width) + '] = {\n'
        output_file.write(headers)
        for row in range(0, map_height):
            output_file.write('{')
            for column in range(0, map_width):
                map_tile = (map_data['layers'][0]['data'][(row * map_width) + column]) - 1
                if map_tile > 255:
                    map_tile = map_tile & ~(0x80000000 | 0x40000000 | 0x20000000)
                if column != map_width - 1:
                    output_file.write(str(map_tile) + ',')
                elif column == map_width - 1:
                    if row != map_height - 1:
                        output_file.write(str(map_tile) + '},\n')
                    elif row == map_height - 1:
                        output_file.write(str(map_tile) + '}\n};\n\n')

        headers = 'u8 collision' + level_number + '[' + str(map_height) + '][' + str(map_width) + '] = {\n'
        output_file.write(headers)
        for row in range(0, map_height):
            output_file.write('{')
            for column in range(0, map_width):
                collision_tile = (map_data['layers'][1]['data'][(row * map_width) + column]) - 1
                if column != map_width - 1:
                    output_file.write(str(collision_tile) + ',')
                elif column == map_width - 1:
                    if row != map_height - 1:
                        output_file.write(str(collision_tile) + '},\n')
                    elif row == map_height - 1:
                        output_file.write(str(collision_tile) + '}\n};\n\n')

        headers = 'u8 rotation' + level_number + '[' + str(map_height) + '][' + str(map_width) + '] = {\n'
        output_file.write(headers)
        for row in range(0, map_height):
            output_file.write('{')
            for column in range(0, map_width):
                rotation_tile = (map_data['layers'][0]['data'][(row * map_width) + column]) - 1
                if rotation_tile > 255:
                    horizontalFlip = rotation_tile & 0x80000000
                    verticalFlip = rotation_tile & 0x40000000
                    diagonalFlip = rotation_tile & 0x20000000
                elif rotation_tile <= 255:
                    horizontalFlip = 0
                    verticalFlip = 0
                    diagonalFlip = 0
                if horizontalFlip != 0 | verticalFlip != 0 | diagonalFlip != 0:
                    print(f'rotationTile: {rotation_tile} horizontalFlip: {horizontalFlip} '
                      f'verticalFlip: {verticalFlip} diagonalFlip: {diagonalFlip}')
                rotation_tile = 0
                if horizontalFlip != 0:
                    rotation_tile += 1
                if verticalFlip != 0:
                    rotation_tile += 2
                if column != map_width - 1:
                    output_file.write(str(rotation_tile) + ',')
                elif column == map_width - 1:
                    if row != map_height - 1:
                        output_file.write(str(rotation_tile) + '},\n')
                    elif row == map_height - 1:
                        output_file.write(str(rotation_tile) + '}\n};\n\n')

    with open(output_header, mode='w') as output_header_file:
        output_header_file.write('#ifndef _LEVEL' + level_number + '_H_\n')
        output_header_file.write('#define _LEVEL' + level_number + '_H_\n')
        output_header_file.write('#define LEVEL_' + level_number + '_MAP_HEIGHT ' + str(map_height) + '\n')
        output_header_file.write('#define LEVEL_' + level_number + '_MAP_WIDTH ' + str(map_width) + '\n')
        output_header_file.write('#include <genesis.h>\n')
        output_header_file.write('extern u8 level' + level_number + '[LEVEL_' + level_number + '_MAP_HEIGHT]'
                                                                    '[LEVEL_' + level_number + '_MAP_WIDTH];\n')
        output_header_file.write('extern u8 collision' + level_number + '[LEVEL_' + level_number + '_MAP_HEIGHT]'
                                                                        '[LEVEL_' + level_number + '_MAP_WIDTH];\n')
        output_header_file.write('extern u8 rotation' + level_number + '[LEVEL_' + level_number + '_MAP_HEIGHT]'
                                                                       '[LEVEL_' + level_number + '_MAP_WIDTH];\n')
        output_header_file.write('#endif')

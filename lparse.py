import csv

map_file = input('Enter Map File Name: ')
collision_file = input('Enter Collision File Name: ')
map_width = input('Enter Map Width: ')
map_height = input('Enter Map height: ')
output_file = input('Enter Output File: ')
level_number = input('Level Number: ')

output_header = output_file + '.h'

with open(map_file) as map_file:
    with open(collision_file) as collision_file:

        list_map_file = list(map_file)
        list_collision_file = list(collision_file)
        print(list_map_file)
        print(list_collision_file)

        try:
            test_output_exists = open(output_file)
        except FileNotFoundError:
            test_output_exists = open(output_file, 'a')
        test_output_exists.close()

        with open(output_file, mode='w') as output_file:
            output_file.write('#include <genesis.h>')
            headers = 'u8 level' + level_number + '[' + map_height + '][' + map_width + '] = {\n'
            output_file.write(headers)
            line_count = 0
            for line in list_map_file:
                line_count += 1
                if line_count != int(map_height):
                    output_file.write('{' + line.rstrip() + '},\n')
                else:
                    output_file.write('{' + line.rstrip() + '}\n')
            output_file.write('};\n\n')

            headers = 'u8 collision' + level_number + '[' + map_height + '][' + map_width + '] = {\n'
            output_file.write(headers)
            line_count = 0
            for line in list_collision_file:
                line_count += 1
                if line_count != int(map_height):
                    output_file.write('{' + line.rstrip() + '},\n')
                else:
                    output_file.write('{' + line.rstrip() + '}\n')
            output_file.write('};\n\n')
            output_file.write('int level_' + level_number + '_map_height = ' + map_height + ';\n')
            output_file.write('int level_' + level_number + '_map_width = ' + map_width + ';\n')
        with open(output_header, mode='w') as output_header_file:
            output_header_file.write('#ifndef _LEVEL' + level_number + '_H_\n')
            output_header_file.write('#define _LEVEL' + level_number + '_H_\n')
            output_header_file.write('extern u8 level' + level_number + '[];\n')
            output_header_file.write('extern u8 collision' + level_number + '[];\n')
            output_header_file.write('extern int level_' + level_number + '_map_height;\n')
            output_header_file.write('extern int level_' + level_number + '_map_width;\n')
            output_header_file.write('#endif')

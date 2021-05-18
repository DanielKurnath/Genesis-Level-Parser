import csv

# map_file = input('Enter Map File Name: ')
# collision_file = input('Enter Collision File Name: ')
# map_width = input('Enter Map Width: ')
# map_height = input('Enter Map height: ')
# output_file = input('Enter Output File: ')
# level_number = input('Level Number: ')

map_file = "G:\\Google Drive\\Genesis Dev\\Code\\2021-05-16 - Battle Engine Demo Attempt" \
           " 2 (Incomplete)\\res\\Test Level_world.csv"
collision_file = "G:\\Google Drive\\Genesis Dev\\Code\\2021-05-16 - " \
                 "Battle Engine Demo Attempt 2 (Incomplete)\\res\\Test Level_collision.csv"
map_width = '40'
map_height = '28'
output_file = "G:\\Google Drive\\Genesis Dev\\Code\\2021-05-16 - Battle Engine Demo Attempt " \
              "2 (Incomplete)\\res\\Test.World.c"
level_number = '1'

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
            output_file.write('};\n')

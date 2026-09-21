def rgb_to_hex(value):
    hex_list = []
    hex_letter = ['a', 'b', 'c', 'd', 'e', 'f']

    str_rgb = value[4:-1]
    rgb = str_rgb.split(',')

    for x in range(0, 3):
        y = int(int(rgb[x]) / 16)
        z = int(rgb[x]) % 16

        if y > 9:
            y = hex_letter[y - 10]
        if z > 9:
            z = hex_letter[z - 10]

        hex_list.append(str(y))
        hex_list.append(str(z))

    hex_color = ''.join(hex_list)

    return f'#{hex_color}'

print(rgb_to_hex('rgb(72, 134, 208)'))

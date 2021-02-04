import os
import sys
import plistlib
palette = ['Red', 'Green', 'Blue']

def cloz(s):
    print(s)
    sys.exit(1)

for file in sys.argv[1:]:
    print("File: %s" % file)
    with open(file, 'rb') as f:
        obj = plistlib.load(f)
        buf = ''
        for i in range(16):
            key = "Ansi %d Color" % i
            if key not in obj:
                cloz("Missing key: %s\n check file" % key)
            color_dict = obj[key]
            hex_color = "#"
            for color in palette:
                color_key = "%s Component" % color
                if color_key not in color_dict:
                    cloz("Missing key: %s\n Check the file" % color_key)
                color_hex = hex(int(round(color_dict[color_key] * 255))).split('x')[1]

                if len(color_hex) < 2:
                    color_hex = '0' + color_hex
                hex_color += color_hex.lower()
            buf += "color%d %s\n" % (i, hex_color)
        output_file_name = os.path.basename(file).replace(' ', '_') + '.conf'
        with open(output_file_name, 'w') as outfile:
            outfile.write(buf)
        print("The outfile is: %s" % output_file_name)
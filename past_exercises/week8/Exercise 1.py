

def order_music_file(in_origin_file, in_origin_list):
    with open(in_origin_file) as file:
            for song in file.readlines():
                in_origin_list.append(song)
    in_origin_list.sort()
    return in_origin_list

def write_ordered_music_file(in_ordered_list):
    with open("new_music.txt",'a') as file2:
        for song2 in in_ordered_list:
            file2.write(song2)


def main():
    ordered_list = []
    origin_file="music.txt"
    write_ordered_music_file(order_music_file(origin_file,ordered_list))


main()
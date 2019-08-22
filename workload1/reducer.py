#!/usr/bin/python3
import sys

def read(file):
    """ read the source file, and return iterator for list
    Input format: key \t value pair from file(stdin)
    Output format: data with format as (key,value)

    """
    for line in file:
        yield line.strip().split("\t", 1)

def video_reducer():
    """return the average country number for each video category
    Input format: key \t value
    Output format: key \t value with data category as key, average country number as value

    """
    country_times = 0 #count the total times for each category
    current_key = None 
    video_id_set = set() #store the video_id for each category
    TIMES = 1
    for key,value in read(sys.stdin):
        key_list = key.split(',')
        if current_key == key_list:
            continue
        elif current_key != None and current_key[0] == key_list[0]:
            video_id_set.add(key_list[1])
            country_times += TIMES
        else:
            if current_key:
                avg_country_num = country_times/len(video_id_set)
                print("{}:\t{}".format(current_key[0],round(avg_country_num,2)))
            video_id_set.clear()
            country_times = 1
            video_id_set.add(key_list[1])
        current_key = key_list

    if current_key != None and current_key[0] == key_list[0]: #for statistics the last record
        video_id_set.add(key_list[1])
        avg_country_num = country_times/len(video_id_set)
        print("{}:\t{}".format(current_key[0],round(avg_country_num,2)))

if __name__ == "__main__":
    video_reducer()
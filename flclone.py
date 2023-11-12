from pydub import AudioSegment
import sys
from datetime import datetime
import os
os.system('cls' if os.name == 'nt' else 'clear')


def get_timestamp(path):
    return [
        os.path.getctime(path),
        os.path.getmtime(path),
        os.path.getatime(path),
    ]


def datetime_print(*args):

    if len(args) == 0:
        print("No arguments were passed")

    elif len(args) == 1:

        timestamps_1 = args[0]
        printable = [datetime.fromtimestamp(ts).strftime(
            '%Y-%m-%d  %H:%M:%S') for ts in timestamps_1]

        print(
            "{:<12} -> \x1b[33m{:<10}\x1b[0m".format('CREATED', printable[0]))
        print(
            "{:<12} -> \x1b[33m{:<10}\x1b[0m".format('MODIFIED', printable[1]))
        print(
            "{:<12} -> \x1b[33m{:<10}\x1b[0m".format('ACCESSED', printable[2]))
        print()

    elif len(args) == 2:

        [timestamps_1, timestamps_2] = args

        printable_1 = [datetime.fromtimestamp(ts).strftime(
            '%Y-%m-%d  %H:%M:%S') for ts in timestamps_1]
        printable_2 = [datetime.fromtimestamp(ts).strftime(
            '%Y-%m-%d  %H:%M:%S') for ts in timestamps_2]

        print("{:<12} -> \x1b[33m{:<25}\x1b[0m {:<12} -> \x1b[33m{:<25}\x1b[0m".format(
            'CREATED', printable_1[0], 'CREATED', printable_2[0]))
        print("{:<12} -> \x1b[33m{:<25}\x1b[0m {:<12} -> \x1b[33m{:<25}\x1b[0m".format(
            'MODIFIED', printable_1[1], 'MODIFIED', printable_2[1]))
        print("{:<12} -> \x1b[33m{:<25}\x1b[0m {:<12} -> \x1b[33m{:<25}\x1b[0m".format(
            'ACCESSED', printable_1[2], 'ACCESSED', printable_2[2]))
        print()

    else:
        print("No more than two arguments allowed")


def filename_print(*args):

    if len(args) < 2:
        print("Internal error. No arguments were passed")
        sys.exit(1)

    elif len(args) == 2:
        [message_1, file_1] = args
        print("\n{}  \x1b[34m{}\x1b[0m".format(message_1, file_1))
        print('-' * 36)

    elif len(args) == 3:
        print("Not enough arguments were passed")
        sys.exit(1)

    elif len(args) == 4:
        [message_1, file_1, message_2, file_2] = args
        print("\n{:<12}  \x1b[34m{:<28}\x1b[0m{:<12}  \x1b[34m{:<28}\x1b[0m".format(
            message_1, file_1, message_2, file_2))
        print('-' * 36 + ' ' * 6 + '-' * 36)

    else:
        print("No more than two arguments allowed")


#########################################################################################
# Convertation
#########################################################################################
# If no arguments in commandline
if len(sys.argv) < 2:
    print("\x1b[33mUsage: python flclone.py source_file [timedonor_file]\x1b[0m")
    print("To convert a file to FLAC and clone its date/time:")
    print(" - If only one file is provided, date/time will be taken from that file.")
    print(" - If two files are provided, date/time will be cloned from the timedonor file.\x1b[0m")
    print()
    print("Necessary arguments were not provided.")
    print("...Exiting !")
    print()
    sys.exit(1)


# If only one file provided
if len(sys.argv) == 2:

    source_file = sys.argv[1]
    source_ext = os.path.splitext(source_file)[1]

    source_timestamp = get_timestamp(source_file)

    filename_print('SOURCE FILE:', source_file)
    datetime_print(source_timestamp)

    proceed = input(
        "Do you want to \x1b[34mconvert it to FLAC\x1b[0m and \x1b[34mclone date/time\x1b[0m to output file ? (y/n): ")

    # proceed = 'y'
    if proceed.lower() == 'y':

        print("\x1b[34mConverting date ->\x1b[0m")
        try:
            output_file = source_file.replace(source_ext, ".flac")
            audio_input = AudioSegment.from_file(source_file)
            audio_input.export(output_file, format="flac", parameters=[
                               "-c:a", "flac", "-compression_level", "12"])
        except:
            print(
                "\n\x1b[31mAn error occured whyle file converting. Exiting.\x1b[0m\n")
            sys.exit(1)

        print("\x1b[34mCloning date/tame ->\x1b[0m")
        try:
            os.utime(output_file, (source_timestamp[2], source_timestamp[1]))

        except:
            print(
                "\n\x1b[31mAn error occured whyle clone date/time. Exiting.\x1b[0m\n")
            sys.exit(1)

        output_timestamp = get_timestamp(output_file)

        filename_print('OUTPUT FILE:', output_file)
        datetime_print(output_timestamp)

        print(
            "\x1b[34mSuccessfully converted to FLAC and cloned date/time !\x1b[0m\n")

    else:
        print("\x1b[34mCancelled by used. Exiting. \x1b[0m")
        sys.exit(0)


# If two file provided
if len(sys.argv) == 3:

    source_file = sys.argv[1]
    source_ext = os.path.splitext(source_file)[1]
    timedonor_file = sys.argv[2]

    source_timestamp = get_timestamp(source_file)
    donor_timestamp = get_timestamp(timedonor_file)

    filename_print('SOURCE FILE:', source_file,
                   'TIMEDONOR FILE:', timedonor_file)
    datetime_print(source_timestamp, donor_timestamp)

    proceed = input(
        "Do you want to \x1b[34mconvert source to FLAC\x1b[0m and \x1b[34mclone date/time\x1b[0m from timestamp file ? (y/n): ")

    # proceed = 'y'
    if proceed.lower() == 'y':

        print("\x1b[34mConverting date ->\x1b[0m")
        try:
            output_file = source_file.replace(source_ext, ".flac")

            audio_input = AudioSegment.from_file(source_file)
            audio_input.export(output_file, format="flac", parameters=[
                               "-c:a", "flac", "-compression_level", "12"])

        except:
            print(
                "\n\x1b[31mAn error occured whyle file converting. Exiting.\x1b[0m\n")
            sys.exit(1)

        print("\x1b[34mCloning date/tame ->\x1b[0m")

        try:
            os.utime(output_file, (donor_timestamp[2], donor_timestamp[1]))

        except:
            print(
                "\n\x1b[31mAn error occured whyle clone date/time. Exiting.\x1b[0m\n")
            sys.exit(1)

        output_timestamp = get_timestamp(output_file)

        filename_print('OUTPUT FILE:', output_file)
        datetime_print(output_timestamp)

        print(
            "\x1b[34mSuccessfully converted to FLAC and cloned date/time !\x1b[0m\n")

    else:
        print("\x1b[34mCancelled by used. Exiting. \x1b[0m")
        sys.exit(0)


if len(sys.argv) > 3:
    print("This script handles up to two arguments only.")
    print("\x1b[33mUsage: python flclone.py source_file [timedonor_file]\x1b[0m")
    print("To convert a file to FLAC and clone its date/time:")
    print(" - If only one file is provided, date/time will be taken from that file.")
    print(" - If two files are provided, date/time will be cloned from the timedonor file.\x1b[0m")
    print()
    print("\x1b[31mToo many arguments were provided !\x1b[0m")
    print("...Exiting !")
    print()
    sys.exit(1)

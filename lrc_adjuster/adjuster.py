import sys
import os


def adjust_timestamp(timestamp, offset):
    minutes, seconds = timestamp.split(":")
    total_seconds = int(minutes) * 60 + float(seconds)
    adjusted_seconds = total_seconds + offset
    adjusted_minutes = int(adjusted_seconds // 60)
    adjusted_seconds %= 60
    adjusted_timestamp = f"{adjusted_minutes:02}:{adjusted_seconds:06.3f}"
    return adjusted_timestamp


def main():
    if len(sys.argv) != 3:
        print("Usage: python lrc-adjuster.py <input_file> <offset>")
        return

    input_file = sys.argv[1]
    offset = float(sys.argv[2])

    with open(input_file, "r") as file:
        lines = file.readlines()

    adjusted_lines = []
    for line in lines:
        if line.startswith("["):
            timestamp_end = line.index("]")
            timestamp = line[1:timestamp_end]
            try:
                adjusted_timestamp = adjust_timestamp(timestamp, offset)
                adjusted_line = f"[{adjusted_timestamp}]{line[timestamp_end+1:]}"
                adjusted_lines.append(adjusted_line)
            except ValueError:
                adjusted_lines.append(line)
        else:
            adjusted_lines.append(line)

    output_file = (
        os.path.splitext(input_file)[0]
        + f"-adjusted{offset}"
        + os.path.splitext(input_file)[1]
    )
    with open(output_file, "w") as file:
        file.writelines(adjusted_lines)

    print(f"Adjusted file saved as '{output_file}'.")


if __name__ == "__main__":
    main()

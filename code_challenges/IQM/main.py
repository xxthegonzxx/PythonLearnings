#!/usr/bin/env python
import create_data
import incremental_interquartile_mean


def main():
    file_path = "data.txt"
    create_data.write_to_file(file_path)
    incremental_interquartile_mean.iqm(file_path)

if __name__ == '__main__':
    main()

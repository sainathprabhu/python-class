'''files is a storege meant for holding the data in specified format
Modes to open a txt file
    1. Read -   *   represented with r
                *   reading content from file will throw an exceptios is source file is not available or read protected

    2. Write -  *   represented with w
                *   opens the file in the writable format,
                *   creates the file and write the contents to it if the file is not availabel
                *   overwrite the content if the content is available

    3. append - *   represented with a
                *   to append the content to the file
                *   create and writes to the file if not available, it appends the content to tht file if it is available

Modes to open byte
    rb
    wb
    ab

adding + to the modes we can enable write function to the normal mode eg: rb+ wb+ ab+

Note: Metadata is data about data

'''


ff = open("/home/hunter/PycharmProjects/python-class/a.txt","r")
print(ff.name)
print(ff.closed)
print(ff.mode)
ff.close()
print(ff.closed)
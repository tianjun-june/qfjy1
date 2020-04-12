with open(r"c:\123.jpg","rb") as stream:
    container = stream.read()

    with open(r"c:\users\111.jpg","wb") as wstream:
        wstream.write(container)


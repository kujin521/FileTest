with open('reader.md','a',encoding="utf-8") as md:
    md.write("添加一行")
    contents=md.read()
    print(contents)

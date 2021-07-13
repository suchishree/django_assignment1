#example program to convert text to speech


from gtts import gTTs
x=gTTs("hello my self rosy")
x.save("one.mp3")

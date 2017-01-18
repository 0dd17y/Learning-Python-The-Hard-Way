class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def print_me_a_song(self):   #Its what it actually does.
        for line in self.lyrics:
            print line
happy_bday = Song(["Happy birthday to you",
                   "I dont want to get sued",
                   "So I'll stop right there"])

song_words =  Song("""Mary had a little lamb",
              The lamb was small unfortunately,
              It could'nt feed all the guests at the dinner party
              """)


bulls_on_parade = Song(["They really rally around the family",
                        "With pockets full of shells"])

happy_bday.print_me_a_song()
bulls_on_parade.print_me_a_song()
song_words.print_me_a_song()
Song("""Hey There! Look!
 I got some lyrics
 NOt from a page in a book
 But i bet you can feel it""").print_me_a_song()







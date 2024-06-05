class Movie:
    def __init__(self,title,hero,heroine):
        self.title=title
        self.hero=hero
        self.heroine=heroine
    def info(self):
        print("Movie Name :",self.title)
        print("Hero Name :",self.hero)
        print("Heroine Name :",self.heroine)

list_of_movies=[]
while True:
    title=input("Enter Movie Name :")
    hero=input("Enter Hero Name :")
    heroine=input("Enter Heroine Name :")
    m=Movie(title,hero,heroine)
    list_of_movies.append(m)
    print("Movie added successfully...")
    option = input("Do you want to add new Movie [Yes/No] :")
    if option.lower()=='no':
        break
print("All Movies Info")
print("_"*50)

for movie in list_of_movies:
    movie.info()
    print() 
    # print("-"*50)

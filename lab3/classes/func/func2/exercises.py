# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1
def imdb_rate(movie):
    for i in movies:
        if i["name"]==movie:
            if i["imdb"] >5.5:
                return True
            else:
                return False    
movie=input()
print(imdb_rate(movie))
#2
def scores(movies):
    films = []
    for i in movies:
        if i["imdb"] > 5.5:
            films.append(i["name"])
    print(*films, sep = "; ")
scores(movies)
#3
def cat(cat,movies):
    same_cat=[]
    for i in movies:
        if i["category"]==cat:
            same_cat.append(i["name"])

        print(*same_cat, sep = "; ")
a=input()
cat(a,movies) 
#4
def avg(spisok,movies):
    summary=0
    for i in spisok:
        for j in movies:
            if i==j["name"]:
                summary+=j["imdb"]

    avg=summary/len(spisok)
    print(avg)
spisok=["We Two", "Exam", "Detective", "What is the name"]
avg(spisok, movies)
#5
def avg_cat(cat,movies):
    summary=0
    summary_cat=0
    for i in movies:
        if i["category"]==cat:
            summary_cat+=1
            summary+=i["imdb"]
    avg_cat=summary/summary_cat
    print(avg_cat)
category="Thriller"
avg_cat(category, movies)
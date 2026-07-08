news1={
    "bbc":"https://www.bbc.com/",
    "times":"https://timesofindia.indiatimes.com/",
    "hindu":"https://www.thehindu.com/",
    "india":"https://www.indiatoday.in/",
}

def new(news):
    return news1.get(news)
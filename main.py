import requests 
# import time
# current_time = time.strftime("%Y-%m-%d") 
#if want current news you add : &from={current_time}, in url
API_KEY="d0cb627dc2fd47d484804de596ad3b37"
def news_class(topic,page_size=20):
    url=f"https://newsapi.org/v2/everything?q={topic}&pageSize={page_size}&sortBy=publishedAt&apiKey={API_KEY}"
    r = requests.get(url)
    if(r.status_code==200):
        data = r.json()
        articles =  data["articles"]
        print(f"\n TOP {len(articles)} news articles about '{topic}':\n")
        for news,article in enumerate(articles, 1):
            print(f"{news}. {article['title']}")
            print(f"  Description: {article['description']}")
            print(f"  PublishedAt: {article['publishedAt']}")
            print(f"  Content: {article['content']}")
            print(f"  Source: {article['source']['name']}")
            print(f"  URL: {article['url']}\n")            
    else:
        print("Failed to fetch news:", r.status_code, r.text)   
if __name__ == "__main__":
    topic = input("Enter a topic (e.g. technology, sports, politics): ")
    news_class(topic)    

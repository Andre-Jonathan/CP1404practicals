import wikipedia

search_title = input("Enter a page title or a phrase: ").title()
while search_title != "":

    try:
        page_search = wikipedia.page(search_title)
        print(page_search)
        print(f"Title: {page_search.title}\nSummary: {page_search.summary}\nURL: {page_search.url}\n")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search_title = input("Enter a page title or a phrase: ").title()

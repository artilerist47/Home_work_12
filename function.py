import  json

def load_posts():
    with open("posts.json", encoding="utf-8") as file:
        return json.load(file)


def get_posts_by_word(word):
    result = []
    for post in load_posts():
        if word.lower() in post["content"].lower():
            result.append(post)
    return result
import json


def load_posts():
    with open("posts.json", encoding="utf-8") as file:
        return json.load(file)


def get_posts_by_word(word):
    result = [post for post in load_posts() if word in post["content"].lower()]
    # result = []
    # for post in load_posts():
    #     if word.lower() in post["content"].lower():
    #         result.append(post)
    return result


def add_post(post):
    posts = load_posts()
    posts.append(post)
    # with open("posts.json", "a", encoding="utf-8") as file:
    with open("posts.json", "w", encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii=False)
    return post









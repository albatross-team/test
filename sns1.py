posts = []
post_id = 1  # 포스트 ID는 1부터 시작

def add_post(content, author):
    global post_id
    post = {
        'id': post_id,
        'author': author,
        'content': content,
        'comments': [],
        'likes': 0
    }
    posts.append(post)
    post_id += 1  # 포스트 추가 후 ID 증가

def add_comment(post_id, comment, author):
    for post in posts:
        if post['id'] == post_id:
            post['comments'].append({'author': author, 'comment': comment})
            return True
    return False

def like_post(post_id):
    for post in posts:
        if post['id'] == post_id:
            post['likes'] += 1
            return True
    return False

def show_feed():
    for post in posts:
        print(f"[{post['id']}] {post['author']}: {post['content']} (좋아요: {post['likes']})")
        for comment in post['comments']:
            print(f"  - {comment['author']}: {comment['comment']}")
        print()

# 메뉴 기반 인터페이스
while True:
    print("\n[1] 포스트 추가 [2] 댓글 추가 [3] 좋아요 [4] 피드 출력 [5] 종료")
    choice = input("메뉴를 선택하세요: ")
    if choice == "1":
        content = input("글 내용: ")
        author = input("작성자: ")
        add_post(content, author)
    elif choice == "2":
        post_id = int(input("포스트 ID: "))
        comment = input("댓글 내용: ")
        author = input("작성자: ")
        add_comment(post_id, comment, author)
    elif choice == "3":
        post_id = int(input("포스트 ID: "))
        like_post(post_id)
    elif choice == "4":
        show_feed()
    elif choice == "5":
        print("프로그램을 종료합니다.")
        break
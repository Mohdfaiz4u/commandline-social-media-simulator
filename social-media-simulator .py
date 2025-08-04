from datetime import datetime

class Post:
    post_counter = 0

    def __init__(self, author, text):
        Post.post_counter += 1
        self.post_id = Post.post_counter
        self.author = author
        self.text = text
        self.timestamp = datetime.now()
        self.likes = set()
        self.comments = []

    def like(self, username):
        self.likes.add(username)

    def comment(self, username, comment_text):
        self.comments.append((username, comment_text))

    def __str__(self):
        time = self.timestamp.strftime("%Y-%m-%d %H:%M")
        comments_str = "\n".join([f"  - {user}: {comment}" for user, comment in self.comments])
        return (f"[{self.post_id}] {self.author} at {time}: {self.text} "
                f"👍{len(self.likes)}\nComments:\n{comments_str if comments_str else '  No comments yet.'}")


class User:
    def __init__(self, username):
        self.username = username
        self.posts = []
        self.following = set()
        self.followers = set()

    def post(self, text):
        p = Post(self.username, text)
        self.posts.append(p)
        return p

    def follow(self, other):
        if other.username == self.username:
            return False
        if other.username in self.following:
            return False
        self.following.add(other.username)
        other.followers.add(self.username)
        return True

    def unfollow(self, other):
        if other.username in self.following:
            self.following.remove(other.username)
            other.followers.discard(self.username)
            return True
        return False

    def get_feed(self, all_posts):
        feed = [p for p in all_posts if p.author in self.following]
        return sorted(feed, key=lambda p: p.timestamp, reverse=True)


class SocialMediaApp:
    def __init__(self):
        self.users = {}
        self.all_posts = []
        self.current_user = None

    def signup(self, username):
        if username in self.users:
            print("Username already taken.")
            return
        self.users[username] = User(username)
        print(f"User '{username}' created.")

    def login(self, username):
        if username not in self.users:
            print("No such user.")
            return
        self.current_user = self.users[username]
        print(f"Logged in as '{username}'.")

    def logout(self):
        if self.current_user:
            print(f"Logged out from {self.current_user.username}.")
        self.current_user = None

    def post(self, text):
        if not self.current_user:
            print("Login first.")
            return
        p = self.current_user.post(text)
        self.all_posts.append(p)
        print(f"Posted with ID {p.post_id}.")

    def follow(self, target_username):
        if not self.current_user:
            print("Login first.")
            return
        target = self.users.get(target_username)
        if not target:
            print("User not found.")
            return
        if self.current_user.follow(target):
            print(f"You now follow {target_username}.")
        else:
            print("Cannot follow yourself or already following.")

    def unfollow(self, target_username):
        if not self.current_user:
            print("Login first.")
            return
        target = self.users.get(target_username)
        if not target:
            print("User not found.")
            return
        if self.current_user.unfollow(target):
            print(f"You have unfollowed {target_username}.")
        else:
            print("You are not following this user.")

    def like(self, post_id):
        if not self.current_user:
            print("Login first.")
            return
        post = next((p for p in self.all_posts if p.post_id == post_id), None)
        if not post:
            print("Post not found.")
        else:
            post.like(self.current_user.username)
            print(f"Liked post {post_id}.")

    def comment(self, post_id, comment_text):
        if not self.current_user:
            print("Login first.")
            return
        post = next((p for p in self.all_posts if p.post_id == post_id), None)
        if not post:
            print("Post not found.")
        else:
            post.comment(self.current_user.username, comment_text)
            print(f"Comment added to post {post_id}.")

    def show_feed(self):
        if not self.current_user:
            print("Login first.")
            return
        feed = self.current_user.get_feed(self.all_posts)
        if not feed:
            print("No posts to show. Follow users to see feed.")
        else:
            print("--- Feed ---")
            for p in feed:
                print(p)

    def show_users(self):
        print("--- Registered Users ---")
        for user in self.users.values():
            print(f"- {user.username} (Followers: {len(user.followers)}, Following: {len(user.following)})")

    def run(self):
        print("Welcome to CLI Social Media! Type 'help' for commands.")
        while True:
            cmd = input("> ").strip().split(maxsplit=1)
            if not cmd:
                continue
            action = cmd[0].lower()
            arg = cmd[1] if len(cmd) > 1 else ""

            if action == "help":
                print("Commands: signup [name], login [name], logout, post [text], "
                      "follow [name], unfollow [name], like [post_id], comment [post_id] [comment text], "
                      "feed, users, exit")
            elif action == "signup":
                self.signup(arg)
            elif action == "login":
                self.login(arg)
            elif action == "logout":
                self.logout()
            elif action == "post":
                self.post(arg)
            elif action == "follow":
                self.follow(arg)
            elif action == "unfollow":
                self.unfollow(arg)
            elif action == "like":
                if arg.isdigit():
                    self.like(int(arg))
                else:
                    print("Usage: like [post_id]")
            elif action == "comment":
                parts = arg.split(maxsplit=1)
                if len(parts) == 2 and parts[0].isdigit():
                    self.comment(int(parts[0]), parts[1])
                else:
                    print("Usage: comment [post_id] [comment text]")
            elif action == "feed":
                self.show_feed()
            elif action == "users":
                self.show_users()
            elif action == "exit":
                print("Goodbye!")
                break
            else:
                print("Unknown command. Type 'help'.")


if __name__ == "__main__":
    app = SocialMediaApp()
    app.run()

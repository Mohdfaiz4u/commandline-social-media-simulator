# commandline-social-media-simulator
# CLI Social Media App

A simple command-line social media application written in Python. Users can sign up, log in, post updates, follow/unfollow others, like and comment on posts, and view a personalized feed.

## Features

- **User Signup & Login:** Create an account, log in, and log out.
- **Post Creation:** Share text posts with the community.
- **Feed:** View posts from users you follow, sorted by newest.
- **Follow/Unfollow:** Build your network by following or unfollowing users.
- **Like & Comment:** Interact with posts by liking or commenting.
- **User Directory:** See all registered users and their followers/following counts.
- **CLI Interface:** All actions are performed via simple commands.

## How to Run

1. **Requirements:**  
   - Python 3.x

2. **Clone or Download:**  
   Save the script as `social_media_app.py`.

3. **Run the App:**
   ```sh
   python social_media_app.py
   ```

4. **Commands:**

   | Command                                | Description                                         |
   |---------------------------------------- |-----------------------------------------------------|
   | `signup [username]`                    | Create a new user account                           |
   | `login [username]`                     | Log into an existing account                        |
   | `logout`                               | Log out of the current account                      |
   | `post [text]`                          | Create a new post                                   |
   | `follow [username]`                    | Follow another user                                 |
   | `unfollow [username]`                  | Unfollow a user                                     |
   | `like [post_id]`                       | Like a post by its ID                               |
   | `comment [post_id] [comment text]`     | Comment on a post                                   |
   | `feed`                                 | View your feed (posts from users you follow)        |
   | `users`                                | List all registered users                           |
   | `help`                                 | Show commands                                       |
   | `exit`                                 | Quit the app                                        |

## Example Session

```text
Welcome to CLI Social Media! Type 'help' for commands.
> signup alice
User 'alice' created.
> login alice
Logged in as 'alice'.
> post Hello, world!
Posted with ID 1.
> signup bob
User 'bob' created.
> login bob
Logged in as 'bob'.
> follow alice
You now follow alice.
> feed
--- Feed ---
[1] alice at 2025-08-04 12:55: Hello, world! 👍0
Comments:
  No comments yet.
> like 1
Liked post 1.
> comment 1 Welcome Alice!
Comment added to post 1.
> feed
--- Feed ---
[1] alice at 2025-08-04 12:55: Hello, world! 👍1
Comments:
  - bob: Welcome Alice!
```

## Notes

- **Post IDs:** Each post has a unique, incrementing ID.
- **Following:** Only posts from users you follow appear in your feed.
- **Likes/Comments:** Only logged-in users can like or comment on posts.
- **Persistence:** Data is **not** saved between runs; this is an in-memory demo.

## License

MIT License

---
Enjoy building your own simple social network!

import requests
import yaml

with open("..userprofile/config.yml", 'r'):
    config = yaml.safe_load(f)

class UserService:

    def __init__(self, username):
        self.username = username
        pass

    def isValidGithubUser(self):

        try:
            print("Checking if valid user ot not")
            request_url = config.user_profile_url.format(username=self.username)
            response = requests.get(request_url)
            print(response.json())
            if 'message' in response.json():
                print("Is not valid user")
                return False
            else:
                print("Is valid user")
                return True
        except Exception as e:
            raise e

    def getUserDetails(self):
        request_url = config.user_profile_url.format(username=self.username)
        response = requests.get(request_url)
        return response.json()

    def getUserFollowers(self):
        user_followers_request_url: str = config.user_followers_url.format(username=self.username)
        print("User followers request url : ", user_followers_request_url)
        try:
            user_followers_response = requests.get(user_followers_request_url)
            return user_followers_response.json()
        except Exception as e:
            raise e

    def getUserGists(self):
        user_gists_request_url: str = config.user_gists_url.format(username=self.username)
        print("User gists request url: ", user_gists_request_url)

        try:
            user_gists_response = requests.get(user_gists_request_url)
            return user_gists_response.json()
        except Exception as e:
            raise e

    def getUserGist(self, gist_id: str):
        user_gist_request_url: str = config.user_gist_url.format(username=self.username, gist_id=gist_id)
        print("User gists request url: ", user_gist_request_url)

        try:
            user_gist_response = requests.get(user_gist_request_url)
            return user_gist_response.json()
        except Exception as e:
            raise e

    def getUserRepos(self):
        user_repos_request_url: str = config.user_repos_url.format(username=self.username)
        print("User repos request url: ", user_repos_request_url)

        try:
            user_repos_response = requests.get(user_repos_request_url)
            return user_repos_response.json()
        except Exception as e:
            raise e

    def getUserRepoLanguages(self, repo_name: str):
        user_repos_languages_request_url: str = config.user_repo_languages_used_url.format(username=self.username,
                                                                                           repo_name=repo_name)
        print("User repos request url: ", user_repos_languages_request_url)

        try:
            user_repos_languages_used_response = requests.get(user_repos_languages_request_url)
            return user_repos_languages_used_response.json()
        except Exception as e:
            raise e

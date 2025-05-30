import requests
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
import colorama
from colorama import Fore, Style

colorama.init()

def handlesweep():
    print(r"""
 _    _                 _ _       _____
| |  | |               | | |     / ____|
| |__| | __ _ _ __   __| | | ___| (_____      _____  ___ _ __
|  __  |/ _` | '_ \ / _` | |/ _ \\___ \ \ /\ / / _ \/ _ \ '_ \
| |  | | (_| | | | | (_| | |  __/____) \ V  V /  __/  __/ |_) |
|_|  |_|\__,_|_| |_|\__,_|_|\___|_____/ \_/\_/ \___|\___| .__/
                                                        | |
                                                        |_|

Made by: Blurredness/PA3MblTOCTb
TG-Channel: https://t.me/Blurredness (russian lang only)
Enjoy >:)
(Thx for using)
""")


user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.203",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.5; rv:109.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (X11; Linux i686; rv:109.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/120.0.6099.119 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-T870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-T720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Vivaldi/6.1.3035.111",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 EdgA/120.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Whale/3.21.192.18 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Brave/120.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPX/120.0.0.0"
]




def check_nickname(username, services, user_agents):
    def check_service(name, url_template):
        url = url_template.format(username=username)
        headers = {
            "User-Agent": random.choice(user_agents)
        }
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code in [200, 201, 204]:
                return name, "Taken", url
            elif response.status_code == 404:
                return name, "Available", None
            else:
                return name, f"Unknown ({response.status_code})", None
        except requests.RequestException as e:
            return name, f"Error: {str(e)}", None

    results = {}

    print("I recommend to check Unknown  Error yourself!")
    print("For some services i rccommend to use VPÑ\n\n")

    with ThreadPoolExecutor(max_workers=25) as executor:
        futures = [executor.submit(check_service, name, url) for name, url in services.items()]
        for future in as_completed(futures):
            service, status, link = future.result()
            results[service] = status

            if status == "Taken":
                print(f"{Fore.GREEN}[+] {service} — Taken{Style.RESET_ALL} ( {link} )")
            elif status == "Available":
                print(f"{Fore.RED}[-] {service} — Available{Style.RESET_ALL}")
            elif status.startswith("Error"):
                print(f"{Fore.MAGENTA}[!] {service} — {status}{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}[?] {service} — {status}{Style.RESET_ALL}")
                
    print(f"\n\n\n{Fore.GREEN}[+] Green - Taken   {Style.RESET_ALL}|  {Fore.RED} [-] Red - Available Username{Style.RESET_ALL}")
    return results


if __name__ == '__main__':
    handlesweep()
    print("\n[1] Nickname Checker")
    print("[2] nothing")
    print("[3] nothing")
    print("[q] Quit")
    choice = input("Choose Function(1): ")

    services = {
    "GitHub": "https://github.com/{username}",
    "Twitter": "https://twitter.com/{username}",
    "Instagram": "https://www.instagram.com/{username}/",
    "TikTok": "https://www.tiktok.com/@{username}",
    "Reddit": "https://www.reddit.com/user/{username}",
    "Pinterest": "https://www.pinterest.com/{username}/",
    "Tumblr": "https://{username}.tumblr.com/",
    "Flickr": "https://www.flickr.com/people/{username}/",
    "Steam": "https://steamcommunity.com/id/{username}",
    "Twitch": "https://www.twitch.tv/{username}",
    "Vimeo": "https://vimeo.com/{username}",
    "SoundCloud": "https://soundcloud.com/{username}",
    "Spotify": "https://open.spotify.com/user/{username}",
    "DeviantArt": "https://www.deviantart.com/{username}",
    "Badoo": "https://badoo.com/profile/{username}",
    "Medium": "https://medium.com/@{username}",
    "About.me": "https://about.me/{username}",
    "Cash App": "https://cash.app/${username}",
    "BuyMeACoffee": "https://buymeacoffee.com/{username}",
    "Keybase": "https://keybase.io/{username}",
    "AngelList": "https://angel.co/u/{username}",
    "ProductHunt": "https://www.producthunt.com/@{username}",
    "500px": "https://500px.com/{username}",
    "Goodreads": "https://www.goodreads.com/{username}",
    "GitLab": "https://gitlab.com/{username}",
    "Kaggle": "https://www.kaggle.com/{username}",
    "Telegram": "https://t.me/{username}",
    "VK": "https://vk.com/{username}",
    "OK.ru": "https://ok.ru/{username}",
    "Ask.fm": "https://ask.fm/{username}",
    "LinkedIn": "https://www.linkedin.com/in/{username}/",
    "Facebook": "https://www.facebook.com/{username}",
    "Patreon": "https://www.patreon.com/{username}",
    "ReverbNation": "https://www.reverbnation.com/{username}",
    "Bandcamp": "https://{username}.bandcamp.com/",
    "Gitee": "https://gitee.com/{username}",
    "Instructables": "https://www.instructables.com/member/{username}/",
    "Behance": "https://www.behance.net/{username}",
    "Dribbble": "https://dribbble.com/{username}",
    "Houzz": "https://www.houzz.com/pro/{username}/",
    "TripAdvisor": "https://www.tripadvisor.com/members/{username}",
    "Mixcloud": "https://www.mixcloud.com/{username}/",
    "SlideShare": "https://www.slideshare.net/{username}",
    "WeHeartIt": "https://weheartit.com/{username}",
    "Last.fm": "https://www.last.fm/user/{username}",
    "Periscope": "https://www.pscp.tv/{username}",
    "Unsplash": "https://unsplash.com/@{username}",
    "HubPages": "https://hubpages.com/@{username}",
    "Trello": "https://trello.com/{username}",
    "Scribd": "https://www.scribd.com/{username}",
    "Lemmy": "https://lemmy.ml/u/{username}",
    "Flipboard": "https://flipboard.com/@{username}",
    "Coderwall": "https://coderwall.com/{username}",
    "HackerRank": "https://www.hackerrank.com/{username}",
    "Duolingo": "https://www.duolingo.com/profile/{username}",
    "Codecademy": "https://www.codecademy.com/profiles/{username}",
    "Codepen": "https://codepen.io/{username}",
    "Chess.com": "https://www.chess.com/member/{username}",
    "Strava": "https://www.strava.com/athletes/{username}",
    "Furaffinity": "https://www.furaffinity.net/user/{username}",
    "Mastodon.social": "https://mastodon.social/@{username}",
    "Itch.io": "https://{username}.itch.io/",
    "Roblox": "https://www.roblox.com/user.aspx?username={username}",
    "NameMC": "https://namemc.com/profile/{username}",
    "Speedrun.com": "https://www.speedrun.com/user/{username}",
    "Anilist": "https://anilist.co/user/{username}/",
    "Gravatar": "https://en.gravatar.com/{username}",
    "HackTheBox": "https://app.hackthebox.com/profile/{username}",
    "Ko-fi": "https://ko-fi.com/{username}",
    "Launchpad": "https://launchpad.net/~{username}",
    "Letterboxd": "https://letterboxd.com/{username}/",
    "Pixiv": "https://www.pixiv.net/en/users/{username}",
    "OpenStreetMap": "https://www.openstreetmap.org/user/{username}",
    "Roboflow": "https://universe.roboflow.com/{username}",
    "Shikimori": "https://shikimori.me/{username}",
    "Scratch": "https://scratch.mit.edu/users/{username}/",
    "Fandom": "https://www.fandom.com/u/{username}",
    "Dev.to": "https://dev.to/{username}",
    "GreasyFork": "https://greasyfork.org/en/users/{username}",
    "Replit": "https://replit.com/@{username}",
    "Keybr": "https://www.keybr.com/profile/{username}",
    "BuySellAds": "https://www.buysellads.com/profile/{username}",
    "Ello": "https://ello.co/{username}",
    "Gumroad": "https://{username}.gumroad.com/",
    "WorldAnvil": "https://www.worldanvil.com/author/{username}",
    "Crowdin": "https://crowdin.com/profile/{username}",
    "ThemeForest": "https://themeforest.net/user/{username}",
    "Codeforces": "https://codeforces.com/profile/{username}",
    "Basecamp": "https://launchpad.37signals.com/u/{username}",
    "Trakt.tv": "https://trakt.tv/users/{username}",
    "FreeCodeCamp": "https://www.freecodecamp.org/{username}",
    "TradingView": "https://www.tradingview.com/u/{username}/",
    "Habr": "https://habr.com/ru/users/{username}/",
    "Kitsu": "https://kitsu.io/users/{username}",
    "Codewars": "https://www.codewars.com/users/{username}",
    "XDA Developers": "https://forum.xda-developers.com/m/{username}.1234567/",
    "LiberaPay": "https://liberapay.com/{username}/",
    "Codingame": "https://www.codingame.com/profile/{username}",
    "Behappy.me": "https://behappy.me/@{username}",
    "Metacritic": "https://www.metacritic.com/user/{username}",
    "Photobucket": "https://app.photobucket.com/u/{username}",
    "Reedsy": "https://reedsy.com/{username}",
    "Read.cv": "https://read.cv/{username}",
    "Notion": "https://{username}.notion.site",
    "Polywork": "https://www.polywork.com/{username}",
    "Quora": "https://www.quora.com/profile/{username}",
    "GitHub Gists": "https://gist.github.com/{username}",
    "StackOverflow": "https://stackoverflow.com/users/{username}",
    "YouTube": "https://www.youtube.com/{username}",
    "Bitbucket": "https://bitbucket.org/{username}",
    "DeviantArt": "https://www.deviantart.com/{username}",
    "Dribbble": "https://dribbble.com/{username}",
    "Envato": "https://codecanyon.net/user/{username}",
    "GitLab": "https://gitlab.com/{username}",
    "Jira": "https://{username}.atlassian.net/",
    "Medium": "https://medium.com/@{username}",
    "StackExchange": "https://stackexchange.com/users/{username}",
    "HackerRank": "https://www.hackerrank.com/{username}",
    "Behance": "https://www.behance.net/{username}",
    "Vimeo": "https://vimeo.com/{username}",
    "Pluralsight": "https://app.pluralsight.com/profile/{username}",
    "Designspiration": "https://www.designspiration.com/{username}/",
    "Codementor": "https://www.codementor.io/@{username}",
    "Contently": "https://{username}.contently.com/",
    "Hashnode": "https://hashnode.com/@{username}",
    "Reverb": "https://reverb.com/shop/{username}",
    "Payhip": "https://payhip.com/{username}",
    "SpeakerDeck": "https://speakerdeck.com/{username}",
    "YCombinator": "https://www.ycombinator.com/companies/{username}",
    "Dailymotion": "https://www.dailymotion.com/{username}",
    "Quizlet": "https://quizlet.com/{username}",
    "Vero": "https://www.vero.co/{username}",
    "OpenCollective": "https://opencollective.com/{username}",
    "Redbubble": "https://www.redbubble.com/people/{username}",
    "Stereogum": "https://www.stereogum.com/author/{username}/",
}
    
    if choice == '1':
    	username = input("Nickname for checking: ")
    	print("Checking...")
    	check_nickname(username, services, user_agents)

    elif choice == '2':
        print("WIP")

    elif choice == '3':
        print("WIP")
        
    elif choice.lower() == 'q':
    	print("""Quiting. Thanks for using my programm!(bad rn). 
Sub to TG: @Blurredness""")
    	exit()
    
    else:
        print("Wrong choice.")

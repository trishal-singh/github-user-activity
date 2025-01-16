import sys
import requests
from rich import print as rich_print

def main():
    if len(sys.argv)==2:
        username=sys.argv[1]
        url = f"https://api.github.com/users/{username}/events"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            event = response.json()
            latest_events = event
            rich_print(f"Latest events for [bold green]{username}[/bold green]:")
            for event in latest_events:
                # Covering only the most common events
                if event['type'] == 'IssueCommentEvent':
                    rich_print(f"- :smiley: commented on issue {event['payload']['issue']['number']}")
                elif event['type'] == 'PushEvent':
                    rich_print(f"- :smiley: pushed to {event['repo']['name']}")
                elif event['type'] == 'IssuesEvent':
                    rich_print(f"- :smiley: created issue {event['payload']['issue']['number']}")
                elif event['type'] == 'WatchEvent':
                    rich_print(f"- :smiley: starred {event['repo']['name']}")
                elif event['type'] == 'PullRequestEvent':
                    rich_print(f"- :smiley: created pull request {event['payload']['pull_request']['number']}")
                elif event['type'] == 'PullRequestReviewEvent':
                    rich_print(f"- :smiley: reviewed pull request {event['payload']['pull_request']['number']}")
                elif event['type'] == 'PullRequestReviewCommentEvent':
                    rich_print(f"- :smiley: commented on pull request {event['payload']['pull_request']['number']}")
                elif event['type'] == 'CreateEvent':
                    rich_print(f"- :smiley: created {event['payload']['ref_type']} {event['payload']['ref']}")
                else:
                    rich_print(f"- :smiley: {event['type']}")
        else:
            rich_print(f"Error fetching events for {username}: {response.status_code}")
    else:
        print("Please Enter One Github Username")
if __name__ == "__main__":
    main()
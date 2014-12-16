
from instagram.client import InstagramAPI

access_token = "1599370650.d1a9900.ef76c35901cf4b768a7a7ae1ceacf094"

api= InstagramAPI(access_token=access_token)
recent_media, next_ = api.user_recent_media(user_id = "1599370650", count = 10)
for media in recent_media:
	print media.caption.text

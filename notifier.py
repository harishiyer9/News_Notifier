from gi.repository import Notify, GdkPixbuf
import time 
from news import NewsList

# One time initialization of libnotify
Notify.init("News Flash")

newslist = NewsList()

for news in newslist:
		
	# Create the notification object
	dict_obj = news
	title = list(dict_obj)[0]
	body = list(dict_obj.values())[0]
	

	notification = Notify.Notification.new(
		title,
		body,
	)

	# Change application name
	notification.set_app_name("News Flash")
	
	# Change summary and body
	notification.update(title,body)
	
	image = GdkPixbuf.Pixbuf.new_from_file("/home/zeno/Downloads/icon.png")
	# Use the GdkPixbuf image
	notification.set_icon_from_pixbuf(image)
	notification.set_image_from_pixbuf(image)

	# Actually show on screen
	notification.show()
	time.sleep(5)




	




# instaloader: A third-party library for downloading Instagram profiles.
# This code uses the instaloader module to download an Instagram profile's pictures 
# (commented out because it requires installation).

import instaloader

loader = instaloader.Instaloader()
name = input("enter name : ")

loader.download_profile(name, profile_pic_only=False)
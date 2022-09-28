#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request
import tweepy

app = Flask(__name__)


@app.route('/search/',methods=['GET'])
def search():
    q=request.args.get('q')
    media = request.args.get('media')
    api_key = 'CxCkNuSCmuelWNslaQhm9G7bq'
    api_key_secret = 'gJMNhCM6GoBAeK086LELVSunbdfSo1a02yeR0ehmAKtA8pkUZT'

    access_token = '1365307419291746313-i2bEAmjz6NPErFs3cVhyE1LG0KF7SO'
    access_token_secret = 'KUCoEdshHZ7VUqKrY7S7FVUrFmjOPaD6uznOoHjzXQhMo'

    # authentication
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    tweets = api.search_tweets(q)
    if media == 'True':
        return str([el for el in tweets if 'media' in el.entities])
    else:
        return str([el for el in tweets if 'media' not in el.entities])

@app.route('/users/<user_id>')
def users(user_id):
    api_key = 'CxCkNuSCmuelWNslaQhm9G7bq'
    api_key_secret = 'gJMNhCM6GoBAeK086LELVSunbdfSo1a02yeR0ehmAKtA8pkUZT'

    access_token = '1365307419291746313-i2bEAmjz6NPErFs3cVhyE1LG0KF7SO'
    access_token_secret = 'KUCoEdshHZ7VUqKrY7S7FVUrFmjOPaD6uznOoHjzXQhMo'

    # authentication
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    user = api.get_user(screen_name=user_id)
    return {"The id is" : str(user.id),
            "The id_str is" : user.id_str,
            "The name is  " : user.name,
            "The screen_name is " : user.screen_name,
            "The location is ":  str(user.location),
            "The profile_location is ":  str(user.profile_location),
            "The description is ":  user.description,


            "The entities are " : str(user.entities),
            "Is the account protected? ":  str(user.protected),

            "The followers_count is ":  str(user.followers_count),
            "The friends_count is ":  str(user.friends_count),
            "The listed_count is ":  str(user.listed_count),
            "The account was created on ":  str(user.created_at),
            "The favourites_count is ":  str(user.favourites_count),
            "The utc_offset is  ":str(user.utc_offset),
            "The geo_enabled is " : str(user.geo_enabled),
            "The verified is " : str(user.verified),
            "The statuses_count is  " : str(user.statuses_count),
            "The lang is ":   str(user.lang),
            "The status ID is " : str(user.status.id),
            "The contributors_enabled is " : str(user.contributors_enabled),
            "The is_translator is " : str(user.is_translator),
            "The is_translation_enabled is " : str(user.is_translation_enabled),

            "The profile_background_color is " : user.profile_background_color,
            "The profile_background_image_url is " :  user.profile_background_image_url,
            "The profile_background_image_url_https is " : user.profile_background_image_url_https,
            "The profile_background_tile is " : str(user.profile_background_tile),
            "The profile_image_url is " :user.profile_image_url,
            "The profile_image_url_https is " : user.profile_image_url_https,
            "The profile_banner_url is " : user.profile_banner_url,
            "The profile_link_color is " : user.profile_link_color,
            "The profile_sidebar_border_color is " : user.profile_sidebar_border_color,
            "The profile_sidebar_fill_color is " : user.profile_sidebar_fill_color,
            "The profile_text_color is " : user.profile_text_color,
            "The profile_use_background_image is " : str(user.profile_use_background_image),

            "The has_extended_profile is " : str(user.has_extended_profile),
            "The default_profile is " :str(user.default_profile),
            "The default_profile_image is " :str(user.default_profile_image),
            "Is the authenticated user following the account? " :str(user.following),

            "Has the authenticated user requested to follow the account? " :str(user.follow_request_sent),
            "Are notifications of the authenticated user turned on for the account? " : str(user.notifications)}



if __name__== '__main__':
    app.run()








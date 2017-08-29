from django.shortcuts import render, redirect

import tweepy

# try:
#     redirect_url = auth.get_authorization_url()
# except tweepy.TweepError:
#     print 'Error! Failed to get request token.'

# auth = tweepy.OAuthHandler('mwGD4LnSsAYe3fHJGgUuHu5Z9', 'Ga3pr3CUZhJMp0lrqrtWQwckINE7R1Jv8NOF0HBbERAdOaBA3X')
# auth.set_access_token('712800559082770432-IHCWzrtKdoC8VxR5hJ4xCgkiCNpYXJF', 'BoIs5m0dtApc98RIXTKaIlTUogxH7MZpnior6z2lwGUG7')

# auth = tweepy.OAuthHandler('mwGD4LnSsAYe3fHJGgUuHu5Z9', 'Ga3pr3CUZhJMp0lrqrtWQwckINE7R1Jv8NOF0HBbERAdOaBA3X')
# auth = tweepy.OAuthHandler('mwGD4LnSsAYe3fHJGgUuHu5Z9', 'Ga3pr3CUZhJMp0lrqrtWQwckINE7R1Jv8NOF0HBbERAdOaBA3X', http://localhost:8000/)

# try:
#     redirect_url = auth.get_authorization_url()
# except tweepy.TweepError:
#     print 'Error! Failed to get request token.'

# session.set('request_token', auth.request_token)

# api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text





# Create your views here.

def twitter(request):
    # auth = tweepy.OAuthHandler('mwGD4LnSsAYe3fHJGgUuHu5Z9', 'Ga3pr3CUZhJMp0lrqrtWQwckINE7R1Jv8NOF0HBbERAdOaBA3X')
    auth = tweepy.OAuthHandler('mwGD4LnSsAYe3fHJGgUuHu5Z9', 'Ga3pr3CUZhJMp0lrqrtWQwckINE7R1Jv8NOF0HBbERAdOaBA3X', 'http://localhost:8000/verified')

    try:
        redirect_url = auth.get_authorization_url()
        print redirect_url
    except tweepy.TweepError:
        print 'Error! Failed to get request token.'

    request.session['request_token'] =  auth.request_token
    print request.session['request_token']



    # print verifier
    # https://api.twitter.com/oauth/request_token


    return redirect(redirect_url)

# def create(request):
#     return render(request, 'ajaxpost/note.html', {'posts':posts})

def verified(request):
    verifier = request.GET.get('oauth_verifier')
    print verifier

    auth = tweepy.OAuthHandler('mwGD4LnSsAYe3fHJGgUuHu5Z9', 'Ga3pr3CUZhJMp0lrqrtWQwckINE7R1Jv8NOF0HBbERAdOaBA3X')
    token = request.session['request_token']
    # print token
    del request.session['request_token']
    auth.request_token = token

    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        print 'Error! Failed to get access token.'

    print auth.access_token, ' and ',  auth.access_token_secret

    # auth = tweepy.OAuthHandler('mwGD4LnSsAYe3fHJGgUuHu5Z9', 'Ga3pr3CUZhJMp0lrqrtWQwckINE7R1Jv8NOF0HBbERAdOaBA3X')
    auth.set_access_token(auth.access_token, auth.access_token_secret)

    api = tweepy.API(auth)

    # api.update_status('tweepy + oauth! I am awesome')

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print tweet.text

    return render(request, 'firsttweet/index.html')
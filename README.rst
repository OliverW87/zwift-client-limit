.. image:: https://pyup.io/repos/github/jsmits/zwift-client/python-3-shield.svg
     :target: https://pyup.io/repos/github/jsmits/zwift-client/
     :alt: Python 3


Zwift Mobile API client written in Python. Heavily inspired by zwift-client_.


Installation
------------

::

    $ git clone ...
    $ python -m venv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt


Usage
-----


Getting follower discrepancy
++++++

::

    $ source .venv/bin/activate
    $ python follower_discrepancy.py

Client
++++++

::

    >>> from zwift import Client
    >>> username = 'your-username'
    >>> password = 'your-password'
    >>> player_id = your-player-id
    >>> client = Client(username, password)


Profile
+++++++

::

    >>> profile = client.get_profile()
    >>> profile.profile  # fetch your profile data
    >>> profile.followers
    >>> profile.get_followers(start)
    >>> profile.followees
    >>> profile.get_followees(start)
    >>> profile.get_activities()  # metadata of your activities
    >>> profile.latest_activity  # metadata of your latest activity


Activity
++++++++

::

    >>> activity = client.get_activity(player_id)
    >>> activities = activity.list()  # your activities (default start is 0, default limit is 20)
    >>> activities = activity.list(start=20, limit=50)
    >>> latest_activity_id = activities[0]['id']
    >>> activity.get_activity(latest_activity_id)  # metadata of your latest activity
    >>> activity.get_data(latest_activity_id)  # processed FIT file data


World
+++++

::

    >>> world = client.get_world(1)  # get world with id 1
    >>> world.players  # players currently present in this world
    >>> world.player_status(player_id) # current player status information like speed, cadence, power, etc.


Credits
---------

.. _zwift-client: https://github.com/jsmits/zwift-client


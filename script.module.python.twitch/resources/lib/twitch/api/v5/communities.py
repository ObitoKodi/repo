# -*- encoding: utf-8 -*-
"""
    Reference: https://dev.twitch.tv/docs/v5/reference/communities/

    Copyright (C) 2016-2018 script.module.python.twitch

    This file is part of script.module.python.twitch

    SPDX-License-Identifier: GPL-3.0-only
    See LICENSES/GPL-3.0-only for more information.
"""

from ... import keys, methods
from ...api.parameters import Cursor
from ...queries import V5Query as Qry
from ...queries import query


# required scope: none
@query
def by_name(name):
    q = Qry('communities', use_token=False)
    q.add_param(keys.NAME, name)
    return q


# required scope: none
@query
def by_id(community_id):
    q = Qry('communities/{community_id}', use_token=False)
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    return q


# required scope: communities_edit
@query
def update(community_id, summary=None, description=None,
           rules=None, email=None):
    q = Qry('communities/{community_id}', method=methods.PUT)
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    q.add_data(keys.SUMMARY, summary)
    q.add_data(keys.DESCRIPTION, description)
    q.add_data(keys.RULES, rules)
    q.add_data(keys.EMAIL, email)
    return q


# required scope: none
@query
def get_top(limit=10, cursor='MA=='):
    q = Qry('communities/top', use_token=False)
    q.add_param(keys.LIMIT, limit, 10)
    q.add_param(keys.CURSOR, Cursor.validate(cursor), 'MA==')
    return q


# required scope: communities_moderate
@query
def get_bans(community_id, limit=10, cursor='MA=='):
    q = Qry('communities/{community_id}/bans')
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    q.add_param(keys.LIMIT, limit, 10)
    q.add_param(keys.CURSOR, Cursor.validate(cursor), 'MA==')
    return q


# required scope: communities_moderate
@query
def ban_user(community_id, user_id):
    q = Qry('communities/{community_id}/bans/{user_id}', method=methods.PUT)
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    q.add_urlkw(keys.USER_ID, user_id)
    return q


# required scope: communities_moderate
@query
def unban_user(community_id, user_id):
    q = Qry('communities/{community_id}/bans/{user_id}', method=methods.DELETE)
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    q.add_urlkw(keys.USER_ID, user_id)
    return q


# required scope: communities_edit
@query
def create_avatar(community_id, avatar_image):
    q = Qry('communities/{community_id}/images/avatar', method=methods.POST)
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    q.add_urlkw(keys.AVATAR_IMAGE, avatar_image)
    return q


# required scope: communities_edit
@query
def delete_avatar(community_id):
    q = Qry('communities/{community_id}/images/avatar', method=methods.DELETE)
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    return q


# required scope: communities_edit
@query
def create_cover(community_id, cover_image):
    q = Qry('communities/{community_id}/images/cover', method=methods.POST)
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    q.add_urlkw(keys.COVER_IMAGE, cover_image)
    return q


# required scope: communities_edit
@query
def delete_cover(community_id):
    q = Qry('communities/{community_id}/images/cover', method=methods.DELETE)
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    return q


# required scope: communities_edit
@query
def get_moderators(community_id):
    q = Qry('communities/{community_id}/moderators')
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    return q


# required scope: communities_edit
@query
def add_moderator(community_id, user_id):
    q = Qry('communities/{community_id}/moderators/{user_id}', method=methods.PUT)
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    q.add_urlkw(keys.USER_ID, user_id)
    return q


# required scope: communities_edit
@query
def delete_moderator(community_id, user_id):
    q = Qry('communities/{community_id}/moderators/{user_id}', method=methods.DELETE)
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    q.add_urlkw(keys.USER_ID, user_id)
    return q


# required scope: any
@query
def get_permissions(community_id):
    q = Qry('communities/{community_id}/permissions')
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    return q


# required scope: none
@query
def report_violation(community_id, channel_id):
    q = Qry('communities/{community_id}/report_channel', use_token=False, method=methods.POST)
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    q.add_data(keys.CHANNEL_ID, channel_id)
    return q


# required scope: communities_moderate
@query
def get_timeouts(community_id, limit=10, cursor='MA=='):
    q = Qry('communities/{community_id}/timeouts')
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    q.add_param(keys.LIMIT, limit, 10)
    q.add_param(keys.CURSOR, Cursor.validate(cursor), 'MA==')
    return q


# required scope: communities_moderate
@query
def add_timeout(community_id, user_id, duration=1, reason=None):
    q = Qry('communities/{community_id}/timeouts/{user_id}', method=methods.PUT)
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    q.add_urlkw(keys.USER_ID, user_id)
    q.add_data(keys.DURATION, duration)
    q.add_data(keys.REASON, reason)
    return q


# required scope: communities_moderate
@query
def delete_timeout(community_id, user_id):
    q = Qry('communities/{community_id}/timeouts/{user_id}', method=methods.DELETE)
    q.add_urlkw(keys.COMMUNITY_ID, community_id)
    q.add_urlkw(keys.USER_ID, user_id)
    return q

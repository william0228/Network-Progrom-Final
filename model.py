from peewee import *
from playhouse.migrate import SqliteMigrator, migrate

db = SqliteDatabase('database.db', pragmas={'foreign_keys': 1})


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()


class Invitation(BaseModel):
    inviter = ForeignKeyField(User, related_name='inviter', on_delete='CASCADE')
    invitee = ForeignKeyField(User, related_name='invitee', on_delete='CASCADE')


class Friend(BaseModel):
    user = ForeignKeyField(User, related_name='friend_user', on_delete='CASCADE')
    friend = ForeignKeyField(User, related_name='friend', on_delete='CASCADE')


class Post(BaseModel):
    user = ForeignKeyField(User, related_name='post_user', on_delete='CASCADE')
    message = CharField()


class Follow(BaseModel):
    follower = ForeignKeyField(User, related_name='follower', on_delete='CASCADE')
    followee = ForeignKeyField(User, related_name='followee', on_delete='CASCADE')


class Token(BaseModel):
    token = CharField(unique=True)
    owner = ForeignKeyField(User, related_name='token_owner', on_delete='CASCADE')

class Group(BaseModel):
    group_name = CharField(unique=False)
    member = ForeignKeyField(User, related_name='group_member', on_delete='CASCADE')

if __name__ == '__main__':

    db.connect()
    db.create_tables([User, Invitation, Friend, Post, Follow, Token, Group])
    
    migrator = SqliteMigrator(db)
    

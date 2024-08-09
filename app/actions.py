from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow
from django.contrib.auth.models import User, ContentType, Group, Permission

from .ui import PermissionEditWindow, UserEditWindow



class UserPack(ObjectPack):
    model = User
    add_to_menu = True
    can_delete = True
    add_window = edit_window = UserEditWindow



class ContentTypePack(ObjectPack):
    model = ContentType
    can_delete = True
    add_to_menu = False   # не добавляем в меню
    add_window = edit_window = ModelEditWindow.fabricate(model)


class GroupPack(ObjectPack):
    model = Group
    add_to_menu = True
    can_delete = True
    add_window = edit_window = ModelEditWindow.fabricate(model)


class PermissionPack(ObjectPack):
    model = Permission
    add_to_menu = True
    can_delete = True
    add_window = edit_window = PermissionEditWindow


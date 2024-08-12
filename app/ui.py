from django.contrib.contenttypes.models import ContentType
from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext


class PermissionEditWindow(BaseEditWindow):
    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(PermissionEditWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'Название',
            name='name',
            allow_blank=False,
            anchor='100%'
        )
        self.field__codename = ext.ExtStringField(
            label=u'Кодовое имя',
            name='codename',
            allow_blank=False,
            anchor='100%'
        )

        # Получаем список ContentType
        content_type = ContentType.objects.all()
        data = [(ct.id, ct.name) for ct in content_type]

        # Создаем ComboBox с помощью make_combo_box
        self.field__content_type = make_combo_box(
            label=u'Выберите тип контента',
            name='content_type_id',
            allow_blank=False,
            anchor='100%',
            data=data,
        )


    def _do_layout(self):
        """
        Здесь следует размещать компоненты в окне
        """
        super(PermissionEditWindow, self)._do_layout()
        self.form.items.extend([
            self.field__name,
            self.field__codename,
            self.field__content_type
        ])

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака

        """
        super(PermissionEditWindow, self).set_params(params)
        self.height = 'auto'


class UserEditWindow(BaseEditWindow):
    def _init_components(self):
        super(UserEditWindow, self)._init_components()

        # Поля, аналогичные фабричному способу
        self.field__username = ext.ExtStringField(
            label=u'Имя пользователя',
            name='username',
            allow_blank=False,
            anchor='100%'
        )
        self.field__first_name = ext.ExtStringField(
            label=u'Имя',
            name='first_name',
            allow_blank=False,
            anchor='100%'
        )
        self.field__last_name = ext.ExtStringField(
            label=u'Фамилия',
            name='last_name',
            allow_blank=False,
            anchor='100%'
        )
        self.field__email = ext.ExtStringField(
            label=u'Email',
            name='email',
            allow_blank=False,
            anchor='100%',
            regex='[^@]+@[^@]+\.[^@]+',
            regex_text='Неверный адрес электронной почты'
        )
        self.field__is_staff = ext.ExtCheckBox(
            label=u'Администратор',
            name='is_staff',
            anchor='100%',
            allow_blank=False,
        )
        self.field__is_active = ext.ExtCheckBox(
            label=u'Активен',
            name='is_active',
            allow_blank=False,
            anchor='100%'
        )
        self.field__is_superuser = ext.ExtCheckBox(
            label=u'Суперпользователь',
            name='is_superuser',
            allow_blank=False,
            anchor='100%'
        )
        self.field__last_login = ext.ExtDateField(
            label=u'Последний вход',
            name='last_login',
            format='d.m.Y',
            allow_blank=False,
            anchor='100%'
        )
        self.field__date_joined = ext.ExtDateField(
            label=u'Дата регистрации',
            name='date_joined',
            format='d.m.Y',
            anchor='100%',
        )
        self.field__password = ext.ExtStringField(
            label=u'Пароль',
            name='password',
            input_type='password',
            allow_blank=False,
            anchor='100%'
        )

    def _do_layout(self):
        super(UserEditWindow, self)._do_layout()
        self.form.items.extend([
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_staff,
            self.field__is_active,
            self.field__is_superuser,
            self.field__last_login,
            self.field__date_joined,
            self.field__password
        ])

    def set_params(self, params):
        super(UserEditWindow, self).set_params(params)
        self.height = 'auto'

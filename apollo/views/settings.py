#-*- coding: utf-8 -*-

from bottle import request, redirect

from share.framework.bottle import MethodView, view, render_template
from share.framework.bottle.engines import db
from share.url_map import url_for

from apollo.models import UserModel
from .forms import UserSettingForm


class SettingsView(MethodView):
    @view('settings.html')
    def get(self, ukey):
        user = UserModel.query.get(ukey)
        form = UserSettingForm(obj=user)
        return {
            'user': user,
            'form': form
        }

    def post(self, ukey):
        user = UserModel.query.get(ukey)

        print request.forms.get('birthday')
        form = UserSettingForm(request.forms)
        if not form.validate():
            return render_template('settings.html', user=user, form=form)

        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for('apollo:www.main'))

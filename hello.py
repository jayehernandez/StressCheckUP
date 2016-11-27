from flask import Flask, render_template, request
from flask_wtf import Form
from wtforms import StringField, IntegerField, BooleanField, RadioField
from wtforms.validators import InputRequired

import stresscheck

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'Yes'

class InputForm(Form):
	# name = StringField('name', validators=[InputRequired()])
	anx = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	dep = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	moo = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	res = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	mot = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	fru = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	ind = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	foc = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	ove = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	irr = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	des = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	con = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	hig = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	nau = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	hea = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	ble = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	slu = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	exh = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	fee = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	med = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	isp = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	iep = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	exc = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])
	esc = RadioField(choices=[('Yes','Yes'),('No','No')], validators=[InputRequired()])

@app.route('/', methods=['GET','POST'])
def index():
	form = InputForm()
	array = []
	if form.validate_on_submit():
		array = [form.anx.data, form.dep.data, form.moo.data, form.res.data, form.mot.data, form.fru.data, form.ind.data, form.foc.data, form.ove.data, form.irr.data, form.des.data, form.con.data, form.hig.data, form.nau.data, form.hea.data, form.ble.data, form.slu.data, form.exh.data, form.fee.data, form.med.data, form.isp.data, form.iep.data, form.exc.data, form.esc.data]
		print array
		array = [1 if x == 'Yes' else 0 for x in array]
		print array
		result = stresscheck.Predicting(array)
		# stresscheck.Testing()
		# dito yung sa tree
		# aadd sa csv yung data
		return render_template('main.html', result=result)
	else:
		print form.dep.data
	return render_template('index.html', form=form)

@app.route('/project')
def project():
	return render_template('project.html')

@app.route('/facts')
def facts():
	return render_template('facts.html')

@app.route('/test')
def test():
	return render_template('test.html')

@app.route('/main')
def main():
	result="Stressed"
	return render_template('main.html', result=result)

if __name__ == '__main__':
	app.run(debug=True)
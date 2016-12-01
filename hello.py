from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import Form
from wtforms import SubmitField, RadioField
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

class addForm(Form):
	yes = SubmitField('Yes')
	no = SubmitField('No')

class noForm(Form):
	tru = RadioField(choices=[('Stressed','Stressed'),('Burnout', 'Burnout'),('Fatigue', 'Fatigue'),('Normal','Normal')], validators=[InputRequired()])

@app.route('/', methods=['GET','POST'])
def index():
	form = InputForm()
	array = []
	if form.validate_on_submit():
		array = [form.anx.data, form.dep.data, form.moo.data, form.res.data, form.mot.data, form.fru.data, form.ind.data, form.foc.data, form.ove.data, form.irr.data, form.des.data, form.con.data, form.hig.data, form.nau.data, form.hea.data, form.ble.data, form.slu.data, form.exh.data, form.fee.data, form.med.data, form.isp.data, form.iep.data, form.exc.data, form.esc.data]
		arr = ""
		arr = ','.join(array)
		array = [1 if x == 'Yes' else 0 for x in array]
		result = stresscheck.Predicting(array)
		return redirect(url_for('main', result=result, arr=arr))
	return render_template('index.html', form=form)

@app.route('/project')
def project():
	return render_template('project.html')

@app.route('/facts')
def facts():
	return render_template('facts.html')


@app.route('/main', methods=['GET', 'POST'])
def main():
	form = addForm()
	if request.method == 'POST':
		arr = request.args.get('arr')
		print arr
		arr = arr.split(',')
		arr = [1 if x == 'Yes' else 0 for x in arr]
		print arr
		if 'yes' in request.form:
			stresscheck.unitTestWrite(arr, 1, request.args.get('result'), request.args.get('result'))
			return redirect(url_for('yes', result=request.args.get('result')))
		elif 'no' in request.form:
			return redirect(url_for('no', result=request.args.get('result'), array=request.args.get('arr')))
	return render_template('main.html', result=request.args.get('result'), form=form)

@app.route('/yes', methods=['GET', 'POST'])
def yes():
	return render_template('yes.html', result=request.args.get('result'))

@app.route('/no', methods=['GET', 'POST'])
def no():
	form = noForm()
	if form.validate_on_submit():
		print form.tru.data
		arr = request.args.get('array')
		print arr
		arr = arr.split(',')
		arr = [1 if x == 'Yes' else 0 for x in arr]
		stresscheck.unitTestWrite(arr, 0, request.args.get('result'), form.tru.data)
		return redirect(url_for('yes', result=request.args.get('result')))
	return render_template('no.html', result=request.args.get('result'), form=form)


if __name__ == '__main__':
	app.run(debug=True)
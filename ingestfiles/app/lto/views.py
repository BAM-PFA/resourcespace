#!/usr/bin/env python3
# standard library modules
# import getpass
import json
import os
import re
import subprocess
import sys
import urllib
import uuid
# non-standard libraries
import wtforms
from flask import render_template, url_for, request, redirect, jsonify
from werkzeug import MultiDict
# local modules
from . import lto
from . import forms
from .. import listObjects
from .. import utils

@lto.route('/lto_menu',methods=['GET','POST'])
def lto_menu():
	return render_template(
		'lto_menu.html',
		title='LTO MENU'
		)


@lto.route('/format_lto',methods=['GET','POST'])
def format_lto():
	currentLTOid = utils.get_current_LTO_id()

	formatLTO = forms.format_form()

	return render_template(
		'format_lto.html',
		title="Format LTO",
		formatForm=formatLTO,
		currentLTOid=currentLTOid
		)

@lto.route('/format_status',methods=['GET','POST'])
def format_status():
	# we are using SCSI (SAS) attached drives in linux so I'll defalt the 
	# device names to nst0 and nst1, which are the non-auto-rewind device 
	# names
	linuxDevices = utils.get_devices()

	statuses = {
		"/dev/nst0":False,
		"/dev/nst1":False
	}

	for device,tapeID in linuxDevices.items():
		MKLTFS = [
		'mkltfs',
		'--device={}'.format(device),
		'--tape-serial={}'.format(tapeID),
		'--volume-name={}'.format(tapeID)
		]

		try:
			out, err = subprocess.Popen(
				MKLTFS,
				stdout=subprocess.PIPE
				).communicate()
			statuses[device] = True
			print(out)
			if not "LTFS15047E" in out:
				statuses[device] = True
			else:
				statuses[device] = "can't format tape, maybe it's already formatted"

		except:
			statuses[device] = "there was an error in the LTFS command execution... meh?"


	return render_template(
		'format_status.html',
		statuses=statuses
		)

@lto.route('/lto_id',methods=['GET','POST'])
def lto_id():
	newLTOid = forms.LTO_id_form()

	return render_template(
		'lto_id.html',
		title='Create LTO ID',
		IDform=newLTOid,
		)

@lto.route('/lto_id_status',methods=['GET','POST'])
def lto_id_status():
	tapeIdRegex = re.compile(r'^((\d{4}[A-Z]A)|(\d{5}A))$')
	ltoIDstatus = False
	try:
		_data = request.form.to_dict(flat=False)
		ltoID = request.form['tapeAid']
		if re.match(tapeIdRegex,ltoID):
			with open(ltoIdFilePath,'w') as idfile:
				idfile.write(ltoID)
			ltoIDstatus = True
		else:
			ltoIDstatus = False
	except:
		_data = 'none'
		ltoID = 'none'

	return render_template(
		'lto_id_status.html',
		ltoID=ltoID,
		title="LTO ID status",
		ltoIDstatus = ltoIDstatus
		)

@lto.route('/mount_lto',methods=['GET','POST'])
def mount_lto():
	mountEmUp = forms.mount()

	return render_template(
		'mount_lto.html',
		title="Mount LTO tapes",
		mountForm=mountEmUp
		)


@lto.route('/mount_status',methods=['GET','POST'])
def mount_status():
	linuxDevices = utils.get_devices()
	statuses = {}
	userId = os.getegid()
	tempDir = utils.get_temp_dir()

	for device, tape in linuxDevices.items():
		mountpoint = os.path.join(tempDir,tape)
		try:
			subprocess.call(['mkdir',mountpoint])
		except:
			print("can't make the mount point... check yr permissions")

		LTFS = [
		'ltfs','-f',
		'-o','work_directory={}'.format(tempDir),
		'-o','noatime',
		'-o','capture_index',
		'-o','devname={}'.format(device),
		'-o','uid={}'.format(userId),
		mountpoint
		]

		try:
			out,err = subprocess.Popen(LTFS,stdout=subprocess.PIPE).communicate()
			statuses[tape] = 'mounted, ready to go'
		except:
			statuses[tape] = 'there was an error in the LTFS command'

	return render_template(
		'mount_status.html',
		title="LTO Mount Status",
		statuses=statuses
		)






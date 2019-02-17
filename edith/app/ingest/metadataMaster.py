#!/usr/bin/env python3
# local imports
from config import app_config
from .. import db
from ..models import Metadata_Field



metadataMasterDict = {}

metadataMasterDict['tags'] = ''
metadataMasterDict['country'] = ''
metadataMasterDict['title'] = ''
metadataMasterDict['nameSubjects'] = ''
metadataMasterDict['frameRateProxy'] = ''
metadataMasterDict['altTitle'] = ''
metadataMasterDict['releaseYear'] = ''
metadataMasterDict['accPref'] = ''
metadataMasterDict['accDepos'] = ''
metadataMasterDict['accItem'] = ''
metadataMasterDict['accFull'] = ''
metadataMasterDict['projGrp'] = ''
metadataMasterDict['directorsNames'] = ''
metadataMasterDict['credits'] = ''
metadataMasterDict['generalNotes'] = ''
metadataMasterDict['conditionNote'] = ''
metadataMasterDict['Barcode'] = ''
metadataMasterDict['language'] = ''
metadataMasterDict['soundCharacteristics'] = ''
metadataMasterDict['color'] = ''
metadataMasterDict['runningTime'] = ''
metadataMasterDict['medium'] = ''
metadataMasterDict['dimensions'] = ''
metadataMasterDict['videoFormat'] = ''
metadataMasterDict['videoStandard'] = ''
metadataMasterDict['ingestUUID'] = ''
metadataMasterDict['eventTitle'] = ''
metadataMasterDict['eventYear'] = ''
metadataMasterDict['eventFullDate'] = ''
metadataMasterDict['eventSeries'] = ''
metadataMasterDict['eventRelatedExhibition'] = ''
metadataMasterDict['eventLocation'] = ''
metadataMasterDict['description'] = ''
metadataMasterDict['creator'] = ''
metadataMasterDict['creatorRole'] = ''
metadataMasterDict['eventOrganizer'] = ''
metadataMasterDict['assetExternalSource'] = ''
metadataMasterDict['copyrightStatement'] = ''
metadataMasterDict['restrictionsOnUse'] = ''
metadataMasterDict['generation'] = ''
metadataMasterDict['frameRateTRTdetails'] = ''
metadataMasterDict['platformOutlet'] = ''
metadataMasterDict['editSequenceSettings'] = ''
metadataMasterDict['additionalCredits'] = ''
metadataMasterDict['postProcessing'] = ''
metadataMasterDict['exportPublishDate'] = ''
metadataMasterDict['PFAfilmSeries'] = ''
metadataMasterDict['recordingDate'] = ''
metadataMasterDict['digitizedBornDigital'] = ''
metadataMasterDict['digitizer'] = ''
metadataMasterDict['locationOfRecording'] = ''
metadataMasterDict['speakerInterviewee'] = ''
metadataMasterDict['filmTitleSubjects'] = ''
metadataMasterDict['topicalSubjects'] = ''
metadataMasterDict['recordingAnalogTechnicalNotes'] = ''
metadataMasterDict['audioRecordingID'] = ''
metadataMasterDict['recordingPermissionsNotes'] = ''
metadataMasterDict['analogTapeNumber'] = ''
metadataMasterDict['analogTapeSide'] = ''
metadataMasterDict['digitizationQCNotes'] = ''

# metadataMasterDict[''] = ''

metadataMasterDict['hasBAMPFAmetadata'] = ""

class Metadata:
	'''
	Metadata instance for an asset being ingested
	'''
	def __init__(self):
		self.metadataDict = {}
		self.available_metadataSources = db.session.query(Metadata_Field).all()
		for fieldName in self.available_metadataSources:
			print(fieldName.data)




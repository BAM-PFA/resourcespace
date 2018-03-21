import pbcore_elements


pbCoreIntelContentAndProp = []
for item in list(pbcore_elements.INTELLECTUAL_CONTENT_ELEMENTS.keys()):
	pbCoreIntelContentAndProp.append(item)
for item in list(pbcore_elements.INTELLECTUAL_PROPERTY_ELEMENTS.keys()):
	pbCoreIntelContentAndProp.append(item)

PBCORE_MAP = {
	"accFull":{
		"instantiationIdentifier":{
			"LEVEL":"INSTANTIATION",
			"source":"PFA accession number",
			"TEXT":"value"
		}
	},
	"title":{
		"pbcoreTitle":{
			"LEVEL":"WORK",
			"titleType":"Main",
			"TEXT":"value"
		}
	},
	"altTitle":{
		"pbcoreTitle":{
			"LEVEL":"WORK",
			"titleType":"Alternative Main",
			"TEXT":"value"
		}
	},
	"releaseYear":{
		"pbcoreAssetDate":{
			"LEVEL":"WORK",
			"dateType":"Released",
			"TEXT":"value"
		}
	},
	"conditionNote":{
		"essenceTrackAnnotation":{
			"LEVEL":"INSTANTIATION",
			"annotationType":"Condition note",
			"TEXT":"value"
		}
	},
	"country":{
		"coverage":{
			"LEVEL":"WORK",
			"TEXT":"value",
			"SIBLING_FIELD":{
				"coverageType":{
					"ref":"http://metadataregistry.org/concept/show/id/2522.html",
					"TEXT":"Spatial"
				}
			}
		}
	},
	"directorsNames":{
		"pbcoreCreator":{
			"LEVEL":"WORK",
			"TEXT":"",
			"SUBELEMENT":{
				"creator":{
					"TEXT":"value"
				}
			},
			"SUBELEMENT":{
				"creatorRole":{
					"source":"PBCore creatorRole",
					"ref":"http://metadataregistry.org/concept/show/id/1303.html",
					"TEXT":"Director(s)"
				}
			}
			
		}
	},
	"Barcode":{
		"instantiationIdentifier":{
			"LEVEL":"INSTANTIATION",
			"source":"PFA barcode",
			"TEXT":"value"
		}
	},
	"generalNotes":{
		"essenceTrackAnnotation":{
			"LEVEL":"INSTANTIATION",
			"annotationType":"General note",
			"TEXT":"value"
		}
	},
	"credits":{
		"pbcoreRightsSummary":{
			"LEVEL":"WORK",
			"TEXT":"",
			"SUBELEMENT":{
				"rightsSummary":{
					"annotation":"Credits statement",
					"TEXT":"value"
				}
			}
		}
	},
	"projGrp":{
		"pbcoreRelation":{
			"LEVEL":"INSTANTIATION",
			"ATTRIBUTE":"DEFAULT_VALUE",
			"TEXT":"Null",
			"SUBELEMENT":{
				"PBCORE_FIELD":{
					"ATTRIBUTE":"DEFAULT_VALUE",
					"TEXT":"Null"
				}
			},
			"SIBLING_FIELD":{
				"PBCORE_FIELD":{
					"ATTRIBUTE":"DEFAULT_VALUE"
				}
			}
		}
	},
	"BAMPFA_FIELD":{
		"PBCORE_FIELD":{
			"LEVEL":"WORK_OR_INSTANTIATION",
			"ATTRIBUTE":"DEFAULT_VALUE",
			"TEXT":"Null",
			"SUBELEMENT":{
				"PBCORE_FIELD":{
					"ATTRIBUTE":"DEFAULT_VALUE",
					"TEXT":"Null"
				}
			},
			"SIBLING_FIELD":{
				"PBCORE_FIELD":{
					"ATTRIBUTE":"DEFAULT_VALUE"
				}
			}
		}
	},
	"BAMPFA_FIELD":{
		"PBCORE_FIELD":{
			"LEVEL":"WORK_OR_INSTANTIATION",
			"ATTRIBUTE":"DEFAULT_VALUE",
			"TEXT":"Null",
			"SUBELEMENT":{
				"PBCORE_FIELD":{
					"ATTRIBUTE":"DEFAULT_VALUE",
					"TEXT":"Null"
				}
			},
			"SIBLING_FIELD":{
				"PBCORE_FIELD":{
					"ATTRIBUTE":"DEFAULT_VALUE"
				}
			}
		}
	},
	"BAMPFA_FIELD":{
		"PBCORE_FIELD":{
			"LEVEL":"WORK_OR_INSTANTIATION",
			"ATTRIBUTE":"DEFAULT_VALUE",
			"TEXT":"Null",
			"SUBELEMENT":{
				"PBCORE_FIELD":{
					"ATTRIBUTE":"DEFAULT_VALUE",
					"TEXT":"Null"
				}
			},
			"SIBLING_FIELD":{
				"PBCORE_FIELD":{
					"ATTRIBUTE":"DEFAULT_VALUE"
				}
			}
		}
	},
	"BAMPFA_FIELD":{
		"PBCORE_FIELD":{
			"LEVEL":"WORK_OR_INSTANTIATION",
			"ATTRIBUTE":"DEFAULT_VALUE",
			"TEXT":"Null",
			"SUBELEMENT":{
				"PBCORE_FIELD":{
					"ATTRIBUTE":"DEFAULT_VALUE",
					"TEXT":"Null"
				}
			},
			"SIBLING_FIELD":{
				"PBCORE_FIELD":{
					"ATTRIBUTE":"DEFAULT_VALUE"
				}
			}
		}
	},
	"BAMPFA_FIELD":{
		"PBCORE_FIELD":{
			"LEVEL":"WORK_OR_INSTANTIATION",
			"ATTRIBUTE":"DEFAULT_VALUE",
			"TEXT":"Null",
			"SUBELEMENT":{
				"PBCORE_FIELD":{
					"ATTRIBUTE":"DEFAULT_VALUE",
					"TEXT":"Null"
				}
			},
			"SIBLING_FIELD":{
				"PBCORE_FIELD":{
					"ATTRIBUTE":"DEFAULT_VALUE"
				}
			}
		}
	}
}

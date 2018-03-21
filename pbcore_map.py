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
		"instantiationAnnotation":{
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
		"instantiationAnnotation":{
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
		"instantiationExtension":{
			"LEVEL":"INSTANTIATION",
			"TEXT":"",
			"SUBELEMENT":{
				"extensionWrap":{
					"TEXT":"",
					"SUBELEMENT":{
						"extensionElement":{
							"TEXT":"isPartOf"
						}
					},
					"SUBELEMENT":{
						"extensionValue":{
							"TEXT":"value"
						}
					},
					"SUBELEMENT":{
						"extensionAuthorityUsed":{
							"TEXT":"DCMI Metadata Terms"
						}
					}
				}
			}
		}
	},
	"ingestUUID":{
		"instantiationAnnotation":{
			"LEVEL":"INSTANTIATION",
			"annotationType":"PFA ingest process unique identifier",
			"TEXT":"value"
		}
	},
	"BAMPFAlocation":{
		"instantiationLocation":{
			"LEVEL":"INSTANTIATION",
			"annotation":"may either be 'BAMPFA Digital Repository or LTO Tape ID",
			"TEXT":"value"
		}
	},
	"eventTitle":{
		"pbcoreTitle":{
			"LEVEL":"WORK",
			"titleType":"Event",
			"titleTypeAnnotation":"BAMPFA metadata definition",
			"TEXT":"value"
		}
	},
	"eventYear":{
		"pbcoreAssetDate":{
			"LEVEL":"WORK",
			"dateType":"Event",
			"annotation":"Year of a recorded event. Describes BAMPFA non-collection assets.",
			"TEXT":"value"
		}
	},
	"eventFullDate":{
		"pbcoreAssetDate":{
			"LEVEL":"WORK",
			"dateType":"Event",
			"annotation":"Full date of a recorded event. Describes BAMPFA non-collection assets.",
			"TEXT":"value"
		}
	},
	"generation":{
		"instantiationGenerations":{
			"LEVEL":"INSTANTIATION",
			"source":"BAMPFA controlled vocabulary",
			"TEXT":"value"
		}
	},
	"language":{
		"instantiationLanguage":{
			"LEVEL":"INSTANTIATION",
			"source":"IS0 639.2",
			"ref":"",
			"TEXT":"value"
		}
	},
	"soundCharacteristics":{
		"instantiationAnnotation":{
			"LEVEL":"INSTANTIATION",
			"annotation":"Sound or silent",
			"TEXT":"value"
		}
	},
	"colorCharacteristics":{
		"instantiationColors":{
			"LEVEL":"INSTANTIATION",
			"source":"BAMPFA controlled vocabulary",
			"TEXT":"value"
		}
	},
	"runningTime":{
		"instantiationDuration":{
			"LEVEL":"INSTANTIATION",
			"annotation":"May be specific to BAMPFA projectors, scan rates, etc.",
			"TEXT":"value"
		}
	},
	"medium":{
		"instantiationMediaType":{
			"LEVEL":"INSTANTIATION",
			"source":"BAMPFA controlled vocabulary",
			"annotation":"BAMPFA source material medium.",
			"TEXT":"value"
		}
	},
	"dimensions":{
		"instantiationDimensions":{
			"LEVEL":"INSTANTIATION",
			"source":"BAMPFA controlled vocabulary",
			"TEXT":"value"
		}
	},
	"videoFormat":{
		"instantiationPhysical":{
			"LEVEL":"INSTANTIATION",
			"source":"BAMPFA controlled vocabulary",
			"TEXT":"Null"
		}
	},
	"videoStandard":{
		"instantiationStandard":{
			"LEVEL":"INSTANTIATION",
			"source":"PBCore instantiationStandard/video",
			"ref":"http://pbcore.org/vocabularies/instantiationStandard/video%23ntsc",
			"TEXT":"vale"
		}
	},
	"BAMPFA_FIELD":{
		"PBCORE_ELEMENT":{
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

BAMPFA_FIELDS = list(PBCORE_MAP.keys())
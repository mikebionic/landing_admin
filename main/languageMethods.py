from flask import session
from main.config import Config

# session = {
# 	"language": 'en'
# }

dbLanguages = {
	"en": 'enUS',
	"ru": 'ruRU',
	"tk": 'tkTM'
}

def dataLangSelector(DictObject):
	try:
		language = session['language'] if 'language' in session else 'tk'
	except:
		language = Config.BABEL_DEFAULT_LOCALE
	convertedJSON = {}

	try:
		if not DictObject:
			raise Exception

		for data in DictObject:
			splittedData = data.split('_')
			if (len(splittedData) > 1) and splittedData[1] == language:
				convertedJSON[splittedData[0]] = DictObject[data]
			if not len(splittedData) > 1:
				convertedJSON[splittedData[0]] = DictObject[data]
	
	except Exception as ex:
		return None
	
	return convertedJSON

## example usage:

# json_usage_status = {
# 	"UsageStatusName_tkTM": 'Plan zat',
# 	"UsageStatusDesc_tkTM": 'Plan zat descr',
# 	"UsageStatusName_ruRU": 'kakaya to vesh',
# 	"UsageStatusDesc_ruRU": 'kakava to vesh desc',
# 	"UsageStatusName_enUS": "some thing",
# 	"UsageStatusDesc_enUS": 'some thing desc',
# 	"CreatedDate": '12.12.2012',
# 	"ModifiedDate": '12.12.2012',
# 	"CreatedUId": 1,
# 	"ModifiedUId": 1,
# 	"GCRecord": None
# 	}

# dataLangSelector(json_usage_status)
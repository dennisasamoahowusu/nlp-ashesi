from custom_actions.action_fees import ActionFees
from custom_actions.action_greet import ActionGreetUser
from custom_actions.action_courses import ActionCourses
from custom_actions.action_admission import ActionAdmissions
from custom_actions.action_offices import ActionOffices
from custom_actions.action_application import ActionApplication
from custom_actions.action_scholarships import ActionScholarships
from custom_actions.action_about_ashesi import ActionAboutAshesi
from custom_actions.action_affirmative_negative import ActionAffirmitiveNegative
from custom_actions.action_bye import ActionSayBye
from custom_actions.action_masters import ActionGraduateProgram
from custom_actions.action_ashesi_education import ActionEducation
from custom_actions.action_ashesi_location import ActionLocation
from custom_actions.action_majors import ActionMajors
##IMPORT POSTGRESS DB
from libraries.postgres import PostGres


class ActionsService():
	"""docstring for ActionsService"""
	def __init__(self):
		self.postgres = PostGres()
		self.action_fees = ActionFees()
		self.action_greet = ActionGreetUser()
		self.action_admission = ActionAdmissions()
		self.action_courses = ActionCourses()
		self.action_application = ActionApplication()
		self.action_offices  = ActionOffices()
		self.action_scholarships = ActionScholarships()
		self.action_about_ashesi = ActionAboutAshesi()
		self.action_affirmitive_negative = ActionAffirmitiveNegative()
		self.action_bye = ActionSayBye()
		self.action_masters = ActionGraduateProgram()
		self.action_ashesi_education = ActionEducation()
		self.action_ashesi_location = ActionLocation()
		self.action_majors = ActionMajors()

	def routeToIntent(self, intent, entity='blank'):
		if intent == "fees":
			return self.action_fees.makeFeesResponse(self.postgres, intent, entity)
		elif intent == "greet":
			return self.action_greet.greetUser()
		elif intent == "admission":
			return self.action_admission.makeAdmissionResponse(self.postgres, intent, entity)
		elif intent == "courses":
			return self.action_courses.makeCoursesResponse(self.postgres, intent, entity)
		elif intent == "offices":
			return self.action_offices.makeOfficesResponse(self.postgres, intent, entity)
		elif intent == "scholarships":
			return self.action_scholarships.makeScholarshipsResponse(self.postgres, intent, entity)
		elif intent == "application":
			return self.action_application.makeApplicationResponse(self.postgres, intent, entity)
		elif intent == "about_ashesi":
			return self.action_about_ashesi.makeAboutAshesiResponse(self.postgres, intent, entity)
		elif intent == "affirmative":
			return self.action_affirmitive_negative.makeAffirmativeNegative(intent)
		elif intent == "negative":
			return self.action_affirmitive_negative.makeAffirmativeNegative(intent)
		elif intent == "bye":
			return self.action_bye.makeByebyeResponse()
		elif intent == "masters":
			return self.action_masters.makegraduateResponse()
		elif intent == "ashesi_location":
			return self.action_ashesi_location.makeLocationResponse(self.postgres, intent, entity)
		elif intent == "ashesi_education":
			return self.action_ashesi_education.makeEducationResponse(self.postgres, intent, entity)
		elif intent == "majors":
			return self.action_majors.makeMajorsResponse(self.postgres, intent, entity)

			


		else:
			return "I'm not trained on this question"




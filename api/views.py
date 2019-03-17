from django.http import HttpResponse

json_data = """
{
	"cafeteria1": {
		"time": "10:00-21:00",
		"menu": {
			"category1": {
				"foodname1": {
					"price": 100,
					"carbo": 3,
					"proteins": 1,
					"fat": 5
				},
				"jeoulieoune": {
					"price": 123,
					"carbo": 51,
					"proteins": 48,
					"fat": 1
				}
			}
		}
	}
}
"""

def index(request):
    return HttpResponse(json_data)

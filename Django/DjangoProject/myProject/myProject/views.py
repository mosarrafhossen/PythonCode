from django.http import HttpResponse


def aboutUs(request):
    return HttpResponse("Welcome to Django Framework")

def contactUs(request):
    return HttpResponse("Mobile: 01700709716 and Email: xen.ict@wzpdcl.gov.bd")

#def contactDetails(request,officeId):
    #return HttpResponse(officeId)


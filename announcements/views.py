from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from announcements.models import Announcement


def dismiss(request, pk):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    
    announcement = get_object_or_404(Announcement, pk=pk)
    
    if announcement.dismissal_type == Announcement.DISMISSAL_SESSION:
        excluded = request.session.get("excluded_announcements", set())
        excluded.add(announcement.pk)
        request.session["excluded_announcements"] = excluded
        status = 200
    elif announcement.dismissal_type == Announcement.DISMISSAL_PERMANENT and request.user.is_authenticated():
        announcement.dismissals.create(user=request.user)
        status = 200
    else:
        status = 409
    
    return HttpResponse(status=status)


def detail(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    return TemplateResponse(request, "announcements/detail.html", {
        "announcement": announcement
    })

from datetime import date

from django.contrib import messages

from backend.service.reports.generate import generate_report
from backend.service.reports.get import get_report
from backend.types.requests import WebRequest
from django.shortcuts import render, redirect


def view_report_endpoint(request: WebRequest, uuid):
    report = get_report(request.actor, uuid)

    if report.failed:
        messages.error(request, report.error)
        return redirect("reports:dashboard")

    return render(request, "pages/reports/monthly_report_base.html", {"report": report.response})
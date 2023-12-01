from flask import Flask, render_template, request, redirect, url_for

class DerivedTables:
    def __init__(self, read_instance):
        self.read_instance = read_instance

    def householdinfo(self, request):
        if request.method == "POST":
            if "action" in request.form and request.form["action"] == "submit":
                householdno = request.form["householdno"]
                householdinfo = self.read_instance.read_householdinfo(householdno)
                return render_template("householdinfo.html", householdinfo=householdinfo)

        return render_template("householdinfo.html", householdinfo=[])

    def incomerecord(self, request):
        incomerecord = []  
        if request.method == "POST":
            if "action" in request.form and request.form["action"] == "submit":
                householdno = request.form["householdno"]
                incomerecord = self.read_instance.read_incomerecord(householdno)

        return render_template("incomerecord.html", incomerecord=incomerecord)

    def unemploymentinfo(self):
        unemploymentinfo = self.read_instance.read_unemploymentinfo()
        return render_template("unemploymentinfo.html", unemploymentinfo=unemploymentinfo)

    def scholarshipinfo(self):
        scholarshipinfo = self.read_instance.read_scholarshipinfo()
        return render_template("scholarshipinfo.html", scholarshipinfo=scholarshipinfo)

# registration.py
import os
from flask import request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

def save_file(file):
    upload_folder = "uploads"

    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    filename = os.path.join(upload_folder, secure_filename(file.filename))
    file.save(filename)
    return filename

def handle_accregistration(request, create_instance):
    print(request.form)
    if request.method == "POST":
        if "action" in request.form:
            if request.form["action"] == "create":
                barangayid = request.form["barangayid"]
                category = request.form["category"]
                lastname = request.form["lastname"]
                firstname = request.form["firstname"]
                middlename = request.form["middlename"]
                sex = request.form["sex"]
                birthdate = request.form["birthdate"]
                birthplace = request.form["birthplace"]
                religion = request.form["religion"]
                civilstat = request.form["civilstat"]
                citizenship = request.form["citizenship"]
                voterprecinct = request.form["voterprecinct"]
                contactno = request.form["contactno"]
                employmentstatus = request.form["employmentstatus"]
                monthlyincome = request.form["monthlyincome"]
                yearlevel = request.form["yearlevel"]
                school = request.form["school"]
                academicyear = request.form["academicyear"]
                scholarship = request.form["scholarship"]
                houseno = request.form["houseno"]
                zone = request.form["zone"]
                streetname = request.form["streetname"]
                city = request.form["city"]
                province = request.form["province"]
                bmiclassification = request.form["bmiclassification"]
                medicalcondition = request.form["medicalcondition"]
                covidvaccinated = request.form["covidvaccinated"]
                maintenancemedicine = request.form["maintenancemedicine"]
                physicalfitness = request.form["physicalfitness"]
                profile_picture = request.files['profile_picture']
                saved_filepath = save_file(profile_picture)
                if saved_filepath:
                    create_instance.create_residentinfo(barangayid, category, lastname, firstname, middlename, sex, birthdate,
                                                        birthplace, religion, civilstat, citizenship, voterprecinct, contactno,
                                                        saved_filepath)

                # Create instances for addressinfo, medicalinfo, adultinfo, studentinfo based on the selected category
                if category == "Adult":
                    create_instance.create_adultinfo(request.form["adult_barangayid"], employmentstatus, monthlyincome)
                    create_instance.create_addressinfo(request.form["address_barangayid"], houseno, zone, streetname, city, province)
                    create_instance.create_medicalinfo(request.form["medical_barangayid"], bmiclassification, medicalcondition, covidvaccinated, 
                                                    maintenancemedicine, physicalfitness)

                elif category == "Student":
                    create_instance.create_studentinfo(request.form["student_barangayid"], yearlevel, school, academicyear, scholarship)
                    create_instance.create_addressinfo(request.form["address_barangayid"], houseno, zone, streetname, city, province)
                    create_instance.create_medicalinfo(request.form["medical_barangayid"], bmiclassification, medicalcondition, covidvaccinated, 
                                                    maintenancemedicine, physicalfitness)
                elif category == "Others":
                    create_instance.create_addressinfo(request.form["address_barangayid"], houseno, zone, streetname, city, province)
                    create_instance.create_medicalinfo(request.form["medical_barangayid"], bmiclassification, medicalcondition, covidvaccinated, 
                                                    maintenancemedicine, physicalfitness)

                return redirect(url_for('accregistration'))

    return render_template("accregistration.html")

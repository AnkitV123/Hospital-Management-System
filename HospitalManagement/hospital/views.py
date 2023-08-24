from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login

# Create your views here.


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def Index(request):
    if not request.user.is_staff:
        return redirect("login")
    doctor = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()
    prescription = Prescription.objects.all()
    d = 0
    p = 0
    a = 0
    m = 0
    for i in doctor:
        d += 1
    for i in patient:
        p += 1
    for i in appointment:
        a += 1
    for i in prescription:
        m += 1
    d1 = {'d': d, 'p': p, 'a': a, 'm': m}
    return render(request, "index.html", d1)


def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST["uname"]
        p = request.POST["pwd"]
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, "login.html", d)


def logout_admin(request):
    if not request.user.is_staff:
        return redirect("login")
    logout(request)
    return redirect("login")


def view_doctor(request):
    if not request.user.is_staff:
        return redirect("login")
    doc = Doctor.objects.all()
    d = {"doc": doc}
    return render(request, "view_doctor.html", d)


def add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect("login")
    if request.method == "POST":
        n = request.POST["name"]
        d = request.POST["d_dob"]
        ema = request.POST["d_email"]
        mob = request.POST["mobile"]
        aad = request.POST["d_aadhar"]
        spc = request.POST["specialization"]
        qua = request.POST["qualification"]
        try:
            Doctor.objects.create(
                name=n,
                d_dob=d,
                d_email=ema,
                mobile=mob,
                d_aadhar=aad,
                specialization=spc,
                qualification=qua,
            )
            error = "no"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, "add_doctor.html", d)


def delete_doctor(request, pid):
    if not request.user.is_staff:
        return redirect("login")
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect("view_doctor")


def view_patient(request):
    if not request.user.is_staff:
        return redirect("login")
    pat = Patient.objects.all()
    d = {"pat": pat}
    return render(request, "view_patient.html", d)


def add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect("login")
    if request.method == "POST":
        reg = request.POST["rdate"]
        n = request.POST["pname"]
        g = request.POST["gender"]
        dob = request.POST["p_dob"]
        ema = request.POST["p_email"]
        add = request.POST["address"]
        mob = request.POST["mobile"]
        aad = request.POST["d_aadhar"]
        stat = request.POST["state"]
        city = request.POST["city"]
        bg = request.POST["blood"]
        dis = request.POST["disease"]
        try:
            Patient.objects.create(
                registrationDate=reg,
                name=n,
                gender=g,
                p_dob=dob,
                p_email=ema,
                address=add,
                mobile=mob,
                p_aadhar=aad,
                state=stat,
                city=city,
                bloodgroup=bg,
                disease=dis,
            )
            error = "no"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, "add_patient.html", d)


def delete_patient(request, pid):
    if not request.user.is_staff:
        return redirect("login")
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect("view_patient")


def view_appointment(request):
    if not request.user.is_staff:
        return redirect("login")
    appoint = Appointment.objects.all()
    d = {"appoint": appoint}
    return render(request, "view_appointment.html", d)


def add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect("login")
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method == "POST":
        d = request.POST["doctor"]
        p = request.POST["patient"]
        d1 = request.POST["date"]
        t = request.POST["time"]
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(
                doctor=doctor,
                patient=patient,
                date1=d1,
                time1=t,
            )
            error = "no"
        except:
            error = "yes"
    d = {'doctor': doctor1, 'patient': patient1, 'error': error}
    return render(request, "add_appointment.html", d)


def delete_appointment(request, pid):
    if not request.user.is_staff:
        return redirect("login")
    appointment = Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect("view_appointment")


def view_prescription(request):
    if not request.user.is_staff:
        return redirect("login")
    prescrip = Prescription.objects.all()
    d = {"prescrip": prescrip}
    return render(request, "view_prescription.html", d)


def add_prescription(request):
    error = ""
    if not request.user.is_staff:
        return redirect("login")
    patient1 = Patient.objects.all()
    if request.method == "POST":
        p = request.POST["patient"]
        m = request.POST["med"]
        dnd = request.POST["dnd"]
        patient = Patient.objects.filter(name=p).first()
        try:
            Prescription.objects.create(
                patient=patient,
                med=m,
                dnd=dnd,
            )
            error = "no"
        except:
            error = "yes"
    d = {'patient': patient1, 'error': error}
    return render(request, "add_prescription.html", d)


def delete_prescription(request, pid):
    if not request.user.is_staff:
        return redirect("login")
    prescription = Prescription.objects.get(id=pid)
    prescription.delete()
    return redirect("view_prescription")

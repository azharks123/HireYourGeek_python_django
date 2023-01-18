from django.shortcuts import redirect, render

from django.shortcuts import render, HttpResponseRedirect
import MySQLdb
import datetime
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import simplejson as json
from datetime import date
from datetime import datetime
import datetime
import webbrowser
import math
import random

db = MySQLdb.connect('localhost', 'root', '', 'dbhireyourgeek')
c = db.cursor()


def index(request):
    return render(request, 'index.html')


def adminhome(request):
    return render(request, 'adminhome.html')


def buyerhome(request):
    return render(request, 'buyerhome.html')


def coderhome(request):
    return render(request, 'coderhome.html')


def buyerreg(request):
    msg = ""
    if(request.POST):
        name = request.POST['name']
        address = request.POST['address']

        email = request.POST['email']
        phone = request.POST['contact']
        password = request.POST['pwd']
        m = "select count(*) count from tblbuyer where bemail='"+str(email)+"'"
        c.execute(m)

        i = c.fetchone()
        if(i[0] == 0):
            s = "insert into tblbuyer(bname,baddress,bemail,bcontact) values('" + \
                name+"','"+address+"','"+email+"','"+phone+"')"
            print(s)
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry registration error"
            else:
                s = "insert into tbllogin (uname,pwd,utype,status) values('" + \
                    email+"','"+password+"','buyer','0')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg = "Sorry some error occured"
                else:
                    msg = "Registration successfull. Login to continue"
        else:
            msg = "Already Added"
    return render(request, 'buyerreg.html', {"msg": msg})


def coderreg(request):
    msg = ""
    if(request.POST):
        name = request.POST['name']
        address = request.POST['address']

        email = request.POST['email']
        phone = request.POST['contact']
        qual = request.POST['qual']
        exp = request.POST['exp']

        image = request.FILES["bio"]
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url2 = fs.url(filename)

        image = request.FILES["photo"]
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url3 = fs.url(filename)
        password = request.POST['pwd']
        m = "select count(*) count from tblcoder where cemail='"+str(email)+"'"
        c.execute(m)

        i = c.fetchone()
        if(i[0] == 0):
            s = "insert into tblcoder(cname,caddress,cemail,ccontact,cqualification,cexperience,cbio,cimg) values('"+name + \
                "','"+address+"','"+email+"','"+phone+"','"+qual+"','"+exp + \
                "','"+uploaded_file_url2+"','"+uploaded_file_url3+"')"
            print(s)
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry registration error"
            else:
                s = "insert into tbllogin (uname,pwd,utype,status) values('" + \
                    email+"','"+password+"','coder','0')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg = "Sorry some error occured"
                else:
                    msg = "Registration successfull. Login to continue"
        else:
            msg = "Already Added"
    return render(request, 'coderreg.html', {"msg": msg})


def login(request):
    msg = ""
    if(request.POST):

        email = request.POST["uname"]
        pwd = request.POST["pwd"]
        s = "select count(*) from tbllogin where uname='"+str(email)+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[0] > 0):
            s = "select * from tbllogin where uname='"+str(email)+"'"
            print(s)
            c.execute(s)
            i = c.fetchone()
            if(i[1] == pwd):
                request.session['email'] = email
                request.session['uid'] = i[1]
                if(i[3] == "1"):
                    if(i[2] == "admin"):
                        request.session['uid'] = i[1]
                        return HttpResponseRedirect("/adminhome")
                    elif(i[2] == "buyer"):

                        msg = ' Welcome Buyer...'
                        g = "select * from tblbuyer where bemail='" + \
                            str(email)+"'"

                        c.execute(g)
                        row1 = c.fetchone()
                        request.session['email'] = row1[3]
                        request.session['uid'] = row1[0]
                        return HttpResponseRedirect("/buyerhome")
                    elif(i[2] == "coder"):
                        msg = ' Welcome Coder...'
                        g = "select * from tblcoder where cemail='" + \
                            str(email)+"'"

                        c.execute(g)
                        row1 = c.fetchone()
                        request.session['email'] = row1[3]
                        request.session['uid'] = row1[0]

                        return HttpResponseRedirect("/coderhome")

                elif(i[3] == "0"):
                    msg = "Your registration is incomplete. Please register"
                else:
                    msg = "You are not authenticated to login"
            else:
                msg = "Incorrect password"
        else:
            msg = "User doesnt exist"
    return render(request, 'login.html', {"msg": msg})


def adminviewbuyer(request):
    # email=request.session["email"]
    # reqid=request.GET.get("id")
    c.execute("select tblbuyer.* from tblbuyer,tbllogin where tbllogin.status='0' and tbllogin.uname=tblbuyer.bemail ")
    data = c.fetchall()
    c.execute("select tblbuyer.* from tblbuyer,tbllogin where tbllogin.status='1' and tbllogin.uname=tblbuyer.bemail ")
    data1 = c.fetchall()
    return render(request, "adminviewbuyer.html", {"data": data, "data1": data1})


def adminviewcoder(request):
    # email=request.session["email"]
    # reqid=request.GET.get("id")
    c.execute("select tblcoder.* from tblcoder,tbllogin where tbllogin.status='0' and tbllogin.uname=tblcoder.cemail ")
    data = c.fetchall()
    c.execute("select tblcoder.* from tblcoder,tbllogin where tbllogin.status='1' and tbllogin.uname=tblcoder.cemail ")
    data1 = c.fetchall()
    return render(request, "adminviewcoder.html", {"data": data, "data1": data1})


def adminupdatebuyer(request):
    if(request.GET):

        email = request.GET.get("uemail")
        st = request.GET.get("status")

        m = ("update tbllogin set status='"+st +
             "' where tbllogin.uname='"+str(email)+"' ")
        c.execute(m)
        print(m)
        db.commit()
        return HttpResponseRedirect("/adminviewbuyer")


def adminupdatecoder(request):
    if(request.GET):

        email = request.GET.get("uemail")
        st = request.GET.get("status")

        m = ("update tbllogin set status='"+st +
             "' where tbllogin.uname='"+str(email)+"' ")
        c.execute(m)
        print(m)
        db.commit()
        return HttpResponseRedirect("/adminviewcoder")


def buyerviewprofile(request):
    uid = request.session['uid']
    s = "select * from tblbuyer where bid='"+str(uid)+"'"
    c.execute(s)
    data = c.fetchall()
    return render(request, 'buyerviewprofile.html', {"data": data})


def buyeraddrequest(request):
    msg = ""
    bid = request.session['uid']
    if(request.POST):
        title = request.POST['title']

        description = request.POST['description']
        duedate = request.POST['duedate']

        image = request.FILES["img"]
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

        s = "insert into tblrequest(bid,title,description,duedate,rfile,status) values('"+str(bid)+"','"+str(
            title)+"','"+str(description)+"','"+str(duedate)+"','"+str(uploaded_file_url)+"','Requested')"
        print(s)

        c.execute(s)
        db.commit()
        msg = " successfull"

    return render(request, 'buyeraddrequest.html', {"msg": msg})


def coderviewrequest(request):
    sd = "select tblbuyer.*,tblrequest.* from tblbuyer,tblrequest where tblbuyer.bid=tblrequest.bid"
    c.execute(sd)
    data = c.fetchall()
    return render(request, 'coderviewrequest.html', {"data": data})


def coderaddbid(request):
    msg = ""
    cid = request.session['uid']
    rid = request.GET.get("rid")
    if(request.POST):
        amount = request.POST['amount']

        duedate = request.POST['duedate']

        # image=request.FILES["img"]
        # fs=FileSystemStorage()
        # filename=fs.save(image.name,image)
        # uploaded_file_url=fs.url(filename)

        s = "insert into tblbid(rid,cid,amt,duedate,status) values('"+str(
            rid)+"','"+str(cid)+"','"+str(amount)+"','"+str(duedate)+"','Requested')"
        print(s)

        c.execute(s)
        db.commit()
        msg = " successfull"

    return render(request, 'coderaddbid.html', {"msg": msg})


def coderviewbid(request):
    uid = request.session['uid']
    sd = "select tblbuyer.*,tblrequest.*,tblbid.* from tblbuyer,tblrequest,tblbid where tblbuyer.bid=tblrequest.bid and  tblrequest.rid=tblbid.rid and tblbid.cid='" + \
        str(uid)+"' and tblbid.status='Requested'"
    c.execute(sd)
    data = c.fetchall()
    return render(request, 'coderviewbid.html', {"data": data})


def coderviewwork(request):
    uid = request.session['uid']
    sd = "select tblbuyer.*,tblrequest.*,tblbid.* from tblbuyer,tblrequest,tblbid where tblbuyer.bid=tblrequest.bid and  tblrequest.rid=tblbid.rid and tblbid.cid='" + \
        str(uid)+"' and tblbid.status<>'Requested'"
    c.execute(sd)
    data = c.fetchall()

    return render(request, 'coderviewwork.html', {"data": data})


def buyerviewworkproject(request):
    uid = request.session['uid']
    qry = f"SELECT * FROM `project`p, `tblrequest`r, `tblcoder`c WHERE p.`rid`=r.`rid` AND p.`cid`=c.`cid` AND r.`bid`='{uid}'"
    c.execute(qry)
    data = c.fetchall()
    return render(request, "buyerviewworkproject.html", {"data": data})


def coderupdateproject(request):
    rid = request.GET['reqid']
    uid = request.session['uid']
    if request.method == "POST":
        file = request.FILES["file"]
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        qry = f"INSERT INTO `project`(`rid`,`cid`,`project`) VALUES ('{rid}','{uid}','{uploaded_file_url}')"
        c.execute(qry)
        db.commit()
        return redirect("/coderviewwork")
    return render(request, "coderupdateproject.html")


def buyerviewbidfirst(request):
    uid = request.session['uid']
    sd = "select tblcoder.*,tblrequest.*,tblbid.* from tblcoder,tblrequest,tblbid where tblcoder.cid=tblbid.cid and  tblrequest.rid=tblbid.rid and tblrequest.bid='" + \
        str(uid)+"' and tblbid.status='Requested'"
    c.execute(sd)
    data = c.fetchall()
    return render(request, 'buyerviewbidfirst.html', {"data": data})


def buyerviewbid(request):
    uid = request.session['uid']
    rid = request.GET.get("rid")
    sd = "select tblcoder.*,tblrequest.*,tblbid.* from tblcoder,tblrequest,tblbid where tblcoder.cid=tblbid.cid and  tblrequest.rid=tblbid.rid and tblrequest.bid='" + \
        str(uid)+"' and tblbid.status='Requested' and tblbid.rid='"+str(rid)+"'"
    c.execute(sd)
    data = c.fetchall()
    return render(request, 'buyerviewbid.html', {"data": data})


def buyerconformbid(request):
    if(request.GET):

        rid = request.GET.get("rid")
        bidid = request.GET.get("bidid")

        m = ("update tblbid set status='Conformed' where tblbid.bidid='"+str(bidid)+"' ")
        c.execute(m)
        print(m)
        db.commit()
        m = ("update tblrequest set status='Conformed' where tblrequest.rid='"+str(rid)+"' ")
        c.execute(m)
        print(m)
        db.commit()
        return HttpResponseRedirect("/buyerviewbidfirst")


def buyerviewworkstatus(request):
    uid = request.session['uid']
    # rid=request.GET.get("rid")
    sd = "select tblcoder.*,tblrequest.*,tblbid.* from tblcoder,tblrequest,tblbid where tblcoder.cid=tblbid.cid and  tblrequest.rid=tblbid.rid and tblrequest.bid='" + \
        str(uid)+"' and tblbid.status<>'Requested'"
    c.execute(sd)
    data = c.fetchall()
    return render(request, 'buyerviewworkstatus.html', {"data": data})


def buyermakepayment(request):
    msg = ""
    rid = request.GET.get("rid")
    bidid = request.GET.get("bidid")
    cid = request.session['uid']
    dc = "select tblbid.amt from tblbid where bidid='"+str(bidid)+"'"
    c.execute(dc)
    detail = c.fetchone()
    amt = detail[0]
    dc = "select tblwork.wid from tblwork where tblwork.bidid='"+str(bidid)+"'"
    c.execute(dc)
    details = c.fetchone()
    wid = details[0]

    if(request.POST):
        rid = request.GET.get("rid")
        mamt = request.POST['amount']

        cdate = date.today()

        dd = "select count(wid) from tblpayment where wid='"+str(wid)+"'"
        c.execute(dd)
        cnt = c.fetchone()
        if(cnt[0] == 0):
            s = "insert into tblpayment(wid,date,amt) values('" + \
                str(wid)+"','"+str(cdate)+"','"+str(mamt)+"')"
            print(s)

            c.execute(s)
            db.commit()
            msg = " successfull"
        else:
            msg = "Already paid"

    return render(request, 'buyermakepayment.html', {"msg": msg, "amt": amt})


def coderupdateworkstatus(request):
    if(request.GET):

        rid = request.GET.get("rid")
        bidid = request.GET.get("bidid")
        status = request.GET.get("status")

        m = ("update tblbid set status='"+str(status) +
             "' where tblbid.bidid='"+str(bidid)+"' ")
        c.execute(m)
        print(m)
        db.commit()
        m = ("update tblrequest set status='"+str(status) +
             "' where tblrequest.rid='"+str(rid)+"' ")
        c.execute(m)
        print(m)
        db.commit()
        # if status = "100 percent complete:
        cc = "select status from tblbid where  tblbid.bidid='"+str(bidid)+"'"
        c.execute(cc)
        da = c.fetchone()
        if(da[0] == '100 percent complete'):
            cdate = date.today()
            m = ("insert  into tblwork(bidid,date,status) values('" +
                 str(bidid)+"','"+str(cdate)+"','Completed')")
            c.execute(m)
            print(m)
            db.commit()
        else:
            return HttpResponseRedirect("/coderviewwork")

        return HttpResponseRedirect("/coderviewwork")


def buyerviewpayment(request):
    uid = request.session['uid']
    # rid=request.GET.get("rid")
    sd = "select tblrequest.title,tblpayment.date,tblpayment.amt from tblrequest,tblpayment,tblwork,tblbid where tblrequest.rid=tblbid.rid and tblbid.bidid=tblwork.bidid and tblwork.wid=tblpayment.wid and tblrequest.bid='" + \
        str(uid)+"'"
    print(sd)
    c.execute(sd)
    data = c.fetchall()
    return render(request, 'buyerviewpayment.html', {"data": data})


def coderviewpayment(request):
    uid = request.session['uid']
    # rid=request.GET.get("rid")
    sd = "select tblrequest.title,tblpayment.date,tblpayment.amt,tblbuyer.bname from tblrequest,tblpayment,tblwork,tblbid,tblbuyer where tblrequest.rid=tblbid.rid and tblbid.bidid=tblwork.bidid and tblwork.wid=tblpayment.wid and tblbuyer.bid=tblrequest.bid"
    c.execute(sd)
    data = c.fetchall()
    return render(request, 'coderviewpayment.html', {"data": data})


def coderviewprofile(request):
    uid = request.session['uid']
    s = "select * from tblcoder where cid='"+str(uid)+"'"
    c.execute(s)
    data = c.fetchall()
    return render(request, 'coderviewprofile.html', {"data": data})

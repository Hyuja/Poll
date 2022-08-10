
from django.shortcuts import redirect, render
import os
from urllib import parse
from .models import *
from userapp.models import *
from plotly.offline import plot
from plotly import graph_objects as go 
from matplotlib import pyplot as plt
import random
from dateutil.relativedelta import relativedelta
import datetime
import folium

def menu (request):
    return render (request, "menu.html")
#===================================================
def CandidateEdit(request):
    Candidates = Candidate.objects.all()
    return render (request, "CandidateEdit.html", {'Candidates' : Candidates})

def PollResult(request):
    if request.user.is_authenticated and request.user.is_staff:
        POLL_CASES = Poll_Cases.objects.all().order_by('poll_case_num')
        Candidates = Candidate.objects.all().order_by('Poll_Case_id')
        
        alllst = Candidate.objects.filter(id = -1)
        for pollcase in POLL_CASES:
            canlst = Candidate.objects.filter(id = -1)
            canlst = canlst | Candidate.objects.filter(Poll_Case_id = pollcase.id).order_by('-votes')       #votes 올림차순. canlst[0]이 최다득표임 
            alllst = alllst | canlst
        return render (request, "PollResult.html", {"POLL_CASES" : POLL_CASES, "alllst" : alllst})
    else:
        return redirect ('accessdenied')

def chart(request, id):
    if request.user.is_authenticated and request.user.is_staff:
        pollcase = Poll_Cases.objects.filter(id = id)
        can = Candidate.objects.filter(Poll_Case_id = pollcase[0].id).order_by('-votes')
        
        colors = []
        for ca in can:
            colors.append(ca.CandidateColor)
        
        #======================================================================================
        
        ##PIE CHART
        labels = []
        values = []
        for ca in can:
            labels.append(str(ca.CandidateNum) + (" ") + str(ca.side) + (" ") + str(ca.CandidateName))
            usc = useraccount.objects.filter(voteresult = ca.CandidateNum)
            values.append(usc.count())
        
        
        piechart = go.Figure(data = [go.Pie(labels = labels, values = values, marker_colors = colors)])
        piechart = plot({'data' : piechart}, output_type = 'div')

        
        #======================================================================================

        ##HORIZIONTAL BAR CHARTS
        top_labels = labels

        y_data = ['70대 이상', '60대', '50대', '40대', '30대', '20대<br>10대 포함']     #fiexed field
        
        x_data = [[], [], [], [], [], []]
        #나이 구하기  
        y20 =  datetime.date.today() - relativedelta(years = 20) + relativedelta(days = 1)
        o20 = y20 - relativedelta(years = 10) - relativedelta(days = 1)
        y30 = o20 + relativedelta(days = 1)
        o30 = y30 - relativedelta(years = 10) - relativedelta(days = 1)
        y40 = o30 + relativedelta(days = 1)
        o40 = y40 - relativedelta(years = 10) - relativedelta(days = 1)
        y50 = o40 + relativedelta(days = 1)
        o50 = y50 - relativedelta(years = 10) - relativedelta(days = 1)
        y60 = o50 + relativedelta(days = 1)
        o60 = y60 - relativedelta(years = 10) - relativedelta(days = 1)
        y70 = o60 + relativedelta(days = 1)
        o70 = y70 - relativedelta(years = 100)
        y20 = datetime.date.today() - relativedelta(years = 10)
        
        yearlyvote = []
        uc2 = useraccount.objects.filter(ifvoted = True, birth__range = [o20, y20])    
        uc3 = useraccount.objects.filter(ifvoted = True, birth__range = [o30, y30])
        uc4 = useraccount.objects.filter(ifvoted = True, birth__range = [o40, y40])
        uc5 = useraccount.objects.filter(ifvoted = True, birth__range = [o50, y50])
        uc6 = useraccount.objects.filter(ifvoted = True, birth__range = [o60, y60])
        uc7 = useraccount.objects.filter(ifvoted = True, birth__range = [o70, y70])
        yearlyvote.append(uc2.count())
        yearlyvote.append(uc3.count())
        yearlyvote.append(uc4.count())
        yearlyvote.append(uc5.count())
        yearlyvote.append(uc6.count())
        yearlyvote.append(uc7.count())

        print(y30)
        print(o30)

        print(yearlyvote)
        
        for c in can:
            u2 = useraccount.objects.filter(ifvoted = True, birth__range = [o20, y20], voteresult = c.CandidateNum)
            x_data[5].append(round((u2.count()/yearlyvote[0])*100, 1))
        for c in can:
            u3 = useraccount.objects.filter(ifvoted = True, birth__range = [o30, y30], voteresult = c.CandidateNum)
            x_data[4].append(round((u3.count()/yearlyvote[1])*100, 1))
        for c in can:
            u4 = useraccount.objects.filter(ifvoted = True, birth__range = [o40, y40], voteresult = c.CandidateNum)
            x_data[3].append(round((u4.count()/yearlyvote[2])*100, 1))
        for c in can:
            u5 = useraccount.objects.filter(ifvoted = True, birth__range = [o50, y50], voteresult = c.CandidateNum)
            x_data[2].append(round((u5.count()/yearlyvote[3])*100, 1))

        for c in can:
            u6 = useraccount.objects.filter(ifvoted = True, birth__range = [o60, y60], voteresult = c.CandidateNum)
            x_data[1].append(round((u6.count()/yearlyvote[4])*100, 1))

        for c in can:
            u7 = useraccount.objects.filter(ifvoted = True, birth__range = [o70, y70], voteresult = c.CandidateNum)
            x_data[0].append(round((u7.count()/yearlyvote[5])*100, 1))

        fig = go.Figure()

        for i in range(0, len(x_data[0])):
            for xd, yd in zip(x_data, y_data):
                fig.add_trace(go.Bar(
                    x=[xd[i]], y=[yd],
                    orientation='h',
                    marker=dict(
                        color=colors[i],
                        line=dict(color='rgb(248, 248, 249)', width=1)
                    )
                ))

        fig.update_layout(
            xaxis=dict(
                showgrid=False,
                showline=False,
                showticklabels=False,
                zeroline=False,
                domain=[0.15, 1]
            ),
            yaxis=dict(
                showgrid=False,
                showline=False,
                showticklabels=False,
                zeroline=False,
            ),
            barmode='stack',
            paper_bgcolor='rgb(248, 248, 255)',
            plot_bgcolor='rgb(248, 248, 255)',
            margin=dict(l=120, r=10, t=140, b=80),
            showlegend=False,
        )

        annotations = []

        for yd, xd in zip(y_data, x_data):
            # labeling the y-axis
            annotations.append(dict(xref='paper', yref='y',
                                    x=0.14, y=yd,
                                    xanchor='right',
                                    text=str(yd),
                                    font=dict(family='Arial', size=14,
                                            color='rgb(67, 67, 67)'),
                                    showarrow=False, align='right'))
            # labeling the first percentage of each bar (x_axis)
            annotations.append(dict(xref='x', yref='y',
                                    x=xd[0] / 2, y=yd,
                                    text=str(xd[0]) + '%',
                                    font=dict(family='Arial', size=14,
                                            color='rgb(248, 248, 255)'),
                                    showarrow=False))
            # labeling the first Likert scale (on the top)
            if yd == y_data[-1]:
                annotations.append(dict(xref='x', yref='paper',
                                        x=xd[0] / 2, y=1.1,
                                        text=top_labels[0],
                                        font=dict(family='Arial', size=14,
                                                color='rgb(67, 67, 67)'),
                                        showarrow=False))
            space = xd[0]
            for i in range(1, len(xd)):
                    # labeling the rest of percentages for each bar (x_axis)
                    annotations.append(dict(xref='x', yref='y', x=space + (xd[i]/2), y=yd, text=str(xd[i]) + '%', font=dict(family='Arial', size=14, color='rgb(248, 248, 255)'),
                                            showarrow=False))
                    # labeling the Likert scale
                    if yd == y_data[-1]:
                        annotations.append(dict(xref='x', yref='paper',
                                                x=space + (xd[i]/2), y=1.1,
                                                text=top_labels[i],
                                                font=dict(family='Arial', size=14,
                                                        color='rgb(67, 67, 67)'),
                                                showarrow=False))
                    space += xd[i]

        fig.update_layout(annotations=annotations)

        fig = plot({'data' : fig}, output_type = 'div')
        #======================================================================================




        return render(request, 'chart.html', context = {'plot_div' : piechart, 'fig' : fig })
    else: 
        return redirect ('accessdenied')

def accessdenied (request):
    return render (request, 'accessdenied.html')

